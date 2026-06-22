import psycopg2

# DB Connection
conn = psycopg2.connect(
    dbname="ATM_code",
    user="postgres",
    password="Adithya13",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Fetch users
cur.execute("SELECT * FROM users_details")
results = cur.fetchall()

# Login
user_name = input("Enter Username: ")
pin_no = input("Enter Your PIN: ")

user_found = False

for value in results:

    if user_name == value[1] and pin_no == str(value[2]):

        user_found = True
        amount = float(value[3])

        while True:

            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Withdrawal")
            print("3. Deposit")
            print("4. Exit")

            option = input("Enter your option (1-4): ")

            if option == "1":
                print(f"\nCurrent Balance: ₹{amount}")

            elif option == "2":

                withdraw = float(input("Enter Withdraw Amount: "))

                if withdraw > amount:
                    print("Insufficient Balance")
                else:
                    amount -= withdraw

                    cur.execute(
                        "UPDATE users_details SET balance = %s WHERE users_name = %s",
                        (amount, user_name)
                    )
                    conn.commit()

                    print("Withdrawal Successful")
                    print(f"Remaining Balance: ₹{amount}")

            elif option == "3":

                deposit = float(input("Enter Deposit Amount: "))

                amount += deposit

                cur.execute(
                    "UPDATE users_details SET account_balance  = %s WHERE users_name = %s",
                    (amount, user_name)
                )
                conn.commit()

                print("Deposit Successful")
                print(f"Updated Balance: ₹{amount}")

            elif option == "4":
                print("Thank you for using ATM")
                break

            else:
                print("Invalid Option. Choose 1-4")

        break

if not user_found:
    print("Invalid Username or PIN")

# Fetch latest data from DB
cur.execute("SELECT * FROM users_details")
updated_results = cur.fetchall()

print("\n--- Updated Users Table ---")
for row in updated_results:
    print(row)

cur.close()
conn.close()

# =========================================================================

# DataBase
# DROP TABLE users_details;
# CREATE TABLE users_details (
# 	id INT PRIMARY KEY,
# 	users_name varchar(100),
# 	pin_number varchar(20),
# 	account_balance decimal(10,2));
# SELECT * FROM users_details;
# INSERT INTO users_details values
# (1, 'Adithya','Adithya@1013', 50000),
# (2, 'Kumar', 'Kumar@111', 45000),
# (3, 'Priya', 'Priya@001', 62000),
# (4, 'Soundarya', 'Sound1019', 35000),
# (5, 'Ajitha', 'Ajitha1010', 55000),
# (6, 'Karthik', 'Karthi123', 48000);
# SELECT * FROM users_details;

