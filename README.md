## jango 自述文件

### jango 是什么

jango 是一个类 Django 的框架，只提供了 Django 的核心功能，主要意义在于教学。

如果你期望搞懂 django 的运行逻辑，又对海量的代码发怵，这个项目可能会帮你开个好头。

### 我需要它吗

Django 2.1.5 版本，已经包含了 77,000 行 python 代码。对于没有太多 django 基础的同学，了解它的脉络显得不是那么轻松。

该项目尝试通过少量代码来描述 django 的核心处理流程。实际上，该项目的 jango 模块只用到了不到 200 行的代码量，而且是在三个小时内完成的项目。希望你也可以轻松阅读这份代码 :)

```shell script
$ cloc jango
       6 text files.
       6 unique files.                              
       0 files ignored.

github.com/AlDanial/cloc v 1.84  T=0.01 s (434.1 files/s, 23511.5 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                           6             61             71            193
-------------------------------------------------------------------------------
SUM:                             6             61             71            193
-------------------------------------------------------------------------------
```

必须承认，对有一定代码基础的同学，该项目只具有娱乐性质。

该项目不是一个完整的 web 框架，它没有 orm，没有模板系统，也没有经过严格的测试，不能用于生产环境。

为了减轻阅读负担，该项目牺牲了一部分严谨的逻辑，灵活对待就好。

### 如何使用

项目克隆到本地后，可使用下面两种方式启动。

```shell script
# 1. 使用内置服务启动
python3 jango/bin/runserver.py 127.0.0.1 5302 demo.settings

# 2. 使用第三方wsgi服务启动（如gunicorn）
gunicorn -b 127.0.0.1:5302 demo.wsgi:application
```

启动后可访问下列 url 验证：

```shell script
curl http://localhost:5302/welcome/pysnow530
curl http://localhost:5302/foo/bar
```

### 相关文章

* [django核心处理流程 1. 路由](https://pysnow530.github.io/2020/03/22/jango-1-route/)
* [django核心处理流程 2. 请求响应逻辑](https://pysnow530.github.io/2020/03/25/jango-2-request-and-response/)
* [django核心处理流程 3. wsgi](https://pysnow530.github.io/2020/03/26/jango-3-wsgi/)
