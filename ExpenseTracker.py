expenseList=[]
print("===============================")
print("Welcome to the Expense Tracker!")
while True:
    print("===============================")
    print("1. Add expenses")
    print("2. View expenses")
    print("3. View total expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        category = input("Enter the category of the expense: ")
        description = input("Enter a description of the expense: ")
        try:
            amount = float(input("Enter the expense amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue
        expense={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        
        expenseList.append(expense)
        print("Expense added successfully!")
    elif choice == '2':
        if(len(expenseList)==0):
            print("No expenses to show.")
        else:
            print("Expenses:")
            for count, expense in enumerate(expenseList, start=1):
                print(f"{count} -> {expense['date']} - {expense['category']} - {expense['description']} - ${expense['amount']:.2f}")
    elif choice == '3':
        total_expenses = sum(expense['amount'] for expense in expenseList)
        print(f"Total expenses: ${total_expenses:.2f}")
    elif choice == '4':
        print("Exiting the Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")