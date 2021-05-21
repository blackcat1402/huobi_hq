#火币行情获取演示 (0420 ) 
from  hb_hq_api import *

#获取价格演示
code='btc.usdt'
print(code,'最新价格',get_last_price(code))
df=get_price(code,count=5,frequency='4h');      #1d:1天  4h:4小时   60m: 60分钟    15m:15分钟
print(df)


code='eth.btc'
print(code,'最新价格',get_last_price(code))