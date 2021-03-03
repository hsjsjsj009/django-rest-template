from ninja.security import HttpBearer
import jwt
from repository.example import get_by_id
from django.conf import settings

from repository.models import Example


class JWTBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, key=settings.JWT['KEY'], algorithms=settings.JWT['ALG'])
            data = get_by_id(payload['user_id'])
            return data
        except(jwt.DecodeError, jwt.ExpiredSignatureError,Example.DoesNotExist):
            return None
