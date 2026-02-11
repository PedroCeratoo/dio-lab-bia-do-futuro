import pandas as pd
import os
import requests
import streamlit as st
import sys


OLLAMA_URL = 
MODELO = "llama3.2"


base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, '..', 'data')



def extrair_dados_csv(pasta):
    conteudo = ""

    arquivos = [f for f in os.listdir(pasta) if f.endswith('.csv')]

    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta, arquivo)
        try:

            df = pd.read_csv(caminho_completo)


            dados_str = df.to_string(index=False)

            conteudo += f"\n--- ARQUIVO: {arquivo} ---\n{dados_str}\n"
        except Exception as e:
            conteudo += f"\nErro ao ler {arquivo}: {e}\n"

    return conteudo



extratos_brutos = extrair_dados_csv(data_path)

SYSTEM_PROMPT = """Você é o Apertô, um consultor dos seus extratos, para tirar qualquer dúvida sobre seus históricos.

OBJETIVO:
Analisar os dados bancários do cliente para fornecer insights sem alucinações.

REGRAS:
- JAMAIS dê informações que não estejam presentes nos dados fornecidos;
- JAMAIS responda a perguntas fora do tema finanças;
- Se não houver dados sobre algo, diga: "Não tenho essa informação na base";
- Use linguagem formal e profissional;
- Responda de forma sucinta e direta;
- Baseie-se exclusivamente nos extratos anexados no contexto."""

contexto = f"""
CLIENTE: Pedro
OBJETIVO: Análise de gastos e saúde financeira.
DOCUMENTOS: Extratos Nubank em formato CSV (Nov/2025 a Jan/2026)

TRANSAÇÕES EXTRAÍDAS:
{extratos_brutos}
"""


def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}"""

    data = {
        "model": MODELO,
        "prompt": prompt,
        "stream": False
    }

    try:
        r = requests.post(OLLAMA_URL, json=data)
        return r.json()['response']
    except Exception as e:
        return f"Erro ao conectar com Ollama: {e}"



st.title("🇧🇷💸 Já se Apertô?? Então entenda como foi seu histórico financeiro !!")

if pergunta := st.chat_input("Me conte sua dúvida..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))



if __name__ == "__main__":
    try:
        from streamlit.web import cli as stcli
    except ImportError:
        from streamlit import cli as stcli

    if not hasattr(sys, 'already_run_under_streamlit'):
        sys.already_run_under_streamlit = True
        sys.argv = ["streamlit", "run", __file__]
        sys.exit(stcli.main())