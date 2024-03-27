from models.user import User
from models.wallet import Wallet

# Create a new user
user = User(
    surname='Doe',
    firstname='John',
    email='john@doe.com',
    password='password123'
)

# Print the user details
print('User surname: ' + user.surname)
print('User firstname: ' + user.firstname)
print('User email: ' + user.email)
print("============================================")
# Check password
print('Password correct: ' + str(user.check_password('password123'))) # True
print('Password incorrect: ' + str(user.check_password('wrongpass'))) # False
print("")
# User should have a wallet
wallet = user.wallet
print('User wallet: ' + str(wallet))

# Check wallet balance
print('Wallet balance: ' + str(wallet[0].get_balance()))

# Deposit into wallet
wallet[0].deposit(100)
print('Wallet balance after deposit: ' + str(wallet[0].get_balance()))

# Withdraw from wallet  
wallet[0].withdraw(50)
print('Wallet balance after withdrawal: ' + str(wallet[0].get_balance()))

print(wallet[0].user.firstname)
print(wallet[0].user.wallet[0].balance)

print("user id", user.id)
print("user id", wallet[0].user_id)

# wallet id
print("wallet id", wallet[0].id)
print("wallet id", user.wallet_id)