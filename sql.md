
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
* 从offset num后开始取  
```  
select *  
from table  
where conditions  
order by field_one desc,field_two asc
limit 5 offset 5;  
```
### 根据时间查询的sql
```  
-- 今天    
select fullName,addedTime from t_user where to_days(addedTime) = to_days(now());   
-- 昨天    
select fullName,addedTime from t_user where to_days(NOW()) - TO_DAYS(addedTime) <= 1;    
-- 近7天    
select fullName,addedTime from t_user where date_sub(CURDATE(),INTERVAL 7 DAY) <= DATE(addedTime);    
-- 近30天    
SELECT fullName,addedTime FROM t_user where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(addedTime);  
-- 本月    
SELECT fullName,addedTime FROM t_user WHERE DATE_FORMAT( addedTime, '%Y%m' ) = DATE_FORMAT( CURDATE() , '%Y%m' );  
-- 上一月    
SELECT fullName,addedTime FROM t_user WHERE PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( addedTime, '%Y%m' ) ) =1;   
-- 查询本季度数据    
select fullName,addedTime FROM t_user where QUARTER(addedTime)=QUARTER(now());   
-- 查询上季度数据    
select fullName,addedTime FROM t_user where QUARTER(addedTime)=QUARTER(DATE_SUB(now(),interval 1 QUARTER));    
-- 查询本年数据    
select fullName,addedTime FROM t_user where YEAR(addedTime)=YEAR(NOW());    
-- 查询上年数据    
select fullName,addedTime FROM t_user where year(addedTime)=year(date_sub(now(),interval 1 year));    
-- 查询距离当前现在6个月的数据    
select fullName,addedTime FROM t_user where addedTime between date_sub(now(),interval 6 month) and now();    
  
-- 查询当前这周的数据    
SELECT fullName,addedTime FROM t_user WHERE YEARWEEK(date_format(addedTime,'%Y-%m-%d')) = YEARWEEK(now());    
-- 查询上周的数据    
SELECT fullName,addedTime FROM t_user WHERE YEARWEEK(date_format(addedTime,'%Y-%m-%d')) = YEARWEEK(now())-1;    
-- 查询上个月的数据     
select fullName,addedTime FROM t_user where date_format(addedTime,'%Y-%m')=date_format(DATE_SUB(curdate(), INTERVAL 1 MONTH),'%Y-%m');   
-- 查询当前月份的数据  
select fullName,addedTime FROM t_user where DATE_FORMAT(addedTime,'%Y%m') = DATE_FORMAT(CURDATE(),'%Y%m');  
select fullName,addedTime FROM t_user where date_format(addedTime,'%Y-%m')=date_format(now(),'%Y-%m');   
  
-- 查询指定时间段的数据  
select fullName,addedTime FROM t_user where addedTime between  '2017-1-1 00:00:00'  and '2018-1-1 00:00:00';     
select fullName,addedTime FROM t_user where addedTime >='2017-1-1 00:00:00'  and addedTime < '2018-1-1 00:00:00';  
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
 
