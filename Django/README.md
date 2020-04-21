# 项目笔记

## 项目描述

编写一个“学习笔记”的 Web 应用程序。主页显示网站描述并邀请用户注册或登录。用户登陆后，就可以创建新主题、添加新条目以及阅读修改既有的条目。

### 文件结构说明

``` txt
|- learning_log  # 项目名
    |- learning_log  # 项目的配置文件
    |   |- settings.py  # 项目的配置
    |   |- urls.py  # url路由配置
    |   |- wsgi.py
    |   |- ...
    |- learning_logs  # 应用 Application
    |   |- templates
    |   |   |- laerning_logs  # 应用程序的模板文件夹
    |   |       |- base.html
    |   |       |- ...
    |   |- models.py  # 模型类，和数据库中的表对应
    |   |- admin.py  # 后台管理，用来注册需要后台管理的模型类
    |   |- views.py  # 视图函数，根据url映射，调用相关函数，使用模板并渲染网页
    |   |- urls.py  # url映射
    |   |- forms.py  # 自定义表单类，继承自Django用来简化模型类的存储与验证
    |   |- ...
    |- users  # 应用 Application
    |   |- ...
    |- ll_env  ## 虚拟环境文件夹，存放pip安装的包
        |- ...
    |- db.sqlite3  # 项目的数据库
    |- manage.py  # 管理和运行项目
```

## Usage

1. 进入项目目录 `learning_log` 创建名为 `ll_env` 虚拟环境 `python -m venv ll_env`
2. 虚拟环境中安装需要的包 `pip install django django-bootstrap3`
3. 运行项目 `python manage.py runserver`

db.sqlite3 中已经存在的用户登录信息

- username: ll_admin（同时也是后台超级管理员）
- password: ~~root123123~~
- username: Alice
- password: ~~root123123~~

## 作者部署的网站

> <https://learning-log.herokuapp.com>

---

## 开发步骤

### Django 入门

#### 建立虚拟环境

``` powershell
cd learning_log  # cd 项目名
python -m venv ll_env  # 创建名为ll_env的虚拟环境
.\ll_env\Scripts\activate  # 激活并使用该虚拟环境
deactivate  # 停止使用虚拟环境
```

#### 创建项目

``` powershell
pip install django  # 虚拟环境中安装Django
django-admin.exe startproject learning_log .  # 当前目录下创建learning_log项目
```

#### 运行项目

``` powershell
python manage.py migrate  # 创建数据库
python manage.py runserver  # 查看项目
```

#### 创建应用程序

``` powershell
python manage.py startapp learning_logs  # 创建应用learning_logs
```

##### 注册应用

`settings.py` 配置 `INSTALLED_APPS` 中增加应用程序 `learning_logs`

##### 定义模型

`models.py` 文件定义学习主题类 `Topic`、信息条目类 `Entry`

##### 修改数据库

``` powershell
python manage.py makemigrations learning_logs  # 修改数据库
python manage.py migrate  # 迁移数据库
```

#### 后台管理

##### 创建超级用户

``` powershell
python manage.py createsuperuser  # 按照提示输入用户名和密码，邮箱可以省略不填
```

##### 向后台网站注册模型

在应用 `learning_logs` 中 `admin.py` 文件注册模型类 `admin.site.register(Topic)` 和 `admin.site.register(Entry)`，然后访问 Django 提供的后台管理页面 <http://localhost:8000/admin/>

#### Django Shell

``` powershell
python manage.py shell  # 使用交互式终端查询数据库内容

>>> from learning_logs.models import Topic
>>> Topic.objects.all()
>>> ...
```

#### 创建网页

##### URL 映射

1. 应用 `learning_logs` 新建 `urls.py` 文件
2. 修改项目 `learning_log` 的配置文件 `urls.py`，使其包含应用 `learning_logs` 的 `urls.py`

##### 编写视图

`views.py` 中编写功能函数

##### 编写模板

1. 在应用 `learning_logs` 文件夹下建立 `templates` 文件夹，在 `templates` 文件夹中再建 `learning_logs` 文件夹（为了方便 Django 自动识别模板文件目录）
2. 创建 `index.html`
3. 模板继承，创建 `base.html`

### 用户账户

#### 添加新主题 Topic

1. 新建 `forms.py` 文件，定义表单类 `TopicForm`，继承自 Django 中的表单，简化数据验证与存储
2. 修改应用 `learning_logs` 中的 `urls.py` 文件，增加 `'new_topic/'` 匹配规则
3. 修改应用 `learning_logs` 中的 `views.py` 文件，增加 `new_topic` 处理函数
4. 编写应用 `learning_logs` 中的模板文件 `new_topic.html`
5. 页面 `topics.html` 增加一个到页面 `new_topic.html` 的链接

#### 添加新条目 Entry （同上）

#### 编辑条目 Entry （同上）

#### 创建用户账户

``` powershell
python manage.py startapp users  # 创建应用users
```

后续使用 Django 自带的用户模型类，所以不用修改 `models.py`

##### 注册新应用

`settings.py` 配置 `INSTALLED_APPS` 中增加应用程序 `users`

##### 添加新 URL 映射

1. 应用 `users` 新建 `urls.py` 文件
2. 修改项目 `learning_log` 的配置文件 `urls.py`，使其包含应用 `users` 的 `urls.py`

#### 添加登录页面

1. 修改应用 `users` 中的 `urls.py` 文件，增加 `url(r'^login/$', login, {'template_name': 'users/login.html'},name='login')` 匹配规则，使用 Django 自带的视图函数 `login`
2. 编写应用 `users` 中的模板文件 `login.html`
3. 页面 `base.html` 增加一个到页面 `login.html` 的链接

#### 添加注销功能

1. 修改应用 `users` 中的 `urls.py` 文件，增加 `r'^logout/$'` 匹配规则
2. 修改应用 `users` 中的 `views.py` 文件，增加 `logout` 处理函数
3. 页面 `base.html` 增加一个到页面 `logout` 的链接

#### 添加注册页面

1. 使用 Django 自带的 `UserCrationForm` 表单
2. 修改应用 `users` 中的 `urls.py` 文件，增加 `r'^register/$'` 匹配规则
3. 修改应用 `users` 中的 `views.py` 文件，增加 `register` 处理函数
4. 编写应用 `users` 中的模板文件 `register.html`
5. 页面 `base.html` 增加一个到页面 `register.html` 的链接

#### 让用户拥有自己的数据

##### 限制访问

给 `views.py` 中的功能函数增加 Django 自带的访问限制 `@login_required`，需要额外在项目配置文件`settings.py` 增加 `LOGIN_URL = '/users/login/'`

##### 将数据关联到用户

- 修改模型类 `Topic`，增加外键使其与用户关联，使用 Django 自带的用户类 `User`
  - 修改模型类后需要迁移数据库（也可以执行 `python manage.py flush` 重建数据表的结构，这会清空所有的记录）
    - `python manage.py makemigrations learning_logs` 更新表结构，需输入默认关联的用户 ID
    - `python manage.py migrate` 更新数据库，新的 `Topic` 实例对象将包含用户字段

##### 只允许用户访问自己的主题

修改 `views.py` 的函数 `topics`，增加 `topics = Topic.objects.filter(owner=request.user).order_by('date_added')`。用户登陆后，`request` 对象将有一个 `user` 属性

##### 保护用户的主题

修改 `views.py` 的函数 `topic`，增加判断 `if topic.owner != request.user:`

##### 保护页面 edit_entry

修改 `views.py` 的函数 `edit_entry`，增加判断`if topic.owner != request.user:`

##### 将新主题关联到当前用户

修改 `views.py` 的函数 `new_topic`，增加`new_topic.owner = request.user`

### 设置样式

#### 安装 bootstrap3

```powershell
pip install django-bootstrap3  # 虚拟环境中安装bootstrap3
```

#### 注册 bootstrap3

`settings.py` 配置 `INSTALLED_APPS` 中增加应用程序 `bootstrap3`

#### 设置 bootstrap3

`settings.py` 配置文件末尾添加启用 Jquery 的设置

#### 使用 Bootstrap 来设置模板文件的样式
