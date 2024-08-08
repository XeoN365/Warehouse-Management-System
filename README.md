# Warehouse Management System

This repository contains a Django web application designed to manage inventory in a warehouse. The application is built using Python and follows the standard Django project layout.

## Project Overview

The Warehouse Management System (WMS) is a web-based application that aims to streamline inventory management tasks within a warehouse. It provides a user-friendly interface for tracking and managing various aspects of inventory, such as products, suppliers, and orders.

Key features of the WMS include:

- Product management: Create, update, and delete product records, including details such as name, description, and price.
- Supplier management: Maintain a list of suppliers, including contact information and their associated products.
- Order management: Create, update, and delete purchase orders, including details such as order date, supplier, and products.
- Inventory tracking: Keep track of the current inventory status, including the quantity of each product in stock.
- Reporting: Generate reports on inventory levels, sales, and other relevant metrics.

## Models

The WMS application includes the following Django models:

1. `Inventory`: Represents a product in the inventory. Fields include `name`, `description`, `price`, and `quantity`.
2. `Order`: Represents a customer order. Fields include `order_number`, `customer_name`, `customer_email`, `order_date`, and a many-to-many relationship with the `Inventory` model through the `OrderItem` model.
3. `OrderItem`: Represents an item in an order. Fields include `order`, `inventory`, and `quantity`.
4. `Shipping`: Represents shipping information for an order. Fields include `order`, `address`, `city`, `state`, `postal_code`, `country`, `status`, and `tracking_number`.

## Getting Started

To run this project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/warehouse_management.git
```

2. Navigate to the project directory:

```bash
cd warehouse_management
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create a superuser for the Django admin interface:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Access the application in your browser by visiting http://localhost:8000.
