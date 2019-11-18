from flask_script import Manager

from {{cookiecutter.app_name}} import create_app
from {{cookiecutter.app_name}}.utils.database import drop, mock, remove_profile
from {{cookiecutter.app_name}}.constants import CONSTANTS

# flask manager wrapper
manager = Manager(create_app(CONSTANTS.get("APP_ENV")))


@manager.command
def drop_database():
    """
    Drops the database specified in the configuration file.
    """
    return drop()


@manager.option("-u", "--username", help="The username to delete")
def delete_profile_by_username(username: str) -> str:
    """
    Removes a profile by their username
    :param username: the username to query the database for
    :return: operation status
    """
    if remove_profile(username):
        return "Deleted {}".format(username)
    else:
        return "Failed to delete {}".format(username)


@manager.option("-c", "--count", help="The amount of fake accounts to create")
def populate_with_mock_data(count: int) -> str:
    """
    Creates mock profiles for testing.
    :param count: the amount of mock profiles to generate
    :return: operation status
    """
    if count:
        print("Preparing to create", count, "fake accounts")
        return mock(int(count))
    else:
        return mock(1)


if __name__ == "__main__":
    manager.run()
