# API-SDK
First test version which includes 7 endpoints:

## Requirements.

Python 3.7+

## Installation & Usage
### pip install



```sh
pip install SDK-Laevitas
```
Then import the package:
```python
from Laevitas import SDK 
```



## Getting Started

Please follow the procedure and then run the following:

```python
from Laevitas import SDK
from Laevitas import item

# create an instance of the API class
sdk = SDK.api()
# Configure your api key
sdk.configure('your-api-key')
#exemples:
#two different method for getatm
response1 = sdk.realtime.options.get_atm(market="derivit",currency="btc")
print(response1.Two_days_ago)
#the second method includes period as a param
response2 = sdk.realtime.options.getatm(market="derivit",currency="btc",period="Two_days_ago")
#Historical data
response3 = sdk.historical.options.iv(market="deribit",instrument="BTC-10JUN21-60000-P")
response4 = sdk.historical.moves.total_oi(currency="btc",start="2022-06-07",end="2022-06-14",limit="10",page="2")
print(response4.items)
for item in response4.items:
    print(item.v)
                                     


```

## Documentation for available API Endpoints

|Class | Sub-class | Method                                                             | Description|
|------------ |-----------|--------------------------------------------------------------------| -------------|
|*realtime* | options   | getatm(market,currency)<br/>get_atm(market, currency, period)      | At the money Implied Volatility Term Structure|
|*realtime* | options   | gex_date(market, currency, maturity)                               | Gamma Exposure by Expiration|
|*realtime* | options   | greeks(market, currency, maturity, optiontype)                     | Greeks|
|*realtime* | derivs    | oi_gainers(market, oitype, period)                                 | oi gainers|
|*historical* | options   | iv(market, instrument, start(opt), end(opt), limit(opt), page(opt) | Instrument Historical Implied Volatility|
|*historical* | moves     | total_oi(currency, start(opt), end(opt), limit(opt), page(opt)     | total oi|








