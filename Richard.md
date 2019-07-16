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
