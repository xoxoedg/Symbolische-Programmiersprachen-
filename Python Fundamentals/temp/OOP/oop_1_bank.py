"""Exercise 1: Bank account class [5 points]

1. Complete Account class with docstrings** [1 point]
    - Properly defined Account class with correct attributes and methods.
    - Every method has a documentation string that describes its functionality.

2. Main application with various accounts** [1 point]
    - Successfully creates multiple account instances.
    - Demonstrates depositing and withdrawing money on those accounts.
    - Changes the account holder of an account using a setter method.

3. Modified withdraw function** [1 point]
    - Ensures that the account balance never drops below -500.
    - If withdrawal would result in a balance less than -500, prints an appropriate error message and does not allow the withdrawal.

4. Implement apply_interest() function** [1 point]
    - Allows account holders to choose between 3 different types of accounts and applies the correct interest rate for each account type.
    - Correctly updates the balance based on the interest rate.
    - Interest rates:
        - Standard Account: 1.2%
        - Gold Account: 1.7%
        - Platinum Account: 2.2%

5. Implement the __str__ magic method** [1 point]
    - Returns a string with the account holder's name.
    - Includes the current balance in the string.
    - States the account type in the string.
"""


class Account:
    """ Here has to be a documentation string that describes
    which data objects this class is designed for.
    You have to remove the pass statement and then write some
    code for the class. """
    pass

if __name__ == "__main__":
    print("Welcome to the Python Bank!")
