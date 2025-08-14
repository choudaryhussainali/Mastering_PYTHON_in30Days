# Exercise: Simple ATM Simulator #

Write a Python program to simulate a simple ATM system.

## Requirements ##
- Start with a balance of 5000.
- Allow the user to:
    1. Check balance
    2. Deposit money
    3. Withdraw money
    4. Exit
- Use a `while` loop to repeatedly show the menu until the user chooses to exit.
- Prevent withdrawal if the amount is greater than the balance.

### Example Output ###
Welcome to the ATM!
    1. Check Balance
    2. Deposit
    3. Withdraw 
    4. Exit

Enter your choice: 1
Your balance is: 5000
Enter your choice: 3
Enter amount to withdraw: 6000
Insufficient funds!
Enter your choice: 4
Thank you for using our ATM!


**Hint:** Use `if-elif-else` statements for menu handling.