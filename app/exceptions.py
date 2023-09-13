from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT,
    detail = 'User already exists'


class IncorrectEmailOrPasswordException:
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = 'Incorrect Email or Password'


class TokenExpiredException:
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = 'Token expired'


class TokenAbsentException:
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = 'Token absent'


class IncorrectTokenFormatException:
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = 'Incorrect token format'


class UserIsNotPresentException:
    status_code = status.HTTP_401_UNAUTHORIZED
