"""
module for admin panel register models here by inheriting Django's
account models (User, UserCredit, MachineInformation)
"""

from django.contrib import admin

from .models import User, UserCredit, MachineInformation

# Register models for admin panel
admin.site.register(User)
admin.site.register(UserCredit)
admin.site.register(MachineInformation)
