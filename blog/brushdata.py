# -*- encoding: utf-8 -*-
import pandas as pd
from mysql import *
from openpyxl import load_workbook

data_base = 'library_name'
PROD = False  # ************************
host = "xxxx" if PROD else "yyyy"

url = r"filename.xlsx"
xls = pd.ExcelFile(url)

def add_sheet(df, name):
    writer = pd.ExcelWriter(url, engine='openpyxl')
    book = load_workbook(writer.path)
    writer.book = book
    df.to_excel(writer, index=False, sheet_name='not_found' + name)
    writer.save()
    writer.close()


# 获取每张表的名字，根据excel表硬编码
groups = ['sheet_name1', 'sheet_name2']


# user_not_in_web = defaultdict(list)
user_not_in_web = []
for group in groups:
    df = pd.read_excel(xls, group).fillna('xxx')
    for _, row in df.iterrows():
        group, domain = row[2], row[4]
        sql = 'SELECT tg.id, td.id ' \
              'from tbl_group as tg ' \
              'inner JOIN tbl_domain as td ' \
              'on tg.id=td.group_id ' \
              'where tg.`name`="{}" and td.`name`="{}"'.format(group, domain)
        ret, msg = upDataToDB(sql, 'get', mysqldb=data_base, host=host)

        # 1.确保查到已有的group和domain
        try:
            group_id, domain_id = ret[0]
        except:
            print(sql)
            continue

        # 2.确保数据库是否有该用户
        user_id = row[1]  # 第二列为工号，根据excel表硬编码
        sql = 'select * from tbl_user where user_id="{}"'.format(user_id)
        ret, msg = upDataToDB(sql, 'get', mysqldb=data_base, host=host)
        if not ret:
            user_not_in_web.append(user_id)
            continue

        # 3.对该用户进行重新设置
        sql = 'UPDATE tbl_user set `group`={},domain_id={} where user_id="{}";'.format(group_id, domain_id, user_id)
        ret, msg = upDataToDB(sql, 'set', mysqldb=data_base, host=host)
        # print(sql)

    print(len(user_not_in_web))
    print(user_not_in_web)
    new = df[df['工号'].isin(user_not_in_web)]
    add_sheet(new, group)
    user_not_in_web = []


# 输出web中未注册的用户
# print(user_not_in_web)
