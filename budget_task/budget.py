
class budget :

   def __init__(self, category, amount):
      self.category = category
      self.amount = amount

   # Class Methods
   def deposit(self):
      return 'Enter amount to deposite'

   def withdraw():
      return 'Enter amount to withdraw'

   def check_balance():
      return 'You current balance is: '


category = budget('Clothing', 1000)
category_2 = budget('Feed', 2000)
category_3 = budget('Entertament', 3000)

print(category.deposit())
print(category_2.deposit())
print(category_3.deposit())