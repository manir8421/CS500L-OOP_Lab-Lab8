
class Customer:
    def __init__(self, account_no: str, lastname: str, firstname: str, account_balance: float) -> None:
        self.__account_no = account_no
        self.__lastname = lastname
        self.__firstname = firstname
        self.__account_balance = account_balance

    @property
    def account_no(self):
        return self.__account_no
    
    @account_no.setter
    def account_no(self, new_account_no):
            self.__account_no = new_account_no

    def get_account_no(self):
        return self.__account_no
    
    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, new_lastname):
        self.__lastname = new_lastname

    @property
    def firstname(self):
        return self.__firstname
    
    @firstname.setter
    def firstname(self, new_firstname):
        self.__firstname = new_firstname

    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, new_amount: float):
        self.__account_balance = new_amount

    def __str__(self) -> str:
        return f"Account No= {self.__account_no}, Last Name= {self.__lastname}, First Name= {self.__firstname}, Account Balance= {self.__account_balance}"

    def __repr__(self) -> str:
        return f"Customer(Account No= {self.__account_no}, Last Name= {self.__lastname}, First Name= {self.__firstname}, Account Balance= {self.__account_balance})"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Customer):
            return NotImplemented
        return self.__account_no == __value.__account_no
    
    def convert_to_list(self) -> list[str]:
        lst = []
        lst.append(self.__account_no)
        lst.append(self.__lastname)
        lst.append(self.__firstname)
        lst.append(self.__account_balance)
        return lst

    


