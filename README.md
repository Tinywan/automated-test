# 一个自动化测试脚本

## 版本映射关系  

|Chromedriver 版本|支持的Chrome版本|
|:---:|:---:|
|v2.43|v69-71|
|v2.42|v68-70|
|v2.41|v67-69|
|v2.40|v66-68|


## 准备工作

#### 升级 `pip` 包管理工具  

```python
python -m pip install --upgrade pip
```
> 如果版本低于2.7，需要升级管理工具，查看版本 `python --version`

#### 安装 selenium webdriver

```python
pip install selenium
```

#### 启动浏览器

```python
from selenium import webdriver

dr = webdriver.Chrome()
```

#### 关闭浏览器  

```python
time.sleep(2)
print 'browser will be closed'
dr.quit() # or dr.close()
print 'browser is closed'
```
> 关闭浏览器有两种方式  
>> 1、`close`方法  
>> 2、`quit`方法

#### 浏览器最大化  

如果在 `webdriver` 测试中使用了 `sikuli` 来对 `flash` 插件进行操作的话，把浏览器最大化无疑是一个比较简单的保证分辨率统一的解决方案。 

```python
dr.maximize_window()
```

#### 设置浏览器大小  

```python
dr.set_window_size(240, 320)
dr.get('http://www.3g.qq.com')
```

#### 访问链接  

```python
url = 'http://www.baidu.com'
print "now access %s" %(url)
dr.get(url)
```

#### 打印当前页面的title及url    

```python
print "title of current page is %s" % (driver.title)
print "url of current page is %s" % (driver.current_url)
```

## Remi is a GUI library

[https://github.com/dddomodossola/remi](https://github.com/dddomodossola/remi) 

#### HELP

* [https://github.com/easonhan007/webdriver_guide](https://github.com/easonhan007/webdriver_guide)   

