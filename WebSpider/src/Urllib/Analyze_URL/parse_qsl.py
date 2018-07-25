from urllib.parse import parse_qsl

query='game=germey&age=22'
print(parse_qsl(query))