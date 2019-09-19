
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
**limit 2,1**  等价于   **limit 1 offset 2**  
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

## mysql 如何用一个表的字段填充另一个表  
* 连表查询，将code_base_update_record中的last_revision字段填充到code_base_info里的last_revision字段中
```  
UPDATE code_base_info 
INNER JOIN `code_base_update_record`
ON code_base_info.id=code_base_update_record.code_base_id
SET code_base_info.last_revision=code_base_update_record.last_revision;  
```
 
 ## 获取表中分组后各组最新的一条数据
 ```  
 select *
from
(SELECT *
FROM `code_base_update_record`
order by `update_time` desc) as tb1
group by tb1.code_base_id
order by tb1.`update_time` desc;  
```  

## 根据字段长度查询  
```  
update `code_base_info` 
set last_revision=''
where length(last_revision)<=8;
```

## 计数  
`select count(*) from tbl`  
`select count(distinct field) from tbl`

# sql关联查询外键字段  
```  
sql = "SELECT gb.id, gb.title, gpx.group_name, gb.state, gb.post_time, ur.userid, ur.name_chs " \
      "FROM `bug` as gb " \
      "inner join `group_x` as gpx " \
      "on gb.cur_groupid=gpx.id " \
      "left join `user` as ur " \
      "on gb.doer=ur.id  " \
      "where gb.id in (%s)" \
      "order by gb.post_time desc;" % ids
bug_detail = Bug_info.objects.using('bug').raw(sql)
```

## 查询到的一张表的值作为另一张表的查询条件获取更改条件  
* 使用其他表中查到的值必须使用inner join  
* inner join可以没有on的条件  
* 必要时内联多张表，分别使用各自属性值
```  
update tbl_domain as td 
inner join (select id from tbl_user where user_id="q00391896") as new 
inner join (select td.id from tbl_group as tg inner join tbl_domain as td on tg.id=td.group_id where tg.`name`='产品二部 基站公共' and td.`name`='L2_MDE') as new2 
set td.pl=new.id 
where td.id=new2.id;
```  

* sql中各属性不用分号，入关与关键字冲突，可以使用反引号或不用  
```  
INSERT INTO `tbl_user`(`user_id`, `role`, `name_chs`, `name_eng`, `email_address`, `mobile_number`,`login_number`, `group`, `domain_id`, `is_superuser`, `username`, `is_staff`, `is_active`)
VALUES('123456', 'guest', 'johnson', 'chenziwei', 'johnson@163.com', '13438490248', 0, 41, 179, 0, 'xwx1452', 0, 1)
```  
* 刷数据库时，先使用硬编码sql语句，开刷后使用for循环模板语法替换


## 根据字段分组筛选分组后大于某个值的分组名  
```  
SELECT target_id, count(target_id) as count
FROM `tbl_perf_record`
group by target_id
having count(target_id)>3;
```

## 连表生成新的表后，用已有新字段再进行连表查询  
```  
-- 已有角色所在分组与domain
select new.id, new.user_id, new.name_chs, new.email, new.`group`, new.domain, ag.`name`
from auth_group as ag
inner join
(select tu.id as id, tu.user_id as user_id, tu.name_chs as name_chs, tu.email_address as email, tg.`name` as `group`, td.`name` as domain, tug.group_id
from tbl_user as tu left join tbl_user_groups as tug on tu.id=tug.user_id
left join tbl_group as tg on tu.`group`=tg.id
left join tbl_domain as td on tu.domain_id=td.id and tg.id=td.group_id
where (tug.group_id is not null) and tu.user_id<>'') as new
on ag.id=new.group_id;
```

## 外键约束影响删除  
* 先取消约束，删除，再回复约束  
```  
SET FOREIGN_KEY_CHECKS=0; 
delete from tbl_perf_scene where id in (63, 64,65,66,67);
SET FOREIGN_KEY_CHECKS=1; 
```



