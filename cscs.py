import math
import sqlite3
import pandas
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
from flask import stream_with_context, Response


sqlite_uri = 'tengjun2_database'
row_limit = 2000
app = Flask(__name__)

airport_data = []


@app.route('/', methods=['GET'])
def index():
    title = 'CS411: Sample Project 2'
    return render_template('index.html', title=title)


@app.route('/query', methods=['POST'])
def process_query():
    sql = request.form['query_string']
    con = sqlite3.connect(sqlite_uri)
    df = pandas.read_sql_query(sql, con).head(row_limit)
    con.close()

    def make_valid(v):
        if v != v:
            return None
        else:
            return v

    column_labels = [col for col in df.columns]
    per_col_values = [
        [make_valid(value) for value in df[col]]
        for col in df.columns
    ]

    response = {
        "query_string": sql,
        "data": {
            "labels": [[col] for col in column_labels],
            "values": per_col_values
        }
    }

    print(response)
    return response

def insert_into_sqlite(csvfile):
    con = sqlite3.connect(sqlite_uri)
    cur = con.cursor()
    cur.execute('''create table if not exists Restaurant1 (
        restaurant_id INT , 
        name TEXT,
        price REAL,
        phone TEXT,
        website TEXT,
        address TEXT,
        add_name TEXT,
        add_num INT) ''')
    con.commit()
    df = pandas.read_csv(csvfile)
    df.to_sql('Restaurant1', con, if_exists='replace', index=False)
    con.commit()
    con.close()

def insert_into_sqlite2(csvfile):
    con = sqlite3.connect(sqlite_uri)
    cur = con.cursor()
    cur.execute('''create table if not exists class (
        restaurant_id INT , 
        class TEXT,) ''')
    con.commit()
    df = pandas.read_csv(csvfile)
    df.to_sql('class', con, if_exists='replace', index=False)
    con.commit()
    con.close()

def insert_into_sqlite1(csvfile):
    con = sqlite3.connect(sqlite_uri)
    cur = con.cursor()
    cur.execute('''create table if not exists user (
        User_id INT , 
        User_Name TEXT,
        Gender TEXT,
        Favoriate_food TEXT,
        Account TEXT,
        Password TEXT) ''')
    con.commit()
    df = pandas.read_csv(csvfile)
    df.to_sql('user', con, if_exists='replace', index=False)
    con.commit()
    con.close()

def insert_into_sqlite3(csvfile):
    con = sqlite3.connect(sqlite_uri)
    cur = con.cursor()
    cur.execute('''create table if not exists Review(
    review_id REAL
    User_id REAL,
    business_id REAL,
    date TIME,
    Text TEXT,
    Rating REAL,
    FOREIGN_KEY(business_id) references Restaurant(restaurant_id),
    FOREIGN_KEY(User_id) references User(user_id)
    )
 ''')
    con.commit()
    df = pandas.read_csv(csvfile)
    df.to_sql('Review', con, if_exists='replace', index=False)
    con.commit()
    con.close()

def insert_into_sqlite4(csvfile):
    con = sqlite3.connect(sqlite_uri)
    cur = con.cursor()
    cur.execute('''create table if not exists Park(
    ROW_ID REAL,
    ZONE REAL,
    ODD_EVEN TEXT,
    ADDR_LOW REAL,
    ADDR_HIGH REAL,
    add_name TEXT)
    ''')
    con.commit()
    df = pandas.read_csv(csvfile)
    df.to_sql('Park', con, if_exists='replace', index=False)
    con.commit()
    con.close()

if __name__ == '__main__':
    insert_into_sqlite('/mp3/restaurant.csv')
    insert_into_sqlite1('/mp3/user.csv')
    insert_into_sqlite2('/mp3/class.csv')
    insert_into_sqlite3('/mp3/review.csv')
    insert_into_sqlite4('/mp3/park.csv')
    app.run(host='0.0.0.0', port=10051, use_debugger=True, use_reloader=True)
