class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append(MenuItem(name, price))

    def display(self):
        print("Menu:")
        for i, item in enumerate(self.items):
            print(f"{i + 1}. {item}")
        print()


class Order:
    def __init__(self):
        self.ordered_items = []

    def add_to_order(self, item):
        self.ordered_items.append(item)

    def calculate_total(self):
        total = sum(item.price for item in self.ordered_items)
        return total

    def display_order(self):
        if not self.ordered_items:
            print("No items in order.")
            return
        print("Your Order:")
        for item in self.ordered_items:
            print(f"- {item.name} - ${item.price:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


class FoodOrderSystem:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def setup_menu(self):
        # Add predefined items to the menu
        self.menu.add_item("Pizza", 8.99)
        self.menu.add_item("Burger", 5.49)
        self.menu.add_item("Pasta", 7.99)
        self.menu.add_item("Salad", 4.99)
        self.menu.add_item("Soda", 1.99)

    def take_order(self):
        self.menu.display()
        while True:
            choice = input("Enter the item number to order (or 'q' to finish): ")
            if choice.lower() == 'q':
                break
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.menu.items):
                    selected_item = self.menu.items[choice - 1]
                    self.order.add_to_order(selected_item)
                    print(f"{selected_item.name} added to your order.\n")
                else:
                    print("Invalid selection, please choose a valid item number.\n")
            else:
                print("Please enter a valid number or 'q' to quit.\n")

    def show_bill(self):
        self.order.display_order()


def main():
    system = FoodOrderSystem()
    system.setup_menu()

    print("Welcome to the Food Order Management System!")
    while True:
        print("\n1. Place an order")
        print("2. View your bill")
        print("3. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            system.take_order()
        elif choice == '2':
            system.show_bill()
        elif choice == '3':
            print("Thank you for visiting! Have a great day.")
            break
        else:
            print("Invalid option, please choose again.")


if __name__ == "__main__":
    main()
