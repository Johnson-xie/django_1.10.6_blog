## 常用命令  

* option + comman + M  隐藏窗口  
* command + q 推出窗口  
* 两指上下滑动  
* 三指到全局  
* 浏览器，两指左右滑动为前进与后退  
* command + N  
* command + T  



## 安装python3  
* 直接下载安装包安装  
* pip3 install virtualenvwrapper  
* 添加workon命令  
```  
* which virtualenvwrapper.sh  
* 打开/Users/用户名/.bash_profile  
/Users/johnson_xie  
* vim .bash_profile  
export WORKON_HOME=$HOME/.virtualenvs  
export VIRTUALENVWRAPPER_SCRIPT=/Library/Frameworks/Python.framework/Versions/3.8/bin/virtualenvwrapper.sh  
export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.8/bin/python3  
export VIRTUALENVWRAPPER_VIRTUALENV=/Library/Frameworks/Python.framework/Versions/3.8/bin/virtualenv  
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'  
source /Library/Frameworks/Python.framework/Versions/3.8/bin/virtualenvwrapper.sh  
```  
* 重启终端或执行source ~/.bash_profile 命令  
* mkvirtualenv -p python3 web  


## mac 修改镜像源  
* 进入根目录：cd ~/  
* 进入.pip目录 cd .pip  
* 如果不存在文件夹就新建mkdir .pip  
* 进入 cd .pip  
* 创建pip.conf文件 touch pip.conf  
* 修改：vim pip.conf  
```  
暂时  
pip install*** -i https://pypi.douban.com/simple  
永久修改内容： 
[global]  
index-url=http://mirrors.aliyun.com/pypi/simple/  
[install]   
trusted-host=mirrors.aliyun.com  
```  


