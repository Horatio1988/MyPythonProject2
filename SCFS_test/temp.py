#coding:utf-8
import json
js = json.loads('{"haha":"哈哈"}')
print json.dumps(js)
print json.dumps(js, ensure_ascii=False)
print type(js)