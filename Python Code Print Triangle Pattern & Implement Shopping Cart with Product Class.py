for i in range (1,6):
    print('*',end='')
    for i in range(6,i-1):
        print('*',end='')
    print()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total_cost(self):
        total_cost = 0
        for product in self.products:
            total_cost += product.price
        return total_cost

def main():
    product1 = Product("iPhone 13 Pro", 999)
    product2 = Product("MacBook Pro", 1499)

    shopping_cart = ShoppingCart()
    shopping_cart.add_product(product1)
    shopping_cart.add_product(product2)

    print("The total cost is:", shopping_cart.get_total_cost())

if __name__ == "__main__":
    main()

    def remove_item(self, product):
        for item in self.items:
            if item["product"] == product:
                self.items.remove(item)




class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price:}"


class Scart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def Ctotal(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def dcart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                print(f"{item['product']} x {item['quantity']}")

# some  products
product1 = Product(1, "Classmate Book", 10.0)
product2 = Product(2, "Colgate paste", 20.0)
product3 = Product(3, "Maggi", 15.0)

#creating shopping cart
cart = Scart()

# Add products to the cart
cart.add_item(product1, 2)
cart.add_item(product2, 1)
cart.add_item(product3, 3)

# Display the cart
cart.dcart()

# Calculate and print the total cost
total_cost = cart.Ctotal()
print(f"Total cost: {total_cost:}")
