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
        print("Please insert coins")
        user_quart = float(input("How many Quarters? "))
        user_dimes = float(input("How many Dimes? "))
        user_nickles = float(input("How many Nickles? "))
        user_pennies = float(input("How many pennies? "))

        def usertot(quart, dim, nick, pen):
            return quart * quarters + dim * dimes + nick * nickle + pen * penny

        user_tot = usertot(user_quart, user_dimes, user_nickles, user_pennies)

         




