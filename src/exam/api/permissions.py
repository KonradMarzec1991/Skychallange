from rest_framework.permissions import BasePermission
from users.models import MyUser


class IsLecturer(BasePermission):

    def has_permission(self, request, view):

        """
        First try/except check is only for development purposes. Admin user do not have 'owner' attribute.
        """

        try:
            id = request.data['owner']
        except:
            return True

        try:
            myuser = MyUser.objects.get(id=id)
        except:
            return False
        return myuser.is_lecturer == True
