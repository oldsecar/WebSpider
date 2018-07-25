import requests

data={
    'name':'oldsecar',
    'age':'20'
}
r=requests.post('http://httpbin.org/post',data=data)
print(r.text)