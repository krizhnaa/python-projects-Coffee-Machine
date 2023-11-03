import cmdata

cm_continue = True
res_suff = False
quarters = 0.25
dimes = 0.10
nickle = 0.05
penny = 0.01

while cm_continue != 'False':
    user_inp = input("What would you like? (espresso/latte/cappuccino): ")

    # print(cmdata.menu['espresso']['ingredients']['water'])

    def cmres(res):
        return cmdata.resources[res]

    if user_inp == 'report':
        print(f"Water : {cmres('water')}ml")
        print(f"Milk : {cmres('milk')}ml")
        print(f"coffee : {cmres('coffee')}g")
        res_suff = False

    if user_inp == 'off':
        cm_continue = False

    def rescheck(coffee, material):
        return cmdata.menu[coffee]['ingredients'][material]

    if user_inp == 'latte' or user_inp == 'espresso' or user_inp == 'cappuccino':
        if rescheck(user_inp, 'water') >= cmres('water'):
            print("Sorry there is shortage in Water")
        elif user_inp != 'espresso' and rescheck(user_inp, 'milk') >= cmres('milk'):
            print("Sorry there is shortage in Milk")
        elif rescheck(user_inp, 'coffee') >= cmres('coffee'):
            print("Sorry there is shortage in Coffee")
        else:
            res_suff = True


    def costcheck(coffee):
        return cmdata.menu[coffee]['cost']

    if res_suff == True:
        print("Please insert the coins")
        user_quart = float(input("How many Quarters? "))
        user_dimes = float(input("How many Dimes? "))
        user_nickles = float(input("How many Nickles? "))
        user_pennies = float(input("How many pennies? "))

        def usertot(quart, dim, nick, pen):
            return quart * quarters + dim * dimes + nick * nickle + pen * penny

        user_tot = usertot(user_quart, user_dimes, user_nickles, user_pennies)

        print(user_tot)
        print(costcheck(user_inp))

        user_change = user_tot - costcheck(user_inp)
        tran_comp = False

        if user_tot == costcheck(user_inp):
            # print(f"Transaction Successful, You will be receiving {user_inp} shortly.")
            tran_comp = True
        elif user_tot > costcheck(user_inp):
            # print(f"Transaction Successful, You will be receiving {user_inp} shortly.")
            tran_comp = True
            print(f"Your change is ${user_change}")
        else:
            print("Sorry that's not enough money. Money refunded")

        if tran_comp == True:
            print(f"You will be receiving your {user_inp} shortly!!!")
            # print(cmdata.resources['water'])
            # print(rescheck(user_inp, 'water'))
            cmdata.resources['water'] -= rescheck(user_inp, 'water')
            if user_inp != 'espresso':
                cmdata.resources['milk'] -= rescheck(user_inp, 'milk')
            cmdata.resources['coffee'] -= rescheck(user_inp, 'coffee')
            # print(cmdata.resources['water'])




