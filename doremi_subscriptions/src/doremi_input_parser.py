import datetime

class InputParser:

	def __init__(self, input_lines):
		self.input_lines = input_lines
		self.subscription_orders = []
		self.topups_orders = []
		self.is_input_valid = False
		self.service_start_date = None
		self.date_valid = False
		self.type_count = {"MUSIC": 0, "VIDEO": 0, "PODCAST": 0, "TEN_DEVICE": 0, "FOUR_DEVICE": 0}

	def parse_inputs(self):
		for _input in self.input_lines:
			_input = _input.split()
			if _input[0].upper() == "ADD_SUBSCRIPTION":
				self.type_count[_input[1]] += 1
				self.subscription_orders.append({"type": _input[1], "plan": _input[2]})
			elif _input[0].upper() == "ADD_TOPUP":
				self.type_count[_input[1]] += 1
				self.topups_orders.append({"type": _input[1], "count": _input[2]})
			elif _input[0].upper() == "PRINT_RENEWAL_DETAILS":
				self.is_input_valid = True
			elif _input[0] == "START_SUBSCRIPTION":
				self.service_start_date = _input[1]

	def subscriptions_duplicated(self):
		if self.type_count["MUSIC"] > 1 or self.type_count["MUSIC"] > 1 or self.type_count["MUSIC"] > 1:
			return "DUPLICATE_CATEGORY"
		else:
			return False

	def topups_duplicated(self):
		if self.type_count["TEN_DEVICE"]>1 or self.type_count["FOUR_DEVICE"]>1:
			return "DUPLICATE_TOPUP"
		else:
			return False

	def is_date_valid(self):
		try:
			_date = datetime.datetime.strptime(self.service_start_date, '%d-%m-%Y')
			return True
		except Exception as err:
			return False
            
