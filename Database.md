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
question1:"Write a sql query to find out the id of the user that the password starts with "a" and who made a comment in 2004"

(SELECT 
    user_id
FROM
    user us2
WHERE
    us2.Password LIKE 'a%') UNION (SELECT 
    us.user_id
FROM
    user us
        JOIN
    review re ON us.User_id = re.User_id
WHERE
    re.date LIKE '2004%')
    
    
question2:

select restaurant_id, name, count(restaurant_id)
from Restaurant1 natural join class
group by restaurant_id
having count(restaurant_id) >=2
order by count(restaurant_id) desc

Indexing:
==========

