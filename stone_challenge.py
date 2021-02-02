# class products
class Product:
    
    def __init__(self, item='', amount=0, price=0):
        self.item = item
        self.amount = amount
        self.price = price    
        
# products list   
produts_list = [
    Product( 'leite', 2, 319 ) ,
    Product( 'macarrão', 5, 220 ) ,
    Product( 'batata', 5, 500 ) ,
    Product( 'queijo', 1, 670 ) ,
    Product( 'mortandela', 1, 780 ) ,
    Product( 'pão', 5, 280 ) 
]
   
# emails list
emails_list = [
    'thomasShelby@gmail.com',
    'bijornIronSide@gmail.com',
    'god@gmail.com',
    'barneyStinson@gmail.com',
    'harryPotter@gmail.com',
    'daenerysTargaryen@gmail.com',
    'reiDaNoite.@gmail',
]

# method that checks whether the lists are correct
def checkData(emails_list, produts_list):
    msg = ''
    
    msg = checkEmails(emails_list)
    if msg:
        return msg
    
    msg = checkProducts(produts_list)
    if msg:
        return msg
    
# method that checks if the email list is correct
def checkEmails(emails_list):
    
    # check if email list is valid
    if emails_list:
        
        # check if list items are of type str
        for email in emails_list:
            if not isinstance(email, str):
                return 'one of the emails is invalid'
        
            # checks if emails are valid
            if '@' not in email or '.com' not in email:
                return 'invalid email'
            
        # check for duplicate emails
        count = 0
        for i in emails_list:
            for y in emails_list:
                
                if i == y:
                    count += 1
                
            if count > 1:
                return 'duplicate emails in the email list, please check'
            count = 0
        
        
    else:
      return 'Empty emails list'



# method that checks if the product list is correct
def checkProducts(produts_list):

    # check if products list is empty
    if produts_list:

        # check if products list is valid
        for product in produts_list:
            
            # check that the product list is the correct type
            if isinstance(product, Product):
                
                # checks that product list items are the correct type
                if not isinstance(product.price, int):
                    return 'the price of one of the items in the product list is incorrect, please enter a whole number'
                if not isinstance(product.item, str) and product.item:
                    return 'the name of one of the items in the product list is incorrect or empty, please enter a text value'
                if not isinstance(product.amount, int):
                    return 'the quantity of one of the items in the product list is incorrect, please enter a whole number'
            else:
                return 'one of the list items is not a valid data type'
    else:
        return 'Empty product list'

# function to return dictionary with emails and agreed payment amount
def dicionaryEmailsList(emails_list, produts_list):
    
    # checks the lists for incorrect data by calling the verification method
    msg = checkData(emails_list,produts_list)
    if msg:
        return msg
    
    # interact about product list and calculate total value of product list        
    value_total = 0
    for product in produts_list:
        value_total += product.amount * product.price
    
    # calculates the individual amount that each user of the email list will pay, removing the penny that may be left
    value_user = value_total // len(emails_list)

    
    # iterates over email list and creates a dictionary
    dicionary = {}
    for email in emails_list:
            dicionary[email] = value_user
    
    # checks if you have a penny left in the calculation and add to the value of the last user
    remainder =  value_total % len(emails_list)
    if remainder == 1:
            dicionary[emails_list[len(emails_list) - 1]] += remainder
            
    # return dicionary
    return dicionary

# print method return
print(dicionaryEmailsList(emails_list, produts_list))