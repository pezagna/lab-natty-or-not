import openai

# Configurar sua chave de API do OpenAI
openai.api_key = "chave api aqui"

def gerar_texto(prompt):
    """
    Gerar texto com base em um prompt usando ChatGPT.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Exemplo de uso
prompt = "Conte uma história sobre uma aventura."
texto_gerado = gerar_texto(prompt)
print("Texto Gerado pelo ChatGPT:", texto_gerado)
