"""
Transaction Module - Transaction class and manager

STEP-BY-STEP GUIDE:
===================
1. Define Transaction class to represent a single transaction
2. Create TransactionManager to handle multiple transactions
3. Implement add, delete, filter operations
4. Integrate with file handler for persistence

LEARNING OBJECTIVES:
- Class design and OOP
- Data validation
- Collection management
- Date/time operations
"""

from datetime import datetime
import uuid


class Transaction:
    """
    Represents a single financial transaction
    
    ATTRIBUTES:
    - id: Unique identifier
    - type: 'income' or 'expense'
    - amount: Transaction amount (positive float)
    - category: Transaction category
    - description: Transaction description
    - date: Transaction date
    """
    
    def __init__(self, trans_type, amount, category, description, date=None):
        """
        Initialize a new transaction
        
        STEP 1: Validate inputs
        STEP 2: Generate unique ID
        STEP 3: Set transaction date
        STEP 4: Store transaction data
        
        Args:
            trans_type (str): 'income' or 'expense'
            amount (float): Transaction amount
            category (str): Category name
            description (str): Transaction description
            date (datetime.date): Transaction date (default: today)
        """
        # STEP 1: Validate transaction type
        if trans_type not in ['income', 'expense']:
            raise ValueError("Transaction type must be 'income' or 'expense'")
        
        # STEP 2: Validate amount
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # STEP 3: Generate unique ID
        self.id = str(uuid.uuid4())
        
        # STEP 4: Set transaction data
        self.type = trans_type
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().date()
    
    def to_dict(self):
        """
        Convert transaction to dictionary
        
        Returns:
            dict: Transaction data as dictionary
        """
        return {
            'id': self.id,
            'type': self.type,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': str(self.date)
        }
    
    def to_file_format(self):
        """
        Convert transaction to file storage format
        
        FORMAT: date|type|amount|category|description|id
        
        Returns:
            str: Pipe-delimited string
        """
        return f"{self.date}|{self.type}|{self.amount:.2f}|{self.category}|{self.description}|{self.id}"
    
    @classmethod
    def from_file_format(cls, line):
        """
        Create transaction from file format string
        
        STEP 1: Split line by delimiter
        STEP 2: Extract fields
        STEP 3: Create transaction object
        STEP 4: Restore ID
        
        Args:
            line (str): Pipe-delimited line from file
            
        Returns:
            Transaction: New transaction object
        """
        # STEP 1: Split and validate
        parts = line.strip().split('|')
        if len(parts) < 5:
            raise ValueError(f"Invalid transaction format: {line}")
        
        # STEP 2: Extract fields
        date_str, trans_type, amount_str, category, description = parts[:5]
        trans_id = parts[5] if len(parts) > 5 else None
        
        # STEP 3: Parse date
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        # STEP 4: Create transaction
        transaction = cls(trans_type, float(amount_str), category, description, date)
        
        # STEP 5: Restore ID if present
        if trans_id:
            transaction.id = trans_id
        
        return transaction
    
    def __str__(self):
        """String representation of transaction"""
        return f"{self.date} - {self.type.capitalize()}: ${self.amount:.2f} ({self.category}) - {self.description}"
    
    def __repr__(self):
        """Developer representation"""
        return f"Transaction(type='{self.type}', amount={self.amount}, category='{self.category}', date='{self.date}')"


class TransactionManager:
    """
    Manages all transactions in the application
    
    RESPONSIBILITIES:
    - Store transactions in memory
    - Add/delete transactions
    - Filter and search transactions
    - Calculate totals and balances
    - Integrate with file handler for persistence
    """
    
    def __init__(self, file_handler):
        """
        Initialize transaction manager
        
        Args:
            file_handler: FileHandler instance for data persistence
        """
        self.transactions = []
        self.file_handler = file_handler
    
    def add_transaction(self, transaction):
        """
        Add a new transaction
        
        STEP 1: Validate transaction
        STEP 2: Add to list
        STEP 3: Save to file
        
        Args:
            transaction (Transaction): Transaction to add
        """
        # STEP 1: Validate
        if not isinstance(transaction, Transaction):
            raise TypeError("Must be a Transaction object")
        
        # STEP 2: Add to list
        self.transactions.append(transaction)
        
        # STEP 3: Save immediately
        self.save_transactions()
    
    def delete_transaction(self, transaction_id):
        """
        Delete a transaction by ID
        
        STEP 1: Find transaction
        STEP 2: Remove from list
        STEP 3: Save changes
        
        Args:
            transaction_id (str): ID of transaction to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        # STEP 1: Find transaction
        for i, trans in enumerate(self.transactions):
            if trans.id == transaction_id:
                # STEP 2: Remove
                self.transactions.pop(i)
                # STEP 3: Save
                self.save_transactions()
                return True
        
        return False
    
    def get_all_transactions(self):
        """
        Get all transactions
        
        Returns:
            list: List of all transactions
        """
        return self.transactions.copy()
    
    def get_transactions_by_type(self, trans_type):
        """
        Filter transactions by type
        
        Args:
            trans_type (str): 'income' or 'expense'
            
        Returns:
            list: Filtered transactions
        """
        return [t for t in self.transactions if t.type == trans_type]
    
    def get_transactions_by_date_range(self, start_date, end_date):
        """
        Filter transactions by date range
        
        Args:
            start_date (datetime.date): Start date (inclusive)
            end_date (datetime.date): End date (inclusive)
            
        Returns:
            list: Transactions within date range
        """
        return [t for t in self.transactions 
                if start_date <= t.date <= end_date]
    
    def get_transactions_by_category(self, category):
        """
        Filter transactions by category
        
        Args:
            category (str): Category name
            
        Returns:
            list: Transactions in category
        """
        return [t for t in self.transactions if t.category == category]
    
    def get_totals(self):
        """
        Calculate total income and expenses
        
        STEP 1: Sum all income transactions
        STEP 2: Sum all expense transactions
        STEP 3: Return both totals
        
        Returns:
            tuple: (total_income, total_expense)
        """
        income_total = sum(t.amount for t in self.transactions if t.type == 'income')
        expense_total = sum(t.amount for t in self.transactions if t.type == 'expense')
        
        return income_total, expense_total
    
    def get_balance(self):
        """
        Calculate current balance
        
        Returns:
            float: Balance (income - expenses)
        """
        income, expense = self.get_totals()
        return income - expense
    
    def save_transactions(self):
        """
        Save all transactions to JSON file
        
        STEP 1: Pass transaction list to file handler
        STEP 2: File handler converts to JSON format
        """
        self.file_handler.save_transactions(self.transactions)
    
    def load_transactions(self):
        """
        Load transactions from JSON file
        
        STEP 1: Load transaction dictionaries from file
        STEP 2: Convert each dictionary to Transaction object
        STEP 3: Add to transactions list
        """
        transaction_dicts = self.file_handler.load_transactions()
        self.transactions = []
        
        for trans_dict in transaction_dicts:
            try:
                # Create transaction from dictionary
                date = datetime.strptime(trans_dict['date'], "%Y-%m-%d").date()
                transaction = Transaction(
                    trans_dict['type'],
                    trans_dict['amount'],
                    trans_dict['category'],
                    trans_dict['description'],
                    date
                )
                # Restore the original ID
                transaction.id = trans_dict['id']
                self.transactions.append(transaction)
            except (ValueError, KeyError) as e:
                print(f"Warning: Skipping invalid transaction: {trans_dict}")
                print(f"Error: {e}")
    
    def get_monthly_transactions(self, month, year):
        """
        Get all transactions for a specific month
        
        Args:
            month (int): Month (1-12)
            year (int): Year
            
        Returns:
            list: Transactions for that month
        """
        return [t for t in self.transactions 
                if t.date.month == month and t.date.year == year]
    
    def get_category_totals(self, trans_type=None):
        """
        Get totals grouped by category
        
        Args:
            trans_type (str): Filter by type ('income'/'expense'), or None for all
            
        Returns:
            dict: {category: total_amount}
        """
        category_totals = {}
        
        transactions = self.transactions if trans_type is None else self.get_transactions_by_type(trans_type)
        
        for trans in transactions:
            if trans.category in category_totals:
                category_totals[trans.category] += trans.amount
            else:
                category_totals[trans.category] = trans.amount
        
        return category_totals
