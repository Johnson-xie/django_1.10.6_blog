# python module  

## [python bisect](http://kuanghy.github.io/2016/06/14/python-bisect)
```  
def binary_search_recursion(lst, value, low, high):
    if high < low:
        return None
    mid = int((low + high) / 2)
    if lst[mid] > value:
        return binary_search_recursion(lst, value, low, mid-1)
    elif lst[mid] < value:
        return binary_search_recursion(lst, value, mid+1, high)
    return mid

def binary_search_loop(lst, value):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if lst[mid] < value:
            low = mid + 1
        elif lst[mid] > value:
            high = mid - 1
        else:
            return mid
    return None

if __name__ == "__main__":
    import random
    lst = [random.randint(0, 10000) for _ in range(100000)]
    lst.sort()

    def test_recursion():
        binary_search_recursion(lst, 999, 0, len(lst)-1)

    def test_loop():
        binary_search_loop(lst, 999)

    import timeit
    t1 = timeit.Timer("test_recursion()", setup="from __main__ import test_recursion")
    t2 = timeit.Timer("test_loop()", setup="from __main__ import test_loop")

    print("Recursion:", t1.timeit())
    print("Loop:", t2.timeit())

```

## random.seed  
seed( ) 用于指定随机数生成时所用算法开始的整数值。 

1.如果使用相同的seed( )值，则每次生成的随即数都相同； 

2.如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。 

3.设置的seed()值仅一次有效  
```  
from numpy import *
num=0
while(num<5):
    random.seed(5)
    print(random.random())
    num+=1  
>>>0.22199317108973948  
>>>0.22199317108973948  
>>>0.22199317108973948  
>>>0.22199317108973948  
>>>0.22199317108973948  

```

```  
from numpy import *
num=0
random.seed(5)
while(num<5):
    print(random.random())
    num+=1
    
 >>>0.22199317108973948  
 >>>0.22199317108973948 
 >>>0.22199317108973948 
 >>>0.22199317108973948 
 >>>0.22199317108973948 
```  

## Unix进程间的通信方式  


## namedtuple设置默认值  
```  
UsrCommitRecord = namedtuple('UsrCommitRecord', ('id email usr codebase code_add code_delete dt_add dt_delete other_add other_delete commit_time commit_notes sub_dir hash'))
UsrCommitRecord.__new__.__defaults__ = (0, '', '', None, 0, 0, 0, 0, 0, 0, '', '', '', '')

```

## 获取近一个月的时间  
```  
now_time = datetime.datetime.now()
pre_time = now_time - datetime.timedelta(days=30)
now_str = now_time.strftime('%Y-%m-%d %H:%M:%S')
pre_str = pre_time.strftime('%Y-%m-%d %H:%M:%S')

```  

## python 打包exe文件  
```  
pip install pyinstaller  
pyinstaller -F script_name.py
```
## json.dumps后中文变unicode编码  
`json.dumps(data, ensure_ascii=False)`  
* 对象转json字符串后写入文件 `json.dump(data, fp)`  
* 直接将文件对象转为python对象 `json.load(fp)`

## groupby  
* 自定义分组  
* 根据第一个元素和第二个元素的组合分组
```  
for key, value in groupby(sorted(data_list, key=lambda x: x[1]), key=lambda x: x[0] + " " + x[1]):
```  
* 自定函数分组  
```  
from itertools import groupby
lst=[2,8,11,25,43,6,9,29,51,66]

def gb(num):
    if num <= 10:
        return 'less'
    elif num >=30:
        return 'great'
    else:
        return 'middle'

print [(k,list(g))for k,g in groupby(sorted(lst),key=gb)]
返回：
[('less', [2, 6, 8, 9]), ('middle', [11, 25, 29]), ('great', [43, 51, 66])]
```

# python 模块说明服务器
`python -m pydoc -p 9999`

# ???
`python -m http.server --cgi`

# python 调用其他脚本
```
添加入口模块路径到sys.path
直接import入口模块，加try
查看sys.modules
动态导入的正则匹配 importlib imp __import__
python 启动新进程的方式 subprocess.Open  ...

1 使用os.system函数运行其他程序
2 使用ShellExecute函数运行其他程序
3 使用CreateProcess函数运行其他程序
4 使用ctypes调用kernel32.dll中的函数
```
# linux orders
**查看指定文件或文件夹大小**  
`du -sh file_or_dir_path`  
**当前目录下所有文件和文件夹各自大小**  
`du --max-depth=1 -h`  
**磁盘**  
df -h
# python 静态扫描工具

## bandit[OSS] – 在Python代码中寻找常见安全问题的工具  
`bandit -r path -f html -o report.html `  
## vulture[OSS] – 寻找Python代码中未使用的类,函数，变量    
this is [vulture](https://pypi.org/project/vulture/) source  
```  
$ vulture myscript.py  # or
$ python3 -m vulture myscript.py
$ vulture myscript.py mypackage/
$ vulture myscript.py --min-confidence 100  # Only report 100% dead code.
```
## coverage.py - 查看python执行覆盖率  
> [coverage文档](http://nedbatchelder.com/code/coverage/cmd.html)

* 跑一个文件，生成html格式结果
```
coverage run file_path
coverage html[or xml]
```  
* 生成多个.coverage文件，合并结果，生成html文件  
```  
coverage run -p file parameter  
coverage combine  
coverage html

```  

```
flake8

jedi[OSS] – Python自动化/静态分析函数库

mccabe[OSS] – 检测McCabe复杂性

mypy[OSS] – Python静态类型分析工具，旨在结合动态类型及静态类型的优点

py-find-injection[OSS] – 从Python代码中寻找SQL注入漏洞

pycodestyle[OSS] – (formerly pep8) Python风格检查工具

pydocstyle[OSS] – Python docstring风格检查工具

pyflakes[OSS] – 检测Python源文件中的错误

pylint[OSS] – 寻找程序错误, 有助于执行编码标准以及嗅探代码异味. 此外它还包括pyreverse (UML图表生成器)以及symilar (一个类似的检测工具). 以及可选的扩展

pyroma[OSS] – 评估Python项目，并列出问题帮助提高代码质量

vulture[OSS] – 寻找Python代码中未使用的类,函数，变量

xenon[OSS] – 使用radon监控代码复杂度
```
# 静态分析工具大集合[简书连接](https://www.jianshu.com/p/7a452a13b339)

# 谷歌快捷键  
* Ctrl + T 新建标签页  
* Ctrl + W 关闭标签页  
* Ctrl + N 新建一个浏览器页面
* Ctrl + Tab 切换标签页(shift 回切)

# python virtualenv virtualenvwrapper windows   

## 安装
```
pip install virtualenv
pip install virtualenvwrapper-win
```

## 常用命令
* 创建基本环境：`mkvirtualenv [环境名]`  
*指定解释器* `mkvirtualenv --python=路径 venv_name`
* 删除环境:`rmvirtualenv [环境名]`
* 激活环境：`workon [环境名]`  
* 退出环境：`deactivate`  
* 列出所有环境：`workon` 或者 `lsvirtualenv`
* 进入虚拟环境目录：`cdvirtualenv`  
* 进入虚拟环境的：`site-packages目录`  
* 列出site-packages目录的所有软件包：`lssitepackages`  
* 退出虚拟环境:`deactivate`  
* 删除虚拟环境：`rmvirtualenv venv`
 
 ## 重建python环境  
 * 冻结环境 `pip freeze > packages.txt `  安装包列表保存到文件packages.txt中　
 * 重建环境 `pip install -r packages.txt`  批量安装对应版本库

# multiprocess  

## 进程池的简单实用
```  
类或函数放顶层
def task(pid):
    # do something
    return result

def main():
    multiprocessing.freeze_support()  windows平台，避免RuntimeError
    pool = multiprocessing.Pool()
    cpus = multiprocessing.cpu_count()   获取核数
    results = []

    for i in xrange(0, cpus):
        result = pool.apply_async(task, args=(i,))   apply同步串行
        results.append(result)

    pool.close()
    pool.join()
    
    获取返回值的过程最好放在进程池回收之后进行，避免阻塞后面的语句
    for result in results:
        print(result.get())

```
# windows 读取mac编写的文件
* 换行符\r，读出来只有  

[django](https://www.jianshu.com/p/d6872e417c17)  
# 打路径标记报错  
* 使用硬标记  

# windows git中文乱码  
* pycharm 临时解决方案 `set LESSCHARSET=utf-8  
[git log](https://segmentfault.com/a/1190000000578037)  
**bash prompt**
```  
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding gbk  
```
# python 检测圈复杂度  
```  
pip install mccabe  
python -m mccabe --min 5 module_name.py

```  
* lizard  
`pip install lizard`
# 字符消除 OJ  
```
import random
# test example
s = ''.join([random.choice(['A', 'B', 'C']) for i in range(20)])
# ABCBCCCAA
# s = 'ABC'
# s = 'AAA'
print(s)

def insert_letter(s):
    if not s:
        return 0
    length = len(s)
    max_eliminate = 0
    origin = s
    s = list(s)
    for letter in 'ABC':
        for i in range(length + 1):
            if i == length:
                s.append(letter)
            else:
                s.insert(i, letter)
            s = ''.join(s)
            count = eliminate_duplication(s)
            if count > max_eliminate:
                max_eliminate = count
            s = list(origin)
    return max_eliminate

def eliminate_duplication(s):
    length = len(s)
    if length <= 1:
        return 0
    i = 0
    s2 = ''
    if s[0] != s[1]:
        s2 += s[0]
    for i in range(1,length-1):
        if s[i] != s[i-1] and s[i] != s[i+1]:
            s2 += s[i]
    if s[i+1] != s[i]:
        s2 += s[i+1]
    del_num = len(s)-len(s2)
    if del_num == 0:
        return 0
    return del_num + eliminate_duplication(s2)


if __name__ == '__main__':
    num = insert_letter(s)
    print(num)
```

# 字典列表多字段排序  
* 先逆序再正序
```  
5
China 32 28 34
England 12 34 22
France 23 33 2
Japan 12 34 25
Rusia 23 43 0
```

```
countries = sorted(countries, key=lambda x: (int(x[1]), int(x[2]), int(x[3]),-ord(x[0][0]),-ord(x[0][1])), reverse=True)
countries = sorted(countries.items(), key=lambda x: (int(x[1][0]), int(x[1][1]), int(x[1][2]),-ord(x[0][0])), reverse=True)
```

# pycharm 解决自动回滚  
按住Ctrl再滑动鼠标  

# [django_tutorial](https://github.com/PrettyPrinted?tab=repositories)  

# 调试测试程序技巧  
* 获取其他接口数据，进行异常捕捉，不符合预期就记录  
* debug模式断点打到异常捕捉中，异常即进入

# 多进程入参异常  
* TypeError: can't pickle _thread.lock objects  
后来查看发现, 进程处理使用了pickle模块(用于python特有的类型和python的数据类型间进行转换)中的dump(obj, file, protocol=None,)方法对参数进行了封装处理。

出现这个问题是因为我在参数传递中传递了我自定义的数据库存储类mymongo实例对象, 造成进程内部处理封装过程无法对其进行处理。

# try threading  
```  
    def get_details(q_in, commit_origin_list):
        while not q_in.empty():
            url = q_in.get()
            commit_origin_list.append(send_request(url))
            q_in.task_done()

    url_queue = Queue()
    commit_origin_list = []

    for commit_id in commit_id_list:
        url_queue.put(os.path.join(head_url, "repository/commits/", str(commit_id)).replace("\\", "/"))

    t_list = []
    for i in range(NUMBER_OF_THREAD):
        t = threading.Thread(target=get_details, args=(url_queue, commit_origin_list))
        t_list.append(t)

    for t in t_list:
        t.start()

    for t in t_list:
        t.join()
```

## urllib带params和headers发起请求（python3）  
``` 
import urllib.parse
import urllib.request
import ssl
from pprint import pprint
import json

HEADERS = {'PRIVATE-TOKEN': 'HSHfzhx4KWMx2xanPm_c'}
params = {'more_info': 'true', 'page': '1', 'per_page': '200', 'ref_name': 'master'}

url_para = urllib.parse.urlencode(params)


url = r'https://code.huawei.com/api/v3/projects/Polestar_CID%2Fweb/repository/commits/'
full_url = url + '?' + url_para

context = ssl._create_unverified_context()

request = urllib.request.Request(full_url, headers=HEADERS)

ret = urllib.request.urlopen(request)

data = ret.read().decode('utf-8')
data = json.loads(data)
pprint(data)
print(len(data))
print(type(data))



```


