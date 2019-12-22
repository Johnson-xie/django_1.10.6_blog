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

## select null + any结果为null  
```  
-- select ISNULL(NULL);
-- select ISNULL(10);
-- 
-- select IFNULL(null,30);
-- select IFNULL(20,30);
-- 
-- select CONCAT('helll', ' ', 'world');
-- select CONCAT('helll', ' ', 10);
-- 
-- select 30 where 10 != 10;
-- select 30 where 10 <> 10;
/*
-- &&   and
-- ||   or 
-- !    NOT
-- 支持对数字和字符的查询
-- select 10 where field like '1__'

select *, 计算表达式 as something
from TABLE
order by something;

select length(field);


##  函数
```  


```  
单行函数
concat isnull length

字符函数
length 获取的是字节长度
upper('hello')
lower('world')




多行函数
avg sum count max min 

*/
/*
-- sql索引从1开始的
select substr('hello world', 5) as name;
-- sql索引从1开始的
select substr('hello world', 1, 5) as name;

select instr('helllworld', 'world');
*/
select concat(trim('  hello world  '), 20);
select concat(trim('a' from 'aaa  hello world  aaa'), 20);
select concat(trim('aa' from 'aaa  hello world  aaa'), 20);
select lpad('xie', 10, '*');
select replace('johnson', 'john', 'jack');
select replace('johnson johnson john', 'john', 'jack');

/*
-- 数学函数
select round(1.2222, 2);
-- 向上取整
select ceil(1.02);
select ceil(1.00);
floor向下取整

truncate截断
mod取余
*/
-- 日期函数
select now();

-- curdate();
-- curtime();

select year(now());
select month(now());
select monthname(now());

select str_to_date('1992-10-05', '%Y-%m-%d');
-- date_format();

select VERSION();
select database();
select user();

/*
-- 流程控制函数
-- IF；

case 字段或表达式
when contant case 显示的值或表达式；
when contant case 显示的值或表达式；
when contant case 显示的值或表达式；
else 显示值或字段；
end;

if else
*/
-- 支持排序的都可以使用max min分组函数
-- 分组函数忽略null值
-- count 计算非空函数

-- select sum(distinct field);

# 多行函数返回的都是一行，和group by一起用返回多个
datediff(now(), 'lf');

# 分组前筛选和分组后筛选


```  


