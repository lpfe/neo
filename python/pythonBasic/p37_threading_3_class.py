#!/usr/bin/env python

import threading, requests, time

class HtmlGetter(threading.Thread) :
    def __init__(self,url) :
        threading.Thread.__init__(self)
        self.url = url

    def run(self) :
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), 'chars')

t = HtmlGetter('https://google.com')
t.start()

print("### END ###")

'''
주소 글자 수 세어준다?
Thread 써서 멀티태스킹이 가능하다?
'''