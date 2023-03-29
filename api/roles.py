from rest_framework_roles.roles import is_user, is_anon, is_admin
from users.models import AppUser


def is_author(request, view):
    return is_user(request, view) and request.user.role == AppUser.AUTHOR


def is_reader(request, view):
    return is_user(request, view) and request.user.role == AppUser.READER


ROLES = {
    # Django out-of-the-box
    'admin': is_admin,
    'user': is_user,
    'anon': is_anon,

    'is_author': is_author,
    'is_reader': is_reader,
}