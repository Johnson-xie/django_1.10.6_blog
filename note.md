# python 在不同层级目录import 模块的方法
***
'''
有一个文件夹/home/a,  里面有个模块叫b.py,  程序里导入模块b？
1).
import sys;
sys.path.append("/home/a/")
import b
2).
在目录里面增加__init__.py文件，里面可以写import时执行的代码，当然也可以留空就可以.
import home.a.b
3). 
from home.a.b import *
前提 home、a中都包括__init__.py
'''
