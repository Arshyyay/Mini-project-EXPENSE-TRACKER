kharche = []

while True:
    print("\n Wellcome to our app. here we help people to track thier expenses!!! \n`")
    print("\n======== MENU ========")
    print("1. Add your expense")
    print("2. Check your expenses")
    print("3. The total spendings")
    print("4. Exit")

    choice = int(input("\nChoose an option: "))

    if choice == 1:
        date = input("Enter the date of expense: ")
        x = int(input("Enter the category of spendings:\n1.Food\n2.Sports\n3.Personal\n4.Other\n"))

        if x == 1:
            category = "Food"
        elif x == 2:
            category = "Sports"
        elif x == 3:
            category = "Personal"
        elif x==4:
            category =input("What was the category other than all this?")
        else:
            print("Pakka sutta fuke ho na?")

        details = input("Give us some details about the product: ")
        amount = float(input("Enter the amount of the product: "))

        expense = {
            "date": date,
            "category": category,
            "details": details,
            "amount": amount
        }

        kharche.append(expense)
        print("\n Expense added successfully!")

    elif choice == 2:
        if len(kharche)==0:
            print("No expenses found.add some expenses dawg!!")
        else:
            for eachkharcha in kharche:
                num=1
                print(f"Here is the details of your expenses: \n Expense number {num}-->{eachkharcha["date"]}-->{eachkharcha["category"]}-->{eachkharcha["details"]}-->{eachkharcha["amount"]}$")
            num+=1
    elif choice==3:
        total=0
        for eachkharcha in kharche:
            total=total+eachkharcha["amount"]
            print(f"The total amount which you've spent by far is {total}")
            
    else:
        print("Thankyou for using this system!! Love you ambani ke aulaad 😂😂")
        break
        print("Choose the valid option idiot!!!")    
            