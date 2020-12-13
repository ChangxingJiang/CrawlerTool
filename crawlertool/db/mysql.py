"""
MySQL相关工具类
"""

from typing import Dict
from typing import List

import mysql.connector


class MySQL:
    def __init__(self, host: str, database: str, user: str, password: str, use_unicode: bool = True):
        """MySQL连接对象构造器

        :param host: 主机名
        :param database: 数据库名
        :param user: 用户名
        :param password: 密码
        :param use_unicode: MySQL连接的use_unicode选项(默认=True)
        """
        self.host, self.database, self.user, self.password = host, database, user, password
        self.connect = mysql.connector.connect(host=host, user=user, password=password, database=database, use_unicode=use_unicode)
        self.cursor = self.connect.cursor()

    def create(self, sql: str):
        """创建数据表到MySQL数据库"""
        return self.execute(sql)

    def insert(self, table: str, data: List[Dict]):
        """写入数据到MySQL数据库

        :param table: 表名
        :param data: 需要写入的多条记录(所有记录的字段名与第一条记录的字段名统一)
        :return: 写入数据是否成功
        """
        if data:
            if self.execute(self.sql_insert(table, data)):
                self.connect.commit()
                return len(data) == self.cursor.rowcount
            else:
                return False
        else:
            return True

    def select(self, table: str, columns: List[str], where: str = ""):
        """ SELECT读取MySQL数据库的数据

        :param table: 表名
        :param columns: 字段列表
        :param where: 在执行SELECT语句时是否添加WHERE子句(默认为空,如添加应以WHERE开头)
        """
        if columns and self.execute(self.sql_select(table, columns, where)):
            return self.cursor.fetchall()
        else:
            return []

    def execute(self, sql: str):
        """执行SQL语句"""
        try:
            self.cursor.execute(sql)
            return True
        except mysql.connector.errors.ProgrammingError:
            print("SQL语句执行异常:", sql)
            return False

    @staticmethod
    def sql_select(table: str, columns: List[str], where: str = ""):
        return "SELECT " + ",".join([column for column in columns]) + " FROM " + table + " " + where

    @staticmethod
    def sql_insert(table: str, data: List[Dict]):
        columns = [(column, type(data[0][column])) for column in data[0]]

        def get_format_val(item, column):
            if column[0] in item and item[column[0]] is not None:
                if column[1] == int or column[1] == float or column[1] == bool:
                    return str(item[column[0]])
                else:
                    return "'" + str(item[column[0]]).replace("'", "") + "'"
            else:
                if column[1] == int or column[1] == float or column[1] == bool:
                    return "0"
                else:
                    return "''"

        return ("INSERT INTO " + table + " (" + ",".join(["`" + column + "`" for column in data[0]]) + ") " +
                "VALUES " + ",".join(["(" + ",".join([get_format_val(item, column) for column in columns]) + ")" for item in data]))

    def close(self):
        self.cursor.close()
