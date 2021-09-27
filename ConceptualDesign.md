UML diagram:
===============
![UML](https://user-images.githubusercontent.com/32198970/134846053-a04c2d73-272c-4568-970e-5e2482a1fd66.png)


Entity Descriptions & Assumptions
===============
User:  
After registering, the user has a specific user name, and a password is required to log in to their account. The account will keep their gender information and registration date. Users can access their own favorites food and restaurants. Also, user can find their friends through their account, and the review wrote by themselves.  

Restaurant:  
Each restaurant is uniquely identified by its own business id, which is its primary key. This entity also include the type of category which act as its foreign key, the telephone it owned, the restaurant’s name, address, rating, review counting, open time in every week and menu.  

Review:  
Each review is identified by the review_id as the primary key. Since every review will have a unique review id. And it includes the user_id who wrote this review, and the business_id which belong to a unique restaurant. The above two attributes are used as foreign keys. Also, the review date, content and rating star from users.   

Category:  
The category table contents different type of restaurant which is the primary key. It also includes the description of each restaurant cuisine, such as taco, Chinese food, Western food, fast food, etc.  

Friend:
Friend table is identified by the friend_id which is the primary key. Users can be find their friends by username, and the common interest will also make them friends.

Parking:
Parking stable is identified by the parking_id which is the primary key. This entity includes location, and the coding range (address range_low, address range_high), street name, street type.


Relationship Descriptions & Assumptions
===============
Many-Many:
1. A user has multiple favorite restaurants, and each restaurant can be loved by multiple users.
2. A restaurant has multiple categories, and a category is corresponding to several restaurants.
3. A restaurant is near multiple parking lots, and a parking lot is corresponding to several restuarants.

1-Many:
1. A user can write multiple reviews, but each review is written by exactly one user.
2. A restaurant has multiple reviews, but each review belongs to exactly one restaurant.
3. A user has multiple friends, and a friend is corresponding to exactly one user.

Relational schema 
===============
Review(Review_id:INT[PK], User_id:INT[FK to User.User_id], Business_id:VARCHAR(256)[FK to Restaurant.Business_id], Date:INT, Text:VARCHAR(256), Rating:INT)

User(User_id:INT[PK], Username:VARCHAR(64), Gender:VARCHAR(64), Join_date:INT, Friend_id:INT, Review_count:INT, Favourite_food:VARCHAR(256), Password:INT)

Friend(Friend_id:INT[PK], User_id:INT[FK to User.User_id], Common_interest)

Restaurant(Business_id:VARCHAR(256)[PK], Resaurant_name:VARCHAR(64)，Category_type:INT[FK to Category.Category_type], Address:VARCHAR(256), Telephone:INT, Rating:INT, Review_count:INT, Open_time:INT, Menu:VARCHAR(64))

Category(Category_type:INT[PK], Description:VARCHAR(256))

Parking(Parking_id:INT[PK], Address_range_low:INT, Address_range_high:INT, Street_direction:VARCHAR(256), Street_name:VARCHAR(256), Street_type:VARCHAR(256))
