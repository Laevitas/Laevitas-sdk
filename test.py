from Laevitas import SDK


sdk = SDK.api()
sdk.configure('api-key')



test1 = sdk.realtime.options.get_atm("deribit","btc")
test2 = sdk.realtime.options.gex_date("deribit","BTC","30SEP22")
test3 = sdk.realtime.options.greeks("deribit","BTC","30SEP22","C")
test4 = sdk.realtime.derivs.oi_gainers("deribit","future","ytd")
test5 = sdk.historical.options.iv("DERIBIT","BTC-30SEP22-20000-C")
test6 = sdk.historical.move.total_oi("btc","2022-06-07","2022-06-14","10","2")

print(test1)
for i in test1.Today:
    print(i.symbol)


