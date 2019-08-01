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

2019-07-23

建立一个关联表作为说明
create table `bug_state`(
state_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
state VARCHAR(10)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;  # 建表也要指定编码方式

insert into `bug_state`(state_id,state) values 
(0, "未同步提单"),
(1, "已同步提单"),
(2, "非问题");

1.建表
2.插入数据
3.修改原有表的外键关联

alter table bug_trace add constraint `sync_dts` foreign key (`sync_dts`) REFERENCES `dts_state` (`state_id`);
desc bug_trace;

django模板语言注释掉不管用，删除花括号
git log获取相关信息
f'git log  --no-merges --format="%nemail=%ae%nuser=%an%ncommit_time=%ai%nhash=%H"  --numstat --since="{pre_str}" --until="{now_str}"'

pycharm 三个快捷键， 
第一个格式化： ctrl + alt + L, 
第二个，规整引入： ctrl +alt +o,crl+alt+i


问题：撤销暂存区的修改

git commit -am "合并提交"
解决冲突后，直接git add file就如库了

git stash clear清空stash

创建生产库的表tbl_perf_monitor_guarder

git stash apply number 
stash不会删除掉

2019-07-23
1.展示方式，是否需要跳转；
2.清楚多余的修改，包括权限和跳转击鼓传花url；
3.扩展到roll release

2019-07-24
1.ci模块下，持续交付，版本信息；
2.脚本刷新抓取的是bug表的信息，所以查取的是bug表模型；

beyond compare快速复制

2019-07-25
git diff HEAD~1 当前的(包括没有提交的)   和上一次commit对比(最新的第二个commit)
git diff HEAD  当前修改未提交  与已修改提交最新的commit对比
git 多次fix
git 本地回退
git push -f
修改后重新push

django 模板注释
单行注释：
使用 {#  #} 单行注释，例如:
{# Everything you see here is a comment. It won't show up in the HTML output. #}
多行注释：
{% comment %} this is a comment {% endcomment %}

查看当前详细分支信息（可看到当前分支与对应的远程追踪分支）:
git branch -vv
查看当前远程仓库信息
git remote -vv
需求分支放太久，就git pull origin master一下

前端减掉原有属性的作用
herf="javascript:void(0)"
action="javascript:void(0)"

single同步提单需求步骤
1.查看同步提单到数据库的数据；
2.击鼓传花提交的字段信息；
3.脚本刷击鼓传花表时刷了哪些数据到dts数据单；
4.绕过击鼓传花表单；

问了杨萍接口，所有问题就解决咯

js 三目运算

api 中接口api/dts/dts_lading/

已下情况的提交方式是怎么提交的ajax
req = json.loads(request.body)

选择图标的本地文件服务器

        $.ajax({
            type: 'POST',
            url: '/api/dts/dts_lading/',
            headers:{'Content-Type':"application/json"},
            dataType: 'json',
            data: {
                'type_name': type_name,
                'version_c':version_c,
                'version_b': version_b,
                'severity_level':severity_level,
                'desc_brief':desc_brief,
                'desc_detail':desc_detail,
                'creator': creator,
                'next_handler':next_handler,
                'detail_version_id':detail_version_id,
                'label':label
            },
        });

ajax发送请求到post接收

request.body接收到的是字节
var formdata = {
                    'type_name': type_name,
                    'version_c':version_c,
                    'version_b': version_b,
                    'severity_level':severity_level,
                    'desc_brief':desc_brief,
                    'desc_detail':desc_detail,
                    'creator': creator,
                    'next_handler':next_handler,
                    'detail_version_id':detail_version_id,
                    'label':label
                };
        $.ajax({
            type: 'POST',
            url: '/api/dts/dts_lading/',
            headers:{
                'Content-Type': 'application/json',
                'contentType': 'application/x-www-form-urlencoded; charset=UTF-8'},
            dataType: 'json',
            data: JSON.stringify(formdata),
            
            async: true,
            success: function(data) {
                if (data.statue === 'ok') {
                    mtsAlert(data.msg);
                    window.location.href = '/ci/daily/{{version.version_alias}}';
                } else {
                    mtsAlert(data.msg);
                }
                $('#prorele_weekl_btn').removeAttr("disabled");
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                $('#prorele_weekl_btn').removeAttr("disabled");
            }
        });

2019-07-26
1.必填字段前端进行验证
2.提交的数据和杨萍确认；
3.修改ajax提交方式
4.约束版本C

python console 右键清屏
struct学习

form表单button type='button'不会提交表单

INSERT INTO `webtest`.`tbl_dts_version` (`version_c`) VALUES 
('5G RAN V100R002C10'),
('5G RAN V100R003C00'),
('5G RAN V100R002C11');

create table tbl_dts_version (
id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
version_c VARCHAR(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

暂时先写死了
之前的label来自bug
dts_label_list = Bug_info.objects.using('db_bug_trace').filter(bug_label__in=label_list, bug_sync_dts=1).values_list('bug_label', flat=True)


前端总结

周一 提单

2019-07-28
性能防线场景下拉框优化
dts_id  dts  中type_id和label的关系


2019-07-27
信息比对
1.版本名 比对
2.license 比对
3.新增 比对 记录
4.新增 加文档

多人开发一个分支，经常性拉取最新，更新本地到最新再推；


git pull更新代码后
git diff HEAD~1  查看更新详情

问题perssion是什么时候渲染的？？？


2019-07-29
基础性能防线，增加相关人员权限，修改列表
提醒菡阁提单操作流程




2019-07-29

提单步骤：
1.check_lading...关闭
2.dts_action打开，运行脚本
3.检查
    动态检查 一行一个单
    codex
    安全编码 静态  动态
4.check_lading打开提单

阅读书籍的时候，读完一章再回过头重新看一下这一章，第一遍可以多敲代码


模型类中User的groups字段直接对应的就是tbl_user_groups的身份表
session提取用户信息

user_id = request.session.get("user_id", "anonymous")
maintainers = User.objects.filter(groups=13).values_list('user_id', flat=True)

指定单个文件，查看不同点
git diff HEAD~1 perf_monitor/views.py

2019-07-30
解决冲突后，拉取最新主干分支到当前分支
解决冲突，
<<<<<<<<<<<<
自己写的内容
===========
别人写的内容
>>>>>>>>>>
修改后add
然后commit
push 

raw(select * from myapp_model默认表名)
log.info内容的站位符，后面全部用逗号隔开入参就可以
log.info('%s,%s',var1,var2)

2019-07-31

多对多表的查询
SELECT tu.user_id,tu.name_chs,tug.group_id
from tbl_user as tu, tbl_user_groups as tug
where tu.id=tug.user_id 
and tug.group_id=13;

关注dts单流程与页面展示接口

脚本刷数据
drumming_flower()  bug---->tbl_dts

脚本刷数据，5分钟跑一下
check_lading()     tbl_dts----->提单返回状态和DTS单号


调接口数据直接到tbl_dts单   ---- /api/dts/dts_lading/
接口并没有type_id这个字段
    击鼓传花该字段为bug的主键id字段；

web dts展示界面接口  ---/dts  获取tbl_dts数据表并展示数据

哪些是运维用户？

codeclub接口

一秒一次
从来没有统计过的库比较多commit信息


HSHfzhx4KWMx2xanPm_c
个人Token查询
http://code.huawei.com/profile/personal_access_tokens

1.获取merge信息
http://code.huawei.com/api/v3/projects/Polestar_CID%2Fweb/merge_requests/?target_branch=master&state=merged&order_by=updated_at&sort=desc&more_info=True

2.根据merge信息获取commit信息
http://code.huawei.com/api/v3/projects/Polestar_CID%2Fweb/merge_requests/2325618/commits?page=1&per_page=5

3.commit id 获取详情信息
http://code.huawei.com/api/v3/projects/Polestar_CID%2Fweb/repository/commits/d4cc3291978896e1e9ed91442a7e3921050d57de

原条件

2019-08-01
http://code.huawei.com/api/v3/contributions/projects/18193?private_token=PRIVATETOKEN&start_time=2016-12-01%2000:00:00%20+0800&end_time=2016-12-07%2023:59:59%20+0800

返回最新的commits信息
http://code.huawei.com/api/v3/projects/Polestar_CID%2Fweb/repository/commits/?more_info=true

post将下载json存为json文件

with open(r"C:\Users\xwx620452\Desktop\response.json", 'r', encoding='utf-8') as f:
    d = json.load(f)
from pprint import pprint
pprint(d)
len(d)    

url = "http://code.huawei.com/api/v3/projects/Polestar_CID%2Fweb/repository/commits/"
headers = {"PRIVATE-TOKEN": "HSHfzhx4KWMx2xanPm_c", "more_info": "true", 'page': '1', 'per_page': '4000'}
ret = requests.get(url, headers=headers)

https 拉代码前设置全局
git config --global http.sslVerify false
遇到错误就谷歌










