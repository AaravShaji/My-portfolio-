''' This program checks whether the customer is eligible for a free delivery if within 20 km radius and purchases
orders above $ 40 and if not, prompts the customer to add a pre-determinded amount set by the program to be eligible. 
'''
def check_free_delivery(amount:float,distance:float)->None:
    if amount < 0 or distance < 0 :
        print('Invalid entry, orders must be positive')
    elif distance >= 0 and distance < 20:
        print('Proceeding to check amount..')
        if amount >= 0 and amount < 40:
            print('Add $ 14.70 to your order to get a free delivery =)')
        else:
            print('You are getting a free delivery ! :D')
    else:
        print('Sorry your not eligible for the free delivery.. :(')

def main():
    amount = float(input('What is the dollar amount for the current order ?'))
    distance = float(input('How far do you stay ?'))
    check_free_delivery(amount,distance)
main()