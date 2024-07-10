from Laevitas import SDK

# create an instance of the API class
sdk = SDK.api()

sdk.configure('api-key')
# try different endpoints , endpoints return json format
test = sdk.analytics.options.strategy_leg_bubble_chart(currency="BTC", maturity='all', strategy='all',
                                                       hours_interval=24, size_filter=0, single_trade=False)
print(test)
