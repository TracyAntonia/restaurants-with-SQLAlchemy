# restaurants-with-SQLAlchemy

## Restaurant Reviews Application
This is a Python application for managing restaurant reviews. It uses SQLAlchemy to interact with a SQLite database and allows you to perform various operations related to customers, restaurants, and reviews.

### Setup
Before running the application, make sure you have the necessary libraries installed. You can install them using pip:
 
    $ pip install sqlalchemy alembic

### Database Initialization
The application uses a SQLite database named restaurant_reviews.db. You can change the database URL as needed.   

    $ engine = create_engine('sqlite:///restaurant_reviews.db')

### Usage
The application defines three main classes: Customer, Restaurant, and Review.

1. Customer Class
The Customer class represents a customer who can leave reviews for restaurants.

Methods:
- full_name(): Returns the full name of the customer.
favorite_restaurant(): Returns the customer's favorite restaurant based on their reviews.
- add_review(restaurant, rating): Adds a review for a restaurant with a star rating.
- delete_reviews(restaurant): Deletes all reviews by the customer for a specific restaurant.

2. Restaurant Class
The Restaurant class represents a restaurant that can receive reviews.

Methods:
- fanciest(): Returns the fanciest restaurant based on the highest price.
- all_reviews(): Returns a list of all reviews for all restaurants.

3. Review Class
The Review class represents a review left by a customer for a restaurant.

Methods:
- full_review(): Returns a string representation of the review.

This code demonstrates how to create customers, restaurants, add reviews, and perform various operations on them. Don't forget to commit changes and close the session when you're done.

### Database Migrations
The application also supports database migrations using Alembic. Make sure to configure Alembic accordingly in the alembic.ini file.
