from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
        Custom user model manager where email is the
        unique identifiers for authentication instead
        of username.
    """

    def create_user(self, first_name, last_name,  email, password, **extra_fields):
        """
            create and save a User with the given
            first name, last name, email, and password
        """
        if not email:
            raise ValueError(_('The Email is required'))
        if not first_name and last_name:
            raise ValueError(_('First and Last Name required'))

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        """
            create and save a Superuser with the given
            first name, last name, email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active=True'))

        return self.create_user(first_name, last_name, email, password, **extra_fields)
