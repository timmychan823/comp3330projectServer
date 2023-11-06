import sqlite3
# Connects to database
# The .db file is created automatically if it does not exist 
con = sqlite3.connect('my-db.db')



# insert test data
testUserData = [["David Lau","davidlau@connect.hku.hk","123456",3,0],["Tammy Chan","tammychan@connect.hku.hk","654321",3,0]]
for user in testUserData:
    insertQuery = f"INSERT INTO User (display_name,email_address,password,year,profile_pic) values (\"{user[0]}\",\"{user[1]}\",\"{user[2]}\",{user[3]},{user[4]});" 
    con.execute(insertQuery)


testHobbyData = [[1,"Tennis"],[2,"Movies"]]
for userHobby in testHobbyData:
    insertQuery = f"INSERT INTO Hobby (user_id,hobby) values ({userHobby[0]},\"{userHobby[1]}\");" 
    con.execute(insertQuery)

testMajorData = [[1,"BBA (A&F)"],[2,"QFin"]]
for userMajor in testMajorData:
    insertQuery = f"INSERT INTO Major (user_id,major) values ({userMajor[0]},\"{userMajor[1]}\");" 
    con.execute(insertQuery)

testChatRoomData = [[1,2]]
for ChatRoom in testChatRoomData:
    insertQuery = f"INSERT INTO ChatRoom (owner1_id,owner2_id) values ({ChatRoom[0]},{ChatRoom[1]});" 
    con.execute(insertQuery)

testMessageData = [[1,"Hello",1]]
for Message in testMessageData:
    insertQuery = f"INSERT INTO Message (chatroom_id,message_content,sender_id) values ({Message[0]},\"{Message[1]}\",{Message[2]});" 
    con.execute(insertQuery)

testMatchData = [[1,"CYM canteen","1130-1230"],[2,"CYM canteen","1130-1230"]]
for Match in testMatchData:
    insertQuery = f"INSERT INTO Match (initiator_id,restaurant_name,proposed_timeslot_of_match) values ({Match[0]},\"{Match[1]}\",\"{Match[2]}\");" 
    con.execute(insertQuery)

testRestaurantData = [["CYM canteen","4/F, Chong Yuet Ming Cultural Centre"],["SU canteen","4/F Haking Wong Building (Podium)"]]
for Restaurant in testRestaurantData:
    insertQuery = f"INSERT INTO Restaurant (restaurant_name,restaurant_location) values (\"{Restaurant[0]}\",\"{Restaurant[1]}\");" 
    con.execute(insertQuery)

testTimeslotData = [["CYM canteen","1130-1230"],["CYM canteen","1230-1330"],["CYM canteen","1330-1430"],["CYM canteen","1430-1530"]]
for Timeslot in testTimeslotData:
    insertQuery = f"INSERT INTO Timeslot (restaurant_name,timeslot) values (\"{Timeslot[0]}\",\"{Timeslot[1]}\");" 
    con.execute(insertQuery)


con.commit()
con.close()