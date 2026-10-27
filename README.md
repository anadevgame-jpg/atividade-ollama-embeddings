# Geração de Embeddings com Ollama

Atividade da disciplina **Tópicos Específicos em Sistemas para Internet I** (TSI - IFRN Campus Natal-Zona Leste).

O objetivo é rodar o Ollama localmente e usar um script em Python para gerar o vetor de embeddings de uma frase simples.

**Aluna:** Ana Paula Dantas Ferreira

## O que o projeto faz

O script `gerar_embeddings.py` se conecta ao Ollama que está rodando na máquina, envia uma frase para o modelo `mxbai-embed-large` e mostra no terminal o tamanho do vetor gerado e os 10 primeiros valores.

## Arquivos

- `gerar_embeddings.py`: script principal
- `requirements.txt`: dependências do Python
- `README.md`: este arquivo

## Pré-requisitos

- Python 3.9 ou mais recente
- Git
- Ollama instalado

## Passo a passo para reproduzir

### 1. Instalar o Ollama

Baixe o instalador no site oficial: https://ollama.com/download

- **Windows e macOS:** é só baixar e instalar normalmente.
- **Linux:** rodar no terminal:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Para conferir se instalou:

```bash
ollama --version
```

### 2. Iniciar o Ollama

No Windows e no macOS o Ollama normalmente já fica rodando em segundo plano depois de instalado (aparece um ícone perto do relógio). Se não estiver, ou se estiver no Linux, abra um terminal e rode:

```bash
ollama serve
```

Deixe esse terminal aberto. Para testar se o serviço está ativo, abra o navegador em http://localhost:11434. Deve aparecer a mensagem `Ollama is running`.

### 3. Baixar o modelo de embeddings

Em outro terminal:

```bash
ollama pull mxbai-embed-large
```

Para ver os modelos baixados:

```bash
ollama list
```

### 4. Clonar este repositório

```bash
git clone https://github.com/anadevgame-jpg/atividade-ollama-embeddings.git
cd atividade-ollama-embeddings
```

### 5. Criar um ambiente virtual e instalar as dependências

Windows:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Linux e macOS:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 6. Executar o script

```bash
python gerar_embeddings.py
```

## Saída esperada

Algo parecido com isto (os números podem mudar um pouco):

```
Conectando ao Ollama local...
Modelo: mxbai-embed-large
Texto: O Instituto Federal oferece o curso de Sistemas para Internet.

Embedding gerado com sucesso!

Tamanho do vetor: 1024 dimensões
Primeiros 10 valores:
  [0] 0.012345
  [1] -0.034567
  ...
```

O modelo `mxbai-embed-large` gera vetores com 1024 dimensões. Escolhi esse modelo porque foi o mesmo usado nos exemplos da disciplina.

## Mudando o texto ou o modelo

Para testar outra frase ou outro modelo, é só alterar as variáveis `TEXTO` e `MODELO` no começo do arquivo `gerar_embeddings.py`. Se trocar o modelo, lembre de baixar ele antes com `ollama pull`.

## Possíveis erros

- **"não consegui conectar no Ollama"**: o serviço não está rodando. Rode `ollama serve`.
- **"model not found"**: o modelo não foi baixado. Rode `ollama pull mxbai-embed-large`.

## Referências

- Documentação do Ollama: https://github.com/ollama/ollama
- Biblioteca Python do Ollama: https://github.com/ollama/ollama-python
- Modelo mxbai-embed-large: https://ollama.com/library/mxbai-embed-large
