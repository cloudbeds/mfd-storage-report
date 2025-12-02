from http import HTTPStatus
from typing import List

import jwt
from fastapi import HTTPException

from app.common.logger import logger


class TokenService:
    def __init__(self, token: str):
        if token.startswith("Bearer "):
            token = token[7:]

        self.access_token = token
        self.token = token

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token):
        try:
            self.__token = jwt.decode(
                token,
                verify=False,
                algorithms=["RS256"],
                options={"verify_signature": False},
            )
        except Exception as exception:
            logger.warning("Error decoding the token", extra={"error": str(exception)})
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, detail="Invalid access token"
            ) from exception

    def get_property_ids(self) -> List[int]:
        return [int(property) for property in self.token.get("propertyIds", [])]

    def get_user_id(self) -> int:
        return int(self.token.get("mfdUserId"))

    def get_email(self) -> str:
        return self.token.get("sub")

    def is_super_admin(self) -> bool:
        return self.token.get("isSuperAdmin", False)
