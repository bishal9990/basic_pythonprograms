balance = 1000.0 #initial balance

print(" Welcome to simple bank ATM")

while True: 
    print("\n Please select an option: ")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input ("Enter your choice (1-4): "))

    if choice == 1:
        print(f"Your current balance is : ${balance: .2f} ")

    elif choice == 2:
              deposit_amount = float(input ("Enter amount to deposit: $"))
              if deposit_amount >0:
               balance += deposit_amount
               print(f"Successfully deposited ${deposit_amount: .2f}. Your new balance is ${balance:.2f}.")
              else: 
                    print(" Deposit amount must be positive: ")

    elif choice == 3: 
              withdrawal_amount = float(input("Enter amount to withdraw:$"))
              
              if withdrawal_amount > balance:
                   print ("Insufficent funds. Please try a smaller amount, ")
                   
              elif withdrawal_amount <= 0:
                   print(" Withdrawal amount must be posutive")

              else:
                   balance -= withdrawal_amount
                   print(f"Successfully withdrew ${withdrawal_amount:.2f}. Your new balance is ${balance:.2f}.")

    elif choice == 4:
           print ("ATM is always open, do utilize it properly Ok, See you again !")
           break  

    else:
           print ("Invalid choice. Please try again. ")            
















