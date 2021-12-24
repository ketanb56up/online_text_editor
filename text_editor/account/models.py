import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models, IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class User(AbstractUser):
    """
    User
        A class for creating user with django`s auth models with
        inheriting the AbstractUser for add more extra class attributes
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, verbose_name="User ID", editable=False
    )
    contact = models.PositiveIntegerField(
        max_length=12, unique=True, verbose_name="Mobile Number", null=True
    )
    user_agent = models.CharField(verbose_name="User Agent", max_length=50)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    created_at = models.DateTimeField(default=now())
    updated_at = models.DateTimeField(default=now())

    def __str__(self):
        return self.username


class UserCredit(models.Model):
    """
    UserCredit
        A class for creating a user`s object for storing the earned
        credits by user.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, verbose_name="ID", editable=False
    )
    user = models.ForeignKey(
        User, unique=True, on_delete=models.CASCADE, verbose_name="User"
    )
    unique_browser = models.BooleanField(default=False, null=False)
    total_credit = models.PositiveIntegerField(default=0, verbose_name="Total Credits")

    created_at = models.DateTimeField(default=now())
    updated_at = models.DateTimeField(default=now())


class MachineInformation(models.Model):
    """
    MachineInformation
        Class is created for storing a unique key/address of
        a client side`s browser or machine
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, verbose_name="ID", editable=False
    )
    user_agent = models.CharField(
        default="user_agent", unique=True, verbose_name="User Agent", max_length=50
    )


@receiver(post_save, sender=User)
def create_credits(sender, instance, created, **kwargs):
    """
    Using post signal for creating user`s credit objects
    and creating MachineInformation's object
    """
    user_agent = MachineInformation.objects.filter(
        user_agent=instance.user_agent
    ).first()

    if created or not instance.is_staff:
        try:
            if user_agent is None:
                UserCredit.objects.create(
                    total_credit=5, user=instance, unique_browser=True
                )
                MachineInformation.objects.create(user_agent=instance.user_agent)
            else:
                UserCredit.objects.create(total_credit=0, user=instance)
        except IntegrityError:
            raise "Duplicate Data not allowed"
