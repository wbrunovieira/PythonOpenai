import tiktoken

codificador = tiktoken.encoding_for_model("gpt-3.5-turbo")

lista_de_tokens = codificador.encode("voce e um categorizador de produtos.")
print(lista_de_tokens)
print(len(lista_de_tokens))
custo_entrada = (len(lista_de_tokens)/1000) * 0.00002
print(custo_entrada)