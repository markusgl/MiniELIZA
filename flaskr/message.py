from marshmallow import Schema, fields, post_load


class Message:
    def __init__(self, message_body):
        self.message_body = message_body


class MessageSchema(Schema):
    message_body = fields.Str(required=True)

    @post_load
    def make_message(self, data):
        return Message(**data)