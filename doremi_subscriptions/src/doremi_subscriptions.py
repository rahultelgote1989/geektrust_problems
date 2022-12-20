
from src.doremi_utils import get_next_renewal_date

SUBSCRIPTIONS_PLANS = {
  "MUSIC": {
    "FREE": {"PRICE": 0, "DURATION": 1},
    "PERSONAL": {"PRICE": 100, "DURATION": 1 },
    "PREMIUM": {"PRICE": 250, "DURATION": 3 }
  },
  "VIDEO": {
    "FREE": {"PRICE": 0, "DURATION": 1 },
    "PERSONAL": {"PRICE": 200, "DURATION": 1 },
    "PREMIUM": {"PRICE": 500, "DURATION": 3 }
  },
  "PODCAST": {
    "FREE": {"PRICE": 0, "DURATION": 1 },
    "PERSONAL": {"PRICE": 100, "DURATION": 1 },
    "PREMIUM": {"PRICE": 300, "DURATION": 3 }
  }
}

class Subscription:

  def __init__(self, category, plan, subscription_date):
    self.category = category
    self.plan = plan
    self.subscription_date = subscription_date

  @property
  def price(self):
    return SUBSCRIPTIONS_PLANS[self.category][self.plan]["PRICE"]

  @property
  def duration(self):
    return SUBSCRIPTIONS_PLANS[self.category][self.plan]["DURATION"]

  @property
  def renewal_date(self):
    return get_next_renewal_date(self.subscription_date, self.duration)



  
