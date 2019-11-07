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

* 查看提交历史  
* git log -p  
* git log -2  
* git log -p -2  
* git log --stat  查看增删改行简略信息  
* git log --oneline  
* git log --pretty=oneline[short, full, fuller]  
* git log --pretty=format:"%h - %an, %ar : %s" 定制格式  
* git log --pretty=format:"%h %s" --graph  
```  
-p
--stat  
--shortstat  
--name-only  
--name-status  
--abbrev-commit 
--relative-date  
--graph  
--pretty  
```  

* git log --since=2.weeks  
* git log --author=xwx620452  
* git log --grep=压缩  
* git log --author=xwx620452 --grep=压缩 --all-match  
* git log -Sfunction_name `git log -Sdef` (添加或移除了def的提交操作)  
```  
-n  
--since,  --after  
--util, --before  
--author  
--committer  
--grep  
-S  
```  
* git	log	--pretty="%h	-	%s"	--author=gitster	--since="2008-10-01" --before="2008-11-01"	--no-merges  

* 撤销操作  
* git commit --amend -m "info" 什么都不改，提交，不改变快照，只改变提交信息，id也会变 
* git commit --amend --no-edit  

* 取消暂存文件  
* git reset HEAD file  
* git checkout file 危险信号  

* 远程仓库  
* git remote 查看远程仓库  
* git remote -v  
* git remote add library_name(custom) url 添加远程仓库  
* git fetch [remote-name]  
* git pull origin master  
* git push origin master
* git remote show [remote-name]  
* git remote rename origin 5gweb 修改远程仓库的简写名，也会修改远程分支名字   
* git remote rm johnson 移除远程仓库  

* 重大节点，打标签  
* git tag  
* git tag -l 'v1.0.1*'  
* git tag -a v1.4 -m "my version 1.4"  
* git tag v1.0.1  
* git tag v1.4-lw  
* git tag -a v1.2  hash-id(校验和) 补打标签  
* git show tag_name  
* git push不会传送标签，需要显示推送 `git push origin v1.2`  
* git tag origin --tags 推送所有标签  


























