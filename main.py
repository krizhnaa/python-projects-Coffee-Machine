import cmdata

cm_continue = True
res_suff = False

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


    if res_suff == True:
        print("Please insert coins")
        user_quart = input("How many Quarters? ")
        user_dimes = input("How many Dimes? ")
        user_nickles = input("How many Nickles? ")
        user_pennies = input("How many pennies? ")


