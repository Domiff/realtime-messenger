from datetime import UTC, datetime

from faker import Faker

from src.auth.schemas import CredentialsSchema, UserSchema
from src.chat.enums import ChatRole, ChatType
from src.chat.schemas import ChatIn, MemberIn, MessageIn

_faker = Faker()


def make_credentials():
    return CredentialsSchema(
        username=_faker.user_name(),
        password=_faker.password(),
        email=_faker.email(),
    ).model_dump()


def make_sub():
    return _faker.random_int(1, 100)


def make_user_schema():
    return UserSchema(
        username=_faker.user_name(),
        password=_faker.password(),
        email=_faker.email(),
        first_name=_faker.first_name(),
        last_name=_faker.last_name(),
        is_active=True,
        created_at=datetime.now(UTC),
    )


def make_chat():
    return ChatIn(name=_faker.word(), type=ChatType.GROUP).model_dump()


def make_message(chat_id: int | None = None, sender_id: int = 1):
    return MessageIn(
        text=_faker.sentence(), chat_id=chat_id, sender_id=sender_id
    ).model_dump()


def make_member(
    user_id: int = 1,
    chat_id: int | None = None,
    role: ChatRole = ChatRole.MEMBER,
):
    return MemberIn(user_id=user_id, chat_id=chat_id, role=role).model_dump()
