from fastapi import APIRouter, Depends

from app.common.dependencies import authorization
from app.modules.product.service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("")
async def products(
    _: dict = Depends(authorization),
):
    return await ProductService.get_products()
