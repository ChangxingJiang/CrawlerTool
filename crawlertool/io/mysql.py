from typing import Dict
from typing import List

import pandas as pd
import sqlalchemy


def _connect_mysql(host: str, user: str, password: str, database: str) -> "sqlalchemy.engine.base.Engine":
    """构造MySQL的链接引擎"""
    return sqlalchemy.create_engine(
        "mysql+pymysql://{0}:{1}@{2}:3306/{3}?charset=utf8".format(user, password, host, database))


def load_mysql(host: str, user: str, password: str, database: str, table: str, columns: List[str]):
    """从MySQL读取数据"""
    sql = "SELECT {0} FROM {1}.{2}".format(",".join(["`" + column + "`" for column in columns]), database, table)
    return pd.read_sql_query(sql, _connect_mysql(host, user, password, database))


def write_mysql(host: str, user: str, password: str, database: str, table: str, columns: List[str], data: List[Dict]):
    """将数据写入到MySQL"""
    df = pd.DataFrame([pd.Series(item) for item in data], columns=columns)
    df.to_sql(table, _connect_mysql(host, user, password, database), index=False, if_exists="append")
