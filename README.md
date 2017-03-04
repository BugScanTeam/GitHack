# GitHack

> `.git` 泄漏利用工具，可还原历史版本

### 依赖

> 不需要安装其它 Python 库，只需要有 git 命令

* git
    * ubuntu/debian: `$ apt-get install git`
    * redhat/centos: `$ yum install git`
    * windows [git-for-windows下载](https://github.com/git-for-windows/git/releases/latest)

**使用前需确保 git 在 环境变量中**

### 使用方法

```
python GitHack.py http://www.example.com/.git/
```

> 还原后的文件在 `dist/` 目录下

### 工作流程

1. 尝试获取 `packs`克隆
2. 尝试目录遍历克隆
3. 尝试从缓存文件(index)、commit记录中恢复

### 截图

![](http://7xtigg.com1.z0.glb.clouddn.com/githack.png)

### 相关链接

* [BugScan](http://www.bugscan.net)
* [GitHack - lijiejie](https://github.com/lijiejie/GitHack)
