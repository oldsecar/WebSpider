import requests

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) Applewebkit/537.36 (KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r=requests.get('http://www.jianshu.com',headers=headers)
exit() if not r.status_code==requests.codes.ok else print("Request Successfully")