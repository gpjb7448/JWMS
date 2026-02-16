"""
Reports Module - Financial report generation
"""

from collections import defaultdict
import calendar


class ReportGenerator:
    """Generates financial reports and summaries"""
    
    def __init__(self, transaction_manager):
        """Initialize with transaction manager"""
        self.transaction_manager = transaction_manager
    
    def generate_monthly_report(self, month, year):
        """Generate monthly financial report"""
        print("\n" + "=" * 70)
        month_name = calendar.month_name[month]
        print(f"MONTHLY REPORT - {month_name} {year}".center(70))
        print("=" * 70)
        
        # Get transactions for the month
        transactions = self.transaction_manager.get_monthly_transactions(month, year)
        
        if not transactions:
            print("\nNo transactions for this month.")
            return
        
        # Calculate totals
        income_total = sum(t.amount for t in transactions if t.type == 'income')
        expense_total = sum(t.amount for t in transactions if t.type == 'expense')
        balance = income_total - expense_total
        
        # Summary
        print(f"\n{'Total Income:':<20} ${income_total:>12,.2f}")
        print(f"{'Total Expenses:':<20} ${expense_total:>12,.2f}")
        print("-" * 70)
        print(f"{'Net Balance:':<20} ${balance:>12,.2f}")
        print("=" * 70)
        
        # Category breakdown
        print("\nCategory Breakdown:")
        print("-" * 70)
        
        # Income categories
        income_by_cat = defaultdict(float)
        expense_by_cat = defaultdict(float)
        
        for t in transactions:
            if t.type == 'income':
                income_by_cat[t.category] += t.amount
            else:
                expense_by_cat[t.category] += t.amount
        
        if income_by_cat:
            print("\nINCOME:")
            for cat, amount in sorted(income_by_cat.items(), key=lambda x: x[1], reverse=True):
                percentage = (amount / income_total * 100) if income_total > 0 else 0
                print(f"  {cat:<18} ${amount:>10,.2f}  ({percentage:5.1f}%)")
        
        if expense_by_cat:
            print("\nEXPENSES:")
            for cat, amount in sorted(expense_by_cat.items(), key=lambda x: x[1], reverse=True):
                percentage = (amount / expense_total * 100) if expense_total > 0 else 0
                print(f"  {cat:<18} ${amount:>10,.2f}  ({percentage:5.1f}%)")
        
        print("=" * 70)
