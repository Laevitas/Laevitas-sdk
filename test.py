from Laevitas import SDK


sdk = SDK.api()
sdk.configure('api-key')



test1 = sdk.realtime.options.get_atm("deribit","btc")
test2 = sdk.realtime.options.getatm("deribit","btc","Today")
test3 = sdk.realtime.options.gex_date("deribit","BTC","30SEP22")
test4 = sdk.realtime.options.greeks("deribit","BTC","30SEP22","C")
test5 = sdk.realtime.derivs.oi_gainers("deribit","future","ytd")
test6 = sdk.historical.options.iv("DERIBIT","BTC-30SEP22-20000-C")
test7 = sdk.historical.moves.total_oi("btc","2022-06-07","2022-06-14","10","2")

print(test5)
for i in test5.data:
    print(i.symbol)


