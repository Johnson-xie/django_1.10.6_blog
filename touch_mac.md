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

