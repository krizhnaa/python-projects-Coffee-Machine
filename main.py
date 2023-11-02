import cmdata

user_inp = input("What would you like? (espresso/latte/cappuccino): ")

# print(cmdata.menu['espresso']['ingredients']['water'])

def cmres(res):
    return cmdata.resources[res]

if user_inp == 'report':
    print(f"Water : {cmres('water')}ml")
    print(f"Milk : {cmres('milk')}ml")
    print(f"coffee : {cmres('coffee')}g")