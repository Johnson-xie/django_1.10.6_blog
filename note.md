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

