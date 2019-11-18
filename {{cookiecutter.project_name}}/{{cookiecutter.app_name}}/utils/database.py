import uuid

from faker import Faker
from pymongo import MongoClient
from pymongo.results import DeleteResult

from {{cookiecutter.app_name}}.constants import CONSTANTS
from {{cookiecutter.app_name}}.utils.passwords import encrypt_password

conn = MongoClient(CONSTANTS.get("MONGO_URL"), retryWrites=False)

profile_collections = conn[CONSTANTS.get("MONGO_DB")].profiles


def mock(count: int) -> str:
    """
     Pre-populates the Mongo graphql with mock data
    :param: count the amount of fake people to generate
    :returns: an indicator that the operation has been completed
    :rtype: str
    """
    # populate data
    for i in range(count):
        fake = Faker().profile(fields=None, sex=None)
        profile_collections.insert_one({
            "email": fake["mail"],
            "password": encrypt_password("password"),
            "name": fake["name"],
            "username": fake["username"],
            "is_check": {
                "status": False,
                "id": uuid.uuid1()
            },
        })

        print("Created: {0}".format(fake["username"]))

    return "Finished populating DB"


def remove_profile(username: str) -> DeleteResult:
    """
    Removes a profile by their username from the database
    :param username: the username to remove
    :return: delete results
    """
    return profile_collections.delete_one({"username": username})


def drop() -> str:
    """
    :returns: an indicator that the operation has been completed
    :rtype: str
    """
    db_to_drop = CONSTANTS.get("MONGO_DB")
    conn.drop_database(db_to_drop)
    return "{0} has been dropped.".format(db_to_drop)
