#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.discount = discount  # store the discount percentage
    self.total = 0  # initialize total to 0
    self.items = []  # initialize items list (avoiding mutable default argument)
    self.last_transaction = 0  # track last transaction for voiding
  
  def add_item(self, title, price, quantity=1):
    self.total += price * quantity  # add item cost to total
    self.last_transaction = price * quantity  # store this transaction amount
    for _ in range(quantity):  # add item to list quantity times
      self.items.append(title)
  
  def apply_discount(self):
    if self.discount > 0:  # check if discount exists
      self.total = int(self.total * (1 - self.discount / 100))  # apply discount and convert to int
      print(f"After the discount, the total comes to ${self.total}.")
    else:  # no discount available
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    self.total -= self.last_transaction  # subtract last transaction from total
