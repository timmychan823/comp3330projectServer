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
    year INTEGER NOT NULL,
    profile_pic INTEGER
);""")

con.execute("""CREATE TABLE IF NOT EXISTS Hobbies (
    user_id INTEGER NOT NULL,
    hobby TEXT NOT NULL
);""")

con.execute("""CREATE TABLE IF NOT EXISTS Majors (
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

con.execute("""CREATE TABLE IF NOT EXISTS Timeslots (
    restaurant_name TEXT NOT NULL,
	timeslot TEXT NOT NULL
);""")

# insert test data
testData = [["Timmy","cshtimmy@connect.hku.hk","123456",3]]
for user in testData:
    print(user)
    insertQuery = f"INSERT INTO User (display_name,email_address,password,year) values (\"{user[0]}\",\"{user[1]}\",\"{user[2]}\",{user[3]});" 
    print(insertQuery)
    con.execute(insertQuery)
con.commit()
con.close()

