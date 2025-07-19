from art import espresso, latte, cappuccino


def prompt_order(flavor):
    match flavor:
        case "espresso":
            print(espresso)
        case "latte":
            print(latte)
        case "cappuccino":
            print(cappuccino)
        case _:
            print("We do not have this flavor. Please try again.")
            flavor = input("What would you like? (espresso/latte/cappuccino)\n")
            prompt_order(flavor)
    if flavor == "espresso" or flavor == "latte" or flavor == "cappuccino":
        print(f"You picked {flavor}! Brewing! :)")


def coffee_machine_report(report_resources):
    print(f"Water: {report_resources["water"]}ml")
    print(f"Milk: {report_resources["milk"]}ml")
    print(f"Coffee: {report_resources["coffee"]}g")
    print(f"Money: ${report_resources["money"]}")


def press_buttons(button, report_resources):
    match button:
        case "report":
            coffee_machine_report(report_resources)
        case "off":
            print("You have pressed the off button.\nSee yah!")
            exit()
        case _:
            print("Oopsie, machine do not have this button.")
            button = input("Type 'report' to display resources or 'off' to turn off machine.\n")
            press_buttons(button, report_resources)


def check_resources(order, order_requirement, report_resources):
    order_proceed = True
    resource_status_dict = {}
    report_resources_copy = {}
    for item in report_resources:
        report_resources_copy[item] = report_resources[item]
    del report_resources_copy["money"]

    if order == 'espresso':
        del report_resources_copy["milk"]

    for resource_order, report_resource in zip(order_requirement, report_resources_copy):
        print(f"({resource_order} _ {report_resource})")
        if order_requirement[resource_order] > report_resources_copy[report_resource]:
            resource_status_dict[resource_order] = 'insufficient resource'
        elif report_resources[report_resource] == 0:
            resource_status_dict[resource_order] = 'depleted resource'
        else:
            resource_status_dict[resource_order] = 'enough resource'

    # make list of resource check
    resource_status_list = []
    for resource in resource_status_dict:
        resource_status_list.append(resource_status_dict[resource])

    print(resource_status_list)
    # identify what type of problem your coffee machine has
    if any(status == 'insufficient resource' for status in resource_status_list):
        for resource_order, report_resource in zip(order_requirement, report_resources):
            if order_requirement[resource_order] > report_resources_copy[report_resource]:
                print(f"Sorry there is not enough {resource_order} to make your {order}.")
        order_proceed = False
    elif any(status == 'depleted resource' for status in resource_status_list):
        for resource_order, report_resource in zip(order_requirement, report_resources):
            if order_requirement[resource_order] > report_resources_copy[report_resource]:
                print(f"Sorry resource {resource_order} is depleted.\nTurn off machine to refill.")
        order_proceed = False
        button = input("Type 'report' to display resources or 'off' to turn off machine.\n")
        press_buttons(button, report_resources)
    else:
        print("All set! Kindly put in coins here.")
        order_proceed = True
    return order_proceed


def collect_coins():
    collect_coins_dict = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    collected_coin = []
    for coin in collect_coins_dict:
        collect_prompt = float(input(f"Please type amount of {coin} to be inserted. "))
        collected_coin.append(collect_prompt * collect_coins_dict[coin])
    print(f"Total coin inserted is ${sum(collected_coin)}.")
    return sum(collected_coin)


def check_coins(payment, price_of_order, machine_money):
    if payment >= price_of_order:
        proceed_order = True
        if payment > price_of_order and machine_money >= (payment - price_of_order):  # change
            print(f"Hey! Here's your change {round(payment - price_of_order,2)}.")
        elif payment > price_of_order and machine_money < (payment - price_of_order):
            print("Oh no, no change for you mwahahaha.")
    else:
        print(f"Hey, price of your order is {price_of_order}. Please try again wen u not broke.")
        proceed_order = False
    return proceed_order

# def update_resources(current_report_resources, latest_order_requirement):
