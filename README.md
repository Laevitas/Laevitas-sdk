# API-SDK
2.0.0a 
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

# create an instance of the API class
sdk = SDK.api()

# Configure your api key
sdk.configure('your-api-key')
# try different endpoints , endpoints return json format
top_traded_option = sdk.analytics.options.top_traded_option(market="DERIBIT",currency="BTC")
instrument_volume_buy_sell = sdk.historical.options.instrument_volume_buy_sell(market="DERIBIT",instrument="BTC-28JUN24-70000-C",start="2023-07-13",end="2023-07-20")
trades = sdk.historical.options.trades(currency="ETH",market="OKEX",date="2023-07-13")             


```

## Documentation for available API Endpoints
https://api.laevitas.ch/swagger/#/






 


