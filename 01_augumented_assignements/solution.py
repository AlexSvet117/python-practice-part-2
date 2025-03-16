# do not change the method name
def main():
    balance = 5000
    print("================== BALANCE ====================", end="\n\n")
    print("")
    print(f"Current Balance: ${balance:.1f}")
    # write your code here with 4 space intentation
    deposit = input("How much do you want to deposit: $")
    deposit_int = float(deposit)
    balance += deposit_int
    print(f"Balance Successfully Updated: ${balance}")
    user_withdrowal = input("How much do you want to withdraw: $")
    print("There is a 3% transaction fee on the withdrawal.")
    user_withdrowal_int = float(user_withdrowal)
    withdrowal_fee = (user_withdrowal_int * 0.03)
    print(f"Withdrawal: ${user_withdrowal_int} - Fee: ${withdrowal_fee}")
    balance -= user_withdrowal_int + withdrowal_fee
    print(f"Balance Successfully Updated: ${balance}")
    print("")
    print("============ TRANSACTION COMPLETED ============")

# do not change the following lines:    
if __name__ == "__main__":
    main()