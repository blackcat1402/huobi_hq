# huobi_intf
提供火币网数据的接口的python封装，封装成pandas的dataframe格式

最简单的例子



```python
code='btc.usdt'
print(code,'最新价格',get_last_price(code))
df=get_price(code,count=5,frequency='4h');      #1d:1天  4h:4小时   60m: 60分钟    15m:15分钟
print(df)

```
### btc日线
![btc日线](https://github.com/mpquant/huobi_hq/blob/main/img/btc425.png)
 

### btc的4小时线
![btc小时线](https://github.com/mpquant/huobi_hq/blob/main/img/btc425_4.png)


