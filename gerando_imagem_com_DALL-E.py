import dalle

# Configurar sua chave de API do DALL-E
dalle.api_key = "chave_api"

def gerar_imagem(descricao):
    """
    Gerar uma imagem com base em uma descrição usando DALL-E.
    """
    response = dalle.text2im({
        "prompt": descricao,
        "size": "1024x1024"
    })
    
    # Salvar a imagem gerada
    imagem_gerada = response["data"][0]
    with open("imagem_gerada.png", "wb") as f:
        f.write(imagem_gerada)

# Exemplo de uso
descricao = "Um gato azul surfando."
gerar_imagem(descricao)
print("Imagem gerada e salva como 'imagem_gerada.png'.")
