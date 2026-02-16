"""
Exercise 11: Shopping List Manager
Add, remove, view items in a list
"""

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("Shopping List Manager".center(50))
    print("=" * 50)
    print("1. View shopping list")
    print("2. Add item")
    print("3. Add multiple items")
    print("4. Remove item")
    print("5. Clear list")
    print("6. Search item")
    print("7. Sort list")
    print("8. Count items")
    print("9. Exit")
    print("=" * 50)


def view_list(shopping_list):
    """Display the shopping list"""
    if not shopping_list:
        print("\n📝 Your shopping list is empty!")
        return
    
    print("\n" + "=" * 50)
    print("Your Shopping List".center(50))
    print("=" * 50)
    
    for idx, item in enumerate(shopping_list, 1):
        print(f"{idx:2d}. {item}")
    
    print("=" * 50)
    print(f"Total items: {len(shopping_list)}")


def add_item(shopping_list):
    """Add an item to the shopping list"""
    item = input("\nEnter item name: ").strip()
    
    if not item:
        print("Item name cannot be empty!")
        return
    
    if item in shopping_list:
        print(f"'{item}' is already in your list!")
    else:
        shopping_list.append(item)
        print(f"✅ Added '{item}' to your list!")


def add_multiple_items(shopping_list):
    """Add multiple items at once"""
    items = input("\nEnter items separated by commas: ")
    item_list = [item.strip() for item in items.split(',')]
    
    added = 0
    for item in item_list:
        if item and item not in shopping_list:
            shopping_list.append(item)
            added += 1
    
    print(f"✅ Added {added} item(s) to your list!")


def remove_item(shopping_list):
    """Remove an item from the shopping list"""
    if not shopping_list:
        print("\n📝 Your shopping list is empty!")
        return
    
    view_list(shopping_list)
    
    try:
        choice = input("\nEnter item number or name to remove: ")
        
        # Try to remove by index
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(shopping_list):
                removed = shopping_list.pop(idx)
                print(f"✅ Removed '{removed}' from your list!")
            else:
                print("Invalid item number!")
        else:
            # Remove by name
            if choice in shopping_list:
                shopping_list.remove(choice)
                print(f"✅ Removed '{choice}' from your list!")
            else:
                print(f"'{choice}' not found in your list!")
                
    except ValueError:
        print("Invalid input!")


def search_item(shopping_list):
    """Search for an item in the shopping list"""
    if not shopping_list:
        print("\n📝 Your shopping list is empty!")
        return
    
    query = input("\nEnter search term: ").strip().lower()
    
    if not query:
        print("Search term cannot be empty!")
        return
    
    matches = [item for item in shopping_list if query in item.lower()]
    
    if matches:
        print(f"\n🔍 Found {len(matches)} match(es):")
        for idx, item in enumerate(matches, 1):
            print(f"  {idx}. {item}")
    else:
        print(f"No items found matching '{query}'")


def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == "1":
            view_list(shopping_list)
            
        elif choice == "2":
            add_item(shopping_list)
            
        elif choice == "3":
            add_multiple_items(shopping_list)
            
        elif choice == "4":
            remove_item(shopping_list)
            
        elif choice == "5":
            confirm = input("\n⚠️ Are you sure you want to clear the list? (y/n): ")
            if confirm.lower() == 'y':
                shopping_list.clear()
                print("✅ List cleared!")
            else:
                print("Cancelled.")
                
        elif choice == "6":
            search_item(shopping_list)
            
        elif choice == "7":
            if shopping_list:
                shopping_list.sort()
                print("✅ List sorted alphabetically!")
                view_list(shopping_list)
            else:
                print("\n📝 Your shopping list is empty!")
                
        elif choice == "8":
            count = len(shopping_list)
            print(f"\n📊 Your list has {count} item(s)")
            
        elif choice == "9":
            print("\n👋 Goodbye! Happy shopping!")
            break
        else:
            print("\n❌ Invalid choice! Please select 1-9.")


if __name__ == "__main__":
    main()
