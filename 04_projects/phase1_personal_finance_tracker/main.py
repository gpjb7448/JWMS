"""
Personal Finance Tracker - Main Application

STEP-BY-STEP GUIDE:
===================
1. Display welcome message and menu
2. Get user choice
3. Execute corresponding function
4. Loop until user exits
5. Save data before exiting

This is the main entry point for the finance tracker application.
"""

import sys
from datetime import datetime
from transaction import Transaction, TransactionManager
from category import CategoryManager
from reports import ReportGenerator
from file_handler import FileHandler
from utils import clear_screen, print_header, get_valid_input, format_currency


def display_menu():
    """
    Display the main application menu
    
    STEP 1: Clear screen for clean display
    STEP 2: Show header
    STEP 3: Display menu options
    STEP 4: Show current balance
    """
    clear_screen()
    print_header("PERSONAL FINANCE TRACKER")
    
    print("\n📊 MAIN MENU")
    print("=" * 60)
    print("1.  💰 Add Income")
    print("2.  💸 Add Expense")
    print("3.  📋 View All Transactions")
    print("4.  🔍 Filter Transactions")
    print("5.  📈 Monthly Report")
    print("6.  📊 Category Summary")
    print("7.  💵 View Balance")
    print("8.  🗑️  Delete Transaction")
    print("9.  📁 Export to CSV")
    print("10. ⚙️  Manage Categories")
    print("0.  🚪 Exit")
    print("=" * 60)


def add_income(transaction_manager, category_manager):
    """
    Add a new income transaction
    
    STEP 1: Get transaction details from user
    STEP 2: Validate input
    STEP 3: Create transaction object
    STEP 4: Add to transaction manager
    STEP 5: Save to file
    """
    print("\n" + "=" * 60)
    print("💰 ADD INCOME".center(60))
    print("=" * 60)
    
    try:
        # STEP 1: Get amount
        amount = float(input("\nAmount: $"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        
        # STEP 2: Select category
        categories = category_manager.get_categories('income')
        print("\nCategories:")
        for idx, cat in enumerate(categories, 1):
            print(f"{idx}. {cat}")
        
        cat_choice = int(input("\nSelect category (number): "))
        if 1 <= cat_choice <= len(categories):
            category = categories[cat_choice - 1]
        else:
            print("❌ Invalid category!")
            return
        
        # STEP 3: Get description
        description = input("Description: ").strip()
        if not description:
            description = f"Income - {category}"
        
        # STEP 4: Get date (or use today)
        date_input = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_input:
            date = datetime.strptime(date_input, "%Y-%m-%d").date()
        else:
            date = datetime.now().date()
        
        # STEP 5: Create and add transaction
        transaction = Transaction('income', amount, category, description, date)
        transaction_manager.add_transaction(transaction)
        
        print(f"\n✅ Income of {format_currency(amount)} added successfully!")
        input("\nPress Enter to continue...")
        
    except ValueError:
        print("❌ Invalid input! Please try again.")
        input("\nPress Enter to continue...")


def add_expense(transaction_manager, category_manager):
    """
    Add a new expense transaction
    
    STEP 1: Get transaction details from user
    STEP 2: Validate input
    STEP 3: Create transaction object
    STEP 4: Add to transaction manager
    STEP 5: Save to file
    """
    print("\n" + "=" * 60)
    print("💸 ADD EXPENSE".center(60))
    print("=" * 60)
    
    try:
        # Similar to add_income but for expenses
        amount = float(input("\nAmount: $"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        
        categories = category_manager.get_categories('expense')
        print("\nCategories:")
        for idx, cat in enumerate(categories, 1):
            print(f"{idx}. {cat}")
        
        cat_choice = int(input("\nSelect category (number): "))
        if 1 <= cat_choice <= len(categories):
            category = categories[cat_choice - 1]
        else:
            print("❌ Invalid category!")
            return
        
        description = input("Description: ").strip()
        if not description:
            description = f"Expense - {category}"
        
        date_input = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_input:
            date = datetime.strptime(date_input, "%Y-%m-%d").date()
        else:
            date = datetime.now().date()
        
        transaction = Transaction('expense', amount, category, description, date)
        transaction_manager.add_transaction(transaction)
        
        print(f"\n✅ Expense of {format_currency(amount)} added successfully!")
        input("\nPress Enter to continue...")
        
    except ValueError:
        print("❌ Invalid input! Please try again.")
        input("\nPress Enter to continue...")


def view_transactions(transaction_manager):
    """
    Display all transactions
    
    STEP 1: Get all transactions
    STEP 2: Sort by date
    STEP 3: Display in tabular format
    """
    print("\n" + "=" * 80)
    print("📋 ALL TRANSACTIONS".center(80))
    print("=" * 80)
    
    transactions = transaction_manager.get_all_transactions()
    
    if not transactions:
        print("\n📝 No transactions yet. Add your first transaction!")
    else:
        # STEP: Display header
        print(f"\n{'Date':<12} {'Type':<10} {'Amount':<12} {'Category':<15} {'Description':<30}")
        print("-" * 80)
        
        # STEP: Display each transaction
        for trans in sorted(transactions, key=lambda x: x.date, reverse=True):
            type_icon = "💰" if trans.type == 'income' else "💸"
            print(f"{trans.date} {type_icon} {trans.type.capitalize():<8} "
                  f"{format_currency(trans.amount):<12} {trans.category:<15} "
                  f"{trans.description[:30]:<30}")
        
        print("-" * 80)
        print(f"Total transactions: {len(transactions)}")
    
    input("\nPress Enter to continue...")


def view_balance(transaction_manager):
    """
    Calculate and display current balance
    
    STEP 1: Calculate total income
    STEP 2: Calculate total expenses
    STEP 3: Calculate net balance
    STEP 4: Display summary
    """
    print("\n" + "=" * 60)
    print("💵 CURRENT BALANCE".center(60))
    print("=" * 60)
    
    total_income, total_expense = transaction_manager.get_totals()
    balance = total_income - total_expense
    
    print(f"\n{'Total Income:':<20} {format_currency(total_income):>15}")
    print(f"{'Total Expenses:':<20} {format_currency(total_expense):>15}")
    print("-" * 60)
    print(f"{'Net Balance:':<20} {format_currency(balance):>15}")
    
    # Visual indicator
    if balance > 0:
        print("\n✅ You're in the positive! Great job! 🎉")
    elif balance < 0:
        print("\n⚠️ You're spending more than earning! Watch out! 💸")
    else:
        print("\n💼 Breaking even!")
    
    print("=" * 60)
    input("\nPress Enter to continue...")


def monthly_report(transaction_manager):
    """
    Generate monthly financial report
    
    STEP 1: Get month and year from user
    STEP 2: Filter transactions for that month
    STEP 3: Calculate income/expense totals
    STEP 4: Show category breakdown
    STEP 5: Display visual chart
    """
    print("\n" + "=" * 60)
    print("📈 MONTHLY REPORT".center(60))
    print("=" * 60)
    
    try:
        month = int(input("\nMonth (1-12): "))
        year = int(input("Year (e.g., 2026): "))
        
        if not (1 <= month <= 12):
            print("❌ Invalid month!")
            return
        
        report_gen = ReportGenerator(transaction_manager)
        report_gen.generate_monthly_report(month, year)
        
    except ValueError:
        print("❌ Invalid input!")
    
    input("\nPress Enter to continue...")


def main():
    """
    MAIN APPLICATION FLOW:
    =====================
    1. Initialize managers (transaction, category, file handler)
    2. Load existing data from files
    3. Display menu and process user choices
    4. Save data on exit
    
    PROGRAM STRUCTURE:
    - Transaction Manager: Handles all transaction operations
    - Category Manager: Manages income/expense categories
    - File Handler: Handles data persistence
    - Report Generator: Creates financial reports
    """
    # STEP 1: Initialize components
    file_handler = FileHandler()
    category_manager = CategoryManager(file_handler)
    transaction_manager = TransactionManager(file_handler)
    
    # STEP 2: Load existing data
    transaction_manager.load_transactions()
    category_manager.load_categories()
    
    # STEP 3: Main application loop
    while True:
        display_menu()
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            add_income(transaction_manager, category_manager)
        elif choice == "2":
            add_expense(transaction_manager, category_manager)
        elif choice == "3":
            view_transactions(transaction_manager)
        elif choice == "4":
            # Filter transactions (to be implemented)
            print("\n🔍 Filter feature coming soon!")
            input("\nPress Enter to continue...")
        elif choice == "5":
            monthly_report(transaction_manager)
        elif choice == "6":
            # Category summary (to be implemented)
            print("\n📊 Category summary coming soon!")
            input("\nPress Enter to continue...")
        elif choice == "7":
            view_balance(transaction_manager)
        elif choice == "8":
            # Delete transaction (to be implemented)
            print("\n🗑️ Delete feature coming soon!")
            input("\nPress Enter to continue...")
        elif choice == "9":
            # Export to CSV (to be implemented)
            print("\n📁 Export feature coming soon!")
            input("\nPress Enter to continue...")
        elif choice == "10":
            # Manage categories (to be implemented)
            print("\n⚙️ Category management coming soon!")
            input("\nPress Enter to continue...")
        elif choice == "0":
            # STEP 4: Save data before exit
            transaction_manager.save_transactions()
            category_manager.save_categories()
            print("\n👋 Thank you for using Personal Finance Tracker!")
            print("💾 Data saved successfully. Goodbye!\n")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice! Please select a valid option.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    """
    PROGRAM ENTRY POINT
    
    When run directly, this starts the finance tracker application.
    Includes basic error handling for unexpected exits.
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please report this issue.")
        sys.exit(1)
