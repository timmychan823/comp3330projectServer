import sqlite3
# Connects to database
# The .db file is created automatically if it does not exist 
con = sqlite3.connect('my-db.db')



con.execute("DROP TABLE User;")
con.execute("DROP TABLE Hobby;")
con.execute("DROP TABLE Major;")
con.execute("DROP TABLE ChatRoom;")
con.execute("DROP TABLE Message;")
con.execute("DROP TABLE Match;")
con.execute("DROP TABLE Restaurant;")
con.execute("DROP TABLE Timeslot;")






con.commit()
con.close()