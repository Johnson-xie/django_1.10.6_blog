## 以下这两种方式最终效果一样  
```  
SELECT bb.borrow_no,bb.create_time FROM borrow bb WHERE bb.create_time>='2018-09-11 00:00:00';  

SELECT bb.borrow_no,bb.create_time FROM borrow bb WHERE bb.create_time>='2018-09-11';  
```  
## 如何查询某一天(2018-09-10)  
* 正确方法
```  
SELECT bb.borrow_no,bb.create_time FROM borrow bb WHERE bb.create_time>='2018-09-10' and bb.create_time <='2018-09-11';  
```  

* 错误方法  
```  
SELECT bb.borrow_no,bb.create_time FROM borrow bb WHERE bb.create_time='2018-09-10';  
```  
## 查询最近几天的信息  
* 2018-09-11 17:53:06  
```select NOW();```  

* 函数CURRENT_DATE()  
```select CURRENT_DATE();```  

## 查询当日结果  
```  
SELECT * FROM borrow bb WHERE DATE_FORMAT(bb.create_time, '%Y%m%d')=DATE_FORMAT(CURRENT_DATE(), '%Y%m%d' );

SELECT * FROM borrow bb WHERE TO_DAYS(bb.create_time)=TO_DAYS(now());
```  

## 查询昨日结果  
```  
SELECT * FROM borrow bb WHERE TO_DAYS( NOW( ) ) - TO_DAYS( bb.create_time) =1;
```  

## 查询近7天的数据  
```  
SELECT * FROM borrow bb WHERE TO_DAYS( NOW( ) ) - TO_DAYS( bb.create_time) <= 7;  
SELECT bb.borrow_no,bb.create_time FROM borrow bb where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(bb.create_time);  
```  

## 查询本月的数据  
```  
SELECT * FROM borrow bb WHERE DATE_FORMAT( bb.create_time, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' );  
```  

## 查询上月数据  
```  
SELECT * FROM borrow bb WHERE PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( bb.create_time, '%Y%m' ) ) =1  
```  

