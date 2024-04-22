from day15_data import MENU

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters": 25,
    "dimes": 10,
    "nickels": 5,
    "cents": 1,
}

keep_running = True


def check_sufficient_resources(drink_selected):
    for r in MENU[drink_selected]['ingredients']:
        r_in_drink = MENU[drink_selected]['ingredients'][r]
        if resources[r] < r_in_drink:
            print(f"Sorry, there's not enough {r}")
            return False
    return True


def subtract_resources(drink_selected):
    for r in MENU[drink_selected]['ingredients']:
        resources[r] -= MENU[drink_selected]['ingredients'][r]


def process_coins(costs):
    sum_inserted = 0
    for c in coins:
        c_quantity = int(input(f"How many {c} do you insert? "))
        sum_inserted += (c_quantity * coins[c]) / 100
        sum_inserted = round(sum_inserted, 2)
    if sum_inserted >= costs:
        change = sum_inserted - costs
        print(f"You inserted {sum_inserted}, your change is {round(change, 2)}")
        return True
    else:
        print(f"Not enough money. You inserted {sum_inserted}, the price is {costs}. Money returned")


def process_coffee(selected):
    global profit
    resource_check = check_sufficient_resources(selected)
    if resource_check:
        price = MENU[selected]['cost']
        print(f"{selected} costs {price}$")
        was_payment_accepted = process_coins(price)
        if was_payment_accepted:
            print(f"Here's your {selected}, enjoy!")
            subtract_resources(selected)
            profit += price
    else:
        return False


def print_report():
    print(f"profit: {profit}")
    for r in resources:
        print(f"{r}: {resources[r]}")


def shut_down():
    global keep_running
    print("shutting down")
    keep_running = False


def selection_process(selected):
    if selected == "espresso" or selected == "latte" or selected == "cappuccino":
        coffee_processed = process_coffee(selected)
        if not coffee_processed:
            return False
    elif selected == "report":
        print_report()
    elif selected == "off":
        shut_down()


def run_program():
    global keep_running
    while keep_running:
        selection = input("What would you like to drink? espresso/latte/cappuccino: ").lower()
        selection_process(selection)


run_program()
