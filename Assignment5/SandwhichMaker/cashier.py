class Cashier:
    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("How many large dollars?: ")) * 1.00
        half_dollars = int(input("How many half dollars?: ")) * 0.50
        quarters = int(input("How many quarters?: ")) * 0.25
        nickels = int(input("How many nickels?: ")) * 0.05
        total = dollars + half_dollars + quarters + nickels
        return round(total, 2)

    def transaction_result(self, coins, cost):
        if coins < cost:
            print(f"Sorry there is not enough {coins}. Money is refunded")
            return False
        elif coins > cost:
            change = round(cost - coins, 2)
            print(f"Here is {change} in change")
        print("Transaction successful.")
        return True
