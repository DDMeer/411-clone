import math
import sqlite3
import mysql.connector
import pandas as pd
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
from flask import stream_with_context, Response

row_limit = 1000
app = Flask(__name__)

mydb = mysql.connector.connect(
        host="localhost",
        user='tengjun2',
        database = 'tengjun2_database',
        password='Teng0707.'
    )
mycursor = mydb.cursor()


@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/restaurant/<id>')
def restaurant(id):
    sql = """select * from Restaurant where restaurant_id = """ + str(id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    rest = []
    for item in result:
        d = dict()
        d['res_id'] = item[0]
        d['name'] = item[1]
        d['price'] = item[2]
        d['phoneNumber'] = item[3]
        d['website'] = item[4]
        d['address'] = item[5]
        rest.append(d)
    print(rest)
    if rest == []:
        return False

    sql2 = """select * from Review where business_id = """ + str(id)
    mycursor.execute(sql2)
    result = mycursor.fetchall()
    review = []
    for item in result:
        d = dict()
        d['review_id'] = item[0]
        d['User_id'] = item[1]
        d['date'] = item[3]
        d['Text'] = item[4]
        d['Rating'] = item[5]
        review.append(d)
    return render_template('res_extend.html', restaurants=rest, reviews = review)

@app.route('/change')
def change():
    return render_template('changepwd.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/searchR',methods = ['GET','POST'])
def searchR():
    name = request.form['resName']
    numCat = int(request.form['catNum'])
    if numCat == 0:
        sql = """select * from Restaurant where name like '"""+name +"""%' """
    else:
        sql = """select restaurant_id, name,count(restaurant_id) from Restaurant natural join Class where name like '"""+name +"""%' """ + """group by restaurant_id having count(restaurant_id) >=""" + str(numCat) +""" order by count(restaurant_id) desc"""
    print(sql)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(result)
    res = []
    for item in result:
        d =dict()
        d['name'] = item[1]
        res.append(d)
    print(res)
    return render_template('searchR.html', restaurants=res)

@app.route('/query', methods=['POST'])
def search_query():
    sql = request.form['query_string']
    mycursor.execute(sql)
    result = mycursor.fetchall()
    df = pd.DataFrame(result).head(row_limit)
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



@app.route('/insert', methods=['POST'])
def insert_query():
    account = request.form['account']
    pwd = request.form['pwd']
    delete_query = 'DELETE FROM User WHERE User_id = 12345'
    sql = """SELECT count(*) from User"""
    mycursor.execute(sql)
    result = mycursor.fetchall()
    response = {
        "data": {
            "values": result
        }
    }
    sql = """INSERT INTO User(User_id, User_Name, Gender, Favoriate_food, Account, Password) VALUES(%s,%s,%s,%s,%s,%s)"""
    record = [(result[0][0], 'unknown', 'unknown', 'unknown', account, pwd)]
    mycursor.executemany(sql, record)
    mydb.commit()
    return response

@app.route('/update', methods=['POST'])
def update_query():
    print(1)
    account = request.form['account']
    pwd = request.form['pwd']
    sql = """
        UPDATE User
        SET Password = "%s"
        WHERE Account = "%s"
    """%(pwd,
         account
    )
    mycursor.execute(sql)
    mydb.commit()
    response = {
        "data": {
            "values": 1
        }
    }
    return response


@app.route('/delete', methods=['POST'])
def delete_query():
    print(1)
    id = request.form['id']
    delete_query = "DELETE FROM Review WHERE review_id = '" + id+"'"
    mycursor.execute(delete_query)
    mydb.commit()
    response = {
        "data": {
            "values": 1
        }
    }
    return response

@app.route('/park', methods=['POST'])
def park_query():
    id = request.form['id']
    sql = "SELECT add_name, ADDR_LOW,ADDR_HIGH FROM Park WHERE add_name in (SELECT add_name FROM Restaurant WHERE restaurant_id = " + str(id) + ") ORDER BY ADDR_LOW"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(result)
    df = pd.DataFrame(result).head(row_limit)

    def make_valid(v):
        if v != v:
            return None
        else:
            return v

    column_labels = ['Address Name','Range Low', 'Range high']
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
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10055, use_debugger=True, use_reloader=True)