from fastapi import FastAPI 
from pydantic import BaseModel #cria um modelo de dados

#criando modelo de dados:
class ProdutoCriar(BaseModel):
    codigo: int
    nome: str
    qtd: int
    preco: float

app = FastAPI()

produtos = [
    {
        'codigo': 1, #não pode repetir o codigo 
        'nome': 'violão',
        'qtd': 12,
        'preco': 500
    }
]

@app.get('/produtos') #definindo rota com get
def listagem_de_produtos(): #criando a função que vai retornar os produtos 
    return produtos

@app.get('/produtos/{codigo}') #Rota recebendo um parametro 
def listar_produto_por_codigo(codigo: int): 
    for i in produtos: #percorre a lista de produtos
        if i['codigo'] == codigo:
            return i #retona a lista de produtos 
    return 'produto não encontrado'

#Criando uma rota usuarios que retorna a frase 'Aqui sera listado os Usuarios' 
@app.get('/usuarios')
def lista_de_usurarios():
    return 'Aqui sera listado os Usuarios!'

@app.post('/produtos') #metodo post cria produtos 
def criar_produto_(dados: ProdutoCriar):
    produtos.append(
        {
            'codigo': dados.codigo,
            'nome': dados.nome,
            'qtd': dados.qtd,
            'preco': dados.preco,
        }
    )
    return 'produto criado'
