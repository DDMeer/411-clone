Data tables:
============
https://github.com/uiuc-fa21-cs411/404-not-found/blob/main/park.csv
https://github.com/uiuc-fa21-cs411/404-not-found/blob/main/restaurant.csv
https://github.com/uiuc-fa21-cs411/404-not-found/blob/main/review.csv
https://github.com/uiuc-fa21-cs411/404-not-found/blob/main/user.csv



DDL commands:
===============

CREATE TABLE Restaurant(
restaurant_id INT PRIMARY KEY, 
name VARCHAR(64) NOT NULL, 
price INT, 
phone VARCHAR(32), 
website VARCHAR(256), 
address VARCHAR(256),
add_name VARCHAR(256), 
add_num INT);


CREATE TABLE User(
User_id INT PRIMARY KEY, 
User_Name VARCHAR(256) NOT NULL, 
Gender VARCHAR(256) NOT NULL, 
Favoriate_food VARCHAR(256),
Account INT,
Password VARCHAR(256)
);

CREATE TABLE Review(
review_id INT PRIMARY KEY,
User_id INT,
business_id INT,
date TIME,
Text Varchar(1024),
Rating DOUBLE,
FOREIGN KEY(business_id) references Restaurant(restaurant_id),
FOREIGN KEY(User_id) references User(user_id)
);

CREATE TABLE Class(
restaurant_id INT, 
class VARCHAR(32),
PRIMARY KEY(restaurant_id,class),
FOREIGN KEY(restaurant_id) references Restaurant(restaurant_id)
);

CREATE TABLE Park(
ROW_ID INT PRIMARY KEY,
ZONE INT,
ODD_EVEN CHAR(10),
ADDR_LOW INT,
ADDR_HIGH INT,
add_name VARCHAR(256));


Two Advanced Queries:
=============
question1:select restuarant that the address of the restuarant has a park (same street or avenue)
![image](https://user-images.githubusercontent.com/32198970/138581134-487b04dc-604b-4996-bf8f-668500a6159d.png)

    
    
question2:

select restaurant_id, name, count(restaurant_id)
from Restaurant1 natural join class
group by restaurant_id
having count(restaurant_id) >=2
order by count(restaurant_id) desc
![image](https://user-images.githubusercontent.com/32198970/138580991-2368b4db-5646-4e28-b605-4a6cf3a76f9d.png)

Indexing:
==========


