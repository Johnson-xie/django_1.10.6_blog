# git

* 提交时报错  
`git commit -m 'add tools'`  
`error: pathspec 'tools'' did not match any file(s) known to git`  
解决  
`git commit -m "add tools"`  
**语法上没有问题，总是提交不了，最后发现，在Linux系统中，commit信息使用单引号”包括，我使用的windows系统，信息应该是双引号”“包括** 

* 本地修改文件未提交至缓存区，复原  
```  
git checkout file  单个文件
git checkout . 全部  
``` 
* 取消已经暂存的文件。即，撤销先前"git add"的操作
`git reset HEAD <file>`

* 从暂存区删除文件  
`git rm --cached filename`  

`git f --cached filename `  磁盘也删除
* 未加入缓存区，撤销修改，退回当前提交版本的状态  
`git checkout .`
```  
git reset --hard HEAD
git reset --hard commit_id
```  
# git 多人开发  
* 切换分支前或fetch等操作前，确保当前分支已提交，无其他修改，是干净的
* 获取他人新推的分支  
1.更新远端分支 `git fetch origin`  
2.显示远端分支 `git branch -r（-a）`  
3.拉取新的分支到本地 `git checkout -b new_local_branch_name origin/remote_new_branch_name`  
4.推送分支上去，并且默认该本地分支的上游 `git push -u origin remote_branch_name`  
* 本地压缩无用提交的commit号 `git rebase -i HEAD~2` (压缩包含当前commit号的2个commit,将压缩号的pick改为fixup,一般第一个不改)  
* 查看当前git全局配置  
`git config --global --list `
*结果*
```
	user.name=xieqiang
	user.email=xieqiang6@huawei.com
	core.autocrlf=true
	core.quotepath=false
	i18n.commitencoding=utf-8
	i18n.logoutputencoding=gbk
	gui.encoding=utf-8
	i18n.commit.encoding=utf-8
```
## git暂时离开未提交修改的分支  
1.使用git stash保存当前进度分支，`git stash save "暂存mesage"`  

2.使用git stash pop恢复进度,`git stash pop 恢复工作进度`  

## git branch操作  
* 删除本地分支 git branch -d <BranchName>  
* 修改本地分支名 git branch -m old new  
* 创建修改分支  git checkout -b branch_name  
	
## 查看版本差别  
* 当前修改与上一个版本差别 git diff file_or_direct  
* git diff --cached file_or_direct  
* git diff HEAD file_or_direct

## 查看单个文件在不同版之间的差异  
`git diff commit_id1 commit_id2 file_name`

## 单个文件回退版本  
```  
git checkout commit_id file_name  
git commit -m "file_name back to commit_id"
```  
## git回到之前分支  
```
git checkout -
```
## git查看自己的配置  
```  
git config --system --list  
git config --global --list
git config --local --list
```

## git覆盖上一条commit信息  
`git commit --amend --no-edit`
* 覆盖上一条记录,没有commit信息  

* 远程仓库回退  
```  
1.本地git log --oneline
2.git reset --hard commit_id
3.git push -f 推送回退的版本，远端即回退
```
# git 撤销文件工作区，或缓存区  
```  
通过 git checkout 文件名 命令可以撤销文件在工作区的修改。 
通过 git reset 文件名 命令可以撤销指定文件的 git add 操作，即这个文件在暂存区的修改。 
通过 git reset 命令可以撤销之前的所有 git add 操作，即在暂存区的修改。
```  
## 查看不同  
```  
git diff HEAD 查看工作树与本地库的不同点  
git diff HEAD~1 查看HEAD和上一个commit的不同点  
git diff HEAD~2 查看HEAD和之前第二个commit的不同点
```

## git log
* 忽略合并的commit号  
`git log --no-merges`
* 推送  
`git push origin remote_branch_name`

## git amend  
* 覆盖上一条commit  
`git commit --amend --no-edit`  
* add commit  
`git commit --am "information"`  

## 远程仓库回退  
1.本地git log --oneline
2.git reset --hard commit_id
3.git push -f 推送回退的版本，远端即回退  
4.直接强推  

## git撤销工作  
```  
git checkout file_path（撤销工作区中的修改）
git reset file_path(撤销暂存区的修改到当前工作区)----->再git checkout file_path撤销工作区的修改
查看暂存区中的文件修改
git diff --cached file_path
查看工作区文件修改
git diff file_path
```  

# rebase  
* 处于游离状态 HEAD detached from commit_id  
`git checkout -b new_branch`  

* rebase解决冲突  
```  
git add .
git rebase --continue
```  

* git 末行模式执行批量修改  
批量替换pick为fixup
`%s/pick/fixup/g`  

* 在自己的分支rebase commit  
`git rebase -i master`  
不是自己的可以丢弃(drop)  
同步代码一定要到最后提交代码的时候再同步  

## 如果rebase遇到困难  
1. 当前源分支同步目标分支代码  
2. 遇到冲入就正常解决，没有遇到就继续  
3. 然后复制出自己修改的代码文件  
4. 从目标分支检出新分支  
5. 在新分支里拷贝进复制出的文件  
6. 提交代码，推送， 提merge  

## git 查看单个文件历史差异  
```git diff 更早的hash_id 更晚的hash_id file_path.py```  


