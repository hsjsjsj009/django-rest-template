from ninja import Router
from ninja.responses import codes_4xx

from server.response import Message
from server.views.example import basic_get, auth_get
from usecases.viewmodel.example import ExampleJWTTokenVM, ExampleDataVM

router = Router()

router.post(path="/", auth=None, response={200: ExampleJWTTokenVM, codes_4xx: Message})(basic_get)
router.get(path="/", response=ExampleDataVM)(auth_get)
