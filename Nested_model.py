from pydantic import BaseModel

# Nested model
class Address(BaseModel):
    city: str
    pincode: int

# Main model
class User(BaseModel):
    name: str
    address: Address


# -----------------------------
# Example usage
# -----------------------------

# Input data (like API request body)
user_data = {
    "name": "Amaan",
    "address": {
        "city": "Aligarh",
        "pincode": 202001
    }
}

# Create object
user = User(**user_data)

# Print object
print("User Object:", user)

# Access nested data
print("City:", user.address.city)
print("Pincode:", user.address.pincode)

# Convert to dictionary
print("As Dict:", user.model_dump())

# Convert to JSON
print("As JSON:", user.model_dump_json())