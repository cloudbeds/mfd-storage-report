from datetime import datetime, timedelta, timezone

import jwt

issued_at = datetime.now(tz=timezone.utc)
expired_at = datetime.now(tz=timezone.utc) - timedelta(minutes=1440)

SUPER_ADMIN_TOKEN = jwt.encode(
    dict(
        firstName="Super",
        sub="super@cloudbeds.com",
        associationIds=[],
        propertyIds=["123", "79", "6", "22425"],
        island=1,
        mfdUserId=1,
        iat=issued_at,
        exp=expired_at,
        isSuperAdmin=True,
    ),
    "token",
    "HS256",
)
USER_TOKEN = jwt.encode(
    dict(
        firstName="User",
        sub="user@cloudbeds.com",
        associationIds=[],
        propertyIds=["123", "79", "6", "22425"],
        island=1,
        mfdUserId=1,
        iat=issued_at,
        exp=expired_at,
        isSuperAdmin=False,
    ),
    "token",
    "HS256",
)
INVALID_TOKEN = jwt.encode(
    dict(
        firstName="Super",
        sub="super@cloudbeds.com",
        associationIds=[],
        propertyIds=[],  # No property IDs
        mfdUserId=1,
        iat=issued_at,
        exp=expired_at,
    ),
    "token",
    "HS256",
)
