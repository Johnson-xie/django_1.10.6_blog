# read git  

## git base  
* git config --list  
* git config [system global local]  
* git config --global core.editor /d/Notepad++/notepad++.exe  

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

* 检出标签  
* git checkout -b new_branch_name tag_name  

* git 别名  
* git config --global alias.co checkout  
* git config --global alias.br branch  
* git config --global alias.ci commit  
* git config --global alias.st status  
* git config --global alias.unstage 'reset HEAD --'  
```  
git unstage fileA == git reset HEAD --fileA  
```  
* git config --global alias.last 'log -1 HEAD'  

## 分支模型  
* git checkout -b new_branch  
* git branch new_branch  
* git checkout new_branch  

* git merge hotbranch (current point to master)  
* git branch -d new_branch  

* 上面表示的是当前所在分支(pull和push都是合并方式的一种)  
```  
<<<<<<< HEAD:index.html
hello world
=======
hell johnson  
>>>>>>> iss53:index.html  
```
* git add file 解决冲突后标记已解决  
* git status  
* git commit  

* git branch  
* git branch -v 查看每一个分支的最后一次提交  
* git branch --merged 查看合并当前分支的分支，列表中分支名字前没有	*	号的分支通常可以使用	git	branch	-d	删除掉  
* git branch --no-merged 查看未合并到当前分支的分支  
* git branch -D br_name  


### 分支开发模式  
* 长期分支  
* 特性分支  
* 远程分支 (远程仓库的引用指针)  
```  
* git ls-remote  
* git remote show  
* git clone -o booyah  
origin/master 指代远端的分支  
* git fetch origin 移动指代远端那个指针到最新  

```

























