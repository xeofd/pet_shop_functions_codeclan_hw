# WRITE YOUR FUNCTIONS HERE

# Function 1: return shop name
def get_pet_shop_name(shop):
    return shop['name']

# Function 2: find total cash
def get_total_cash(shop):
    return shop['admin']['total_cash']

# Function 3: Add or remove cash
def add_or_remove_cash(shop, ammount):
    shop['admin']['total_cash'] += ammount

# Function 4: Count ammount of pets sold
def get_pets_sold(shop):
    return shop['admin']['pets_sold']

# Function 5: Increase ammount of pets sold
def increase_pets_sold(shop, ammount):
    shop['admin']['pets_sold'] += ammount

def get_stock_count(shop):
    count = 0
    for pet in shop['pets']:
        count += 1
    
    return count

# Function 6: Get pets by type
def get_pets_by_breed(shop, breed):
    count = []
    for pet in shop['pets']:
        if (pet['breed'] == breed):
            count.append(pet)
    return count

# Function 7: Get pet by name
def find_pet_by_name(shop, name):
    for pet in shop['pets']:
        if (pet['name'] == name):
            return pet

# Function 8: Remove pet by name
def remove_pet_by_name(shop, name):
    for pet in shop['pets']:
        if (pet['name'] == name):
            pet['name'] = ""

# Function 9: Add pet to stock
def add_pet_to_stock(shop, new_pet):
    shop['pets'].append(new_pet)

# Function 10: Get customer cash
def get_customer_cash(customer):
    return customer['cash']

# Function 11: Remove customer cash
def remove_customer_cash(customer, cash_to_remove):
    customer['cash'] -= cash_to_remove

# Function 12: Get customer pet count
def get_customer_pet_count(customer):
    return len(customer['pets'])

# Function 13: Add pet to customer
def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)

# Function 13: Check if a customer can buy a pet
def customer_can_afford_pet(customer, pet):
    if (customer['cash'] >= pet['price']):
        return True
    return False

# Function 14: Sell pet to customer
def sell_pet_to_customer(shop, pet, customer):
    if (pet in shop['pets']):
        if (customer['cash'] >= pet['price']):
            add_pet_to_customer(customer, pet)
            remove_customer_cash(customer, pet['price'])
            increase_pets_sold(shop, 1)
            add_or_remove_cash(shop, pet['price'])