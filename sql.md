
# sql语句  
***
##  select
* 跳过前两条数据，取两条数据
```  
select *  
from table  
where field=""
limit 2,2;  
```  
* 查询某字段中有某字符  
```  
select *  
from table  
where field like "%??%"  
order by time_field desc;
```



## delete  
* 不加调价，直接删表  
`delete from table;`  
* 一般需要加条件  
```  
delete from table 
where time_field > "2019-04-01 00:00:00";
```
 
