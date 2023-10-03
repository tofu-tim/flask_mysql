from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']   
        self.whole_name = self.first_name + self.last_name 

    @classmethod
    def get_all(cls):
        from flask_app.models.dojo import Dojo
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.db).query_db(query)
        ninja = []
        for u in results:
            ninja.append( cls(u) )
        return ninja

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data ={"id": id}
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s,dojo_id=%(dojo_id)s,updated_at=NOW() WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)