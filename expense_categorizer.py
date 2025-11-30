# Expense Categorization Starter Script
# Ronald's AI Finance Assistant (Prototype)

# Sample expense list
expenses = [
    "Bought groceries at supermarket - ₱1500",
    "Grab ride to office - ₱250",
    "Paid electricity bill - ₱2000",
    "Dinner at restaurant - ₱800",
    "Netflix subscription - ₱550"
]

# Define categories with keywords
categories = {
    "Food": ["groceries", "restaurant", "dinner", "lunch", "snacks"],
    "Transport": ["ride", "taxi", "bus", "train", "grab"],
    "Utilities": ["electricity", "water", "internet", "bill"],
    "Entertainment": ["netflix", "movie", "cinema", "game", "concert"],
    "Other": []
}

# Categorize expenses
def categorize_expense(expense):
    expense_lower = expense.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in expense_lower:
                return category
    return "Other"

# Run categorization
for expense in expenses:
    category = categorize_expense(expense)
    print(f"{expense} → {category}")