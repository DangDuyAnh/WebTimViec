from rest_framework import exceptions

from ..user.authentication import SafeJWTAuthentication

from .models import Employer
from ..user.role import RoleID

class EmployerJWTAuthentication(SafeJWTAuthentication):

    def authenticate(self, request):
        authed = super().authenticate(request)

        if authed is None: return None

        (user, _) = authed

        users = Employer.objects.filter(user=user)

        if not users.exists():
            raise exceptions.AuthenticationFailed('Unexpected user role')

        employer = users.first()

        if employer.status != 1:
            raise exceptions.AuthenticationFailed('Unaccepted employer')

        user.role_id = RoleID.EMPLOYER
        user.employer = employer

        return (user, None)