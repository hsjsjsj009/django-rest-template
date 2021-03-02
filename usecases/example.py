from datetime import datetime, timedelta
from typing import Optional

import jwt
from django.conf import settings

from repository.models import Example
import repository.example as example_repo
from server.views.requests.example import LoginData
from usecases.viewmodel.example import ExampleVM, ExampleJWTTokenVM


def login(data: LoginData) -> Optional[ExampleVM]:
    try:
        data = example_repo.get_by_integer_and_text(data.number, data.text)
        return ExampleVM(id=data.id)
    except Example.DoesNotExist:
        return None


def generate_token(user_id: int) -> ExampleJWTTokenVM:
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(minutes=settings.JWT['EXP'])
    }
    token = jwt.encode(payload, key=settings.JWT['KEY'])
    return ExampleJWTTokenVM(token=token)
