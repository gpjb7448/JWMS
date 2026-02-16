# Phase 1 Project: Personal Finance Tracker

## 📋 Project Overview

A command-line personal finance management application that helps users track income, expenses, and manage their budget.

## 🎯 Learning Objectives

**Concepts Covered:**
- Functions and modular programming
- File I/O (reading/writing text files)
- Data structures (lists, dictionaries)
- User input validation
- Basic error handling
- Date/time operations
- Data persistence
- Report generation

## 📁 Project Structure

```
phase1_personal_finance_tracker/
├── README.md                 # This file
├── main.py                   # Main application entry point
├── transaction.py            # Transaction class and operations
├── category.py               # Category management
├── reports.py                # Report generation functions
├── file_handler.py           # File I/O operations
├── utils.py                  # Utility functions
├── data/                     # Data storage directory
│   ├── transactions.txt      # Transaction data
│   └── categories.txt        # Category data
└── requirements.txt          # Dependencies (none for this project)
```

## ✨ Features

### Core Features
- ✅ Add income transactions
- ✅ Add expense transactions
- ✅ View all transactions
- ✅ Filter transactions by date range
- ✅ Filter transactions by category
- ✅ Calculate balance (income - expenses)
- ✅ Categorize transactions
- ✅ Generate monthly/yearly reports
- ✅ Export data to CSV
- ✅ Data persistence (file-based)

### Categories
- Income: Salary, Business, Freelance, Investment, Other
- Expenses: Food, Transport, Bills, Entertainment, Shopping, Healthcare, Education, Other

## 🚀 How to Run

```bash
# Navigate to project directory
cd phase1_personal_finance_tracker

# Run the application
python main.py
```

## 📝 Usage Examples

### Adding Income
```
Select option: 1
Amount: 5000
Category: Salary
Description: Monthly salary
Date (YYYY-MM-DD) or press Enter for today: 2026-02-01
```

### Adding Expense
```
Select option: 2
Amount: 150
Category: Food
Description: Groceries
Date (YYYY-MM-DD) or press Enter for today: 
```

### Viewing Transactions
```
Select option: 3
```

### Generating Monthly Report
```
Select option: 5
Month (1-12): 2
Year: 2026
```

## 💾 Data Storage

**All data is stored in JSON format** for better structure and easier manipulation:

**transactions.json structure:**
```json
{
  "transactions": [
    {
      "id": "unique_id",
      "date": "2026-02-01",
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
```

**categories.json structure:**
```json
{
  "income": ["Salary", "Business", "Freelance", "Investment", "Gift", "Other"],
  "expense": ["Food", "Transport", "Bills", "Entertainment", "Shopping", 
              "Healthcare", "Education", "Housing", "Personal", "Other"],
  "metadata": {
    "last_updated": "2026-02-16T19:00:00"
  }
}
```

**Features:**
- ✅ Structured JSON format
- ✅ Automatic backups (keeps last 5 versions)
- ✅ Metadata tracking (last updated, transaction count)
- ✅ Easy to read and edit
- ✅ CSV export capability

## 🎓 Step-by-Step Implementation Guide

### Step 1: Project Setup
1. Create project directory structure
2. Create empty data files
3. Set up main.py with menu

### Step 2: Transaction Class
1. Design Transaction data structure
2. Implement validation
3. Add string representation

### Step 3: File Operations
1. Implement save_transaction()
2. Implement load_transactions()
3. Handle file errors

### Step 4: Core Features
1. Add transaction (income/expense)
2. View transactions
3. Calculate balance
4. Delete transaction

### Step 5: Filtering & Search
1. Filter by date range
2. Filter by category
3. Search by description

### Step 6: Reporting
1. Monthly summary
2. Category breakdown
3. Income vs Expense chart (text-based)

### Step 7: Polish
1. Input validation
2. Error handling
3. User-friendly messages
4. Data backup

## 🔧 Technical Details

### Transaction Data Structure
```python
{
    'id': 'unique_id',
    'date': '2026-02-01',
    'type': 'income' or 'expense',
    'amount': 5000.00,
    'category': 'Salary',
    'description': 'Monthly salary'
}
```

### File Format
- Delimiter: Pipe (|)
- Encoding: UTF-8
- Line ending: \n

## 📊 Sample Reports

### Monthly Summary
```
==========================================
     MONTHLY REPORT - February 2026
==========================================
Total Income  : $5,000.00
Total Expenses: $1,250.00
Net Balance   : $3,750.00
==========================================

Category Breakdown:
------------------------------------------
INCOME:
  Salary          : $5,000.00 (100%)
------------------------------------------
EXPENSES:
  Food            : $450.00 (36%)
  Transport       : $300.00 (24%)
  Bills           : $500.00 (40%)
==========================================
```

## 🧪 Testing Checklist

- [ ] Add income transaction
- [ ] Add expense transaction
- [ ] View all transactions
- [ ] Calculate correct balance
- [ ] Filter by date range
- [ ] Filter by category
- [ ] Generate monthly report
- [ ] Handle invalid input
- [ ] Handle file errors
- [ ] Data persists after restart

## 🚧 Future Enhancements

**Phase 1.1:**
- Budget setting and tracking
- Recurring transactions
- Multiple accounts

**Phase 1.2:**
- Graphical charts (matplotlib)
- Database storage (SQLite)
- Export to Excel

**Phase 1.3:**
- GUI version (Tkinter)
- Web interface (Flask)
- Mobile app integration

## 📚 Concepts Learned

After completing this project, you will understand:
- How to structure a Python project
- File-based data persistence
- Working with dates and times
- Data validation and error handling
- Report generation
- Modular code organization
- User interface design (CLI)

## 💡 Tips

1. **Start Simple**: Get basic add/view working first
2. **Test Frequently**: Test after each feature
3. **Handle Errors**: Validate all user input
4. **Use Functions**: Break code into small functions
5. **Document**: Add docstrings to all functions
6. **Backup Data**: Don't lose transaction data!

## 🎯 Success Criteria

You've successfully completed this project when you can:
- Track income and expenses
- View transaction history
- Generate accurate reports
- Handle errors gracefully
- Persist data between sessions
- Filter and search transactions

---

**Happy Coding! 💰✨**
