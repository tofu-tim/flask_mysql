from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    db = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name'] 
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def dojo_ninjas(cls, id):
        query = """
            SELECT dojos.name, ninjas.id, ninjas.first_name, ninjas.last_name, ninjas.age, ninjas.dojo_id
            FROM dojos
            LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
        """
        data = {'id': id}
        results = connectToMySQL(cls.db).query_db(query, data)
        print("Results:", results)
        
        if results:
            dojo = cls(results[0])
            dojo.ninjas = [Ninja(row) for row in results]
            return dojo
        else:
            return None
        
    # @classmethod
    # def dojo_ninjas(cls, id):
    #     query = """
    #         SELECT ninjas.id, ninjas.first_name, ninjas.last_name, ninjas.age
    #         FROM dojos
    #         LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
    #         WHERE dojos.id = %(id)s;
    #     """
    #     data = {'id': id}
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     if not results:
    #         return None 
    #     dojo = cls(results[0])
    #     dojo.ninjas = [Ninja(row) for row in results]
    #     return dojo



