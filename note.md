# python 在不同层级目录import 模块的方法
***

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

# BOM标记，文件开头 \ufeff
***
utf-8编码产生的csv文件，excel打开乱码，使用utf_8_sig带BOM的编码格式就可以正常解码咯。  

将BOM头去掉，代码如下：

  if text.startswith(u'\ufeff'):    
    text = text.encode('utf8')[3:].decode('utf8')    
    
