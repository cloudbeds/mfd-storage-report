import datetime

import jwt
import pytest

from app.common.token_service import TokenService


class TestTokenService:
    tokens = (
        dict(
            firstName="Super",
            sub="super@cloudbeds.com",
            associationIds=[123],
            propertyIds=[1, 2, 3],
            mfdUserId=1,
        ),
        dict(
            firstName="Super",
            sub="super@cloudbeds.com",
            associationIds=[123],
            propertyIds=[1, 2, 3],
            mfdUserId="1",
        ),
        dict(
            firstName="Super",
            sub="super@cloudbeds.com",
            associationIds=[123],
            mfdUserId=1,
            propertyIds=[1, 2, 3],
        ),
        dict(
            firstName="Super",
            sub="super@cloudbeds.com",
            associationIds=[123],
            mfdUserId=1,
        ),
    )

    @pytest.mark.parametrize("token", tokens)
    def test_token_service(self, token):
        issued_at = datetime.datetime.now(tz=datetime.timezone.utc)
        expired_at = datetime.datetime.now(
            tz=datetime.timezone.utc
        ) - datetime.timedelta(minutes=1440)

        token["iat"] = issued_at
        token["exp"] = expired_at

        token_service = TokenService(f"Bearer {jwt.encode(token ,'token', 'HS256')}")
        assert token_service.get_user_id() == int(token.get("mfdUserId"))
        assert token_service.get_property_ids() == token.get("propertyIds", [])
        assert type(token_service.is_super_admin()) is bool
