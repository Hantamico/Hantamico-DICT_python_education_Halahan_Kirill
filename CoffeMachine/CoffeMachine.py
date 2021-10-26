
#
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee in to the cup")
# print("Pouring some milk in to the cup")
# print("Coffee is ready")

# water = 200
# milk = 50
# coffee = 15
#
# user_input = int(input("How many cup of coffee you need:" "\n>"))
#
# needed_milk = 200*user_input
# needed_water = 50*user_input
# needed_coffe = 15*user_input
#
#
# print("For", user_input, "Cup of coffee tou will need:")
# print("Water=", needed_water, "ml." "\nMilk=", needed_milk, "ml." "\nCoffee=", needed_coffe, "g.")


def count_cups(water, milk, coffee, cups) -> str:
    possible = min([water//200, milk//50, coffee//15])

    if possible == cups:
        announce = "Yes, I can make that amount of coffee"
    elif possible > cups:
        announce = f" Yes, I can make that amount of coffee (and even {possible - cups} more than that)"
    else:
        announce = f" I can make only {possible} cups of coffee"
    return announce


def main():
    water = int(input("Print how many ml of water coffee machine has\n>"))
    milk = int(input("Print how many ml of milk coffee machine has\n>"))
    coffee = int(input("Print how many grams of coffee coffee machine has\n>"))
    cups = int(input("Print how many cups of coffee you will need\n>"))
    print(count_cups(water, milk, coffee, cups))


main()
