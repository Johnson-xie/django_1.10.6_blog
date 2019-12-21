## distinct  
* 可以，根据两个字段去重  
```select distinct a, b from table```  

## group by  
* 多个字段分组  
```select * from table group by a, b```  

* 报错  
```select distinct a, distinct b from table```  

## in ('abc', 'abc%')不支持like  

## <=> 安全等于  
```  
select * from table where field <=> full;  
select * from table where field is full;  
```  

## 这两种情况不同  
* null判断不同  
```  
select * from table;  
select * from table where field like "%%";

```  


