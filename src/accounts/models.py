import re

from django.apps import apps
from django.utils import timezone
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from main_app.mixins import ModelMixin, SoftDeleteMixinManager

# Create your models here.


class CustomUserManager(BaseUserManager, SoftDeleteMixinManager):
    use_in_migrations = True

    def _create_user(self, cell_phone, email, password, **extra_fields):
        """
        Create and save a user with the given cell_phone, email, and password.
        """
        if not cell_phone:
            raise ValueError("The given cell_phone must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        # username = GlobalUserModel.normalize_username(username)
        user = self.model(cell_phone=cell_phone, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, cell_phone, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(cell_phone, email, password, **extra_fields)

    def create_superuser(
        self, cell_phone, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(cell_phone, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, ModelMixin):
    username_validator = UnicodeUsernameValidator()
    cell_phone = models.CharField(
        max_length=10,
        unique=True,
        help_text=_(
            "Required. 10 characters or fewer. just digits and start with 9"
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that cell phone already exists."),
        },
    )
    email = models.EmailField(verbose_name="email address", unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    objects = CustomUserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "cell_phone"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    @classmethod
    def clean_cell_phone(cls, cell_phone):
        """
        Cleans and validates the cell_phone field.
        Returns:
            A cleaned cell_phone number.
        """
        string_regex = r"^9\d{9}$"
        match = re.match(string_regex, cell_phone)
        if match is None:
            raise ValidationError("the cell phone is note validated")
        else:
            return str(cell_phone)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        self.cell_phone = self.clean_cell_phone(self.cell_phone)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        else:
            return self.cell_phone
