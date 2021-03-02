from datetime import datetime, timedelta
from typing import Union, Tuple, Dict, Any

from django.conf import settings
import usecases.example as example_uc

import jwt

from repository.models import Example
from server.views.requests.example import LoginData
from usecases.viewmodel.example import ExampleJWTTokenVM


def basic_get(request, login_data: LoginData) -> Union[Tuple[int, Dict[str, str]], ExampleJWTTokenVM]:
    data = example_uc.login(login_data)
    if data is None:
        return 404, {'message': "User Not Found"}
    return example_uc.generate_token(data.id)


def auth_get(request) -> Example:
    auth_data: Example = request.auth
    return auth_data
