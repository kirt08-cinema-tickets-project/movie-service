import grpc
from src.core.exceptions import ServiceError


class InvalidDataException(ServiceError):
    grpc_status = grpc.StatusCode.FAILED_PRECONDITION
    default_message = "No one or Several amount of movies with such slug"