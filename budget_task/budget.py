
class budget :

   # The constructor to the class
   def __init__(self, category, amount):
      self.category = category
      self.amount = amount
      self.account = list()

   # Class Methods
   def deposit(self, amount):
      """ A deposit method that accepts an amount and category to deposit into """
      balance = 0
      balance += amount
      self.account.append({'amount': amount})
      return 'You deposited #%d into %s account your balance is #%d' % (amount, self.category, balance)

   def withdraw(self, amount):
      """ A withdraw method accepts an amount and category 
      to withdraw from, and also checks to see if the amount 
      to withdraw doesn't exceed the balance the category 
      """
      # amount = int(input('Enter amount to withdraw: '))
      if(self.check_balance(amount)):
         self.account.append({'amount': -amount})
         return 'Take your cash'
      return 'Insufficient fund'

   
   def check_balance( self, amount ):
      """ A check balance method  """
      balance = 0
      for item in self.account:
         balance +=item['amount']
      
      return balance

   def transfer_fund(self, amount, category):
      if (check_balance(amount)):
         self.withdraw(amount, 'Transfer to' + self.category)
         self.deposit(amount, 'Transfer from' + self.category)
         return True
      
      return False

category = budget('Clothing', 1000)
category_2 = budget('Food', 2000)
category_3 = budget('Entertament', 3000)

# print(category.deposit(1000))
print(category_2.withdraw(1000))
# print(category_2.deposit(2000))
# print(category_3.deposit(3000))