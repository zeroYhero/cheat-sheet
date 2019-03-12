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
