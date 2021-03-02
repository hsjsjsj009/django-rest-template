from ninja import Schema


class ExampleVM(Schema):
    id: int


class ExampleJWTTokenVM(Schema):
    token: str


class ExampleDataVM(Schema):
    integer_field: int
    text_field: str
