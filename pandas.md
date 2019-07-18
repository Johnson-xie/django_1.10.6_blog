## pandas 按列去重  
***  
```  
df = DataFrame({'k': [1, 1, 2, 2]})
print data
IsDuplicated = data.duplicated() 
print IsDuplicated
print type(IsDuplicated)
data = data.drop_duplicates()
```
* 结果  
```
   k
0  1
1  1
2  2
3  2

0    False
1     True
2    False
3     True

   k
0  1
2  2  
DataFrame的duplicated方法返回一个布尔型Series,表示各行是否重复行。
而 drop_duplicates方法，它用于返回一个移除了重复行的DataFrame
这两个方法会判断全部列，你也可以指定部分列进行重复项判段。
例如，希望对名字为k2的列进行去重，
data.drop_duplicates(['k2'])
```  


## df根据某列判断是在一个数组中，进行比对，选出没有的  
```  
arr = ['a', 'b', 'c']
df[df["column"].isin(arr)]
```  
* 手动构造数组  
```  
array = df['field']  
array = list(array)
```  
* 取反,比对选出列中字段 在数组中没有的  
`df[~df['field'].isin(list(n))] `

## pandas导出mysql中数据  
* 数据库链接对象  
* sql语句  
* pandas命令  
```  
import pandas as pd
import MySQLdb
handle = MySQLdb.connect(host="xxx.xxx..xxx.xxx",user="root",port=xxxx, passwd="xxxxxx",db="xxxxx",charset="utf8")
sql = xxxxx     #查询语句
df = pd.read_sql(sql, con=handle)
handle.close()
df.to_excel(r'./1.xlsx', sheet_name='data')
```  





