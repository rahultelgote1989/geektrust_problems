"""
File: to get topups and top up balances
"""
topup_plans = {
	"four_device": {"device": 4, "price": 50, "duration": 1},
	"ten_device": {"device": 10, "price": 100, "duration": 1}
}

class TopUps:

	def __init__(self, topup, items):
		self.devices = topup_plans[topup.lower()]["device"]
		self.price = topup_plans[topup.lower()]["price"]
		self.duration = topup_plans[topup.lower()]["duration"]
		self.items = items

	@property
	def cost(self):
		return int(self.items) * int(self.price)

	

	
