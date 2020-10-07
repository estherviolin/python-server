CUSTOMERS = [
      {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct"
    },
    {
      "id": 2,
      "name": "Esther Sanders",
      "address": "10 Main St"
    },
    {
      "id": 3,
      "name": "Heather",
      "address": "1 Broadway"
    },
    {
      "email": "esther@esther.com",
      "password": "1234",
      "name": "Esther Sanders",
      "id": 4
    }
]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer