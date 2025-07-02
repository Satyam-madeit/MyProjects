import csv


class Item:
    """Represents a single item in the inventory."""
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_list(self):
        return [self.name, str(self.quantity), str(self.price)]

    def __str__(self):
        return f"{self.name} | Quantity: {self.quantity} | Price: ₹{self.price:.2f}"


class InventoryManager:
    """Manages a collection of inventory items."""
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        if name in self.items:
            return "Item already exists."
        self.items[name] = Item(name, quantity, price)
        return "Item added successfully."

    def view_items(self):
        if not self.items:
            return "Inventory is empty."
        return "\n".join(str(item) for item in self.items.values())

    def update_quantity(self, name, quantity):
        if name in self.items:
            self.items[name].quantity = quantity
            return "Quantity updated successfully."
        return "Item not found."

    def delete_item(self, name):
        if name in self.items:
            del self.items[name]
            return "Item deleted successfully."
        return "Item not found."

    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Quantity", "Price"])
            for item in self.items.values():
                writer.writerow(item.to_list())
        return "Inventory saved to file."

    def load_from_csv(self, filename):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    name, quantity, price = row
                    self.items[name] = Item(name, int(quantity), float(price))
            return "Inventory loaded from file."
        except FileNotFoundError:
            return "File not found."


def main():
    inventory = InventoryManager()

    while True:
        print("\n--- Inventory Manager ---")
        print("1. Add Item")
        print("2. View All Items")
        print("3. Update Item Quantity")
        print("4. Delete Item")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: ₹"))
            print(inventory.add_item(name, quantity, price))

        elif choice == "2":
            print(inventory.view_items())

        elif choice == "3":
            name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity: "))
            print(inventory.update_quantity(name, quantity))

        elif choice == "4":
            name = input("Enter item name to delete: ")
            print(inventory.delete_item(name))

        elif choice == "5":
            print(inventory.save_to_csv("inventory.csv"))

        elif choice == "6":
            print(inventory.load_from_csv("inventory.csv"))

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
