import hashlib
from api_models.users import GetSessionResponse, UserLoginResponse, UserLogoutResponse
from fastapi import HTTPException
from user_database import USER_DATABASE as db
from utils import users_util, sessions_util
from datetime import datetime

def user_login(username: str, password: str) -> UserLoginResponse:
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    login_result = sessions_util.is_valid_login(username, hashed_password) # returns False if invalid login

    if login_result:
        user_id, role = login_result
        session_id = sessions_util.create_session(user_id, role)
        return UserLoginResponse(session_id=session_id, message=f'User {username} successfully logged in')
    else:
        if users_util.username_exists(username):
            raise HTTPException(status_code=401, detail='Invalid password')
        raise HTTPException(status_code=401, detail='Account does not exist')

def get_all_sessions() -> list[GetSessionResponse]:
    FIELD_NAMES = ['session_id', 'user_id', 'role', 'creation_time', 'expiration_time']

    rows = db.execute_sql_read_fetchall(f"SELECT * FROM sessions")
    sessions = [dict(zip(FIELD_NAMES, row)) for row in rows]
    return [GetSessionResponse(**x) for x in sessions]

def get_session(session_id: str | None) -> GetSessionResponse:
    if session_id is None:
        raise HTTPException(status_code=401, detail='Unauthorized session')

    FIELD_NAMES = ['session_id', 'user_id', 'role', 'creation_time', 'expiration_time']

    result = db.execute_sql_read_fetchone('SELECT * FROM sessions WHERE session_id = %s',
                                 params=(session_id,))

    if result is None:
        raise HTTPException(status_code=401, detail='Unauthorized session')

    expiration_time = result[4]
    assert isinstance(expiration_time, datetime), \
        f"Expected `expiration_time` to be type `datetime`, got {type(expiration_time)}."

    if not sessions_util.is_expired_session(expiration_time):
        # Convert `datetime` instances to string before returning.
        converted = [x.isoformat() if isinstance(x, datetime) else x for x in result]
        return GetSessionResponse(**dict(zip(FIELD_NAMES, converted)))

    raise HTTPException(status_code=401, detail='Unauthorized session')

def user_logout(session_id: str) -> UserLogoutResponse:
    try:
        sessions_util.delete_session(session_id)
        return UserLogoutResponse(message=f'Session {session_id} successfully deleted')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Unable to logout user: {e}')

