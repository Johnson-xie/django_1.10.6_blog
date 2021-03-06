# python 在不同层级目录import 模块的方法
***
```
  有一个文件夹/home/a,  里面有个模块叫b.py,  程序里导入模块b？  

  1).
  import sys;  
  sys.path.append("/home/a/")  
  import b  
  2).  
  在目录里面增加__init__.py文件，里面可以写import时执行的代码，当然也可以留空就可以.  
  import home.a.b  
  3).   
  from home.a.b import *  
  前提 home、a中都包括__init__.py  
```
# BOM标记，文件开头 \ufeff
***
utf-8编码产生的csv文件，excel打开乱码，使用utf_8_sig带BOM的编码格式就可以正常解码咯。  

将BOM头去掉，代码如下：
```
  if text.startswith(u'\ufeff'):    
    text = text.encode('utf8')[3:].decode('utf8')    
```
# csv文件读取报错
***
**_csv.Error: field larger than field limit (131072)**
头部添加  
```
import csv  
import sys  
csv.field_size_limit(sys.maxsize)  
**csv.Error: line contains NULL byte**
去掉文件中的\0及null字符  
csv_readfile = csv.reader((line.replace('\0', '') for line in csv_read))  
传入的是迭代器对象  
```

# 轮子感悟
***
今后遇到这类问题，应该首先考虑我可以用语言（例如python）的什么模块或者函数去解决这个问题，而不是赶紧就着手自己造轮子去写繁杂的代码，毕竟自己写出来的未必尽善尽美地兼容了。

# GIT撤销修改的不同阶段
> http://einverne.github.io/post/2017/12/git-reset.html

# pandas处理工资报表简单操作
***
#### 读取excel参数

* sheet_name=[0,1,2] 或具体名字
* index_col="col_label" 取col的label为行索引
* skiprows=2 跳过前2行，默认开始行即第三行为header的label



#### 向excel_abspath中插入新的sheet
**插入新的sheet**
```  
import openpyxl import load_workbook
import pandas as pd  
dataframe = pd.DataFrame({col1:[row1,row2,row3],col2:[row1,row2,row3],col3:[row1,row2,row3]})
excelWriter = pd.ExcelWriter(excel_abspath,engine='openpyxl)
book = load_workbook(excelEriter.path)
excelWriter.book = book
dataframe.to_excel(excel_writer=excelWriter,sheet_name='new_sheet_name',index=None)
excelWriter.close()

```  

```  
def add_sheet(df, name):
    writer = pd.ExcelWriter(url, engine='openpyxl')
    book = load_workbook(writer.path)
    writer.book = book
    df.to_excel(writer, index=False, sheet_name='not_found' + name)
    writer.save()
    writer.close()
```



#### 简单行里操作  
*取指定列的数据
```df[['label1','label2']```
*获取行  
```df.iloc[index]```
* 获取行的指定列值
df.iloc[index]['col_label']
* 返回df的元组(行数，列数)
```df.shape ```
#### dataframe拼接  
```df.append(df2)```

## pandas 筛选含某字段的数据
**拼接df**
```
new = [df1,df2,df3,]
df = pd.concat(new)
```
**筛选数据与取反**
```
new = df[~df['fpath'].str.contains('open_source|opensource')]  多个字段用|分割，取反不包含使用~
```

## 添加行
* df['new_field'] = value or Series  
## 自定义函数处理一列中每行的内容  
* new_col = df['col_filed'].apply(func)  

## 添加自定义列名
* names = ("columns_1","columns_2",)  
## 提取列数据，从新设置索引  
```  
df = pd.read_csv(path,names=("path",))

df['py'] = df[df.path.str.endswith('.py')].dropna(axis=1).reset_index().path
df['sh'] = df[df.path.str.endswith('.sh')].dropna(axis=1).reset_index().path
df['bat'] = df[df.path.str.endswith('.bat')].dropna(axis=1).reset_index().path
```

## 计算各列非空数据总数  
`df.count()`

# 蔓藤
## 建文件
```
df = pd.dataframe({'col_field':[1,2,3],'col_field2':['a','b','c']})  
```

# pandas  

### read excel  
**先读出来看一下，再设置索引**
```
df = pd.read_excel(path,index_col='col_field')
```

### 排序
```  
products = pd.read_excel('C:/Temp/List.xlsx', index_col='ID')
products.sort_values(by=['Worthy', 'Price'], ascending=[True, False], inplace=True)
print(products)  

```
### 重新设置索引，会生成新的df
`df = df.set_index('field')`  

### 使用函数处理列数据 或判断
```
    
def validate_age(a):
    return 18 <= a <= 30


def level_b(s):
    return 60 <= s < 90


students = pd.read_excel('C:/Temp/Students.xlsx', index_col='ID')
students = students.loc[students['Age'].apply(validate_age)].loc[students.Score.apply(level_b)]  # 两种语法
print(students)  
```

### 两个表根据索引进行合并 左连接和右连接
```   

students = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Students', index_col='ID')
scores = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Scores', index_col='ID')
table = students.join(scores, how='left').fillna(0)  没有就填充数据  
table.Score = table.Score.astype(int)  

查看数据格式 table.Score.dtype


```

### 数据校验
```
def score_valication(row):
    try:
        assert 0 <= row.Score <= 100
    except:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}')


students = pd.read_excel('C:/Temp/Students.xlsx')
# print(students)
students.apply(score_valication, axis=1)  传入的是行对象
```  

### 处理文本，添加行
```  
employees = pd.read_excel('C:/Temp/Employees.xlsx', index_col='ID')
df = employees['Full Name'].str.split(expand=True)
employees['First Name'] = df[0]
employees['Last Name'] = df[1]
print(employees)  
```

# 行列求和  

```  
students = pd.read_excel('C:/Temp/Students.xlsx', index_col='ID')

row_sum = students[['Test_1', 'Test_2', 'Test_3']].sum(axis=1)
row_mean = students[['Test_1', 'Test_2', 'Test_3']].mean(axis=1)

students['Total'] = row_sum
students['Average'] = row_mean

col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean()
col_mean['Name'] = 'Summary'
students = students.append(col_mean, ignore_index=True)
print(students)
```

# loc和iloc的差别  
```  

* 选取标签为A和C的列，并且选完类型还是dataframe  

df = df.loc[:, ['A', 'C']]
df = df.iloc[:, [0, 2]]  

* 选取标签为C并且只取前两行，选完类型还是dataframe  

df = df.loc[0:2, ['A', 'C']]  
df = df.iloc[0:2, [0, 2]]   

* 聪明的朋友已经看出iloc和loc的不同了：loc是根据dataframe的具体标签选取列，而iloc是根据标签所在的位置，从0开始计数。  
* 第二个示例中的的0:2表示选取第0行到第二行，这里的0:2相当于[0,2）前闭后开，2是不在范围之内的。  
* 还有一种方式是使用df.icol(i)来选取列，选取完的也不是dataframe而是series，i为该列所在的位置，从0开始计数。  
```
* 如果你想要选取某一行的数据。  
`df.loc[[i]]或者df.iloc[[i]]`

# 去重和找重

```  

dupe = students.duplicated(subset='Name')  
dupe = dupe[dupe == True]  # dupe = dupe[dupe]  
print(students.iloc[dupe.index])  

students.drop_duplicates(subset='Name', inplace=True, keep='last') # keep=first  
print(students)  

```

# 转置  
```  
pd.options.display.max_columns = 999  
videos = pd.read_excel('C:/Temp/Videos.xlsx', index_col='Month')  
table = videos.transpose()  
table = videos.T  
print(table)  
```
# 读取csv文本文件  
```  

students1 = pd.read_csv('C:/Temp/Students.csv', index_col='ID')  
students2 = pd.read_csv('C:/Temp/Students.tsv', sep='\t', index_col='ID')  
students3 = pd.read_csv('C:/Temp/Students.txt', sep='|', index_col='ID')  

```

# pandas读取一个excel文件里的多张表  
* 已知表名  
```  
xls = pd.ExcelFile('path_to_file.xls')
df1 = pd.read_excel(xls, 'Sheet1')
df2 = pd.read_excel(xls, 'Sheet2')
```

* 未知sheet_name待续......











#### 打包py为exe文件  
```pyinstall -F script_name.py --hidden-import=pandas._libs.tslibs.timedeltas```

# notepad++ 常用快捷键
- ctrl + shift + 上下移动行内容
- ctrl + g 跳转到指定行
- ctrl + d 复制黏贴当前行(pycharm ctrl + d)
- ctrl + l 删除光标所在行(pycharm ctrl + y)
- shift + home/end(选择光标至头或至尾内容)

| 一个普通标题 | 一个普通标题 | 一个普通标题 |
| ------ | ------ | ------ |
| 短文本 | 中等文本 | 稍微长一点的文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

# python 获取脚本嵌套调用执行的模块信息
```
import sys
abspath = '/root/Desktop/hell.py'
sys.path.append(os.path.dirname(abspath))
import os.path.basename(abspath)
try:
    sys.module.values().__file__
except AttributeError as e:
    pass
```


# timeit  
```  

import timeit  
from math import sin  
def func():  
	result = 0
	for i in rane(10000):
		result += sin(i)
t.timeit.Timer("func","from __main__ import func")  
t.timeit(10次)  
```  

# pip 打包当前环境依赖包  
* 导出当前包名
```  
pip freeze
```  
* 根据导出的包表安装包  
`pip install -r project_name/requirements.txt`

# python2 或 python3装包错误解决  
* pip install package_name  
* pythonn setup.py install (下的python包)  
* pip install *.whl (下的轮子包)

# 转化时间字符串  
```  
u'2017-07-12T11:44:42.000+08:00'
t = time.strptime(s, '%Y-%m-%dT%H:%M:%S.000+08:00')
d = datetime.datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
```  

# 字典列表，根据某个值进行分组  
```  
from operator import itemgetter
from itertools import groupby
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
#operator模块提供的itemgetter函数用于获取对象的哪些维的数据
rows.sort(key=itemgetter('date'))
for date,items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
```  

```  
07/01/2012
  {'address': '5412 N CLARK', 'date': '07/01/2012'}
  {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
07/02/2012
  {'address': '5800 E 58TH', 'date': '07/02/2012'}
  {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
  {'address': '1060 W ADDISON', 'date': '07/02/2012'}
07/03/2012
  {'address': '2122 N CLARK', 'date': '07/03/2012'}
07/04/2012
  {'address': '5148 N CLARK', 'date': '07/04/2012'}
  {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
```














