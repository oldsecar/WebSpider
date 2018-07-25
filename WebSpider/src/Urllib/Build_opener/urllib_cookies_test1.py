import http.cookiejar,urllib.request

cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name+'='+item.value)

cookie=http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))