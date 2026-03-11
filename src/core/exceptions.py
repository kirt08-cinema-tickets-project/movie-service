import grpc
import logging


log = logging.getLogger(__name__)

class ServiceError(Exception):
    grpc_status = grpc.StatusCode.INTERNAL
    default_message = ""

    def __init__(self, message: str | None = None):
        if message is None:
            message = self.default_message

        super().__init__(message)
        self.message = message

        log.error(f"{self.__class__.__name__}: {message}")
