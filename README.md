1. Activate the virtual environment first by "source venv/bin/activate" </br>
2. Create the database by "python3 createDataBase.py"</br>
3. Insert testing data by "python3 insertTestingData.py"</br>
4. Start the server by "python3 server.py"</br>
5. After starting the server, you should see the serverIPandPortNumber (not the localhost and port number), copy that and assign it to serverIPAndPort inside Constants.kt in the comp3330project repo</br>

If you want to delete all data in tables or all the tables: </br>
</t>Delete all data in tables (without deleting tables): "python3 clearAllDataInAllTables.py"</br>
</t>Delete all tables in the database: "python3 dropAllTables.py"</br>
