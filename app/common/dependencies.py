from http import HTTPStatus

from fastapi import Depends, Header, HTTPException
from fastapi.security import HTTPBearer

from app.common.token_service import TokenService


def authorization(
    X_PROPERTY_ID: int = Header(),
    token: str = Depends(
        HTTPBearer(
            bearerFormat="JWT",
            scheme_name="Authorization",
            description="Token",
            auto_error=False,
        )
    ),
):
    if not token:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail="Access token is missing"
        )

    token_service = TokenService(token.credentials)
    if not (
        X_PROPERTY_ID in token_service.get_property_ids()
        or token_service.is_super_admin()
    ):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Property ID provided is not authorized via access token",
        )

    return dict(property_id=X_PROPERTY_ID, token=token.credentials)
