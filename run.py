#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2020/2/4 3:51 下午
@Author  :
@Desc    :
@Email   : zhaoboy9692@163.com
@File    : run.py
"""

import frida

from flask import Flask, jsonify, request


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


js = open('test.js', 'r', encoding='utf8').read()
# session = frida.get_usb_device().attach('me.ele')
session = frida.get_usb_device().attach('com.ss.android.ugc.aweme')
script = session.create_script(js)
script.on('message', on_message)
script.load()

app = Flask(__name__)


@app.route('/test')
def hello_world():
    args = request.args['url_path']
    res = script.exports.callsecretfunctioneleme(args)
    return jsonify(res)


@app.route('/dy')
def dy_test():
    #浏览器访问不建议用get，会进行urlencode
    url = 'https://aweme-lq.snssdk.com/aweme/v1/aweme/post/?max_cursor=0&user_id=1028768810424894&count=20&retry_type=no_retry&iid=184358846342967&device_id=2277828257122173&ac=wifi&channel=wandoujia_aweme1&aid=1128&app_name=aweme&version_code=670&version_name=6.7.0&device_platform=android&ssmix=a&device_type=Pixel&device_brand=google&language=zh&os_api=27&os_version=8.1.0&uuid=351615082104688&openudid=3d57b21540251c2e&manifest_version_code=670&resolution=1080*1794&dpi=420&update_version_code=6702&_rticket=1590890088312&app_type=normal&js_sdk_version=1.16.3.5&ts=1590890117&sec_user_id=MS4wLjABAAAA-7QwzV-uUTfGr3sbh6ZjhKMDNJDtH5AXBrX07t7QCkZdHY3xksemJ472P_IH6-lN'
    # url = request.args['url'] #
    res = script.exports.callsecretfunctionedy(url)
    return res


if __name__ == '__main__':
    app.run()
