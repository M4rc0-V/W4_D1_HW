from datetime import datetime as dt

class User():
    def __init__(self, first_name, last_name, email, created_on):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.created_on = dt.utcnow()

    def change_first_name(self, new_name):
        self.first_name = new_name
    def change_last_name(self, new_name):
        self.last_name = new_name









class Employee(User):
    def __init__(self, first_name, last_name, email, created_on, home_address, security_level, department, employee_id):
        super().__init__(self, first_name, last_name, email, created_on)
        self.home_address = home_address
        self.security_level = security_level
        self.department = department
        self.employee_id = employee_id

    def change_department(self, new_department):
        self.departemnt = new_department








class Customer(User):
    def __init__(self, first_name, last_name, email, created_on, shipping_address, billing_address, purchase_history, customer_id):
        super().__init__(self, first_name, last_name, email, created_on)
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_history = purchase_history
        self.customer_id = customer_id

    def change_billing_address(self, new_billing_address):
        self.billing_address = new_billing_address
    def change_shipping_address(self, new_shipping_address):
        self.shipping_address = new_shipping_address










































