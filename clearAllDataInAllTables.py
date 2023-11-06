import sqlite3
# Connects to database
# The .db file is created automatically if it does not exist 
con = sqlite3.connect('my-db.db')



con.execute("DELETE FROM User;")
con.execute("DELETE FROM Hobby;")
con.execute("DELETE FROM Major;")
con.execute("DELETE FROM ChatRoom;")
con.execute("DELETE FROM Message;")
con.execute("DELETE FROM Match;")
con.execute("DELETE FROM Restaurant;")
con.execute("DELETE FROM Timeslot;")






con.commit()
con.close()