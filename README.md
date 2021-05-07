# 火币网行情最简封装接口
提供火币网数据的接口的python封装，封装成pandas的dataframe格式

### 接口说明
* get_price接口得到火币网行情数据，返回dataframe的格式

* 为了支持多交易所(币安，okex等),我们规范定义了几个核心数据格式
   * 交易对统一用 btc.usdt  ，  eth.usdt  ，    eth.btc  这样的中间加.分割的格式
   * 时间周期统一用 1d: 一天 ，  4h: 四小时 ，  60m: 60分 ，  15m:15分 ，  5m:5分 ，   1m:1分   这样的格式


最简单的例子



```python
from  hb_hq_api import *

code='btc.usdt'
print(code,'最新价格',get_last_price(code))
df=get_price(code,count=5,frequency='4h');      #1d:1天  4h:4小时   60m: 60分钟    15m:15分钟
print(df)

#结果参看下面的截图
```
## btc日线
![btc日线](/img/btc425.png)
 

## btc的4小时线
![btc小时线](/img/btc425_4.png)


## 需安装第三方库
* requests
* pandas
 

----------------------------------------------------
### 巴特量化(BestQuant)：数字货币 股市量化工具 行情系统软件提供商
----------------------------------------------------

![加入群聊](/img/qrcode.png) 

