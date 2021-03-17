import settings_u
import os
from coinbase.wallet.client import Client

API_KEY=os.getenv("c_bot_API_KEY")
API_SECRET=os.getenv("c_bot_API_SECRET")


client = Client(API_KEY,API_SECRET,api_version="YYYY-MM-DD")	#we'll need to setup some indirection and import
currency_code='USD'
pair="BTC-USD"

#price=client.get_spot_price(currency=currency_code)
price=client.get_spot_price(currency_pair=pair)

print('Current bitcoin price is %s: %s'%(price.currency,price.amount))

