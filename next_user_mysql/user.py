from mysqlconnections import connectToMySQL


class User:
    def __int__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['first_name']
        self.updated_at = data['first_name']


    @classmethod
    def get_all(cls):    #selecting the table in my first_user file in SQL
        query = "SELECT * FROM users;"
        results = connectToMySQL('first_user').query_db(query)
        users = []
        for user in results:
            users.append(cls)
        return users
  
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('first_user').query_db( query, data )
