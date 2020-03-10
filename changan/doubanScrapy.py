import os
import pandas as pd
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
#chromedriver对应版本下载地址
#http://chromedriver.storage.googleapis.com/index.html

#豆瓣从2017年10月开始全面禁止爬取数据。在非登录状态下仅仅可以爬取200条短评
#登录状态下可以爬取500条数据。
#白天一分钟最多可以爬40次，晚上60次，超过次数会封IP地址

class CommentsCrawler(object):
    """
    豆瓣评论爬虫类
    """
    def __init__(self,subject_url,output_path,username,pwd):
        self.subject_url=subject_url#待爬取电影的url地址
        self.output_path=output_path#爬取结果保存的地址
        self.username=username
        self.pwd=pwd

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        self.all_comments_file=os.path.join(output_path,"all_comments.csv")
        self.diver=webdriver.Firefox()
        self._simulate_login()

    def _simulate_login(self):
        """
        模拟登陆
        :return:
        """
        #模拟登陆豆瓣
        login_url="https://www.douban.com"
        self.diver.get(login_url)
        self.diver.switch_to.frame(self.diver.find_element_by_tag_name("iframe"))

        #点击密码登录
        pwd_login=self.diver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
        pwd_login.click()

        #输入账号
        username_input=self.diver.find_element_by_xpath('//*[@id="username"]')
        username_input.clear()
        username_input.send_keys(self.username)

        #输入密码
        pwd_input=self.diver.find_element_by_xpath('//*[@id="password"]')
        pwd_input.clear()
        pwd_input.send_keys(self.pwd)

        #登录
        bottom=self.diver.find_element_by_class_name('account-form-field-submit')
        bottom.click()

        #登录后等待10秒
        time.sleep(10)

    def get_all_comments(self):
        """
        获取全剧豆瓣评论，最多爬取500条评论
        :return:
        """
        user_id_list=[]#用户id
        user_city_list=[]#用户所在城市
        rating_list=[]#爬取的评分列表
        comment_date_list=[]#爬取评论日期列表
        comment_list=[]#爬取评论列表

        comment_index=0#起始序列号
        while True:
            #全剧评论的起始页
            all_comm_url=self.subject_url+'comments?start={}&limit=20&sort=new_score&status=P'.format(comment_index)
            self.diver.switch_to_default_content()
            self.diver.get(all_comm_url)
            print("正在爬取第{}页的记录……".format(int(comment_index/20+1)))
            #访问成功
            soup=BeautifulSoup(self.diver.page_source)
            comment_tag_list=soup.find_all(class_="comment")
            if len(comment_tag_list)>0:
                for comment_tag in comment_tag_list:
                    #获取用户id
                    user_id=comment_tag.find(class_='comment-info').find('a').text.strip()

                    #获取用户所在城市
                    #获取用户主页地址
                    user_page_url=comment_tag.find(class_="comment-info").find('a').get('href')
                    self.diver.get(user_page_url)
                    user_soup=BeautifulSoup(self.diver.page_source)
                    try:
                        user_city=user_soup.find(class_='user-info').find('a').text.strip()
                    except Exception as e:
                        print("用户信息获取异常：",e)
                        user_city=''

                    #获取评分
                    rating=comment_tag.find(class_='rating').get('title').strip() \
                        if comment_tag.find(class_='rating') is not None else ''
                    #获取评论的时间
                    comment_date=comment_tag.find(class_='comment-time').text.strip() \
                        if comment_tag.find(class_='comment-time') is not None else ''
                    #获取评论内容
                    comment=comment_tag.find(class_="short").text.strip() \
                        if comment_tag.find(class_='short') is not None else ''

                    user_id_list.append(user_id)
                    user_city_list.append(user_city)
                    rating_list.append(rating)
                    comment_date_list.append(comment_date)
                    comment_list.append(comment)

                comment_index+=20

                #在当前页面随机停留的时间
                time.sleep(random.random()*3)
            else:
                #如果当前页面没有评论，则停止爬虫，保存结果
                self._save_to_file(user_id_list,user_city_list,rating_list,comment_date_list,comment_list)
                break
    def _save_to_file(self,user_id_list,user_city_list,rating_list,comment_date_list,comment_list):
        """
        保存爬取的结果
        :param user_id_list:
        :param user_city_list:
        :param rating_list:
        :param comment_date_list:
        :param comment_list:
        :return:
        """
        results_df=pd.DataFrame()
        results_df['user_id']=user_id_list
        results_df['city']=user_city_list
        results_df['rating']=rating_list
        results_df['date']=comment_date_list
        results_df['comment']=comment_list
        results_df.to_csv(self.all_comments_file,encoding='utf-8',index=False)

        print("以爬取{}条评论记录".format(len(comment_list)))
        print("结果保存在{}".format(self.all_comments_file))




if __name__ == '__main__':
    #长安十二时辰 豆瓣地址
    subject_url="https://movie.douban.com/subject/26849758/"
    output_path='./chang_an'

    username=''#请填写用户名
    pwd=''#请填写用户密码
    cc=CommentsCrawler(subject_url,output_path,username,pwd)
    cc.get_all_comments()


