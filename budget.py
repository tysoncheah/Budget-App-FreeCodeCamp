#Hi there, if you have any feedback on the code,
#feel free to contact me on linkedin
#https://www.linkedin.com/in/tyson-cheah

class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=None):
    if description != None:
      self.ledger.append({'amount': amount , 'description': description})
    else:
      self.ledger.append({'amount': amount , 'description':''})
  
  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance += i['amount']
    return balance

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def withdraw(self, amount, description=None):
    if self.check_funds(amount) == True:
      if description != None:
        self.ledger.append({'amount':-(amount) , 'description':description})
      else:
        self.ledger.append({'amount':-(amount) , 'description':''})
      return True
    else:
      return False

  def transfer(self, amount, transfer_category):
    if self.check_funds(amount) == True:    
      self.ledger.append({'amount':-(amount) , 'description': f'Transfer to {transfer_category.name}'})
      
      transfer_category.deposit(amount , description = f'Transfer from {self.name}')
      return True
    else:
      return False 

  def __str__(self):
    name = self.name
    categories_str = name.center(30, '*')
    for i in self.ledger:
      try:
        ledger_description = i['description'][0:23]
      except:
        ledger_description = ''
      
      ledger_amount = str('{:.2f}'.format(i['amount']))
      categories_str += f'\n{ledger_description:<23}{ledger_amount:>7}'
    categories_str += '\nTotal: ' + str(self.get_balance())
    return categories_str

def create_spend_chart(categories):
  spend_dic = {}
  for i in categories:
    s = 0
    for j in i.ledger:
      if j['amount'] <=0:
        s += abs(j['amount']) 
    spend_dic[i.name] = round(s,2)    
  total = sum(spend_dic.values())
  percent_dict = {}
  for p in spend_dic.keys():
    percent_dict[p] = round(spend_dic[p]/total,2)*100
  output = 'Percentage spent by category\n'
  for n in range(100,-10,-10):
      output += f'{n}'.rjust(3) + '| '
      for i in percent_dict.values():
        if i >= n :
          output += 'o  '
        else:
          output += '   '
      output += '\n'
  output += '    '+ '-'*(len(categories)*3+1)
  output += '\n     '
  key_list = list(spend_dic.keys())
  max_len = max(len(i) for i in key_list)
  for i in range(max_len):
    for l in key_list:
      if len(l) > i:
        output += l[i] + '  '
      else: 
        output += '   '
    if i < max_len-1:
      output += '\n     '
  return output
