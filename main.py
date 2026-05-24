# Expense Tracker Project

expenses = [] #list of expenses in form of Dictionary
print("Welcome to the Expense Tracker: Khrcha kaam Kiya karo")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View ALL Expenses")
    print("3. View Total khrcha")
    print("4. Exit")

    choice = int(input("Please Enter your choice: "))

# Add Expense
    if choice == 1:
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Transport): ")
        description = input("Enter a brief description: ")
        amount = float(input("Enter the amount: "))
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        print("\nDone. Expense Added Successfully!")

    # 2 View ALL Expenses
    elif choice == 2:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("==== All Expenses ===")
            count = 1
            for expense in expenses:
                print(f"{count}. Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: {expense['amount']}")
                count += 1

    # 3 View Total spending
    elif choice == 3:
        total_expense = sum(expense['amount'] for expense in expenses)
        print(f"Total Expense so far is: {total_expense}")

    # 4 Exit
    elif (choice == 4):
        print("Exiting the Expense Tracker. Fir Milte!")
        break

    else:
        print("Invalid choice. Please try again.")  
    

    
