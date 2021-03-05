import datetime
import sys

for line in sys.stdin:

    data = line.strip().split("\t")

current_time = datetime.datetime.now()
current_store = input("store number")
current_item = input("inventory") #item sku
current_cost = input("money")
current_payment = input("vendor") #invoice total paid 

if len(data) == 4:

    data= (current_time, current_store, current_item, current_cost, current_payment) 

print("{0}\t{1}\{3}{4}")