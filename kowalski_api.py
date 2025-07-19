from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from kowalski import Agent, client, kowalski_system_prompt

app = FastAPI()

# Permitir requisições do seu front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Troque para o domínio do seu front-end em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

kowalski_agent = Agent(client=client, system_prompt=kowalski_system_prompt)

@app.post("/chat")
async def chat_endpoint(msg: Message):
    response = kowalski_agent(msg.message)
    return {"response": response} 