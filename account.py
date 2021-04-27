#account manager
import settings_u
import os
from coinbase.wallet.client import Client


class Account:
	
	#initialization function
	
	def __init__(self,test=True, starting_amt=10000):
		'''
			-every account has a connection to the client
			-"test" indicates if we are connecting to a real account or not
			this will determine if we're dealing with live values or not
			-accoutn value holds the quantities in each of the coin types
		'''
		self.client=Client(os.getenv("c_bot_API_KEY"),os.getenv("c_bot_API_SECRET"),api_version="YYYY-MM-DD")
		if test:
			#allow users to 
			self.account_value={"USD":starting_amt,"BTC":0,"ETH":0}
		else:
			#this will just iterate through the account types and assign each to a dict value
			#currently just prints out the account values
			self.accounts=self.client.get_accounts()
			for curr in self.accounts['data']:
				print (curr['balance'])

			'''["BTC"])
			print(self.accounts["ETH"])
			print(self.accounts["USC"])'''
			

acc=Account(False)
		