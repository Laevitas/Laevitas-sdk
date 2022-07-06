from package import SDK
import array as arr
from typing import List, Set, Tuple, Dict


sdk = SDK.api()
sdk.configure("c23682e9-0f28-4af6-886f-4ee5b1a7c215")
test1 = sdk.realtime.options.get_atm("deribit","btc")
#test2 = SDK.api("c23682e9-0f28-4af6-886f-4ee5b1a7c215").realtime.options.get_atm("deribit","btc")
#test3 = SDK.api("c23682e9-0f28-4af6-886f-4ee5b1a7c215").realtime.options.gex_date("deribit","btc","30SEP22")
#test4 = SDK.api("c23682e9-0f28-4af6-886f-4ee5b1a7c215").realtime.options.greeks("deribit","btc","30SeP22","C")
test5 = sdk.historical.moves.total_oi("btc","2022-06-07","2022-06-14","10","2")
#test6 = SDK.api("c23682e9-0f28-4af6-886f-4ee5b1a7c215").historical.derivs.summary("btc","2022-06-07","2022-06-14","10","1")
#test6 = SDK.api("123").realtime.derivs.oi_gainers("BITMEX","FUTURE","ytd")
test1.date
print(test5.items
      )
for item in test5.items:
    print(item.date)
#for item in test5.items:
#    print(item.)
#for item in test6.items.item:
#    print(item)
#for items in test5.items.v :
#    print(items)

#for o in test5.items:
#    print(o)
#print(test6)
#test5 = SDK.api("c23682e9-0f28-4af6-886f-4ee5b1a7c215").historical.options.iv("deribit","ETH-10JUN22-60000-C","2022-06-07","2022-06-14","10","2")
#test1.alldata