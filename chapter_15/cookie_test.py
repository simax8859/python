from urllib.request import *
import http.cookiejar, urllib.parse

# 以指定文件创建CookieJar对象， 该对象可以把cookie信息保存在文件里
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
# 创建HTTPCookieProcessor
cookie_processor = HTTPCookieProcessor(cookie_jar)
# 创建OpenerDirector对象
opener = build_opener(cookie_processor)

# 定义模拟Chrome浏览器的User-Agent
user_agent = r'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36' \
    r'(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

# 定义请求头
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

# ---------------下面代码发送登录的POST请求--------------
# 定义登录系统的请求参数、
params = {'name': 'crazyit.org', 'pass': 'leegang'}
postdata = urllib.parse.urlencode(params).encode()
# 创建向登录页面发送POST请求的Request
request = Request('http://localhost:8888/test/login.jsp', data=postdata, headers= headers)

# 使用OpenerDirector发送POST请求
response = opener.open(request)
print(response.read().decode('utf-8'))

# 将cookie信息写入文件中
# cookie_jar.save(ignore_discard=True, ignore_expires=True)


# ---------------下面代码发送访问被保护资源的GET请求--------------
# 创建向被保护页面发送GET请求的Request
request = Request('http://localhost:8888/test/secret.jsp', headers= headers)
response = opener.open(request)
print(response.read().decode())

