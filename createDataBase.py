import sqlite3
# Connects to database
# The .db file is created automatically if it does not exist 
con = sqlite3.connect('my-db.db')

# Creates table
con.execute("""CREATE TABLE IF NOT EXISTS User (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    display_name TEXT NOT NULL,
    email_address TEXT NOT NULL,
    password TEXT NOT NULL,
    year INTEGER,
    profile_pic INTEGER DEFAULT 0
);""")

con.execute("""CREATE TABLE IF NOT EXISTS Hobby (
    user_id INTEGER NOT NULL,
    hobby TEXT NOT NULL
);""")

con.execute("""CREATE TABLE IF NOT EXISTS Major (
    user_id INTEGER NOT NULL,
    major VARCHAR NOT NULL
);""")

con.execute("""CREATE TABLE IF NOT EXISTS ChatRoom (
    chatroom_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    owner1_id INTEGER NOT NULL,
	owner2_id INTEGER NOT NULL
);""")

con.execute("""CREATE TABLE IF NOT EXISTS Message (
    chatroom_id INTEGER NOT NULL,
	sent_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	message_content TEXT NOT NULL,
    sender_id INTEGER NOT NULL
);""")

con.execute("""CREATE TABLE IF NOT EXISTS Match (
    initiator_id INTEGER NOT NULL,
	restaurant_name TEXT NOT NULL,
	proposed_timeslot_of_match TEXT NOT NULL
);""")


con.execute("""CREATE TABLE IF NOT EXISTS Restaurant (
    restaurant_name TEXT NOT NULL,
	restaurant_location TEXT NOT NULL
);""")

con.execute("""CREATE TABLE IF NOT EXISTS Timeslot (
    restaurant_name TEXT NOT NULL,
	timeslot TEXT NOT NULL
);""")



con.commit()
con.close()

