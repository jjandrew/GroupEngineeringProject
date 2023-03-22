""" Outlines the class for generating tokens for gamekeeper account activation """
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """ Returns a hash value of some of the user's details to create a unique
    token for identifying them.

    Args:
        PasswordResetTokenGenerator: The token object used to reset the user's
        password.
    """
    def _make_hash_value(self, user, timestamp):
        """ Generates a hash value for the account.

        Args:
            user: User: The User object corresponding to the user for which an
                object is being created.
            timestamp: A salt value (the current time) time make the hash more
                unique.

        Returns:
            float: A hash value which is the sum of the text type of three
                provided fields.
        """
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()
