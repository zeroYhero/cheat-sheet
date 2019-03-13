## 注册一个Hello页面
Flask的特点在于轻量级，可扩展。
采用如下最小原型即可创建一个本地helloworld页面：

```python
from flask import Flask

__author__ = '郑钰航'
app = Flask(__name__)

#采用装饰器将hello函数注册到url地址‘/hello’
@app.route('/hello')
def hello():
    return 'hello, world!'

#打开调试模式后可以实现函数的实时监控和生效，无需重启服务
app.run(debug=True)
```
## 另一种路由的注册方式
```python
@app.route('/hello')
```
这个装饰器函数实际上是封装了一个`add_url_rule()`，所以以上脚本也可以这样写：

```python
from flask import Flask

__author__ = '郑钰航'
app = Flask(__name__)

def hello():
    return 'hello, world!'

add_url_rule('/hello', view_func=hello)
app.run(debug=True)
```
## run()的参数
host定义网站服务器的ip地址，常采用'0.0.0.0'来表示
port定义接口号
```python
run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
```
## run()的参数
```python
@app.route('/hello')
def hello():
    return 'hello, world!'
```


