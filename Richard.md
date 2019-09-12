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

2019-08-02
checkin工具交付

checkin相关维护，问题定位

基础性能防线优化
权限表维护检查
查看指定节点后的log日志，格式化输出
git log 90b4afe865066f04dc44f4ae2203dadf9e43d721..HEAD  --no-merges --format="%nemail=%ae%nuser=%an%ncommit_time=%ai%ncommit_info=%s%nhash=%H"  --numstat
git log 955cf85b1ea9319f0c2eedba9e182c09ffaed858..HEAD  --no-merges --format="%nemail=%ae%nuser=%an%ncommit_time=%ai%ncommit_info=%s%nhash=%H"  --numstat
查看库下日志，格式化
git log --no-merges --format="%nemail=%ae%nuser=%an%ncommit_time=%ai%ncommit_info=%s%nhash=%H"  --numstat
git 获取日志信息的办法

1. codeclub 获取整个commits信息 hash_key: {}
2. mysql获取已提交信息 {hash_key}
3. git log根据code_base_info last_revision获取没有上库的hash_key
4. 根据3中未上库的信息，查找user_id，组装大的sql语句
5. 一次性插入库


mysql备份数据库表
create table user_commit_record_copy_xq as select * from usr_commit_record;
原表3148条
DELETE FROM usr_commit_record WHERE code_base_id=44;


zip(*values)

2019-08-05
一张表里的数据不在另一张表里，确定一下，多数据的在前面
select  *  
from  user_commit_record_copy_xq AS xq  
where xq.code_base_id=44
and xq.hash_key  NOT IN(select  usr_commit_record.hash_key  from usr_commit_record  where code_base_id=44);


导出excel表
1.sql语句；
2.导出excel;
3.pandas对比；

SELECT tu.user_id, tu.name_chs, tg.`name`, td.`name`
FROM `tbl_user` as tu,tbl_group as tg, tbl_domain as td
where tu.`group`=tg.id
and tg.id=td.group_id
and tu.domain_id=td.id
and tu.`group`=35;


后台提单接口先接收，前台可以使用页面表单或ajax发起请求；

2019-08-05

多选插件 是一个对象
部署新工具，推包

2019-08-06
checkin工具优化转测邮件


制作表单
涉及数据库


弹出框中插入input标签，场景在数据库中获取；
数据库行场景固定，其他行可以自行编辑；

创建外键表
create table `tbl_perf_guarder`(
id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
version VARCHAR(10),
scenes_id int,
guarder varchar(10),
remark VARCHAR(255),
foreign key(scenes_id) references tbl_perf_scene(id)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;


select tpg.id, tpg.version, tpg.remark, tps.scene_name, tu.user_id, tu.name_chs 
from tbl_perf_guarder as tpg inner join tbl_perf_scene as tps on tpg.scenes_id=tps.id 
left join tbl_user as tu on tpg.guarder=tu.user_id 
where tpg.version="20A" 
order by tps.scene_name;

'id', 'remark', 'scene_name',  'user_id', 'version', 'name_chs'
模态框中的表格二次打开宽度变化，表格中宽度写死就没有变化了
{'data': 'version',
    'render': function (data, type, row, meta) {
        return '<input id="' + row.id + '_version' + '" style="width:40px;" value="' + data + '" readonly>';
    }
},

模态框高度调整https://blog.csdn.net/u014326004/article/details/69789187
<div class="modal fade" id="tb_guarder" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog" style="width:980px;height:900px">
        <div class="modal-content">

从session取值
# user_id = request.session.get("user_id", "anonymous")
# person = User.objects.get(user_id=user_id)

'initComplete': function (settings){
                $('.select_user').autocomplete({
                source: users
                });
            }

.ui-autocomplete {
    z-index: 1050;
    max-height: 320px;
    overflow : auto;
}

模态框提示在下面，调整到上面

2019-08-07

select tps.id, tps.scene_name, tu.user_id, tu.name_chs from tbl_perf_guarder as tpg, tbl_perf_scene as tps ,tbl_user as tu where tpg.scenes_id=tps.id and tu.user_id = tpg.user_id and tpg.version='20A';

select distinct tpt.scene_name, tpt.id, tu.user_id, tu.name_chs from tbl_perf_scene as tpt left join tbl_perf_target as tps on tps.scene_id=tpt.id left join tbl_perf_guarder as tpg on tpt.id=tpg.scenes_id left join tbl_user as tu on tu.user_id=tpg.user_id where tps.display=1 and tps.version =22 and tpg.version='20A' order by tps.id;

select tps.scene_name, tps.scene_desc, tpt.id, tpt.target_name, tpt.lower_limit, tpt.upper_limit, tpt.name_related
from tbl_perf_target tpt
join tbl_perf_scene tps on tpt.scene_id=tps.id
where tpt.display=1 and tpt.version = 22
order by tps.id asc,tpt.id asc;


select tps.scene_name, tps.scene_desc, tpt.id, tpt.target_name, tpt.lower_limit, tpt.upper_limit, tpt.name_related, tu.user_id, tu.name_chs from tbl_perf_target as tpt join tbl_perf_scene as tps on tpt.scene_id=tps.id left join tbl_perf_guarder as tpg on tps.id=tpg.scenes_id left join tbl_user as tu on tu.user_id=tpg.user_id where tpt.display=1 and tpt.version=22 and tpg.version='20A' order by tps.id asc,tpt.id asc;

subprocess.Popen(cmd)输出编码问题
>>> import locale
>>> locale.getdefaultlocale()
('zh_CN', 'cp936')

import locale
cmd = cmd.encode(locale.getdefaultlocale()[1])
subprocess.Popen(cmd)
设置->首选项->语言->右下角 替换为空格

312库

$('#id').siblings() 当前元素所有的兄弟节点
$('#id').prev() 当前元素前一个兄弟节点
$('#id').prevaAll() 当前元素之前所有的兄弟节点
$('#id').next() 当前元素之后第一个兄弟节点
$('#id').nextAll() 当前元素之后所有的兄弟节点

坚持刷OJ

2019-08-7
前端展示问题
权限问题
单个运维人到多个

git reset --hard  回到当前版本

需求：监听mongo数据
1.数据来自mongo,通过web的接口获取数；

2.网页前端效果和后台接口比对数据；

3.pycharm console 调试接口


发邮件的接口api send_mail_service

2019-08-09
调整标签对齐位置
<a href="javascript:void(0)" onclick="show_guarder('20A')" style='float:right;margin-top:7px;margin-right:5px;'>看护责任人</a>
修改长度
alter table `tbl_perf_guarder` modify user_id varchar(200);



周一
击鼓传花隐藏label

create table `tbl_perf_guarder`(
id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
version VARCHAR(10),
scenes_id int,
field varchar(100),
user_id varchar(200),
remark VARCHAR(255),
foreign key(scenes_id) references tbl_perf_scene(id)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

2019-08-12

部署fossid 20B
登入部署的机器
查看各参数和调用的任务
复制替换，询问代码路径
现获取所有目录，然后看子目录

删除 Software: tiny-AES-c
增加 Software: Newlib

链表，手动插入表数据19B 20A


2019-08-14

django重构击鼓传花
击鼓传花定位
基础性能防线优化-前端优化
冯骋工具word
fossid 工程维护 <property name="PBI_IDS" value="23247136"/>   OK






http://5g.rnd.huawei.com/BugTrace/?/bugtrace/view/605/
DB Error, could not query the database MySQL Error: Unknown column 'z00241929' in 'where clause'Error Query: select detail_version_id, label from bug_trace where bugid=z00241929 order by post_time desc limit 1

周三之前
2019-08-15
转测加个背景
开发背景：提升生命周期交付件质量，准确输出开源软件声明，需开发license自动比对
提升确认效率

正则表达式
group(0)表示取全部
group(1)表示取第一个括号

2019-08-16

输出另一个修改后的文件  OK
调整格式  OK
配置执行文件直接放到源文件路径  OK
增加输出路径  OK
5G是否使用，如果没有，就都使用  OK

【请假告知】请假2019/8/16 因个人急事请假0.5天，工作无委托，如有事情请电话联系13438490248，给大家带 
来的不便敬请谅解，谢谢！

2019-08-19
dts提单脚本添加20B版本

2019-08-20

适配版本空间
我们这边是根据email或user_id来找id值的
email和user_id均来自codeclub,codeclub的数据来自git log配置；

模板中的上下文在模板上下文设置中

2019-08-21
OJ 60 769

php迁移到django项目

1.原项目页面图分析(首页，bug列表页，bug详情页，项目设置页)；

2.根据各页面内容div分析各页面版块，分页面版块需要填充的内容定制后台接口(可以使用google浏览器查看后台数据)；

3.连表sql语句测试，orm返回数据，等序列化；


分析门户模块流程

登录页面
判断是否是post请求，
    1.get请求获取sesstion，看是否登录；
        1.1没有获取到user_id，设置test_cookie，render登录界面；
        1.2从session中获取到了user_id,根据user_id查表，获取用户的姓名，分组,domain，render登录界面；
    2.post请求(输入密码和用户名点击登录)
        1.1验证之前设置的cookie；
        1.2调接口验证用户和密码(从其他华为表取数据)，根据web tbl_user更新bug user的表，登录成功后，前端跳转到首页；

登出api
获取当前session的user_id，从表中删除，重定向到登录视图；


击鼓传花不用登录了，直接可以跳转
CID用户1，普通用户0,可以添加分组

# pylint: disable=W1401,W0403,W0604,W0612,W0603,R0101,E0401,C0103,C0111,C0301

2019-08-23
基础性能防线tbl_perf_target刷展示场景
update tbl_perf_target as tpt
set display=0
where tpt.scene_id=8 and tpt.target_name not in ('VOS_PID_NRCU_RTM=1133','NR_UEMDAEMON','NRCU_UEMWORK1','NRDU_UEMWORK1','NRCU_UEMWORK2','NRCU_UEMWORK3','NRDU_UEMWORK3','NR_OMA2','NR_OMA3','NR_OMA4','NRDU_UEMWORK2','NR_OMA1','NR_ENV');

update tbl_perf_target as tpt
set display=1
where tpt.scene_id=8 and tpt.target_name in ('VOS_PID_NRCU_RTM=1133','NR_UEMDAEMON','NRCU_UEMWORK1','NRDU_UEMWORK1','NRCU_UEMWORK2','NRCU_UEMWORK3','NRDU_UEMWORK3','NR_OMA2','NR_OMA3','NR_OMA4','NRDU_UEMWORK2','NR_OMA1','NR_ENV');

update tbl_perf_target as tpt
set display=0
where tpt.scene_id=9 and tpt.target_name not in ('NR_CFGMASTER','VOS_PID_NRCU_RTM=1133','NR_CECPM','NRDU_CERMC','NR_UECPM','NRDU_UEBPRMC','NRCU_CEIM','NRDU_CEIMC','NRCU_ICEM','NR_TIFM','NRDU_UEUPMC','NR_UEUPA','NR_PAGING','NR_LICM','NRCU_CERRM','NRCU_LNWM','NR_OM','NR_OMA2','NR_OMA4','NRDU_ICEMC','NRCU_ICEMSLAVE','NR_ENV','NR_OMA1');

update tbl_perf_target as tpt
set display=1
where tpt.scene_id=9 and tpt.target_name in ('NR_CFGMASTER','VOS_PID_NRCU_RTM=1133','NR_CECPM','NRDU_CERMC','NR_UECPM','NRDU_UEBPRMC','NRCU_CEIM','NRDU_CEIMC','NRCU_ICEM','NR_TIFM','NRDU_UEUPMC','NR_UEUPA','NR_PAGING','NR_LICM','NRCU_CERRM','NRCU_LNWM','NR_OM','NR_OMA2','NR_OMA4','NRDU_ICEMC','NRCU_ICEMSLAVE','NR_ENV','NR_OMA1');


2019-08-26
# 获取看护人配置，只要显示的场景
select tpg.id, tpg.version, tpg.remark, tps.scene_name, tpg.field, tpg.user_id 
from tbl_perf_guarder as tpg inner join tbl_perf_scene as tps on tpg.scenes_id=tps.id 
left join tbl_user as tu on tpg.user_id=tu.user_id 
where tpg.version='20B' and scenes_id in (24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37) 
order by tpg.id;

# 获取要显示的所有场景
scenes_id = PerfTarget.objects.filter(display=1, version=version_dict[version]).values_list('target_s_id',flat=True).distinct()

# 生产库补齐没有显示的场景

2019-08-27
# 和库之后再执行，还有脚本刷库
insert into tbl_perf_guarder
(version, scenes_id)
values 
('20A', 2),
('20A', 11),
('20A', 13),
('20A', 16);

2019-08-28
击鼓传花跳转(测试环境)，跳转过去到的是生产库，需要改两个地方的配置


be469d4712b5c7a9a1bad959d004c0956b607f05

2019-08-29
切https

checkin脚本  web项目  数据库
requests
urllib.request.urlopen()


import urllib
import requests
url = r'https://code.huawei.com/api/v3/projects/Polestar_CID%2Fweb/repository/commits/'
url = r'http://code.huawei.com/api/v3/projects/Polestar_CID/web/repository/commits/'


HEADERS = {'PRIVATE-TOKEN': 'HSHfzhx4KWMx2xanPm_c'}
params = {'more_info': 'true', 'page': '1', 'per_page': '200', 'ref_name': 'master'}
HTTPS_CRT_FILE = r"D:\wokroom_door\web\mysite\config\ca-bundle.crt"
result = requests.get(url, headers=HEADERS, params=params, verify=HTTPS_CRT_FILE, timeout=60)


request = urllib.request.Request(url, headers=HEADERS)
response = urllib.request.urlopen(request, data=params)

action="?/bugtrace/add/"
表单直接提交问题


select * from tbl_user_groups as tug inner join (select id from tbl_user where user_id="z00355998") as tbl_user inner join auth_group as ag on tug.group_id=ag.id where tug.user_id=tbl_user.id and ag.display=1;
tuple([1,2])
(1, 2)
tuple([1])
(1,)


看护人和场景强绑定，增加一个看护人字段，但是场景又是一对多的？？？
2019-08-30
切换远端库
.gitconfig添加远端库
git remote -v查看
git remote rm origin


2019-09-02
dts同步提单看护
手动插入其他平台dts提单数据，修改击鼓传花状态；
定位dts同步提单失败；
insert into tbl_dts (dts_id, dts_type, type_id, version_R, version_C, version_baseline, desc_brief, desc_detail, creator, next_handler)
values ('DTS2019083103052', 3, 627, 'BTS3900 V100R016', 'BTS3900 V100R016C00', 'BTS3900 V100R016C00B000', 'LN并发模块，CPRIMUX组网，LTE为汇聚方。被汇聚方N侧RRU断链', 'LN并发模块，CPRIMUX组网，LTE为汇聚方。被汇聚方N侧RRU断链', 'zhengyanan 00405918', 'zhengyanan 00405918');

刷新tbl_user用户表

$('.stop-enter').keydown(function(){
    console.log('hello johnson');
    if (event.keyCode==13) {
        return false;
    }
});
jquery enter时间捕捉

2019-09-02

击鼓传花dts单脚本修改；OK
email检查并自动更正；  OK
击鼓传花django后台；  
刷mongo，还没有做完https迁移

USER_ID = 'xwx620452'
PRIVATE_TOKEN = 'HSHfzhx4KWMx2xanPm_c'
HTTPS_CRT_FILE = r"D:\wokroom_door\web\mysite\config\ca-bundle.crt"

(http://|https://)(code-sh.rnd.huawei.com|code.huawei.com)


git reset a4e215234aa4927c85693dca7b68e9976948a35e MainActivity.java
git checkout .
git commit -m "info"

换库以后切换git配置
[remote "origin"]
    url = http://code-sh.rnd.huawei.com/5gcid/web.git 
    fetch = +refs/heads/*:refs/remotes/origin/*

门户测试环境
10.186.87.54：8080
http://10.186.87.54:8080/login/?next=/


ftp上传服务器接口
10.171.25.20 

作为另一个结果的子查询
select id from tbl_perf_scene as tps where tps.id not in (select scenes_id as id from tbl_perf_guarder as tpg where tpg.version='20B'); 

a = PerfGuard.objects.filter(version="20B").values_list('scenes_id',flat=True)
b = PerfScene.objects.values_list('id', flat=True)
b - a

Manager.raw()只能查询，不能插入语句
2019-09-04
击鼓传花新增关联功能
刷基础性能防线数据库
击鼓传花django后台；
上线基础性能防线功能改进

击鼓传花bug添加DTS手动提单字段

1.git rebase -i 不是自己提交的那个最早节点
2.遇到问题解决， 保留最新或旧的commi comment
3.解决冲突，git rebase --continue
4.检查代码，产生了一个新的commit信息


远程回退git push -f
navicat拖拽同步表
alert调试jquery流程

2019-09-05
1.后台接收参数名细看，前端name="dts_doer "多了一个空格造成后台参数名多了一个下划线；
2.数据库改参数，根据依据获取变量，理清调用关系，一层一层往上走的；

修改数据库字段长度
alter table bug_trace modify column root_cause char(10);
alter table bug_trace modify column root_cause_explain char(255);

git reset --hard 强制回到本地head
一般使用git reset HEAD <file>
git rm --cached 文件名 ，可以从缓存区移除文件，使该文件变为未跟踪的状态，

git push -f

git branch -vv
git branch -r
git checkout -b 本地分支名x origin/远程分支名x

查找commit info
#查当前分支
git log | grep "message"——
#查本地的BanchName分支
git log BanchName | grep "message"
#查远程的BanchName分支
git log origin/BanchName | grep "message"
git show commit_number  显示修改信息

20A 20B

CODE MBTS
MBTS fossid工程
20A施旭涛
20B宣树兵

alter table `bug` add DTS_number varchar(100);
2019-09-06
1.每日版本中，查看击鼓传花增加版本号信息；
2.部署新的脚本工具；

寻找基础性能防线如何渲染的数据，发现和是否超上限的关系；
打开响应，看响应的数据结构，绑定相关数据；

2019-09-06
修改前端选择过滤功能


2019-09-09
git rebase -i master

alter table `tbl_perf_target` add daily_upper_limit INTEGER;

fossid维护

post_time = models.DateTimeField(auto_now_add=True)
update_time = models.DateTimeField(auto_now=True)

git log -n 10
git diff --check
git diff --cached


# 每日防线加上dts单号

django 模型添加报错
字段如果为空可以输入None，如果类型是int，给空字符串会报错
ValueError: invalid literal for int() with base 10: ''

2019-09-11

dts迁移到web
fossid
django集成

pip freeze > requirements.txt
1.ftp服务器1.控制面板->程序和功能->打开或关闭windows功能,在列表里面找到 internet信息服务,选中"ftp服务",确定.
2.异步回调  Pool().apply_async(uploadfile, (file_name, file_path), callback=os.remove)
3.ftp上传服务器接口
def uploadfile(filename, localpath):
    try:
        ftp_server = '10.62.59.53'
        username = 'xwx620452'
        password = 'xq19921005....'
        ftp = FTP()
        ftp.connect(ftp_server, 21)
        ftp.login(username, password)

        remotepath = filename
        bufsize = 1024
        fp = open(localpath, 'rb')
        ftp.storbinary('STOR ' + remotepath, fp, bufsize)  # 上传文件
        fp.close()  # 关闭文件
        ftp.quit()
    except Exception as MSG:
        print('上传失败:', MSG)
    return localpath
4.django接收文件
file = request.FILES.get('attach', 'false')

if file != 'false':
    file_name = str(bug.post_time) + '.file'
    file_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'static', 'tmp', file_name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

时间搓转时间
pycharm代码补全
File → Setting → Editor → Code Completion → 

2019-09-12
连表级联删除

20B刷生产库，隐藏掉多余的数据

update tbl_perf_target as tpt
set display=0
where tpt.scene_id=8 and tpt.target_name not in ('VOS_PID_NRCU_RTM=1133','NR_UEMDAEMON','NRCU_UEMWORK1','NRDU_UEMWORK1','NRCU_UEMWORK2','NRCU_UEMWORK3','NRDU_UEMWORK3', 'NR_OMA2','NR_OMA3','NR_OMA4','NRDU_UEMWORK2','NR_OMA1','NR_ENV', 'ROSA_SWM_LOCAL_PID');

update tbl_perf_target as tpt
set display=0
where tpt.scene_id=9 and tpt.target_name not in ('NR_CFGMASTER','VOS_PID_NRCU_RTM=1133','NR_CECPM','NRDU_CERMC','NR_UECPM','NRDU_UEBPRMC','NRCU_CEIM','NRDU_CEIMC','NRCU_ICEM','NR_TIFM','NRDU_UEUPMC','NR_UEUPA','NR_PAGING','NR_LICM','NRCU_CERRM','NRCU_LNWM','NR_OM','NR_OMA2','NR_OMA4','NRDU_ICEMC','NRCU_ICEMSLAVE','NR_ENV','NR_OMA1', 'ROSA_SWM_LOCAL_PID');

update tbl_perf_target as tpt
set display=1
where tpt.scene_id=8 and tpt.target_name='ROSA_SWM_LOCAL_PID';

update tbl_perf_target as tpt
set display=1
where tpt.scene_id=9 and tpt.target_name in ('ROSA_SWM_LOCAL_PID', 'NR_PAGING');

2019-09-12
前端bug, bugtrace提交时
CIE权限认证
登录重定向
文件共享解决方案
提交人不存在bugtrace库




















































