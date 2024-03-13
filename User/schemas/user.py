def user_entity(item) -> dict:  #db document to dict
    return {
        "id" : str(item["_id"]),
        "name" : item["name"],
        "email" : item["email"],
        "password" : item["password"]
    }

def users_entity(entity) -> list : # to list
    return [user_entity(user) for user in entity]