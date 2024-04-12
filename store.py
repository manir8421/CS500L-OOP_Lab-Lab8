
from customers import Customer
from customer_reposatery import CustomerRepository
import csv
class Store:
    def __init__(self, storename: str, filename: str) -> None:
        self.__storename = storename
        self.__filename = filename
        self.__customers: list[Customer] = []
        self.get_customers_from_db()

    def get_store_name(self):
        return self.__storename

    def add_customer(self, customer:Customer):
        if customer not in self.__customers:
            self.__customers.append(customer)
            self.save_customers_to_db()

    def update_customer(self, updated_customer: Customer):
        for i, cust in enumerate(self.__customers):
            if cust.account_no.lower().strip() == updated_customer.account_no.lower().strip():
                cust.lastname = updated_customer.lastname
                cust.firstname = updated_customer.firstname
                cust.account_balance = updated_customer.account_balance
                self.save_customers_to_db()
                break


    def remove_customer(self, account_no):
        self.__customers = [customer for customer in self.__customers if customer.get_account_no() != account_no]
        self.save_customers_to_db()

    def check_customer_exists(self, account_number):
        for customer in self.__customers:
            if customer.get_account_no() == account_number:
                return True
        return False
    
    def delete_customer(self, account_number):
        self.__customers = [customer for customer in self.__customers if customer.get_account_no() != account_number]
        self.save_customers_to_db()

    def search_customers_by_lastname(self, last_name):
        return [customer for customer in self.__customers if customer.lastname.lower() == last_name.lower()]

    def get_customer_by_account_number(self, account_number):
        for customer in self.__customers:
            if customer.get_account_no() == account_number:
                return customer
        return None

    def get_customers_from_db(self):
        repos = CustomerRepository("customers.csv")
        self.__customers = repos.read_customers()

    
    def save_customers_to_db(self):
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file)
            for customer in self.__customers:
                writer.writerow([customer.account_no, customer.lastname, customer.firstname, customer.account_balance])

    def get_customers(self) -> list:
        return self.__customers
    