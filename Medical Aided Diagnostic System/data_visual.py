from flask import Blueprint, jsonify

import utils.analyse as analyse
import utils.feature_importances as feature

"""
应用蓝图，将数据分析可视化
用到的路由单独放在此文件中
"""

us = Blueprint('us', __name__)


@us.route('/scatter_age_thalach', methods=['GET'])
def test():
    res = analyse.age_thalach()
    age_have = [int(i) for i in res['have'][0]]
    thalach_have = res['have'][1]
    have = []
    for i, j in zip(age_have, thalach_have):
        have.append([i, j, '患病'])
    age_no = [int(i) for i in res['no'][0]]
    thalach_no = res['no'][1]
    no = []
    for i, j in zip(age_no, thalach_no):
        no.append([i, j, '未患病'])
    # print(have)
    return jsonify({'have': have, 'no': no})


@us.route('/sex_distribution', methods=['GET'])
def sex_distribution():
    """
    获取男女比例分布
    :return:
    """
    count, ratio = analyse.get_ratio()
    have = [count['have_countmale'], count['have_countfemal']]  # 患病男女
    no = [count['no_countmale'], count['no_countfemale']]
    # print(no)
    return jsonify({'have': have, 'no': no})


@us.route('/cp', methods=['GET'])
def cp():
    """
    胸痛类型分布
    :return:
    """
    have,no=analyse.cp()
    return jsonify({'have': have, 'no': no})


@us.route('/age_trestbps', methods=['GET', 'POST'])
def age_trestbps():
    """
    散点图，年龄 血压 患病三者关系
    :return:
    """
    res = analyse.age_trestbps()
    # print(res)
    age_have = [int(i) for i in res['have'][0]]
    trestbps_have = res['have'][1]
    have = []
    for i, j in zip(age_have, trestbps_have):
        have.append([i, j, '患病'])
    age_no = [int(i) for i in res['no'][0]]
    trestbps_no = res['no'][1]
    no = []
    for i, j in zip(age_no, trestbps_no):
        no.append([i, j, '未患病'])
    # print(have)
    return jsonify({'have': have, 'no': no})


@us.route('/trestbps_thalach',methods=['GET'])
def trestbps_thalach():
    """
    血压和心率
    :return:
    """
    res = analyse.trestbps_thalach()
    # print(res)
    thalach_have = [int(i) for i in res['have'][0]]
    trestbps_have = res['have'][1]
    have = []
    for i, j in zip(thalach_have, trestbps_have):
        have.append([i, j, '患病'])
    thalach_no = [int(i) for i in res['no'][0]]
    trestbps_no = res['no'][1]
    no = []
    for i, j in zip(thalach_no, trestbps_no):
        no.append([i, j, '未患病'])
    # print(have)
    return jsonify({'have': have, 'no': no})


@us.route('/corr',methods=['GET'])
def get_corr_data():
    """
    获取协方差计算结果
    :return:
    """
    res=analyse.correlation()
    return jsonify({'data':res})

@us.route('/feature_important',methods=['GET'])
def get_feature():
    x,y=feature.get_feature_importance()
    return jsonify({'x':x,'y':y})