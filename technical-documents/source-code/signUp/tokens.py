""" Outlines the tokens to be used for resetting the user's password """
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """ Generates the token for validating a user's account.

    Args:
        PasswordResetTokenGenerator (PasswordResetTokenGenerator): The object
            used for generating a token when resetting the password, done to
            prevent having to rewrite functionality.
    """
    def _make_hash_value(self, user, timestamp):
        """ Generates a hash value for the token being generated.

        Args:
            self : The name of the building to calculate points for
                provided as a string for readability.
            user : The user object for which the token is being generated.
            timestamp : The time when the token was generated (salt used for
                the hash value).

        Returns:
            int: days_since: The number of days since a building has been
                checked, given as an integer.
        """
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()
