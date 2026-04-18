from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class AdministratorRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name='Administrators').exists()

    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to access this page.")