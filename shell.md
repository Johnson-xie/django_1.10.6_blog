# shell
## 查询文件中的特定行  
```  
sed -n 18p file_path  
* 输出为变量  
line=`sed -n 18p file_path`
```
* 注意赋值等号两边不要有空格
## 判断句变量获取方式  
```if [ "$line" != "profile = 'prod'" ];then echo "settings.py 线上环境已修改,请检查后启动";exit; fi```
## 正则匹配文件中的行，并替换  
* 前面是正则表达式，后面是替换内容
```  
sed -i "s/^profile.*dev[\'\"]$/# profile = 'dev'/g" /Web/CIweb/mysite/mysite/settings.py
sed -i "s/^#.*profile.*prod[\'\"]$/profile = 'pro'/g" /Web/CIweb/mysite/mysite/settings.py
```
