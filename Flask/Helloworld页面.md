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
## Response对象
添加装饰器后的函数将被flask框架转化为视图函数，返回的是一个response对象
```python
@app.route('/hello')
def hello():
    return 'hello, world!'
```
可以导入make_response()函数生成response对象
并且给response.headers字段赋值如
```python
def Hello():
headers = {
    'content-type': 'text/plain'
    'location': 'www.baidu.com'
}
response = make_response('hello,world!', 301)
response.headers = headers
return response
```
通过location字段和301状态码可以实现重定向
## 视图函数的简化
返回response函数并不需要如上复杂的代码编写，可以简化为：
```python
def Hello():
headers = {
    'content-type': 'text/plain'
    'location': 'www.baidu.com'
}
return 'hello,world!', 301, headers
```
这是flask中最常用的视图函数编写方式
