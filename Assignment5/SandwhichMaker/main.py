import data
import sandwich_maker
import cashier

# resources and recipes init
recipes = data.recipes()
resources = data.resources()

# instances of classes
maker = sandwich_maker.SandwichMaker(resources)
cash = cashier.Cashier()

### Make an instance of SandwichMachine class and write the rest of the codes ###
def print_report(resources):
    print(f"Bread: {resources['bread']} slice(s)")
    print(f"Ham: {resources['ham']} slice(s)")
    print(f"Cheese: {resources['cheese']} slice(s)")

is_on = True
while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report(maker.machine_resources)
    elif choice in recipes:
        sandwich = recipes[choice]
        if maker.check_resources(sandwich["ingredients"]):
            payment = cash.process_coins()
            if cash.transaction_result(payment, sandwich["cost"]):
                maker.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid input.")