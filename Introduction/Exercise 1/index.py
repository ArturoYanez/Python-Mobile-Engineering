# One iteration for each client
for i in range(3):
    # Enter the money
    print('Please enter the money: ')
    money = float(input())
    # Amount Validation
    if money >= 0.6:
        # Stock of products
        stock = [
            'Water Icecream',
            'Vanilla Icecream',
            'Icexcream Bombon',
            'Icekrevm Bombon',
            'Icecrema Bombon',
            'Random Fruit Icecream',
            '1/4 kg Box of Icecream']
        purchase = []
        
        # System of validations
        while money >= 0.6:
            if 0.6 <= money < 1:
                money -= 0.6
                change = money
                purchase.append(stock[0])
            elif 1 <= money < 1.6:
                money -= 1
                change = money
                purchase.append(stock[1])
            elif 1.6 <= money < 1.7:
                money -= 1.6
                change = money
                purchase.append(stock[2])
            elif 1.7 <= money < 1.8:
                money -= 1.7
                change = money
                purchase.append(stock[3])
            elif 1.8 <= money < 2.9:
                money -= 1.8
                change = money
                purchase.append(stock[4])
            elif money >= 2.9:
                print('You can choose two options:')
                print('1- ' + stock[-2] + ' or 2- ' + stock[-1])
                print('Choose an option: ')
                switch = False
                while not switch:
                    option = int(input())
                    if option == 1:
                        money -= 2.9
                        change = money
                        purchase.append(stock[-2])
                        switch = True
                    elif option == 2:
                        money -= 2.9
                        change = money
                        purchase.append(stock[-1])
                        switch = True
                    else:
                        print('Enter a valid option from the list...')
                        
        # Resukts of the buy
        print("Thank you for buying: " + ', '.join(purchase))
        print("Your change is: $" + str(change))
        
    else:
        print('Insufficient amount... Please try again')

print('Thanks for using our software! :D')