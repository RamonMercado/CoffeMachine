from Menu import MENU

WATER = 1000  # milliLiters
MILK = 500  # miLliLiters
COFFEE = 76  # grams
ESPRESSO_PRICE = 1.5
LATTE_PRICE = 2.5
CAPPUCCINO_PRICE = 3
MONEY = 0
machine_on = True


def report():
    global WATER, MILK, COFFEE
    money_reformat = "{:.2f}".format(MONEY)
    print(f"Water: {WATER}\nMilk: {MILK}\nCoffee: {COFFEE}\nMoney: {money_reformat}")


def make_espresso():
    global WATER, COFFEE
    WATER -= 50
    COFFEE -= 18
    print("Here's your espresso. Enjoy!")


def make_latte():
    global WATER, COFFEE, MILK
    WATER -= 200
    COFFEE -= 24
    MILK -= 150
    print("Here's your latte. Enjoy!")

def make_cappuccino():
    global WATER, COFFEE, MILK
    WATER -= 250
    COFFEE -= 24
    MILK -= 100
    print("Here's your cappuccino. Enjoy!")


def check_resources(water, milk, coffee):
    global MILK, WATER, COFFEE
    if (MILK - milk) < 0:
        print("Sorry there is not enough milk.")
        return False
    elif (WATER - water) < 0:
        print("Sorry there is not enough water.")
        return False
    elif (COFFEE - coffee) < 0:
        print("Sorry there is not enough coffee.")
        return False
    return True


def check_transaction(total, prices):
    global MONEY

    if total - prices >= 0:
        change = total - prices
        MONEY = MONEY + prices
        return [True, change]
    else:
        total = "{:.2f}".format(total)
        print(f"Sorry that's not enough money. {total} refunded")
        return [False, total]


def process_coins():
    print("Please insert coins.")
    number_quarters = int(input("how many quarters?: "))
    number_dimes = int(input("how many dimes?: "))
    number_nickles = int(input("how many nickles?: "))
    number_pennies = int(input("how many pennies?: "))

    total = 0.25 * number_quarters + 0.10 * number_dimes + 0.05 * number_nickles + 0.01 * number_pennies

    return total


def run_machine():
    selection = input("What wold you like? (Espresso/Latte/Cappuccino): ").lower()
    if selection == 'espresso':
        resource_available = check_resources(50, 0, 18)
        if resource_available:
            money_inserted = process_coins()
            result = check_transaction(money_inserted, ESPRESSO_PRICE) #return [Boolean, Money change]
            if result[0] and resource_available:
                make_espresso()
                if result[1] > 0:
                    change = "{:.2f}".format(result[1])
                    print(f"Here is ${change} dollars in change")
            else:
                return
        else:
            return
    elif selection == 'latte':
        resource_available = check_resources(200, 150, 24)
        if resource_available:
            money_inserted = process_coins()
            result = check_transaction(money_inserted, LATTE_PRICE)  # return [Boolean, Money change]
            if result[0] and resource_available:
                make_latte()
                if result[1] > 0:
                    change = "{:.2f}".format(result[1])
                    print(f"Here is ${change} dollars in change")
            else:
                return
        else:
            return
    elif selection == 'cappuccino':
        resource_available = check_resources(520, 100, 24)
        if resource_available:
            money_inserted = process_coins()
            result = check_transaction(money_inserted, CAPPUCCINO_PRICE)  # return [Boolean, Money change]
            if result[0] and resource_available:
                make_cappuccino()
                if result[1] > 0:
                    change = "{:.2f}".format(result[1])
                    print(f"Here is ${change} dollars in change")
            else:
                return
        else:
            return
    elif selection == 'off':
        print("Good bye!")
        global machine_on
        machine_on = False
        return
    elif selection == 'report':
        report()
    else:
        print('Wrong selection, try again!')
        return


while machine_on:
    run_machine()
