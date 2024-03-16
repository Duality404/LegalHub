from time import sleep
import mysql.connector

class mysqlPool:
    def __init__(self, user, password, dbName, host="127.0.0.1", port=3306):
        self.connections = []
        self.user = user
        self.host = host  
        self.port = port  
        self.password = password  # mysql password
        self.dbName = dbName    # database to connect

    def execute(self, syntax: str)->None|list:
        count =1
        while count<5:
            try:
                if self.connections:
                    connection = self.connections.pop()
                    if connection.is_connected():
                       break 
                connection = mysql.connector.connect(user=self.user, host=self.host, port=self.port, password=self.password, database=self.dbName)
                break
            except Exception as e:
                
                count += 1
        if count>= 5:
            return None

        cursor = connection.cursor()
        data = None
        try:
            cursor.execute(syntax)
            data = cursor.fetchall()
            connection.commit()
        except Exception as e:
            print("Exception while executing query : ", e)
            return None  
        
        self.connections.append(connection)
        return data

connection = mysqlPool(user = "root", password = '011235', dbName = "legalhub" )


