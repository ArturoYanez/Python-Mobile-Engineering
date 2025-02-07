# Inputs:
# hour between 1 and 12
# age
# repeat 3 times and SUBMIT


free_ticket = True


def party_security(hour):
    global free_ticket
    age = int(input('Enter your age please: '))
    if age >= 18:
        if 2 <= hour < 7 and free_ticket:
            print('Congrats, you can enter free!')
            free_ticket = False
        elif hour > 12 or hour < 1:
            print('Sorry, the party is over...')
        else:
            print('Pay your ticket and enter to the party...')
    else:
        print("Sorry, you can't enter to this party...")


party_security(int(input('Enter the hour: ')))
party_security(int(input('Enter the hour: ')))
party_security(int(input('Enter the hour: ')))
