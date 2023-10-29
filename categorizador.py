import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt_sistema = """
voce é um categorizador de produtos.

voce deve escolher uma categoria da lista abaixo:
##### Lista de categorias validas
Beleza
Bebidas
Alimentos
Bebidas
esportes
Outros

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
      "content": "bola de basquete"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  n=5
)

for i in range(0,5):
    print(resposta.choices[i].message.content)
    print("-----------------")