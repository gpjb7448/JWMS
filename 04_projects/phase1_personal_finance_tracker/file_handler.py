"""
File Handler Module - JSON-based Data Persistence

LEARNING OBJECTIVES:
- Working with JSON files
- Data serialization and deserialization
- Structured data storage
- Error handling with files

This module uses JSON format for data storage, which provides:
- Better data structure
- Easy data manipulation
- Human-readable format
- Standard format for data exchange
"""

import os
import json
from datetime import datetime


class FileHandler:
    """
    Handles file I/O for data persistence using JSON format
    
    FILES:
    - data/transactions.json: Transaction data in JSON format
    - data/categories.json: Category data in JSON format
    - data/backup/: Backup directory for data files
    
    JSON STRUCTURE:
    
    transactions.json:
    {
        "transactions": [
            {
                "id": "unique_id",
                "date": "2026-02-16",
                "type": "income",
                "amount": 5000.00,
                "category": "Salary",
                "description": "Monthly salary"
            }
        ],
        "metadata": {
            "last_updated": "2026-02-16T19:00:00",
            "total_transactions": 1
        }
    }
    
    categories.json:
    {
        "income": ["Salary", "Business", "Freelance", "Investment", "Gift", "Other"],
        "expense": ["Food", "Transport", "Bills", "Entertainment", "Shopping", 
                    "Healthcare", "Education", "Housing", "Personal", "Other"],
        "metadata": {
            "last_updated": "2026-02-16T19:00:00"
        }
    }
    """
    
    def __init__(self, data_dir='data'):
        """
        Initialize file handler and create data directory
        
        STEP 1: Set up file paths
        STEP 2: Create data directory if needed
        STEP 3: Create backup directory
        STEP 4: Initialize empty JSON files if they don't exist
        """
        # STEP 1: Set up file paths
        self.data_dir = data_dir
        self.transactions_file = os.path.join(data_dir, 'transactions.json')
        self.categories_file = os.path.join(data_dir, 'categories.json')
        self.backup_dir = os.path.join(data_dir, 'backup')
        
        # STEP 2: Create data directory if it doesn't exist
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        # STEP 3: Create backup directory
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
        
        # STEP 4: Initialize empty JSON files if they don't exist
        self._initialize_files()
    
    def _initialize_files(self):
        """Initialize empty JSON files if they don't exist"""
        # Initialize transactions file
        if not os.path.exists(self.transactions_file):
            self._save_json(self.transactions_file, {
                "transactions": [],
                "metadata": {
                    "last_updated": datetime.now().isoformat(),
                    "total_transactions": 0
                }
            })
        
        # Initialize categories file
        if not os.path.exists(self.categories_file):
            self._save_json(self.categories_file, {
                "income": ["Salary", "Business", "Freelance", "Investment", "Gift", "Other"],
                "expense": ["Food", "Transport", "Bills", "Entertainment", "Shopping", 
                           "Healthcare", "Education", "Housing", "Personal", "Other"],
                "metadata": {
                    "last_updated": datetime.now().isoformat()
                }
            })
    
    def _save_json(self, filepath, data):
        """
        Save data to JSON file with pretty formatting
        
        Args:
            filepath: Path to JSON file
            data: Data to save (dict or list)
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving JSON file {filepath}: {e}")
        except json.JSONEncodeError as e:
            print(f"Error encoding JSON data: {e}")
    
    def _load_json(self, filepath):
        """
        Load data from JSON file
        
        Args:
            filepath: Path to JSON file
            
        Returns:
            dict or list: Loaded data, or None if error
        """
        if not os.path.exists(filepath):
            return None
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except IOError as e:
            print(f"Error loading JSON file {filepath}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {filepath}: {e}")
            return None
    
    def save_transactions(self, transactions_list):
        """
        Save transactions to JSON file
        
        STEP 1: Convert transaction objects to dictionaries
        STEP 2: Create JSON structure with metadata
        STEP 3: Backup existing file
        STEP 4: Save new data
        
        Args:
            transactions_list: List of Transaction objects
        """
        # STEP 1: Convert to dictionaries
        transactions_data = [t.to_dict() for t in transactions_list]
        
        # STEP 2: Create JSON structure
        data = {
            "transactions": transactions_data,
            "metadata": {
                "last_updated": datetime.now().isoformat(),
                "total_transactions": len(transactions_data)
            }
        }
        
        # STEP 3: Backup existing file
        self._backup_file(self.transactions_file)
        
        # STEP 4: Save
        self._save_json(self.transactions_file, data)
    
    def load_transactions(self):
        """
        Load transactions from JSON file
        
        Returns:
            list: List of transaction dictionaries
        """
        data = self._load_json(self.transactions_file)
        
        if data is None:
            return []
        
        return data.get('transactions', [])
    
    def save_categories(self, categories_dict):
        """
        Save categories to JSON file
        
        Args:
            categories_dict: Dictionary with 'income' and 'expense' keys
        """
        # Add metadata
        data = categories_dict.copy()
        data['metadata'] = {
            "last_updated": datetime.now().isoformat()
        }
        
        # Backup existing file
        self._backup_file(self.categories_file)
        
        # Save
        self._save_json(self.categories_file, data)
    
    def load_categories(self):
        """
        Load categories from JSON file
        
        Returns:
            dict: Categories dictionary
        """
        data = self._load_json(self.categories_file)
        
        if data is None:
            return {}
        
        # Remove metadata before returning
        categories = {k: v for k, v in data.items() if k != 'metadata'}
        return categories
    
    def _backup_file(self, filepath):
        """
        Create a backup of the file with timestamp
        
        Args:
            filepath: Path to file to backup
        """
        if not os.path.exists(filepath):
            return
        
        try:
            # Create backup filename with timestamp
            filename = os.path.basename(filepath)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"{filename}.{timestamp}.backup"
            backup_path = os.path.join(self.backup_dir, backup_filename)
            
            # Copy file
            with open(filepath, 'r', encoding='utf-8') as source:
                with open(backup_path, 'w', encoding='utf-8') as backup:
                    backup.write(source.read())
            
            # Keep only last 5 backups
            self._cleanup_old_backups(filename)
            
        except Exception as e:
            print(f"Warning: Could not create backup: {e}")
    
    def _cleanup_old_backups(self, filename, keep_count=5):
        """
        Keep only the most recent backups
        
        Args:
            filename: Base filename to clean up
            keep_count: Number of backups to keep
        """
        try:
            # Get all backup files for this filename
            backups = [f for f in os.listdir(self.backup_dir) 
                      if f.startswith(filename)]
            
            # Sort by modification time
            backups.sort(key=lambda x: os.path.getmtime(
                os.path.join(self.backup_dir, x)), reverse=True)
            
            # Delete old backups
            for old_backup in backups[keep_count:]:
                os.remove(os.path.join(self.backup_dir, old_backup))
                
        except Exception as e:
            print(f"Warning: Could not cleanup old backups: {e}")
    
    def export_to_csv(self, transactions_list, filename):
        """
        Export transactions to CSV file
        
        Args:
            transactions_list: List of Transaction objects
            filename: CSV filename to create
        """
        import csv
        
        try:
            csv_path = os.path.join(self.data_dir, filename)
            
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow(['Date', 'Type', 'Amount', 'Category', 'Description'])
                
                # Write transactions
                for trans in transactions_list:
                    writer.writerow([
                        trans.date,
                        trans.type,
                        trans.amount,
                        trans.category,
                        trans.description
                    ])
            
            print(f"✅ Exported to {csv_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error exporting to CSV: {e}")
            return False
