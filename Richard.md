2019-07-10
perf_monitor----->drumming

drumming
改后台视图url到本地击鼓传花
理清之前的流程，然后添加label


web去击鼓传花数据库获取数据，每条数据有状态，展示在web界面；
根据前端已经获取的label，拼接传入击鼓传花的数据库，
已有数据库，添加一个字段label-----------alter table `bug` add label varchar(32);
后端获取state , label
php段隐藏表单中字段----＜input type="hidden" name="..." value="..."＞ 

解BUG:
    改后很久出现的错误----(1054, "Unknown column 'bug.label' in 'field list'")
    删除字段
    alter table `bug` drop column label; 
    修改字段
    alter table `bug` add label varchar(32);
    去掉模型中的字段后正常了？？
    项目中其他地方用使用了该模型查询生产库，而生产库没有添加该字段，生产库填完该字段后应该不会报错
    启动全局搜素找到原因咯
结论：
    数据库的模型字段要和数据库字段对应，一旦调用模型时，与数据库不匹配就会报1054错误。

页面数据来自mongo,每条数据是否显示击鼓传花信息，取决于击鼓传花数据库；
目前页面数据来自于生产库，显示取决击鼓传花开发库，只要在开发库里添加信息就可以咯；

1.测试，弄清哪里的数据来自生产库，哪里的来自测试库，弄清配置与id----弄清数据库的关联性；
2.遇到要权限的地方测试，如果是前端的要权限，直接注释掉再测试；


2019-07-11
1.搞个定时任务触发脚本推包看uci还是time.sleep;
2.爬去web数据；


2019-07-15
1.前端表单为选择标签；
2.选择的数据来自后台给的数据；

？从第二列开始填补；
删除功能；
自动填充后端来的数据到选择标签；
自定义属性data-xxx
readonly="readonly" 只读
前端input 属性写错 reamark,后台form验证失败。

获取到指定列的数据；
'columnDefs': [
                {
                    targets: 0,
                    createdCell: function(cell, cellData, rowData, rowIndex, colIndex) {
                        $(cell).on('click', function() {
                            var guarder_id = rowData.id;
                            select_guarder(guarder_id);
                        });
                    }
                }
            ]

2019-07-16

添加css标签将提示模态框展示
数组使用autocomplete自动提示并填充；
$("#id").autocomplete({
    source: user_ids
});


4RULSIH54N-eyJsaWNlbnNlSWQiOiI0UlVMU0lINTROIiwibGljZW5zZWVOYW1lIjoiMjA5OSAxODExIiwiYXNzaWduZWVOYW1lIjoiIiwiYXNzaWduZWVFbWFpbCI6IiIsImxpY2Vuc2VSZXN0cmljdGlvbiI6IkZvciBlZHVjYXRpb25hbCB1c2Ugb25seSIsImNoZWNrQ29uY3VycmVudFVzZSI6ZmFsc2UsInByb2R1Y3RzIjpbeyJjb2RlIjoiSUkiLCJwYWlkVXBUbyI6IjIwMTktMTEtMjcifSx7ImNvZGUiOiJBQyIsInBhaWRVcFRvIjoiMjAxOS0xMS0yNyJ9LHsiY29kZSI6IkRQTiIsInBhaWRVcFRvIjoiMjAxOS0xMS0yNyJ9LHsiY29kZSI6IlBTIiwicGFpZFVwVG8iOiIyMDE5LTExLTI3In0seyJjb2RlIjoiR08iLCJwYWlkVXBUbyI6IjIwMTktMTEtMjcifSx7ImNvZGUiOiJETSIsInBhaWRVcFRvIjoiMjAxOS0xMS0yNyJ9LHsiY29kZSI6IkNMIiwicGFpZFVwVG8iOiIyMDE5LTExLTI3In0seyJjb2RlIjoiUlMwIiwicGFpZFVwVG8iOiIyMDE5LTExLTI3In0seyJjb2RlIjoiUkMiLCJwYWlkVXBUbyI6IjIwMTktMTEtMjcifSx7ImNvZGUiOiJSRCIsInBhaWRVcFRvIjoiMjAxOS0xMS0yNyJ9LHsiY29kZSI6IlBDIiwicGFpZFVwVG8iOiIyMDE5LTExLTI3In0seyJjb2RlIjoiUk0iLCJwYWlkVXBUbyI6IjIwMTktMTEtMjcifSx7ImNvZGUiOiJXUyIsInBhaWRVcFRvIjoiMjAxOS0xMS0yNyJ9LHsiY29kZSI6IkRCIiwicGFpZFVwVG8iOiIyMDE5LTExLTI3In0seyJjb2RlIjoiREMiLCJwYWlkVXBUbyI6IjIwMTktMTEtMjcifSx7ImNvZGUiOiJSU1UiLCJwYWlkVXBUbyI6IjIwMTktMTEtMjcifV0sImhhc2giOiIxMTA3MzgwNy8wIiwiZ3JhY2VQZXJpb2REYXlzIjowLCJhdXRvUHJvbG9uZ2F0ZWQiOmZhbHNlLCJpc0F1dG9Qcm9sb25nYXRlZCI6ZmFsc2V9-rlH9JbPzbld/Oak51Co3HlhD6xgE7CsvbrLl6RCySuv2sw37KBfDPY1PT2lAEkW0MJkUtGtmSHVp/jk8F4RuHGvouJFMdCtnsKdnebdjaPsKpjgxoreWlOu8VCnrGh+3mmuswzGKouw52ffxbmsvGFa5ybvWv7mj9gqSY0V20OcgCmIT3dlj4f9xc0iA9o7z1pvedVzcOrxVKvLmmqRp+4zMfNuMQB5sraznW9BxslR1sWN0pUOu9/J+k7IH6Wld/oGv5dtHYFqk5RinSBMTjYlZ+X4AV5f83Z4SkzbHqy2fGC6S3NoifaVFxRSP5TQDe6hsg7Fzic6k1iWAup89pg==-MIIElTCCAn2gAwIBAgIBCTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTE4MTEwMTEyMjk0NloXDTIwMTEwMjEyMjk0NlowaDELMAkGA1UEBhMCQ1oxDjAMBgNVBAgMBU51c2xlMQ8wDQYDVQQHDAZQcmFndWUxGTAXBgNVBAoMEEpldEJyYWlucyBzLnIuby4xHTAbBgNVBAMMFHByb2QzeS1mcm9tLTIwMTgxMTAxMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxcQkq+zdxlR2mmRYBPzGbUNdMN6OaXiXzxIWtMEkrJMO/5oUfQJbLLuMSMK0QHFmaI37WShyxZcfRCidwXjot4zmNBKnlyHodDij/78TmVqFl8nOeD5+07B8VEaIu7c3E1N+e1doC6wht4I4+IEmtsPAdoaj5WCQVQbrI8KeT8M9VcBIWX7fD0fhexfg3ZRt0xqwMcXGNp3DdJHiO0rCdU+Itv7EmtnSVq9jBG1usMSFvMowR25mju2JcPFp1+I4ZI+FqgR8gyG8oiNDyNEoAbsR3lOpI7grUYSvkB/xVy/VoklPCK2h0f0GJxFjnye8NT1PAywoyl7RmiAVRE/EKwIDAQABo4GZMIGWMAkGA1UdEwQCMAAwHQYDVR0OBBYEFGEpG9oZGcfLMGNBkY7SgHiMGgTcMEgGA1UdIwRBMD+AFKOetkhnQhI2Qb1t4Lm0oFKLl/GzoRykGjAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBggkA0myxg7KDeeEwEwYDVR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0PBAQDAgWgMA0GCSqGSIb3DQEBCwUAA4ICAQAF8uc+YJOHHwOFcPzmbjcxNDuGoOUIP+2h1R75Lecswb7ru2LWWSUMtXVKQzChLNPn/72W0k+oI056tgiwuG7M49LXp4zQVlQnFmWU1wwGvVhq5R63Rpjx1zjGUhcXgayu7+9zMUW596Lbomsg8qVve6euqsrFicYkIIuUu4zYPndJwfe0YkS5nY72SHnNdbPhEnN8wcB2Kz+OIG0lih3yz5EqFhld03bGp222ZQCIghCTVL6QBNadGsiN/lWLl4JdR3lJkZzlpFdiHijoVRdWeSWqM4y0t23c92HXKrgppoSV18XMxrWVdoSM3nuMHwxGhFyde05OdDtLpCv+jlWf5REAHHA201pAU6bJSZINyHDUTB+Beo28rRXSwSh3OUIvYwKNVeoBY+KwOJ7WnuTCUq1meE6GkKc4D/cXmgpOyW/1SmBz3XjVIi/zprZ0zf3qH5mkphtg6ksjKgKjmx1cXfZAAX6wcDBNaCL+Ortep1Dh8xDUbqbBVNBL4jbiL3i3xsfNiyJgaZ5sX7i8tmStEpLbPwvHcByuf59qJhV/bZOl8KqJBETCDJcY6O2aqhTUy+9x93ThKs1GKrRPePrWPluud7ttlgtRveit/pcBrnQcXOl1rHq7ByB8CFAxNotRUYL9IF5n3wJOgkPojMy6jetQA5Ogc8Sm7RG6vg1yow==

php修改
走原流程，看数据库的变化;
单选框;
根据选框值进行判断
学习php


未解决的问题：
1.建一张关联备注表；
2.dts同步提单携带版本号和label;  ----提单接口
latin-1解码永远不会报错


2019-07-16
对接张菡阁：
1.工具部署；
2.前端效果；
3.基础性能防线暂时接口人；
4.需求转测与澄清补发
同步提单按钮找dts提单；

问题：本地apache如何放文件进去,访问地址；
解决：目前配置的路径为击鼓传花项目首页，将文件放到击鼓传花项目配置路径，使用击鼓传花配置的ip与port进行访问；



2019-07-17

脚本，刷数据库

1.获取数据excel数据；
2.备份数据库表命令；
3.链接数据库，进行插入替换；

纠错：
    关键字参数报错，入参需要和关键字形参对齐，而不是内部属性对齐；


刷库到code_base_info
navicat 红色字样代表报错，字段相当于属性，直接使用

sql语句插入模板
数据读取与清理 pandas
拼接，链接数据库执行

学习：学些sql语句书籍

1.关联添加字段
2.连表关联修改

sql查看表如何创建的:  show create TABLE `tbl_group`;

重设为0
UPDATE tbl_user 
set `group`=0,`domain_id`=0 
where `group` in (30,13,14,34,33);


很多置为0的user，需要解决；



2019-07-18
1.学习pymysql

筛选比对
arr = ['a', 'b', 'c']
df[df["column"].isin(arr)]

1.设置对应user group domain_id =0
select *
from tbl_user as tu
inner join tbl_group as tg
on tu.group=tg.group_id
where tg.name in ('UE开发', '开发二部 成都-L2', '开发二部 成都-L3', '开发二部', '基站产品二部');

select *
from tbl_user 
where `group` in (13, 14, 30, 33, 34);

2.group设为0
3.刷数据库
4.确认重复人员


如果是pl

select id from tbl_user where user_id="q00391896";

update tbl_domain
set pl=(select id from tbl_user where user_id="q00391896")
where id=(select td.id from tbl_group as tg inner join tbl_domain as td on tg.id=td.group_id where tg.`name`='产品二部 基站公共' and td.`name`='L2_MDE')


(select td.id from tbl_group as tg inner join tbl_domain as td on tg.id=td.group_id where tg.`name`='产品二部 基站公共' and td.`name`='L2_MDE');

2019-07-18
1.明天来测label能否关联上
2.整理击鼓传花代码

2019-07-19

1.数据库作为中间接口；---一个人放，脚本定时去取；

mysql添加多个字段
alter table `tbl_dts` add (
`detail_version_id` varchar(200), 
`label` varchar(200)
);

远端未受保护分支回退

1.本地回退---git reset --hard~1
2.git push -f(未默认上游分支的git push -u origin master -f  )
3.本地前进:
    git reflog --oneline
    git reset --hard commit_id
    git commit
4.推送git push

2019-07-22
同步最新的070102修改内容
git stash list
git stash pop num
git stash save 'm'

task 重新调整dts_static脚本

击鼓传花需求
添加关联表作解释
detail_version_id` label这两个字段在击鼓传花同步提单的方式是通过后台查询数据库，再拼装插入，如果后续有问题，可以在前端查询数据库放入表单再提交；

修改字段sql   
alter table `bug_trace`
modify column root_cause varchar(10);

pylint 113次扫描  http://100.106.248.198:3000/projects/web_uci_project/builds/111?t=924  br_uci_report

2019-07-22
1.认领pylint；
2.基础性能防线；




