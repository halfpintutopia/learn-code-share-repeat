from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_bytes, force_str
from django.conf import settings

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ..serializers import UserSerializer

User = get_user_model()


class RegisterUser(APIView):
    """
    View to get and update a user's profile
    """
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        """
        Update the user's profile details and send a verification email
        """
        serializer = UserSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = serializer.save()
            user.save()

            # Send verification email
            mail_subject = _("Activate your user profile on Learn Share Code Repeat")
            message = render_to_string("email/activate.html",
                                       {
                                           "request": "request",
                                           "user": user,
                                           "domain": settings.BASE_URL,
                                           "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                                           "token": user.user_profile.email_verification_token,
                                           "username": user.username
                                       })
            email = EmailMessage(
                mail_subject,
                message,
                "info@learnsharecoderepeat.com",
                [user.email]
            )
            email.content_subtype = "html"
            email.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateUser(APIView):
    """
    Activate user account
    """

    @staticmethod
    def get(request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist
        ):
            user = None
        if user is not None and user.user_profile.email_verification_token == token:
            user.user_profile.is_email_verified = True
            user.save()
            return Response(
                {
                    "message": "Thank you for confirming your email . Now you can login to you account"
                }
            )
        else:
            return Response(
                {
                    "error": "Activation link is invalid"
                }
            )
