import mysql.connector
import pandas as pd
# pd_reader = pd.read_csv('Restaurant.csv')
# l = []
# for i in range(1110):
#     f = (int(pd_reader.loc[i]['restaurant_id']),pd_reader.loc[i]['name'],float(pd_reader.loc[i]['price']),pd_reader.loc[i]['phone'],pd_reader.loc[i]['website'],pd_reader.loc[i]['address'],pd_reader.loc[i]['add_name'],int(pd_reader.loc[i]['add_num']))
#     l.append(f)

# pd_reader = pd.read_csv('class.csv')
# l = []
# for i in range(810):
#     f = (int(pd_reader.loc[i]['restaurant_id']),pd_reader.loc[i]['class'])
#     l.append(f)

pd_reader = pd.read_csv('review.csv')
l = []
for i in range(1034):
    f = (int(pd_reader.loc[i]['Account']),int(pd_reader.loc[i]['business_id']),pd_reader.loc[i]['date']
        ,pd_reader.loc[i]['Text'],int(pd_reader.loc[i]['Rating']))
    l.append(f)

# pd_reader = pd.read_csv('Park.csv')
# l = []
# for i in range(9119):
#     f = (int(pd_reader.loc[i]['ROW_ID']),int(pd_reader.loc[i]['ZONE']),pd_reader.loc[i]['ODD_EVEN'],int(pd_reader.loc[i]['ADDR_LOW']),int(pd_reader.loc[i]['ADD_HIGH']),pd_reader.loc[i]['add_name'])
#     l.append(f)

# pd_reader = pd.read_csv('User.csv')
# l = []
# for i in range(1001):
#     f = (int(pd_reader.loc[i]['Account']),pd_reader.loc[i]['User_Name'],pd_reader.loc[i]['Gender'],pd_reader.loc[i]['Favoriate_class'],pd_reader.loc[i]['Password'])
#     l.append(f)

create_query_User = """
CREATE TABLE User(
    Account BIGINT PRIMARY KEY, 
    User_Name VARCHAR(256) NOT NULL, 
    Gender VARCHAR(10), 
    Favoriate_class VARCHAR(256), 
    Password VARCHAR(20) NOT NULL
)
"""

create_query_Res ='''
CREATE TABLE Restaurant( restaurant_id INT PRIMARY KEY, 
    name VARCHAR(64) NOT NULL, 
    price FLOAT, 
    phone VARCHAR(32), 
    website VARCHAR(256), 
    address VARCHAR(256), 
    add_name VARCHAR(256), 
    add_num INT);
'''

create_query_Review ='''
CREATE TABLE Review( 
    review_id  int primary key not null auto_increment,
    Account BIGINT, 
    business_id INT, 
    date DATE, 
    Text Varchar(4096), 
    Rating int, 
    FOREIGN KEY(business_id) references Restaurant(restaurant_id), 
    FOREIGN KEY(Account) references User(Account) );
'''
create_query_Class ='''
CREATE TABLE Class( 
    restaurant_id INT, 
    class VARCHAR(32), 
    PRIMARY KEY(restaurant_id,class), 
    FOREIGN KEY(restaurant_id) references Restaurant(restaurant_id) );
'''

create_query_Park = '''
CREATE TABLE Park(ROW_ID INT PRIMARY KEY, 
    ZONE INT, 
    ODD_EVEN VARCHAR(10), 
    ADDR_LOW INT, 
    ADDR_HIGH INT, 
    add_name VARCHAR(256));
'''
mydb = mysql.connector.connect(
        host="localhost",
        user='ddmer',
        database = 'ddmer_database',
        password='%dbZvhSJa26%)'
    )
insert_query_user = '''INSERT INTO User(Account, User_Name, Gender, Favoriate_class, Password)
VALUES(%s,%s,%s,%s,%s)'''

insert_query_res = '''INSERT INTO Restaurant(restaurant_id, name,
    price,
    phone,
    website,
    address,
    add_name,
    add_num)
  VALUES(%s,%s,%s,%s,%s,%s, %s, %s)'''

insert_query_park = '''INSERT INTO Park(ROW_ID,
    ZONE,
    ODD_EVEN,
    ADDR_LOW,
    ADDR_HIGH,
    add_name)
    VALUES(%s,%s,%s,%s,%s,%s)'''

insert_query_class = '''INSERT INTO Class(restaurant_id,
    class)
    VALUES(%s,%s)'''

insert_query_Review = '''INSERT INTO Review(
    Account,
    business_id,
    date,
    Text,
    Rating )
    VALUES(%s,%s,%s,%s,%s)'''

drop_table_query = "DROP TABLE Review"

# insert_query = '''INSERT INTO User(User_id, User_Name, Gender, Favoriate_food, Account, Password)
# VALUES
#     (2,'3','4','NULL',23,'1233')'''
# insert_query = 'DELETE FROM User WHERE User_id = 2'
# mycursor = mydb.cursor()
# mycursor.execute('select * from User')
# print([row for row in mycursor])

# mycursor.execute(create_query_Review)

# mycursor.execute(drop_table_query)
#
# mycursor.executemany(insert_query_Review,l)
# mydb.commit()