"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def __repr__(self):
        return "<Customer: {}, {}, {}, {}>".format(self.first_name, self.last_name, self.email, self.password)


def read_customer_from_file(filepath):
#Add a function to read the customers.txt and populate a dictionary 
    customer_types = {}

    with open(filepath) as file:
        for line in file:
            (first_name, last_name, email, password) = line.strip().split("|")
        
            customer_types[email] = Customer(first_name, last_name, email, password) 
    return customer_types


def get_by_email(email):
    if email in customer_types:
        return customer_types[email]
    else:
        return None


customer_types = read_customer_from_file("customers.txt")