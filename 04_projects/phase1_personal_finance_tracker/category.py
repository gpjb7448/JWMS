"""
Category Module - Category management

LEARNING OBJECTIVES:
- Managing predefined categories
- File I/O for category data
- Data validation
"""


class CategoryManager:
    """
    Manages income and expense categories
    
    DEFAULT CATEGORIES:
    - Income: Salary, Business, Freelance, Investment, Other
    - Expense: Food, Transport, Bills, Entertainment, Shopping, Healthcare, Education, Other
    """
    
    def __init__(self, file_handler):
        """Initialize category manager with default categories"""
        self.file_handler = file_handler
        self.categories = {
            'income': ['Salary', 'Business', 'Freelance', 'Investment', 'Gift', 'Other'],
            'expense': ['Food', 'Transport', 'Bills', 'Entertainment', 'Shopping', 
                       'Healthcare', 'Education', 'Housing', 'Personal', 'Other']
        }
    
    def get_categories(self, category_type):
        """Get list of categories for a type"""
        return self.categories.get(category_type, [])
    
    def add_category(self, category_type, category_name):
        """Add a new category"""
        if category_type in self.categories:
            if category_name not in self.categories[category_type]:
                self.categories[category_type].append(category_name)
                self.save_categories()
                return True
        return False
    
    def save_categories(self):
        """Save categories to JSON file"""
        self.file_handler.save_categories(self.categories)
    
    def load_categories(self):
        """Load categories from JSON file"""
        loaded_categories = self.file_handler.load_categories()
        if loaded_categories:
            self.categories = loaded_categories
