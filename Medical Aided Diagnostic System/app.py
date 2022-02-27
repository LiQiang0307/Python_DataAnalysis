from flask import Flask, render_template, request, session, redirect

import model.predict
import utils.mysql as mysql

app = Flask(__name__)
app.secret_key = 'app'
app.debug = True

import data_visual  # 导入蓝图

app.register_blueprint(data_visual.us)  # 注册蓝图


# 路由
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')  # 获取POST传过来的值
    pwd = request.form.get('pwd')  # 获取POST传过来的值

    #  数据库操作 查找用户名和密码
    sql = 'select * from user where username = "{}"'.format(user)
    # print(sql)
    try:
        res = mysql.mysql_query(sql)[0]
    except:
        res = None
    # print(res)
    if (res is not None) and user == res['username'] and pwd == res['password']:
        # 用户信息放入session
        session['user_info'] = user
        return redirect('/index')
    else:
        return render_template('login.html', msg='用户名或密码错误')


@app.route('/index', methods=['GET'])
def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    return render_template('index.html')


@app.route('/getPredict', methods=['GET'])
def get_predict():
    return render_template('predict.html')


@app.route('/getData', methods=['GET', 'POST'])
def getData():
    """
    获取数据进行预测
    :return:
    """
    sex = request.values.get('sex')
    if sex == '男':
        sex = 1
    else:
        sex = 0
    age = int(request.values.get('age'))
    cp = float(request.values.get('trestbps'))
    trestbps = float(request.values.get('trestbps'))
    chol = float(request.values.get('chol'))
    fbs = float(request.values.get('fbs'))
    restecg = float(request.values.get('restecg'))
    thalach = float(request.values.get('thalach'))
    exang = float(request.values.get('exang'))
    oldpeak = float(request.values.get('oldpeak'))
    slope = float(request.values.get('slope'))
    ca = float(request.values.get('ca'))
    thal = float(request.values.get('thal'))

    path = 'model/心脏病预测KNN.m'
    res = model.predict.predict(path, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca,
                                thal)

    if res == 1:
        result = '算法预测出可能有心脏病（预测结果仅供参考）'
    if res == 0:
        result = '算法预测出没有心脏病（预测结果仅供参考）'
    return result


@app.route('/visual', methods=['GET'])
def visual():
    """
    进入可视化界面
    :return:
    """
    # 判断用户是否登录，如果未登录，则不能跳转到可视化界面
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    return render_template('visual.html')


if __name__ == '__main__':
    app.run()
