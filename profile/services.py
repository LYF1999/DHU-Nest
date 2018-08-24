from django.contrib.auth.models import User


class ProfileService:

    @classmethod
    def get_profile_by_user(cls, user):
        try:
            return user.profile
        except User.profile.RelatedObjectDoesNotExist:
            return None
