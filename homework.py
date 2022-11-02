from datetime import datetime as dt

class User:  
    def __init__(self, first_name, last_name, email, created_on, id): 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_on = created_on
        self.id = id

    def __repr__(self): 
        return f"User('{self.first_name}', '{self.last_name}', '{self.email}', '{self.created_on}', '{self.id}')"

    def __str__(self): 
        return f"{self.first_name} {self.last_name} {self.email} {self.created_on} {self.id}"

    def __eq__(self, other): 
        return self.email == other.email

    def __hash__(self): 
        return hash(self.email)

    def change_first_name(self, new_first_name): 
        self.first_name = new_first_name 

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name


class Employee(User):
    def __init__(self, first_name, last_name, email, created_on, home_address, security_level, department, id):
        super().__init__(first_name, last_name, email, created_on, id)
        self.home_address = home_address
        self.security_level = security_level
        self.department = department

    def change_department(self, new_department): 
        self.department = new_department


class Customer(User): 
    def __init__(self, first_name, last_name, email, created_on, shipping_address, billing_address, purchase_history, id):
        super().__init__(first_name, last_name, email, created_on, id)
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_history = purchase_history

    def change_billing_address(self, new_billing_address): 
        self.billing_address = new_billing_address

    def change_shipping_address(self, new_shipping_address): 
        self.shipping_address = new_shipping_address


if __name__ == '__main__':
    employees = [ Employee("John","Smith","JSmith@email.com",dt.utcnow(),"7834 85Th Ave SE","6","Sales","928375"),
                  Employee("Matt","Murphy","MMurphy@email.com",dt.utcnow(),"6545 92Th St SW","2","Marketing","546854"),
                  Employee("Jessica","McChicken","JMcChicken@email.com",dt.utcnow(),"1600 10th Blvd","HR","324885") ]

    customers = [ Customer("Sammy","White","SWhite@email.com",dt.utcnow(),"312 Nevada","312 Nevada",["Fruit","Water"],"548484"),
                  Customer("Jimothy","Timothy","JTimothy@email.com",dt.utcnow(),"Ohio St",["Alcohol","Booze","Liquor","Moonshine"],"548488"),
                  Customer("Boe","Jiden","BJiden@email.com",dt.utcnow(),"Saturn","Saturn",["Ford F150","Tesla Model X"],"216846") ]
    
    users = employees + customers
    users.sort(key=lambda user: user.created_on, reverse=True)
    print(*users,sep='\n')
































