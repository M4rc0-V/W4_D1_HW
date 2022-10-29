from datetime import datetime as dt

class User():
    def __init__(self, first_name, last_name, email, created_on):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_on = dt.utcnow()

    def change_first_name(self, new_name):
        self.first_name = new_name
    def change_last_name(self, new_name):
        self.last_name = new_name









class Employee(User):
    def __init__(self, first_name, last_name, email, created_on, home_address, security_level, department, employee_id):
        super().__init__(first_name, last_name, email, created_on)
        self.home_address = home_address
        self.security_level = security_level
        self.department = department
        self.employee_id = employee_id

    def change_department(self, new_department):
        self.departemnt = new_department








class Customer(User):
    def __init__(self, first_name, last_name, email, created_on, shipping_address, billing_address, purchase_history, customer_id):
        super().__init__(first_name, last_name, email, created_on)
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_history = purchase_history
        self.customer_id = customer_id

    def change_billing_address(self, new_billing_address):
        self.billing_address = new_billing_address
    def change_shipping_address(self, new_shipping_address):
        self.shipping_address = new_shipping_address

John = Employee("John","Smith","JSmith@email.com",dt.utcnow(),"7834 85Th Ave SE","6","Sales","928375")
Matt = Employee("Matt","Murphy","MMurphy@email.com",dt.utcnow(),"6545 92Th St SW","2","Marketing","546854")
Jessica = Employee("Jessica","McChicken","JMcChicken@email.com",dt.utcnow(),"1600 10th Blvd","HR","324885")

Sammy = Customer("Sammy","White","SWhite@email.com",dt.utcnow(),"312 Nevada","312 Nevada",["Fruit","Water"],"548484")
Jimothy = Customer("Jimothy","Timothy","JTimothy@email.com",dt.utcnow(),"Ohio St",["Alcohol","Booze","Liquor","Moonshine"],"548488")
Boe = Customer("Boe","Jiden","BJiden@email.com",dt.utcnow(),"Saturn","Saturn",["Ford F150","Tesla Model X"],"216846")


































