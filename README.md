# 🇧🇷💸 Apertô – Consultor Inteligente de Extratos com LLM Local

## 📌 Sobre o Projeto

O **Apertô** é um agente financeiro que analisa extratos bancários em CSV utilizando um modelo de linguagem rodando localmente via **Ollama (llama3.2)**.

Ele atua como um consultor dos seus extratos, permitindo que você faça perguntas sobre seu histórico financeiro e receba respostas:

- Baseadas exclusivamente nos dados fornecidos
- Sem alucinações
- Sem extrapolações
- Com linguagem formal e profissional

---

## 🎯 Objetivo

Transformar extratos bancários brutos em respostas inteligentes e confiáveis através de um LLM local.

O agente é capaz de responder perguntas como:

- Quanto gastei no mês?
- Quais foram meus maiores gastos?
- Existe aumento nas despesas?
- Quais transações aconteceram em determinado período?
- Tenho recorrência em algum tipo de gasto?

Sempre com base exclusiva nos dados carregados.

---

## 🧠 Funcionamento do Sistema

### 🔄 Fluxo da Aplicação

1. A aplicação inicia via **Streamlit**
2. Todos os arquivos `.csv` dentro da pasta `data/` são lidos automaticamente
3. Os dados são convertidos para texto estruturado
4. O conteúdo é injetado no contexto do prompt
5. A pergunta do usuário é enviada ao modelo `llama3.2` via Ollama
6. O modelo retorna a resposta com base apenas nos extratos

---

## 📂 Leitura Automática dos Dados

O sistema:

- Percorre a pasta `data/`
- Lê todos os arquivos `.csv`
- Converte cada DataFrame em string
- Consolida tudo em um único bloco de contexto

Isso permite múltiplos extratos (ex: Nov/2025 a Jan/2026).

---

## 🤖 Modelo Utilizado

- LLM rodando localmente via **Ollama**
- Modelo: `llama3.2`

Endpoint utilizado:

