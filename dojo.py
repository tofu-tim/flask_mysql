from mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.zip_code = data['zip_code']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (location,zip_code) VALUES (%(location)s,%(zip_code)s);"

        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET location=%(location)s,zip_code=%(zip_code)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
