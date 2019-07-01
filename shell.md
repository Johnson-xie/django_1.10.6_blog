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
## 正则搜索文件中的行  
* -a && and -o or ||
```  
dev=`sed -n "/^profile.*dev[\'\"]$/p" /c/Users/xwx620452/Desktop/settings.py`
prod=`sed -n "/^#.*profile.*prod[\'\"]$/p" /c/Users/xwx620452/Desktop/settings.py`
if [ "$dev" != "" -a "$prod" != "" ];then 
	echo "settings.py 线上环境有改动,请检查后启动"
	echo "$dev"
	echo "$prod"
	exit
fi
```

## 正则匹配使用  
```  
line=`sed -n 18p /c/Users/xwx620452/Desktop/settings.py`
reg="^#.*profile.*prod[\'\"]$"

if [[ "$line" =~ $reg ]];then 
	echo "settings.py 线上环境已修改,请检查后启动"
	exit
fi

```  

## shell调用python,获取python返回值  
```  
python中print正常打印到终端，使用sys.exit(0)返回值到shell终端  
shell 中直接调用python脚本:python script_name.py  
shell中获取返回值：$?  

```




