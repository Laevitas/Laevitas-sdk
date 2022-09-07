from Laevitas import SDK



"""test1 = sdk.realtime.options.get_atm("deribit","btc")
test2 = sdk.realtime.options.gex_date_all("deribit","btc")
test3 = sdk.realtime.options.maturities("deribit","btc")
test4 = sdk.realtime.options.oi_expiry("deribit","btc")
test5 = sdk.realtime.options.oi_strike_all("deribit","btc")
test6 = sdk.realtime.options.oi_type("deribit","btc")
test7 = sdk.realtime.options.top_traded_option("deribit","btc")
test8 = sdk.realtime.options.v_expiry("deribit","btc")
test9 = sdk.realtime.options.v_strike_all("deribit","btc")"""
#volume_buy_sell_all
"""test44 = sdk.realtime.options.oi_net_change("deribit","btc","30SEP22","1")
print(test44)"""
"""test10 = sdk.realtime.options.gex_date("deribit","BTC","30SEP22")
test11 = sdk.realtime.options.greeks("deribit","BTC","30SEP22","C")

test12 = sdk.realtime.derivs.oi_gainers("deribit","future","ytd")

test13 = sdk.historical.options.iv("DERIBIT","BTC-30SEP22-20000-C")
test14 = sdk.historical.move.total_oi("btc","2022-06-07","2022-06-16","10","2")
test15 = sdk.historical.options.iv_bid_ask("deribit","btc","c_10","2022-06-07","2022-06-16","10","2")"""
#test13 = sdk.realtime.futures.snapshot(market="deribit")
#test14 = sdk.historical.futures.perpetual_funding("deribit","BTC","2022-07-25","2022-08-01","10","1")
#test15 = sdk.realtime.derivs.price_gainers("deribit","future","2")


sdk = SDK.api()
sdk.configure('35ee699f-7003-4fad-948f-921d4fdb7603')
test = sdk.realtime.options.instruments(market="deribit",currency="btc")
print(test["data"][0].keys())








