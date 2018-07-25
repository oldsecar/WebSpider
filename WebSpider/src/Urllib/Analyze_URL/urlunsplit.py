from urllib.parse import urlunsplit

data=['http','www.baidu.com','index.html','a=6','comment']
print(urlunsplit(data))
'''len(data)should be less or equal to 5'''