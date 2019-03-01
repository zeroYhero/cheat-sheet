##安装django的方式
- option1：pip install Django==2.1.7
- option2：下载源码，进入根目录执行`python setup.py install`

##创建一个新的项目
- 在指定目录下执行`django-admin startproject mysite`

##manage.py的作用
- 与项目进行交互的命令行工具集入口（项目管理器）
- `python manage.py`可查看常用命令
- `python manage.py runserver`用于运行服务器

##文件夹下各模块作用
- wsgi.py：应用与服务器的网关接口
- urls.py：url配置文件，用于配置项目中所有页面的url
- setting.py：
