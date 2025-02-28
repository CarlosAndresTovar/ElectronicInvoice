from fastapi import FastAPI, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from db.db import session

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_tocken(user_id: str, password: str):
    return {"user_id": user_id,
            "password": password}

@app.post("/token", tags=["Credencials"])
async def get_access_tocken(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    session.add(form_data)
    session.commit()
    return form_data
