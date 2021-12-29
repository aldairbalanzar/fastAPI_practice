def user_entity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "dark_mode": user["dark_mode"]
    }

def all_users_entity(collection) -> list:
    return [user_entity(user) for user in collection]