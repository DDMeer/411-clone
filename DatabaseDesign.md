Data tables:
============
[park](https://github.com/uiuc-fa21-cs411/404-not-found/blob/main/park.csv)
![image](https://user-images.githubusercontent.com/32198970/138581294-3205a8f3-5679-4e70-a08b-4266e5b46e6a.png)


[restaurant](https://github.com/uiuc-fa21-cs411/404-not-found/blob/main/restaurant.csv)
![image](https://user-images.githubusercontent.com/32198970/138581288-6026b4a9-c6a7-4edb-ba6a-b9ca45d8da2f.png)


[review](https://github.com/uiuc-fa21-cs411/404-not-found/blob/main/review.csv)
![image](https://user-images.githubusercontent.com/32198970/138581295-a5e13b14-c27a-4d46-8352-f0ffe6bf7a20.png)


[user](https://github.com/uiuc-fa21-cs411/404-not-found/blob/main/user.csv)
![image](https://user-images.githubusercontent.com/32198970/138581293-4c597d21-2998-4651-9cc7-1cc7df366786.png)






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
Find restaurants with two or more categories
![image](https://user-images.githubusercontent.com/32198970/138580991-2368b4db-5646-4e28-b605-4a6cf3a76f9d.png)

Indexing:
==========

[index](https://docs.google.com/document/d/1Ef8UV4sY3QB1KDEQAHGMFftPNH53Ybj8xudKwiioe0k/edit)
