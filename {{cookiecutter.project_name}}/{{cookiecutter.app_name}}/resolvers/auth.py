import uuid

from graphene import ObjectType, Field, String, Schema, Boolean

from {{cookiecutter.app_name}}.schemas.profile import ProfileSchema
from {{cookiecutter.app_name}}.utils.database import profile_collections
from {{cookiecutter.app_name}}.utils.email import send_confirmation_email
from {{cookiecutter.app_name}}.utils.passwords import decrypt_password, encrypt_password
from {{cookiecutter.app_name}}.utils.webtokens import decode_token


class Query(ObjectType):
    """
    Defines the query types
    """
    login = Field(ProfileSchema, username=String(), password=String())
    register = Field(ProfileSchema,
                     email=String(),
                     password=String(),
                     username=String(),
                     name=String())

    profile = Field(ProfileSchema, required=True, token=String(required=True))
    profile_confirmation = Boolean(uniqid=String(), email=String())
    confirm_email_resend = Boolean(email=String())

    def resolve_login(self, info, username, password):
        """
        Login resolver
        :param info:
        :param username: username to lookup
        :param password: password to hash against
        :return: the profile fetched from mongoDB
        """
        profile = profile_collections.find_one({"username": username})
        if profile:
            if decrypt_password(password, profile["password"]):
                return profile
            else:
                raise Exception("The password is incorrect. Please try again.")
        else:
            raise Exception(
                "The profile by the username {}, was not found in the system.".format(
                    username))

    def resolve_register(self, info, email, password, username, name):
        """
        Register resolver
        :param info:
        :param email: email to register with
        :param password: password to hash
        :param username: username to act as a primary key for lookups
        :param name: a name
        :return:
        """
        print(email, password, username, name)
        if profile_collections.find_one({"username": username}):
            raise Exception(
                "Profile with that username currently exists in the system.")
        else:
            generated_uuid = str(uuid.uuid1())
            profile_payload = {
                "email": email.lower(),
                "password": encrypt_password(password=password),
                "username": username,
                "name": name,
                "is_verified": {
                    "status": False,
                    "id": generated_uuid
                },
            }
            send_confirmation_email(email, generated_uuid)
            _id = profile_collections.insert_one(profile_payload)
            profile_payload["_id"] = _id.inserted_id
            return profile_payload

    def resolve_profile(self, info, token):
        """
        Resolves a profile given the authentication token
        :param info:
        :param token: the signed token
        :return: profile information if the token is valid
        """
        decoded = decode_token(token)
        if decoded:
            profile = profile_collections.find_one(
                {"username": decoded["username"]})
            if profile:
                return profile
            else:
                raise Exception(
                    "Couldn't find the profile with the username: {}.".format(
                        decoded["username"]))
        else:
            raise Exception("Token is invalid.")


authentication_schema = Schema(query=Query,
                               types=[ProfileSchema])
