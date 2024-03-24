a = [2, 3, 6, 4, 4, 5]
target_sum = 8

pairs = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target_sum:
            pairs.append((a[i], a[j]))

print(f"Pairs with sum {target_sum}: {pairs}")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def display_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                product = item["product"]
                quantity = item["quantity"]
                print(f"{product.name} x{quantity} - ${product.price:.2f} each")

# Sample products
product1 = Product("Product 1", 10.0)
product2 = Product("Product 2", 20.0)
product3 = Product("Product 3", 15.0)

# Create a shopping cart
cart = ShoppingCart()

# Add products to the cart
cart.add_item(product1, 2)
cart.add_item(product2, 1)
cart.add_item(product3, 3)

# Display the cart
cart.display_cart()

# Calculate and print the total cost
total_cost = cart.calculate_total()
print(f"Total cost: ${total_cost:.2f}")
