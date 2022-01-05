class Category:
  def __init__(self, name):
    self.n = name
    self.ledger = []
    self.funds = 0
    self.withdraws = 0

  def __str__(self): 
    output = ""
    numStars = int((30 - len(self.n))/2)
    for i in range(numStars):
      output = output + "*"
    output = output + self.n
    for i in range(numStars):
      output = output + "*"
    output = output + "\n"
    for i in self.ledger:
      p = str(i['amount'])
      if ('.' not in p):
        p = p + '.00'
      p = p.rjust(30 - len(i['description'][0:23]))
      output = output + i['description'][0:23] + p + "\n"
    output = output + "Total: " + str(self.funds)
    return output.rstrip('\n')

  def deposit(self, amount, desc = ""):
    self.ledger.append({"amount": amount, "description": desc})
    self.funds+=amount
  
  def withdraw(self, amount, desc = ""):
    if (self.check_funds(amount)):
      self.funds-=amount
      self.withdraws+=amount
      self.ledger.append({"amount": -1*amount, "description": desc})
      return True
    else:
      return False

  def get_balance(self):
    return self.funds

  def transfer(self, amount, category):
    if (self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + str(category.n))
      category.deposit(amount, "Transfer from " + self.n)
      return True
    return False
  
  def check_funds(self, amount):
    if (amount > self.funds):
      return False
    else:
      return True



def create_spend_chart(categories):
  percentages = []
  names = []
  sum = 0
  for i in categories:
    sum = sum + i.withdraws
    names.append(i.n)
  for i in categories:
    percentages.append((i.withdraws/sum)*100)
  output = "Percentage spent by category" + "\n"
  for i in range (100,-1,-10):
    label = str(i) + "|"
    label = label.rjust(4)
    label = label + " "
    for j in percentages:
      if (j > i):
        label = label + "o  "
      else:
        label = label + "   "
    output = output + label + "\n"
  output = output + "    --"
  for i in range(len(categories) + 1):
    output = output + "--"
  output = output + "\n     "
  count = 0
  
  for i in range(len(max(names, key=len))):
    for j in categories:
      if (len(j.n) > count):
        output = output + j.n[count] + "  "
      else:
        output = output + "   "
    output = output + "\n     "
    count+=1
  return output.rstrip() + "  "
