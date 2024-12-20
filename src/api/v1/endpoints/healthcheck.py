from fastapi import APIRouter, status

from src.common.dto import HealthCheckResponseSchema


healthcheck_router = APIRouter(tags=["healthcheck"])


@healthcheck_router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=HealthCheckResponseSchema,
    response_description='Health resource',
    description='Retrieves a health status of the application',
    summary='Retrieves a health status of the application'
)
async def healthcheck_endpoint() -> HealthCheckResponseSchema:
    return HealthCheckResponseSchema(healthy=True)
