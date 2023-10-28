import openai
import dotenv
import os

dotenv.load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.organization = os.getenv('OPENAI_ORGANIZATION')

resposta = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {
            "role": 'system',
            "content": 'Gere nome de empresas fictícias sem descrição de acordo a requisição do usuário'
            
        },
        {
            "role": 'user',
            "content": 'Gere 5 nomes de empresas'
            }
    ]
)

print(resposta)