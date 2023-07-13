from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, NoResultFound
from starlette import status

from core.helpers.debug_message_helper import debug_message


class ServerException(HTTPException):
    def __init__(self, detail):

        match detail:
            case detail_instance if isinstance(detail_instance, IntegrityError):
                self.status_code = status.HTTP_400_BAD_REQUEST
                self.detail = debug_message(detail)

            case detail_instance if isinstance(detail_instance, NoResultFound):
                self.status_code = status.HTTP_404_NOT_FOUND
                self.detail = detail.args[0]

            case _:
                self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
                self.detail = detail

        super().__init__(status_code=self.status_code, detail=self.detail)
