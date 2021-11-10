
#
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee in to the cup")
# print("Pouring some self.milk in to the cup")
# print("Coffee is ready")

# water = 200
# self.milk = 50
# coffee = 15
#
# user_input = int(input("How many cup of coffee you need:" "\n>"))
#
# needed_self.milk = 200*user_input
# needed_water = 50*user_input
# needed_coffe = 15*user_input
#
#
# print("For", user_input, "Cup of coffee tou will need:")
# print("Water=", needed_water, "ml." "\nmilk=", needed_self.milk, "ml." "\nCoffee=", needed_coffe, "g.")


class ResourceError(Exception):
    pass


class CoffeeMachine(object):
    """CoffeeMachine"""
    running = False

    def __init__(self, water=400, money=550, coffee=120, milk=540, cups=9):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

        if not CoffeeMachine.running:
            self.main()

    def print_parametrs(self):
        print("Coffee machine has:")
        print(self.money, "UAH")
        print(self.coffee, "grams of coffee")
        print(self.water, "ml of water")
        print(self.milk, "ml of self.milk")
        print(self.cups, "Cups")

    def select_action(self) -> str:
        return input("CHOOSE ACTION\n-buy\n-fill\n-take\n-remaining\n-exit\n>")

    def select_drink(self) -> int:
        back = input("What are you want to buy\n1-espresso\n2-latte\n3-cappuccino\nback - to main menu\n>")
        if back == "back":
            return self.main()
        return int(back)

    def is_enough(self, need_water=0, need_milk=0, need_coffee=0):

        if self.water < need_water:
            print("Sorry, not enough water!\n")
            raise ResourceError
        if self.milk < need_milk:
            print("Sorry, not enough self.self.milk!\n")
            raise ResourceError
        if self.coffee < need_coffee:
            print("Sorry, not enough beans!\n")
            raise ResourceError
        if self.cups < 1:
            print("Sorry, not enough cups\n")
            raise ResourceError
        print("I have enough resources, making you a coffee!\n")

    def buy_drinks(self):
        drink = self.select_drink()

        try:
            if drink == 0:
                pass
            if drink == 1:
                self.is_enough(need_coffee=16, need_water=250)

                self.money += 4
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
            elif drink == 2:
                self.is_enough(need_water=350, need_coffee=20, need_milk=75)

                self.money += 7
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
            elif drink == 3:
                self.is_enough(need_water=350, need_milk=100, need_coffee=12)

                self.money += 6
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
        except ValueError:
            self.main()

    def fill_machine(self):
        while input == "":
            self.water += int(input("Write how many ml of water do you want to add\n>"))
            self.milk += int(input("Write how many ml of self.milk do you want to add\n>"))
            self.coffee += int(input("Write how many grams of coffee do you want to add\n>"))
            self.cups += int(input("Write how many cups do you want to add\n>"))

    def take_money(self):
        print("I give you", self.money, "money")
        self.money -= self.money

    def main(self):
        self.running = True
        self.print_parametrs()

        while True:
            action = self.select_action()

            if action == "buy":
                self.buy_drinks()
            elif action == "fill":
                self.fill_machine()
            elif action == "take":
                self.take_money()
            elif action == "exit":
                exit()
            elif action == "remaining":
                self.print_parametrs()


CoffeeMachine(water=400, money=550, coffee=120, milk=540, cups=9)


# def print_parametrs():
#     print("Coffee machine has:")
#     print(money, "UAH")
#     print(coffee, "grams of coffee")
#     print(water, "ml of water")
#     print(self.milk, "ml of self.milk")
#     print(cups, "Cups")
#
#
# def select_action():
#     return input("CHOOSE ACTION\n-buy\n-fill\n-take\n-remaining\n-exit\n>")
#
#
# def select_drink() -> int:
#     back = input("What are you want to buy\n1-espresso\n2-latte\n3-cappuccino\nback - to main menu\n>")
#     if back == "back":
#         return main()
#     return int(back)
#
#
# def is_enough(need_water=0, need_self.milk=0, need_coffee=0):
#     if water < need_water:
#         print("Sorry, not enough water!\n")
#         raise ResourceError
#     if self.milk < need_self.milk:
#         print("Sorry, not enough self.milk!\n")
#         raise ResourceError
#     if coffee < need_coffee:
#         print("Sorry, not enough beans!\n")
#         raise ResourceError
#     if cups < 1:
#         print("Sorry, not enough cups\n")
#         raise ResourceError
#     print("I have enough resources, making you a coffee!\n")
#
#
# def buy_drinks():
#     global money, coffee, self.milk, water, cups
#     drink = select_drink()
#
#     try:
#         if drink == 0:
#             pass
#         if drink == 1:
#             is_enough(need_water=250, need_coffee=16)
#             money += 4
#             water -= 250
#             coffee -= 16
#             cups -= 1
#         elif drink == 2:
#             is_enough(need_water=350, need_coffee=20, need_self.milk=75)
#
#             money += 7
#             water -= 350
#             self.milk -= 75
#             coffee -= 20
#             cups -= 1
#         elif drink == 3:
#             is_enough(need_water=350, need_self.milk=100, need_coffee=12)
#             money += 6
#             water -= 200
#             self.milk -= 100
#             cups -= 1
#         else:
#             raise ValueError
#     except ResourceError:
#         pass
#
#
# def fill_machine():
#     global water, coffee, self.milk, cups
#     water += int(input("Write how many ml of water do you want to add\n>"))
#     self.milk += int(input("Write how many ml of self.milk do you want to add\n>"))
#     coffee += int(input("Write how many grams of coffee do you want to add\n>"))
#     cups += int(input("Write how many cups do you want to add\n>"))
#
#
# def take_money():
#     global money
#     print("I give you", money, "money")
#     money = 0
#
#
# def main():
#     print_parametrs()
#
#     while True:
#         action = select_action()
#
#         if action == "buy":
#             buy_drinks()
#         elif action == "fill":
#             fill_machine()
#         elif action == "take":
#             take_money()
#         elif action == "exit":
#             exit()
#         elif action == "remaining":
#             print_parametrs()
#
#
# main()
