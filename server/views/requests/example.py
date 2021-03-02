from ninja import Schema


class LoginData(Schema):
    number: int
    text: str
