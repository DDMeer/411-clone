import math
import sqlite3
import pandas
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
from flask import stream_with_context, Response

sqlite_uri = 'changli9.db'
row_limit = 2000
app = Flask(__name__)

restaurant_data = []

def index():
    title = 'Restaurant Finding Page'
return render_template('index.html', title=title)

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
    cur.execute('''create table if not exists restaurant1 (
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
    df.to_sql('restaurant', con, if_exists='replace', index=False)
    con.commit()
con.close()

if __name__ == '__main__':
    insert_into_sqlite('restaurant.csv')
    app.run(host='0.0.0.0', port=10051, use_debugger=True, use_reloader=True)
