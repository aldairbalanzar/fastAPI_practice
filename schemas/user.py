def user_entity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "first_name": user["_first_name"],
        "last_name": user["_last_name"],
        "email": user["_email"]
    }

def all_users_entity(collection) -> list:
    return [user_entity(user) for user in collection]