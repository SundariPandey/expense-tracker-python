#Expense Tracker Project

expensesList = [] #list of expenses in form of dictionary
print("WELCOME TO YOUR SMART EXPENSE MANAGER Save And Invest Every Penny")

while True:
   print("\n--- 💰 Personal Expense Tracker 💰 ---")
   print("1. Add New Expense")
   print("2. View All Expenses")
   print("3. View Total Expenses")
   print("4. Category Wise Expense")
   print("5. Delete Expense")
   print("6. Exit")

   choice= int(input("Please Enter your choice: "))

#1.Add new expenses
   if(choice == 1):
      date = input("On which date did you spend it?Please Enter your date: ")
      category = input("Enter the Category(food,Travel,Makeup,Books): ")
      description = input("Any Other Detail: ")
      amount = float(input("Enter the amount: "))

      expense = {
      "date": date,
      "category": category,
      "description": description,
      "amount": amount
       }

      expensesList.append(expense)
      print("\n Done! Expense added successfully")

# 2.View all expenses
   elif(choice == 2):
    if(len(expensesList) == 0):
      print("No expenses Added.Go spend first")
    else:
      print("=====This is all your expense=====")
      count = 1
      for eachkharcha in expensesList:
        print(f"Expense Number {count} ->{eachkharcha["date"]},{eachkharcha["category"]}, {eachkharcha["description"]},{eachkharcha["amount"]}  ")
        count =  count + 1

#3.View total expenses
   elif(choice == 3):
      total = 0
      for eachkharcha in expensesList:
        total = total + eachkharcha["amount"]

      print("\n TOTAL KHARCHA ₹= ",total)


# 4. Category Wise Expense

   elif(choice == 4):
      categoryList = {}

      for eachkharcha in expensesList:

            category = eachkharcha["category"]
            amount = eachkharcha["amount"]

            if category in categoryList:
                categoryList[category] = categoryList[category] + amount
            else:
                categoryList[category] = amount

      print("\nCategory Wise Expense:")
      for category in categoryList:
       print(category, "=", categoryList[category])

#5. Delete Expenses
   elif choice == 5:

        deltExpense = int(input("Enter expense number to delete: "))

        if deltExpense <= len(expensesList):

            expensesList.pop(deltExpense - 1)

            print("Expense deleted successfully")

        else:
            print("Invalid expense number")

#Exit
   elif(choice == 6):
     print("Thank you for using the system")
     break
   else:
     print("INVALID CHOICE. TRY AGAIN")

      

    




    
