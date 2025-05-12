from menu import Menu  
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee=CoffeeMaker()
moneymachine=MoneyMachine()

continueious=False

while continueious is not True:
    ask = input(f"What would you like to take latte/capaccino/espresso: ")
    if ask == "exitnow" :
        exit()
    if ask != "report":
        item = menu.find_drink(ask)
        enough = coffee.is_resource_sufficient(drink=item)
        if enough == True:
            moneymachine.make_payment(item.cost)
            coffee.make_coffee(item)
    else:
        coffee.report()
        moneymachine.report()
