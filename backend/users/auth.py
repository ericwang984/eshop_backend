

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.serializers import UserSerializer


class QuerystringJSONWebTokenAuthentication(JSONWebTokenAuthentication):
    """
    Allow jwt token to be passed in via querystring (aswell as via header),
    """
    def get_jwt_value(self, request):
        jwt = super(QuerystringJSONWebTokenAuthentication, self).get_jwt_value(request)
        if not jwt and 'jwt' in request.query_params:
            return request.query_params['jwt']
        return jwt


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.

    Example:

    def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user).data
        }

    """

    if user.is_staff:
        user_dic = UserSerializer(user).data
        user_dic['permissions'] = user.get_all_permissions()
        return {
            'token': token,
            'user': user_dic
        }

    return {
        'token': token,
        'user': UserSerializer(user).data
    }



