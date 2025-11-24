import sys

# --- GLOBAL DATA STRUCTURES ---

# Product Catalog: A dictionary where keys are Product IDs and values are product details.
CATALOG = {
    101: {"name": "Python Book (Beginner)", "price": 45.99, "stock": 10},
    102: {"name": "Webcam (HD 1080p)", "price": 29.50, "stock": 25},
    103: {"name": "Mechanical Keyboard", "price": 75.00, "stock": 5},
    104: {"name": "4K Monitor (27 inch)", "price": 299.99, "stock": 3},
    105: {"name": "Coffee Mug (Coding)", "price": 9.99, "stock": 50}
}

# Shopping Cart: A dictionary to store {Product ID: Quantity}
shopping_cart = {}


# --- CORE APPLICATION FUNCTIONS ---

def display_catalog():
    """Prints the entire product catalog to the console."""
    print("\n--- Available Products ---")
    print(f"{'ID':<4} | {'Product Name':<30} | {'Price':>8} | {'Stock':>5}")
    print("-" * 55)
    for product_id, details in CATALOG.items():
        print(f"{product_id:<4} | {details['name']:<30} | ${details['price']:>7.2f} | {details['stock']:>5}")
    print("-" * 55)

def add_to_cart():
    """Prompts the user for a product ID and quantity to add to the cart."""
    try:
        product_id = int(input("Enter Product ID to add: "))
        if product_id not in CATALOG:
            print("Error: Invalid Product ID.")
            return

        product = CATALOG[product_id]
        
        # Check current stock
        if product['stock'] <= 0:
            print(f"Error: {product['name']} is currently out of stock.")
            return

        quantity = int(input(f"Enter quantity for {product['name']} (Max {product['stock']}): "))
        
        if quantity <= 0:
            print("Error: Quantity must be greater than zero.")
            return

        if quantity > product['stock']:
            print(f"Error: We only have {product['stock']} in stock. Adding max available.")
            quantity = product['stock']

        # Update cart and stock
        current_in_cart = shopping_cart.get(product_id, 0)
        
        # If we are adding more than what's available (including what's already reserved in the cart)
        available_to_add = product['stock'] - current_in_cart
        if quantity > available_to_add:
             print(f"Warning: Only {available_to_add} more units available. Adding {available_to_add}.")
             quantity = available_to_add

        # Finally, update the cart and reduce the 'available' stock for this session
        shopping_cart[product_id] = current_in_cart + quantity
        
        print(f"Added {quantity} x {product['name']} to the cart.")

    except ValueError:
        print("Error: Please enter a valid number for ID and quantity.")

def remove_from_cart():
    """Prompts the user to remove a product from the cart."""
    if not shopping_cart:
        print("Your cart is empty.")
        return
        
    view_cart(show_total=False)
    
    try:
        product_id = int(input("Enter Product ID to remove (or 0 to cancel): "))
        
        if product_id == 0:
            return

        if product_id not in shopping_cart:
            print("Error: Product not found in cart.")
            return
            
        del_quantity = int(input(f"Enter quantity to remove for {CATALOG[product_id]['name']} (Currently {shopping_cart[product_id]} in cart): "))
        
        if del_quantity <= 0:
            print("Error: Quantity to remove must be positive.")
            return

        current_qty = shopping_cart[product_id]
        
        if del_quantity >= current_qty:
            del shopping_cart[product_id]
            print(f"Removed all {current_qty} units of {CATALOG[product_id]['name']} from the cart.")
        else:
            shopping_cart[product_id] -= del_quantity
            print(f"Removed {del_quantity} units of {CATALOG[product_id]['name']}. {current_qty - del_quantity} remain.")

    except ValueError:
        print("Error: Please enter a valid number.")

def view_cart(show_total=True):
    """Displays the current contents of the shopping cart and calculates the total."""
    if not shopping_cart:
        print("\n--- Your Shopping Cart ---")
        print("Your cart is empty. Time to shop!")
        return 0.0

    print("\n--- Your Shopping Cart ---")
    print(f"{'ID':<4} | {'Product Name':<30} | {'Qty':>3} | {'Unit Price':>10} | {'Subtotal':>10}")
    print("-" * 65)
    
    total = 0.0
    for product_id, quantity in shopping_cart.items():
        if product_id in CATALOG:
            product = CATALOG[product_id]
            subtotal = product['price'] * quantity
            total += subtotal
            print(f"{product_id:<4} | {product['name']:<30} | {quantity:>3} | ${product['price']:>9.2f} | ${subtotal:>9.2f}")
    
    if show_total:
        print("-" * 65)
        print(f"{'Total':<50} | {'':>10} | ${total:>9.2f}")
        print("-" * 65)
    
    return total

def checkout():
    """Calculates the final total and 'processes' the order."""
    final_total = view_cart()
    
    if final_total == 0.0:
        return

    print("\n--- Checkout Summary ---")
    print(f"Order Total: ${final_total:.2f}")

    # Simple payment simulation
    while True:
        payment_method = input("Enter payment method (Card/Cash): ").strip().lower()
        if payment_method in ['card', 'cash']:
            break
        else:
            print("Invalid payment method. Please enter 'Card' or 'Cash'.")

    print(f"\nProcessing payment via {payment_method.capitalize()}...")
    
    # --- Stock Reduction (The core business logic) ---
    print("Updating inventory...")
    for product_id, quantity in shopping_cart.items():
        CATALOG[product_id]['stock'] -= quantity
    
    # Clear the cart for the next customer
    shopping_cart.clear()
    
    print("\n=============================================")
    print("  Order Successfully Placed! Thank you!  ")
    print("=============================================")
    print("Returning to main menu...")


def main_menu():
    """The main command-line interface loop."""
    print("=============================================")
    print("   Python E-Commerce Console App (v1.0)  ")
    print("=============================================")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. View Products")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Remove Item from Cart")
        print("5. Checkout")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            display_catalog()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            remove_from_cart()
        elif choice == '5':
            checkout()
        elif choice == '6':
            print("\nThank you for shopping! Goodbye.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main_menu()
