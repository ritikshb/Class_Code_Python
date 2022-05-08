logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
auction_dic = {}
print(logo)
def auction(name,bit_price):
  auction_dic[name] = bit_price
input_user = True
while input_user:
  name = input("Enter name of bidder: ")
  amount = int(input("Enter Bit amount: "))
  auction(name,amount)
  user_ask = input("You want add more participant then enter 'yes' otherwise 'no'").lower()
#   clear()
  if user_ask == 'no':
    input_user = False
max = 0
new_name = ''
for key in auction_dic:
  if max<auction_dic[key]:
    new_name = key
    max = auction_dic[key]
print(f"Max bidder is {new_name} and bid is {max}")