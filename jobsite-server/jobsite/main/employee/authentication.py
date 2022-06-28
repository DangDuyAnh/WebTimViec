from rest_framework import exceptions

from ..user.authentication import SafeJWTAuthentication

from .models import Employee
from ..user.role import RoleID

class EmployeeJWTAuthentication(SafeJWTAuthentication):

    def authenticate(self, request):
        authed = super().authenticate(request)

        if authed is None: return None

        (user, _) = authed

        users = Employee.objects.filter(user=user)

        if not users.exists():
            raise exceptions.AuthenticationFailed('Unexpected user role')

        employee = users.first()

        #if employer.status != 1:
        #    raise exceptions.AuthenticationFailed('Unaccepted employer')

        user.role_id = RoleID.EMPLOYEE
        user.employee = employee

        return (user, None)