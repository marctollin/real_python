import sqlite3

with sqlite3.connect("blog.db") as connection:

	c = connection.cursor()

	c.execute(""" CREATE TABLE posts (title TEXT, post TEXT ) """)

	c.execute("""INSERT INTO posts VALUES("good", "I\'m good.") """)

	c.execute("""INSERT INTO posts VALUES ("excellent", "I\'m excellent.") """)

	c.execute("""INSERT INTO posts VALUES ("okay", "I\'m okay.") """)

