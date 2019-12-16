# -- coding: utf-8 --

#使用post方式爬取数据  有道翻译
# http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule

#请求头信息
# i: 爬虫
# from: AUTO
# to: AUTO
# smartresult: dict
# client: fanyideskweb
# salt: 15706925116113
# sign: 85e3cf5e35ba6341f12bbc5f5572f919
# ts: 1570692511611
# bv: 9915c65c9e78cfd742d6a24e66b85108
# doctype: json
# version: 2.1
# keyfrom: fanyi.web
# action: FY_BY_REALTlME

import requests
import json
#
# #构建请求头字典
#
def get_translate_date(word=None):
    url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    request_header = {'i': word, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb',
                      'salt': '15706925116113', 'sign': '85e3cf5e35ba6341f12bbc5f5572f919', 'ts': '1570692511611',
                      'bv': '9915c65c9e78cfd742d6a24e66b85108', 'doctype': 'json', 'version': '2.1',
                      'keyfrom': 'fanyi.web', 'action': 'FY_BY_REALTlME','typoResult':'false'}
    post = requests.post(url, data=request_header)
    print(post)
    content = json.loads(post.text)
    print(content)
    print(content['translateResult'][0][0]['tgt'])

if __name__ == 'main':
    get_translate_date("中国")



