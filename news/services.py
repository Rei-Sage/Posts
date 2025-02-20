from django.contrib.auth import get_user_model
from news.models import CustomUser as UserModel

User: UserModel = get_user_model()