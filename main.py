#coding:utf-8

import requests

signurl = "http://jjds.iwillgo.cn/index/index_one_nine_six/refresh_data?open_id=oxw605G80s_a3nS4ipK-TRvMzTfo&user_id=52363472&refresh_version=1454&last_load_time=37"

topicurl= "http://jjds.iwillgo.cn/index/index_one_nine_six/sprint_game"

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
    



