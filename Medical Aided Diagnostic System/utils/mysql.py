import pymysql


# 数据库功能
def connect_mysql():
    # 连接mysql数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='mysql',
        db='mads',
        charset='utf8')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 执行完毕返回的结果默认以元组的形式保存,指定cursor返回字典格式，方便操作
    return conn, cursor


def colse_mysql_conn(conn, cursor):
    """
    关闭数据库的连接
    :param conn:
    :param cursor:
    :return:
    """
    cursor.close()
    conn.close()


# sql查询函数
def mysql_query(sql, *args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return:
    """
    # 连接数据库，创建游标
    conn, cursor = connect_mysql()
    # 执行sql语句
    cursor.execute(sql, args)
    # 获取返回的数据（元组形式）
    res = cursor.fetchall()
    # 关闭游标，以及数据库连接
    colse_mysql_conn(conn, cursor)
    return res


if __name__ == '__main__':
    sql = 'select * from user where username = "admin"'
    res = mysql_query(sql)
    print(res)
