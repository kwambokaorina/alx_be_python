# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\nYour shopping list:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")

def main():
    shopping_list = []  # Start with an empty list
    while True:
        display_menu()  # Show the menu
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)  # Add an item
        elif choice == '2':
            remove_item(shopping_list)  # Remove an item
        elif choice == '3':
            view_list(shopping_list)  # Display the shopping list
        elif choice == '4':
            print("Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
