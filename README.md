# python_console_shopping_app
Python E-Commerce Console App (v1.0)

A simple, command-line interface (CLI) application built with Python to simulate basic e-commerce functionality, including viewing a product catalog, adding items to a shopping cart, and checking out.

Features

Product Catalog: View a pre-defined list of products with current stock and prices.

Shopping Cart: Add, remove, and manage product quantities in a session-based cart.

Stock Management: Automatic stock checks and reduction upon checkout.

Checkout Process: Calculates the final total and simulates order processing.

Setup and Installation

This application has no external dependencies and can be run with a standard Python installation.

Save the Code: Ensure the Python script (ecommerce_app.py) is saved.

Ensure Python is Installed: The application is compatible with Python 3.x.

How to Run

Execute the main file from your terminal:

python ecommerce_app.py


This will launch the main menu interface.

Usage

The application is entirely menu-driven. Upon startup, you will see the main menu:

=============================================
   Python E-Commerce Console App (v1.0) 
=============================================

--- Main Menu ---
1. View Products
2. Add Item to Cart
3. View Cart
4. Remove Item from Cart
5. Checkout
6. Exit
Enter your choice (1-6):


Key Functions

1. View Products: Displays the current CATALOG with Product ID, Name, Price, and available Stock.

2. Add Item to Cart: Prompts for a Product ID and Quantity. Includes validation to ensure the quantity does not exceed available stock.

3. View Cart: Shows the current items in the shopping_cart, calculating the subtotal for each item and the grand total.

4. Remove Item from Cart: Allows you to remove a specific quantity or all units of an item from the cart.

5. Checkout: Displays the final total, simulates a payment method entry, and critically, reduces the stock in the global CATALOG before clearing the cart.

6. Exit: Closes the application.


Future Enhancements

Persistence: Save and load catalog/cart data to a file (e.g., JSON or CSV) instead of using in-memory data.

User Accounts: Implement basic user login to save and load different shopping carts.

Advanced Validation: Improve input validation and error handling across all functions.

Fancier UI: Explore using a library like curses or rich for a more visually appealing console interface.
