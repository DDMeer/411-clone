import math
import sqlite3

import mysql.connector
import pandas as pd
import datetime
from flask import Flask, session, render_template, make_response, flash
from flask import redirect, request, jsonify, url_for
from flask import stream_with_context, Response

row_limit = 1000
app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user='ddmer',
    database='ddmer_database',
    password='%dbZvhSJa26%)'

)
mycursor = mydb.cursor()
app.config["SECRET_KEY"] = "dfasdfasdge"

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

    sql2 = """select * from Review natural join User where business_id = """ + str(id)
    mycursor.execute(sql2)
    result = mycursor.fetchall()
    print(result)
    review = []
    for item in result:
        d = dict()
        d['review_id'] = item[0]
        d['User_name'] = item[6]
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
    sql = """select * from Restaurant where name like '"""+name +"""%' """
    # sql = """select restaurant_id, name,count(restaurant_id) from Restaurant natural join Class where name like '"""+name +"""%' """ + """group by restaurant_id having count(restaurant_id) >=""" + str(2) +""" order by count(restaurant_id) desc"""
    mycursor.execute(sql)
    result = mycursor.fetchall()
    res = []
    for item in result:
        d =dict()
        d['name'] = item[1]
        d['res_id'] = item[0]
        res.append(d)
    print(res)
    return render_template('searchR.html', restaurants=res)

@app.route('/two',methods = ['GET','POST'])
def two():
    name = request.form['resName']
    sql = """select restaurant_id, name,count(restaurant_id) from Restaurant natural join Class where name like '"""+name +"""%' """ + """group by restaurant_id having count(restaurant_id) >=""" + str(2) +""" order by count(restaurant_id) desc"""
    mycursor.execute(sql)
    result = mycursor.fetchall()
    res = []
    for item in result:
        d = dict()
        d['name'] = item[1]
        d['res_id'] = item[0]
        res.append(d)
    print(res)
    return render_template('searchR.html', restaurants=res)
@app.route('/permission/<data1>')
def permission(data1):
    session["data1"] = data1
    return render_template('search.html')


@app.route('/user/<Account>')
def user(Account):
    sql = """select * from User where Account = """ + str(Account)
    mycursor.nextset()
    mycursor.execute(sql)
    result = mycursor.fetchall()
    user = []
    for item in result:
        d = dict()
        d['Account'] = item[0]
        d['name'] = item[1]
        d['gender'] = item[2]
        d['class'] = item[3]
        user.append(d)
    if user == []:
        return False
    mycursor.nextset()
    sql2 = """select * from Review join Restaurant on Review.business_id = Restaurant.restaurant_id where Account = """ + str(Account)
    mycursor.execute(sql2)
    result = mycursor.fetchall()
    print(result)
    review = []
    for item in result:
        d = dict()
        d['review_id'] = item[0]
        d['Account'] = item[1]
        d['date'] = item[3]
        d['Text'] = item[4]
        d['Rating'] = item[5]
        d['restaurant_id'] = item[6]
        d['name'] = item[7]
        d['web'] = item[10]
        review.append(d)
    return render_template('user_extend.html', user = user, reviews = review)




@app.route('/restaurant/add_comment/<data>', methods=['GET', 'POST'])
def add_comment(data):
    if request.method == 'POST':
        if session.get("data1") is None:
            return "<script>alert('Not logged in, you can comment after logging in！');window.location.href='/'</script>"
        text = request.form.get('text')
        rating = request.form.get('rating')
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = """INSERT INTO Review(Account,business_id,date,Text,Rating) VALUES(%s,%s,%s,%s,%s)"""
        record = [(session.get("data1"), data, date, text, rating)]
        mycursor.executemany(sql, record)
        mydb.commit()
        print(date)
        return "<script>alert('successfully revised！');window.location.href='/restaurant/"+data+"'</script>"

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
    name = request.form['name']
    gender = request.form['gender']
    fav_class = request.form['fav_class']
    sql = """INSERT INTO User(Account, User_Name, Gender, Favoriate_class, Password) VALUES(%s,%s,%s,%s,%s)"""
    record = [(account, name, gender, fav_class, pwd)]
    mycursor.executemany(sql, record)
    mydb.commit()
    response = {
        "data": {
            "values": 1
        }
    }
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
    print(id)
    delete_query = "DELETE FROM Review WHERE review_id = '" + id+"'"
    mycursor.execute(delete_query)
    mydb.commit()
    response = {
        "data": {
            "values": 1
        }
    }
    print(1111)
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

@app.route('/call', methods=['POST'])
def call():
    account = request.form['id']
    print(account)
    sql0 = """Select avg(Rating) From  User natural join Review where Account =""" + str(account)+""" Group by Account"""
    mycursor.execute(sql0)
    result = mycursor.fetchall()
    if result != []:
        rate = float(result[0][0])
    else:
        rate = 5
    sql = """call Friend(""" + str(account) +',' + str(rate)+')'
    sql = """call Friend(%s,%s); """%(account,rate)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(result)
    df = pd.DataFrame(result).head(row_limit)

    def make_valid(v):
        if v != v:
            return None
        else:
            return v

    column_labels = ['Account','Name', 'Gender','Favorite_Class', 'Type']
    per_col_values = [
        [make_valid(value) for value in df[col]]
        for col in df.columns[1:]
    ]

    response = {
        "query_string": sql,
        "data": {
            "labels": [[col] for col in column_labels],
            "values": per_col_values
        }
    }
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10051, use_debugger=True, use_reloader=True)
