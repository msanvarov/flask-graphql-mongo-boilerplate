import string
import pytest

from random import choice
from {{cookiecutter.app_name}}.utils.database import remove_profile

def test_root_endpoint(client):
    """
    / endpoint (GET)
    Fetches root route
    """
    res = client.get("/")
    assert res.status_code == 200, "failed get request"
    assert res.data == b"GraphQL server is listening on /graphql"


def test_registration(graphql):
    """
    /graphql endpoint (POST)
    Registers a test account
    """
    query = {"query": """{
      register(email: "test@test.com", password: "password", username: "test", name: "test") {
        email
        token
      }
    }"""}
    res = graphql(query)
    assert res.status_code == 200
    assert res.json["data"]


def test_profile_exists(graphql):
    """
    /graphql endpoint (POST)
    Tries to re-register the same account
    """
    query = {"query": """{
      register(email: "test@test.com", password: "password", username: "test", name: "test") {
        email
        token
      }
    }"""}
    res = graphql(query)
    assert len(res.json["errors"]) == 1
    assert res.json["errors"][0][
               "message"] == "Profile with that username currently exists in the system."


def test_login(graphql):
    """
    /graphql endpoint (POST)
    Login's to created account
    """
    query = {"query": """
    {
      login(username: "test", password: "password") {
        email
        token
      }
    }
    """}
    res = graphql(query)
    assert res.status_code == 200


def test_profile(graphql):
    """
    /graphql endpoint (POST)
    Token authentication to fetch profile data
    """
    query_profile = {"query": """
       {
         login(username: "test", password: "password") {
           email
           token
         }
       }"""}
    res = graphql(query_profile)
    token = res.json['data']['login']['token']
    query = {
        "query": "{profile(token: \"" + token + "\") { email name username " \
                                                "isVerified }}"}
    res = graphql(query)
    assert res.status_code == 200


def test_login_wrong_password(graphql):
    """
    /graphql endpoint (POST)
    Tries to login with false credentials
    """
    query = {"query": """
      {
        login(username: "test", password: "wrong") {
          email
          token
        }
      }
      """}
    graphql(query)
    with pytest.raises(Exception) as exception:
        assert exception == "The password is incorrect. Please try again."


def test_long_no_profile(graphql):
    """
    /graphql endpoint (POST)
    Deletes and tries to fetch deleted account
    """
    test_remove_created_account()
    query = {"query": """"
    {
      login(username: "test", password: "I don't exist") {
        email
        token
      }
    }
    """}
    graphql(query)
    with pytest.raises(Exception) as exception:
        assert exception == "The profile by the username test, was not found in the system."


def test_user_wrong_token(graphql):
    """
    Test trying to authenticate with an unsigned token.
    """
    def random(length=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(choice(letters) for _ in range(length))

    query = {"query": "{profile(token: \"" + random(
        50) + "\") { email name username isVerified }}"}
    graphql(query)
    with pytest.raises(Exception) as exception:
        assert exception == "Token is invalid."


def test_remove_created_account():
    """
    Drop the test profile from database
    """
    assert remove_profile("test")
