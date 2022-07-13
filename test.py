from Laevitas import SDK


sdk = SDK.api()
sdk.configure('api-key')



test1 = sdk.realtime.options.get_atm("deribit","btc")
test5 = sdk.historical.moves.total_oi("btc","2022-06-07","2022-06-14","10","2")
print(test1)
for i in test5.items:
    print(i.date)
