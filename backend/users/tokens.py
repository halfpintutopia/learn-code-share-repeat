from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class TokenGenerator(PasswordResetTokenGenerator):
    """
    Generates a token that will be used to verify a user's email address
    """

    def _make_hash_value(self, user, timestamp):
        """
        Creates a hash value using the user's primary key, timestamp, and whether the user's email is verified
        :param user: The user whose email is being verified
        :param timestamp: The timestamp that the email verification was created
        :return: A hash value that is used to verify the user's email
        """
        return (
                text_type(user.pk) + text_type(timestamp) +
                text_type(user.user_profile.is_email_verified)
        )


account_activation_token = TokenGenerator()
