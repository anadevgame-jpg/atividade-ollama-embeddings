"""
Atividade - Tópicos Específicos em Sistemas para Internet I
Geração de embeddings com o Ollama rodando localmente.

O script conecta no Ollama, manda uma frase simples para um modelo
de embeddings e mostra o vetor gerado (tamanho e primeiros valores).
"""

import ollama

# Modelo de embeddings usado
MODELO = "mxbai-embed-large"

# Texto que vai virar vetor
TEXTO = "O Instituto Federal oferece o curso de Sistemas para Internet."


def gerar_embedding(texto, modelo):
    """Envia o texto para o Ollama e devolve o vetor de embeddings."""
    resposta = ollama.embed(model=modelo, input=texto)
    # A resposta traz uma lista de vetores (um para cada texto enviado).
    # Como mandei só um texto, pego o primeiro.
    return resposta["embeddings"][0]


def mostrar_resumo(vetor, quantidade=10):
    """Mostra o tamanho do vetor e alguns valores do começo."""
    print(f"Tamanho do vetor: {len(vetor)} dimensões")
    print(f"Primeiros {quantidade} valores:")
    for i, valor in enumerate(vetor[:quantidade]):
        print(f"  [{i}] {valor:.6f}")


def main():
    print("Conectando ao Ollama local...")
    print(f"Modelo: {MODELO}")
    print(f"Texto: {TEXTO}\n")

    try:
        vetor = gerar_embedding(TEXTO, MODELO)
    except ConnectionError:
        print("Erro: não consegui conectar no Ollama.")
        print("Verifique se ele está rodando (comando: ollama serve).")
        return
    except ollama.ResponseError as erro:
        print(f"Erro do Ollama: {erro.error}")
        print(f"Verifique se o modelo foi baixado (comando: ollama pull {MODELO}).")
        return

    print("Embedding gerado com sucesso!\n")
    mostrar_resumo(vetor)


if __name__ == "__main__":
    main()
