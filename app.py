import flask

from flask import Flask
import sqlite3

app=Flask(__name__)

#with sqlite3.connect("new.db") as conn:
#	cursor=conn.cursor()
#	cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")
#	cursor.execute("INSERT INTO population VALUES ('New York City', 'NY', 820000) ")



@app.route('/<my_string>')
def hello_world(my_string):
	return "Hello %s" % (my_string)


@app.route('/int/<int:my_int>')
def hello_coffee(my_int):
	return "I will have %s coffees, please" % (my_int)


@app.route('/float/<float:my_float>')
def hello_coffee_sql(my_float):
	rows=[]
	with sqlite3.connect("new.db") as conn:
		cursor = conn.cursor()
		for row in cursor.execute("SELECT * from population"):
			rows.append(row)
	
	return "I will have %s coffees, please, see rows %s" % (my_float, str(rows))



if __name__=='__main__':
	app.run(debug=True)
