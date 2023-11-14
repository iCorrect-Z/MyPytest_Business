# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @Time    : 2023/11/14 15:01
# @Author  : Correct-Z
# @Blog    ：

import pymysql
from data.config_env import MYSQL_CONFIG


class MysqlDb():

    def __init__(self, host, port, user, password, db_name):

        self.db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db_name
        )

        self.cur = self.db.cursor()

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作

        self.cur.close()

        self.db.close()

    def select_db(self, sql):
        """查询"""

        self.cur.execute(sql)

        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        """更新/插入/删除"""
        try:

            self.cur.execute(sql)

            self.db.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))

            self.db.rollback()


if __name__ == '__main__':
    aa=217940 #参数化sql
    mysql_db = MysqlDb(*MYSQL_CONFIG)
    print(mysql_db.select_db(f'SELECT * FROM client_sell_order where sellOrderId={aa}')[0])
    # mysql_db.execute_db("INSERT INTO case_test( aa, `add`) VALUES ('1', '1');")
    # mysql_db.execute_db(f"UPDATE case_test SET aa = '2', `add` = {aa} WHERE id = 1;")
    # mysql_db.execute_db(f"delete from case_test where aa={aa}")
    # print(mysql_db.select_db('SELECT * FROM case_test'))
    # # 多表联查
    # print(mysql_db.select_db("SELECT * FROM apitest_environment as e left join auth_user as u on e.user_id=u.id "))
