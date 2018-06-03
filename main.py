#coding:utf-8

import requests
import json
import win32gui, win32ui, win32con,win32api
import time

signurl = "http://jjds.iwillgo.cn/index/index_one_nine_six/refresh_data?open_id=oxw605G80s_a3nS4ipK-TRvMzTfo&user_id=52363472&refresh_version=1454&last_load_time=37"

topicurl= "http://jjds.iwillgo.cn/index/index_one_nine_six/sprint_game"
'''
class getmaster(object):
    def __init__(self):
        self.agent = "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/151 MMWEBSDK/19 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN"
        self.headers = {'User-Agent': self.agent,}
        self.s = requests.session()
        
    def getanswer(self,n,url1,url2):
        r = self.s.get(url,headers = self.headers)
        resutlt = r.content
        sign = result["sign"]
        data = {"sprint_sort_id": 1,"user_id": 52363472,"open_id": "oxw605G80s_a3nS4ipK-TRvMzTfo","sign":sign}
        r = s.post(url,data = data, headers = headers)
        answer = r.content
        for i in range(39):
            answer[i]["is_true"]
        
if __name__ =="__main__":
'''

def get_topic(filename):
    #preRes=[]
    answerlist = []
    try:
        with open(filename,"r")as f:
            topic = json.loads(f.read())
        for i in range(40):
            #preRes.append(topic[str(i)]["num1"]+topic[str(i)]["symbol"]+topic[str(i)]["num2"])
            answerlist.append(topic[str(i)]["is_true"])
        return answerlist
    except:
        pass


def tapScreen(x, y):
    """模拟鼠标点击"""
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

for k in range(12):
    aa = get_topic("responsebody.json")
    if k in [0,1]:
        try:
            for i in aa:
                if i==1:
                    tapScreen(116,461)
                    time.sleep(1)
                else:
                    tapScreen(163,461)
                    time.sleep(1)
            k = k+1
            time.sleep(1)
        except:
            break
    elif k==2:
        try:
            for i in aa:
                if i==1:
                    tapScreen(116,461)
                    time.sleep(.5)
                else:
                    tapScreen(163,461)
                    time.sleep(.5)
            k = k+1
            time.sleep(.5)
        except:
            break
    elif k==3:
        try:
            for i in aa:
                if i==1:
                    tapScreen(116,461)
                    time.sleep(0.4)
                else:
                    tapScreen(163,461)
                    time.sleep(0.4)
            k = k+1
            #time.sleep(.5)
        except:
            break
    elif k==4:
        try:
            for i in range(len(aa)):
                if i<39:
                    if aa[i]==1:
                        tapScreen(116,461)
                        time.sleep(0.3)
                    else:
                        tapScreen(163,461)
                        time.sleep(0.3)
                else:
                    if aa[i]==1:
                        tapScreen(116,461)
                        time.sleep(0.02)
                    else:
                        tapScreen(163,461)
                        time.sleep(0.02)
            k = k+1
            #time.sleep(0.2)
        except:
            break
    else:
        try:
            for i in aa:
                if i==1:
                    tapScreen(116,461)
                    time.sleep(0.15)
                else:
                    tapScreen(163,461)
                    time.sleep(0.15)
            k = k+1
            #time.sleep(0.1)
        except:
            break



