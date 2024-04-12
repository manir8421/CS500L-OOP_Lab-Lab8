
from store import Store
from customers import Customer
class StoreApp:
    def __init__(self) -> None:
        self.__store = Store("My Store", "customers.csv")
        self.__store.get_customers_from_db()

    def show_title(self):
        print("The Store Application")

    def show_menu(self):
        print("\n===== MENU ====")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. View All Customers")
        print("4. Delete Customer")
        print("5. Search Customer by Last Name")
        print("6. Display Customer with Highest Account Balance")
        print("7. Display Customer with Lowest Account Balance")
        print("8. Exit")

    def add_customer_flow(self):
        account_number = None
        
        while not account_number:
            account_number_input = input("Enter account number: ").strip()  
            if account_number_input:
                try:
                    account_number_int = int(account_number_input)
                    if not self.__store.check_customer_exists(str(account_number_int)):
                        account_number = str(account_number_int) 
                    else:
                        print("Account number already exists! Please enter a different account number.")
                except ValueError:
                    print("Invalid input! Account number must be an integer. Please try again.")
            else:
                print("Account number cannot be empty! Please enter a valid account number.")
        
        first_name = input("Enter first name: ").title()
        last_name = input("Enter last name: ").title()

        account_balance = None
        while account_balance is None:
            account_balance_input = input("Enter account balance: ")
            try:
                account_balance = float(account_balance_input)
            except ValueError:
                print("Invalid account balance! Please enter a numaric number.")
                account_balance = None
        account_balance = round(account_balance, 2)

        customer = Customer(account_number, last_name, first_name, account_balance)
        self.__store.add_customer(customer)
        print("Customer added successfully.")

    def update_customer_flow(self):
        print("Update Customer Information")
        account_number = input("Enter account number of the customer to update: ")
        existing_customer = self.__store.get_customer_by_account_number(account_number)
        if not existing_customer:
            print("Customer not found.")
            return
        print("Enter new details of the customer:")
        first_name = input(f"First Name [{existing_customer.firstname}]: ").title()
        last_name = input(f"Last Name [{existing_customer.lastname}]: ").title()
        account_balance_input = input(f"Account Balance [{existing_customer.account_balance}]: ")
        account_balance = float(account_balance_input) if account_balance_input else existing_customer.account_balance

        updated_customer = Customer(account_number,last_name,first_name, account_balance)
        self.__store.update_customer(updated_customer)
        print("Customer updated successfully.")



    def view_customers_flow(self):
        print("View Customers")
        print("1. View in forward order")
        print("2. View in backward order")
        choice = input("Choose an option (1 or 2): ")

        customers = self.__store.get_customers()
        
        if not customers:
            print("No customer in the list, empty list.")
            return
        
        if choice == '1':
            for customer in customers:
                print(customer)
        elif choice == '2':
            for customer in reversed(customers):
                print(customer)
        else:
            print("Invalid choice. Returning to main menu.")


    def delete_customer_flow(self):
        print("Delete Customer")
        account_number = input("Enter the account number of the customer you want to delete: ")
        customer_exists = self.__store.check_customer_exists(account_number)
        if customer_exists:
            confirmation = input("Are you sure, you want to delete this customer? (y/n): ").lower()
            if confirmation == 'y':
                self.__store.delete_customer(account_number)
                print("Customer deleted successfully.")
            else:
                print("Operation cancelled.")
        else:
            print("Customer not found.")


    def search_customer_by_lastname_flow(self):
        print("Search Customer by Last Name")
        last_name = input("Enter the last name of the customer you are searching for: ").title()
        matching_customers = self.__store.search_customers_by_lastname(last_name)

        if matching_customers:
            print(f"Found {len(matching_customers)} customer with last name '{last_name}':")
            for customer in matching_customers:
                print(customer)
        else:
            print("No customers found with that last name.")

    
    def display_highest_balance_customer(self):
        customers = self.__store.get_customers()
        if customers:
            highest_balance_customer = max(customers, key=lambda customer: customer.account_balance)
            print("The customer with the highest account balance is:")
            print(highest_balance_customer)
        else:
            print("No customers found.")


    def display_lowest_balance_customer(self):
        customers = self.__store.get_customers()
        if customers:
            lowest_balance_customer = min(customers, key=lambda customer: customer.account_balance)
            print("The customer with the lowest account balance is:")
            print(lowest_balance_customer)
        else:
            print("No customers found.")


    def process_command(self, command) -> bool:
        cont = True
        if command == 1:
            self.add_customer_flow()
        elif command == 2:
            self.update_customer_flow()
        elif command == 3:
            self.view_customers_flow() 
        elif command == 4:
            self.delete_customer_flow()  
        elif command == 5:
            self.search_customer_by_lastname_flow()  
        elif command == 6:
            self.display_highest_balance_customer() 
        elif command == 7:
            self.display_lowest_balance_customer() 
        elif command == 8:
            print("Exiting program...")
            cont = False
        else:
            print("Invalid command! Please try again.")
        return cont

def main():
    app = StoreApp()
    app.show_title()

    cont = True
    while cont:
        app.show_menu()
        try:
            command = int(input("\nEnter your choice: "))
            cont = app.process_command(command)
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()