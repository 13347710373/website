#### 1.0 新建mysql数据库:
CREATE DATABASE website

#### 1.1 新建django工程:
$ django-admin startproject website
在__init__.py添加
import pymysql
pymysql.install_as_MySQLdb()

#### 1.2 新建一个应用
$ python3 manage.py startapp duck

#### 1.4 生成数据库执行文件
$ python3 manage.py makemigrations

#### 1.5 同步数据库
$ python3 manage.py migrate

### 2.0 运行服务
$ python3 manage.py runserver 0.0.0.0:8000

### 爬虫
#### 获取关注列表
https://api.bilibili.com/x/relation/followings?vmid=412573535&pn=1&ps=50&order=desc&jsonp=jsonp

