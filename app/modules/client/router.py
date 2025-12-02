from fastapi import APIRouter, Depends

from app.common.dependencies import authorization
from app.modules.client.service import ClientService

router = APIRouter(
    prefix="/clients",
    tags=["Clients"],
)


@router.get("")
async def get_clients(
    _: dict = Depends(authorization),
):
    return await ClientService.get_clients()
