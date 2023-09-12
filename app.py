# Necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from alembic.config import Config

# Database initialization
engine = create_engine('sqlite:///restaurant_reviews.db')

# Session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Customer class
class Customer(Base):
    # Table name
    __tablename__ = 'customers'

    # Table columns
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')

    # Full customer name 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Customer's favorite restaurant
    def favorite_restaurant(self):
        highest_rating = 0
        favorite = None
        for review in self.reviews:
            if review.star_rating > highest_rating:
                highest_rating = review.star_rating
                favorite = review.restaurant
        return favorite

    # Restaurant review
    def add_review(self, restaurant, rating):
        review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        self.reviews.append(review)

    # Delete reviews
    def delete_reviews(self, restaurant):
        for review in self.reviews:
            if review.restaurant == restaurant:
                self.reviews.remove(review)

# Restaurant class
class Restaurant(Base):
    # Table name
    __tablename__ = 'restaurants'

    # Table columns
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')

    # Fanciest restaurant
    @classmethod
    def fanciest(cls):
        return max(cls.all(), key=lambda r: r.price)

    # Restaurants reviews
    @classmethod
    def all_reviews(cls):
        all_reviews = []
        for restaurant in cls.all():
            for review in restaurant.reviews:
                all_reviews.append(f"Review for {restaurant.name} by {review.customer.full_name()}: {review.star_rating} stars.")
        return all_reviews

# Review class
class Review(Base):
    # Table name
    __tablename__ = 'reviews'

    # Table columns
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    star_rating = Column(Integer)

    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

    # Review string
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."

# Database migrations
alembic_cfg = Config("alembic.ini")
command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    
    # Close
    session.close()
