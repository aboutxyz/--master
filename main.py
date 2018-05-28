#coding:utf-8

import requests

agent = 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/151 MMWEBSDK/19 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN'

headers = {#"charset":" utf-8",
#"Accept-Encoding":" gzip",
#"referer":" https://servicewechat.com/wxe91bc022c0c198cb/25/page-frame.html",
#"content-type":" application/json",
#"Content-Length":" 649",
#"Host":" jjds.iwillgo.cn",
#"Connection":" Keep-Alive",
'User-Agent': agent,}

data = {"sprint_sort_id": 1,
  "user_id": 52363472,
  "open_id": "oxw605G80s_a3nS4ipK-TRvMzTfo",
  "sign": "eb8bbr9sUad8OdBp5koC9e62nZQKCnbtx4Bopau58juQBG75NYw0+CpINSf9+NM2K40qUxL+f/qDnP4iMjCwfUnPdkZNNxsAiqVSAJU3hmT4ZRXx5+sznNtUw5FW6GG0+eWKKBUYqxeBpnv1P8yr4WDkpXYgzoZJ1sf4cwCZ7L4vmCxtsHhuLk4QoXHiODU1eV51dUhsDeghZiqIIrC5ZbS/NwbH8TUIvTFXPnLCLdI7d+xfvT5LE2oBog7Oe/c93Y0OB6Ve7YZUngu9fSWqDVtvtGieeziXwL2QHf0H4u5OLRPpvLhaeI7IivrATJ3cRFpNcFTv5CdjBAbuPnVDVaXk+ezaerYoP7vn8aKpR6ia0NlH4FXY6X9gBz3GqVc2IbZScjcNZUYSQBXXnbDgzrshpc5StSH4WpUpABUKxO1vZs6GEji7kHgTe3l3TO0bM7329x/kpUfkUrMhRX5drZeVG4vShA84yPpEOhUahwlmrIBnf6TVMzSohJiACL4aT9VxDkRYfHjOPprEByMJS9BJ4MfraaTSxlYSVRH/zmqefyQ"}

url= "http://jjds.iwillgo.cn/index/index_one_nine_six/sprint_game"
s = requests.session()
r = s.post(url,data = data, headers = headers)
print(r.content)
