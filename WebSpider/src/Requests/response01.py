import requests

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) Applewebkit/537.36 (KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r=requests.get('http://www.jianshu.com',headers=headers)
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)