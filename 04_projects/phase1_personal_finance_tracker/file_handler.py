"""
File Handler Module - Data persistence operations
"""

import os


class FileHandler:
    """
    Handles file I/O for data persistence
    
    FILES:
    - data/transactions.txt: Transaction data
    - data/categories.txt: Category data
    """
    
    def __init__(self, data_dir='data'):
        """Initialize file handler and create data directory"""
        self.data_dir = data_dir
        self.transactions_file = os.path.join(data_dir, 'transactions.txt')
        self.categories_file = os.path.join(data_dir, 'categories.txt')
        
        # Create data directory if it doesn't exist
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def save_transactions(self, lines):
        """Save transaction lines to file"""
        try:
            with open(self.transactions_file, 'w', encoding='utf-8') as f:
                for line in lines:
                    f.write(line + '\n')
        except IOError as e:
            print(f"Error saving transactions: {e}")
    
    def load_transactions(self):
        """Load transaction lines from file"""
        if not os.path.exists(self.transactions_file):
            return []
        
        try:
            with open(self.transactions_file, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip()]
        except IOError as e:
            print(f"Error loading transactions: {e}")
            return []
    
    def save_categories(self, lines):
        """Save category lines to file"""
        try:
            with open(self.categories_file, 'w', encoding='utf-8') as f:
                for line in lines:
                    f.write(line + '\n')
        except IOError as e:
            print(f"Error saving categories: {e}")
    
    def load_categories(self):
        """Load category lines from file"""
        if not os.path.exists(self.categories_file):
            return []
        
        try:
            with open(self.categories_file, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip()]
        except IOError as e:
            print(f"Error loading categories: {e}")
            return []
