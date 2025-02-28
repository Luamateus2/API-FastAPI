from decimal import Decimal
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from enum import Enum

router = APIRouter(prefix="/contas-a-pagar")

# Enum para garantir tipos válidos de "tipo"
class TipoConta(Enum):
    PAGAR = "PAGAR"
    RECEBER = "RECEBER"

# DTO de Entrada
class contaPagarReceberRequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: TipoConta  # Usando o Enum para validação

# DTO de Resposta
class contaPagarReceberResponse(contaPagarReceberRequest):
    id: int

@router.get("/", response_model=List[contaPagarReceberResponse])
def listar_contas():
    return [
        contaPagarReceberResponse(
            id=1,
            descricao="Aluguel",
            valor=1000.50,
            tipo=TipoConta.PAGAR
        ),
        contaPagarReceberResponse(
            id=2,
            descricao="Salário",
            valor=1000.50,
            tipo=TipoConta.RECEBER
        ),
    ]

@router.post("/", response_model=contaPagarReceberResponse, status_code=201)
def criar_conta(conta: contaPagarReceberRequest):
    # Geração de ID exemplo (pode ser ajustado de acordo com o banco de dados)
    novo_id = 3
    return contaPagarReceberResponse(
        id=novo_id,
        descricao=conta.descricao,
        valor=conta.valor,
        tipo=conta.tipo
    )
