from django.contrib.auth.models import Permission
from django.core.management.base import BaseCommand

from core.constant import ADMIN, CLIENT, GROUPS
from core.utils import get_group
from user.models import UsrUser


class Command(BaseCommand):
    help = "Seed the database for superuser."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")
        parser.add_argument("--group", type=str, help="Group", required=False)

    def handle(self, *args, **options):
        """
        Handle the command execution.

        :param args: Command arguments.
        :param options: Command options.
        """
        self.stdout.write("Seeding data...")
        mode = options["mode"]
        seed_functions = {
            "create_superuser": create_superuser,
            "assign_permissions_to_group": assign_permissions_to_group,
        }
        seed_function = seed_functions.get(mode)
        if seed_function:
            seed_function(self.stdout, options)
        else:
            self.stdout.write("Invalid Mode!")
        self.stdout.write("Done.")


def get_admin_group():
    """
    Get the admin group.

    :return: Admin group.
    """
    return get_group(GROUPS[ADMIN])


def give_all_permissions_to_admin():
    """
    Give all permissions to the admin group.
    """
    admin_group = get_admin_group()
    permissions = Permission.objects.all()
    admin_group.permissions.set(permissions)


def create_superuser(stdout, options):  # noqa
    """
    Create a superuser with necessary details and permissions.

    :param stdout: Command output stream for logging.
    :param options: Additional command options.
    """
    stdout.write("Creating Superuser...")
    admin_group = get_admin_group()
    extra_fields = {
        "created_by": "system",
        "updated_by": "system",
        "username": "Hunny Jain",
        "display_name": "Hunny Jain",
        "first_name": "Hunny",
        "last_name": "Jain",
        "is_default": True,
        "is_it_admin": True,
    }
    superuser = UsrUser.objects.create_superuser(
        "hunny1@gmail.com", "hunny", **extra_fields
    )
    superuser.groups.add(admin_group)
    stdout.write("Superuser Created.")
    give_all_permissions_to_admin()
    stdout.write("Assigned All Permissions to Superuser.")


def assign_permissions_to_group(stdout, options):
    """
    Assign permissions to a specific group.

    :param stdout: Command output stream for logging.
    :param options: Additional command options.
    """
    group = options.get("group", "").capitalize()
    if group not in GROUPS.keys():
        stdout.write("Invalid Group!")
        return

    stdout.write(f"Assigning Permissions to {group}.")
    if group == ADMIN:
        give_all_permissions_to_admin()
    elif group == CLIENT:
        pass
    stdout.write(f"Assigned All Permissions to {group}.")
