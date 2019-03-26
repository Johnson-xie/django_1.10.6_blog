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
import panas
dataframe = pd.DataFrame({col1:[row1,row2,row3],col2:[row1,row2,row3],col3:[row1,row2,row3]})
excelWriter = pd.ExcelWriter(excel_abspath,engine='openpyxl)
book = load_workbook(excelEriter.path)
excelWriter.book = book
dataframe.to_excel(excel_writer=excelWriter,sheet_name='new_sheet_name',index=None)
excelWriter.close()

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
# git

* 提交时报错  
`git commit -m 'add tools'`  
`error: pathspec 'tools'' did not match any file(s) known to git`  
解决  
`git commit -m "add tools"`  
**语法上没有问题，总是提交不了，最后发现，在Linux系统中，commit信息使用单引号”包括，我使用的windows系统，信息应该是双引号”“包括** 

* 本地修改文件未提交至缓存区，复原  
```  
git checkout file  单个文件
git checkout . 全部  
``` 
* 取消已经暂存的文件。即，撤销先前"git add"的操作
`git reset HEAD <file>`

* 从暂存区删除文件  
`git rm --cached filename`  

`git f --cached filename `  磁盘也删除
* 未加入缓存区，撤销修改，退回当前提交版本的状态  
`git checkout .`
```  
git reset --hard HEAD
git reset --hard commit_id
```

