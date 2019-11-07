# read git  

## git base  
* git config --list  
* git config [system global local]  

* git clone  
* git clone url custom_local_repository_name  

### add the file ----> edit the file ---> add the file ---> commit file  
* git init  
* git add file/directory  
* git status  
* git status -s  
* git status --short

* git reset HEAD <file>  取消暂存区的文件  
* git checkout --<file>  放弃修改  
* .gitignore  自动生成的文件，临时文件  
```  
  *.[oa]  
  *~  
  .idea/  
  *.pyc  
  
  *.a  
  !lib.a  (!用于取反，追踪指定特殊被排除的文件)  
  doc/**/*.pdf  
  doc/*.txt  
```  

* git diff  工作区和暂存区的差异  
```  
edit file  
git diff  有差异  
git add file  
git diff 无差异  
git reset HEAD 
git diff 有差异  
```

* git diff --cached  
* git diff --stated  和--cached相同  

* git commit  
* git commit --global core.editor 编辑器  
* git commit -m "info"  
* git commit -v 记录详细修改内容  
* git commit -a 跳过add,直接commit,前提是已追踪的文件修改  
* git commit -am "info"  

* 移除文件  
* git rm file 会永久删除文件  
* git rm -f  
* git rm --cached file/directory 不小心添加了没有文件到暂存区，从暂存区取出不再跟踪  
* git rm log/\*.log  

* 移动文件  
* git mv file_from file_to  改文件名  
```  
git mv readme.md readme  
相当于 
mv readme.md readme    
git rm readme.md  
git add readme
```
























