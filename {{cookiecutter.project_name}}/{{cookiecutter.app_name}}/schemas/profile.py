from graphene import ObjectType, String, Boolean

from {{cookiecutter.app_name}}.utils.webtokens import encode_token


class ProfileSchema(ObjectType):
    """
    Profile Schema defining the types and relationship between Fields in your
    API.
    """
    _id = String(required=True)
    username = String(required=True)
    name = String()
    email = String()
    is_verified = Boolean(required=True)
    token = String()

    def resolve_is_verified(self, info):
        """
        Checks if the profile requesting access has the 'is_verified' status checked
        :param info: general request metadata
        """
        print(info)
        return self["is_verified"]["status"]

    def resolve_token(self, info):
        """
        Returns a web token for authentication
        :param info: general request metadata
        """
        print(info)
        return encode_token({"username": self["username"]})
