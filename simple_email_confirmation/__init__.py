__version__ = '0.9'

from .models import SimpleEmailConfirmationUserMixin, EmailAddress
from .signals import (
    email_confirmed, unconfirmed_email_created, primary_email_changed,
)
