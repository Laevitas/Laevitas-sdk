from Laevitas import SDK


sdk = SDK.api()
sdk.configure('api-key')
test1 = sdk.realtime.options.get_atm("deribit","btc")
test2 = sdk.realtime.options.gex_date_all("deribit","btc")
test3 = sdk.realtime.options.maturities("deribit","btc")
test4 = sdk.realtime.options.oi_expiry("deribit","btc")
test5 = sdk.realtime.options.oi_strike_all("deribit","btc")
test6 = sdk.realtime.options.oi_type("deribit","btc")
test7 = sdk.realtime.options.top_traded_option("deribit","btc")
test8 = sdk.realtime.options.v_expiry("deribit","btc")
test9 = sdk.realtime.options.gex_date("deribit","BTC","30SEP22")
test10 = sdk.realtime.options.greeks("deribit","BTC","30SEP22","C")

test11 = sdk.realtime.derivs.oi_gainers("deribit","future","ytd")

test12 = sdk.historical.options.iv("DERIBIT","BTC-30SEP22-20000-C")
test13 = sdk.historical.move.total_oi("btc","2022-06-07","2022-06-16","10","2")




print(test10.datajson)
#print(test3.data)
for i in test10.data:
    print(i.maturity)





