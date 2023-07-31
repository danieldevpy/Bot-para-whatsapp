from fastapi import FastAPI, HTTPException, Request
import json
from app.models import crud


app = FastAPI()
@app.post("/requeriments")
async def open(request: Request):
    try:
        data = await request.json()
        message_group = f'*CHAMADO ABERTO NO GLPI*;Titulo: {data["title"]} Solicitante: {data["name"]}, {data["sector"]},' \
                        f' {data["unity"]};Solicitação: {data["message"]};Numero para contato: {data["number"]}'
        crud.alert_group(message_group)

        return {"message": "Requisição processada com sucesso!"}
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="JSON inválido.")