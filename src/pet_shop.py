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
        if (pet == breed):
            count.append(pet)
    return count