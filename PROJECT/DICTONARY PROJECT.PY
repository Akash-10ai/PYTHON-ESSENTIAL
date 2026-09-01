
#Scenario
#The inventory store scenario project utilizes a dictionary-based approach to develop a robust system for managing and tracking inventory in a retail store.
#Note:- You will be working with two product details.

#STEP 1 CREATE AN EMPTY DICTIONARY
inventory_dict = {}

# STEP 2 STORE THE FIRST PRODUCT DETAILS IN VARIABLE 

productNo1 = "mobile phone"
productNo1_quantity = 5
productNo1_price = 20000
productNo1_releaseYear = 2020

# STEP 3  Add the details in invantory 

inventory_dict["ProductNo1"] = productNo1
inventory_dict["ProductNo1_quantity"] = productNo1_quantity
inventory_dict["ProductNo1_price"] = productNo1_price
inventory_dict["ProductNo1_releaseYear"] = productNo1_releaseYear

# STEP 4 STORE THE SECOND PRODUCT DETAILS IN VARIABLE

productNo2 = "Laptop"
productNo2_quantity = 10
productNo2_price = 50000
productNo2_releaseYear = 2023

# STEP 5  Add the details in invantory

inventory_dict["ProductNo2"] = productNo2
inventory_dict["ProductNo2_quantity"] = productNo2_quantity
inventory_dict["ProductNo2_price"] = productNo2_price
inventory_dict["ProductNo2_releaseYear"] = productNo2_releaseYear

# STEP 6 DISPLAY THE PRODUCT PRESENT IN THE INVENTORY

print("The product present in the inventory are:",inventory_dict["ProductNo1"],"and",inventory_dict["ProductNo2"])


#STEP 7 CHEAK IF PRODUCTNO 1_ RELEWSEYEAR AND PRODUCT NO 2_RELEASEYEAR IN INVANTORY


print("productNo1_releaseYear" in inventory_dict.values())
print("productNo2_releaseYear" in inventory_dict.values())

#STEP 8 DELETE RELEASE YEAR OF BOTH THE PRODUCT FROM INVENTORY

del inventory_dict["ProductNo1_releaseYear"]
del inventory_dict["ProductNo2_releaseYear"]
