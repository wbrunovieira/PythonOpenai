import os
import openai
import dotenv

def categorizaProduto(nome_do_produto, categorias_validas):
    prompt_sistema = f"""
    voce é um categorizador de produtos.

    voce deve escolher uma categoria da lista abaixo:
    se as categorias informadas nao forem categorias validas, responda com "Nao posso ajuda lo com isso"
    ##### Lista de categorias validas
   {categorias_validas}

    #### exemplo:
    bola de futebol
    esportes
    O formato de saida deve ser apenas o nome da categoria. 
    """
    resposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": prompt_sistema
        },
        {
        "role": "user",
        "content": nome_do_produto
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    
    )
    print(resposta.choices[0].message.content)
        

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
print("Digite as categorias validas")
categorias_validas = input()
while True:
    print("Digite o nome do produto")
    nome_do_produto = input()
    categorizaProduto(nome_do_produto, categorias_validas)