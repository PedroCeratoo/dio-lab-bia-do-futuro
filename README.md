# 🇧🇷💸Apertô - Agente de Controle Financeiro do Cotidiano com IA Generativa

## Contexto

No Brasil, controlar o dinheiro não é opcional — é necessidade.

Entre boletos, PIX, cartão de crédito, mercado e imprevistos, o brasileiro vive fazendo conta para garantir que o mês feche no azul.

Este projeto propõe a criação de um **Agente Financeiro Inteligente**, focado no cotidiano, que utiliza IA Generativa para analisar extratos bancários e transformar dados brutos em:

- 📊 Resumo claro de gastos  
- 🧾 Organização automática por categorias  
- ⚠️ Alertas sobre excessos e padrões recorrentes  
- 📅 Projeção de fechamento do mês  
- 💡 Recomendações práticas e realistas  

> O objetivo não é sugerir investimentos, mas ajudar o usuário a organizar o presente antes de planejar o futuro.

---

## 🎯 Problema que o Projeto Resolve

Muitas pessoas:

- Não sabem exatamente quanto gastam por categoria  
- Descobrem que o dinheiro acabou apenas no fim do mês  
- Não têm clareza sobre gastos fixos e variáveis  
- Vivem no “acho que deu”  

O agente resolve isso transformando o extrato bancário em:

- Visão consolidada  
- Diagnóstico financeiro mensal  
- Alertas inteligentes  
- Recomendações acionáveis  

---

## 📦 O Que Você Deve Entregar

### 1️⃣ Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:**  
  Organização financeira mensal a partir da análise de extrato bancário.

- **Problema Resolvido:**  
  Falta de clareza sobre fluxo de caixa pessoal.

- **Persona e Tom de Voz:**  
  Linguagem simples, brasileira, próxima e levemente bem-humorada, mantendo responsabilidade.  
  Exemplo:  
  > “Seu gasto com delivery já virou assinatura mensal, hein 👀”

- **Arquitetura:**  
  - Upload de extrato (CSV)  
  - Processamento e categorização das transações  
  - Análise via LLM  
  - Geração de diagnóstico e recomendações  

- **Segurança:**  
  - Nunca inventar valores  
  - Responder apenas com base nos dados fornecidos  
  - Indicar quando não houver informação suficiente  

📄 `docs/01-documentacao-agente.md`

---

### 2️⃣ Base de Conhecimento

Utilize os dados disponíveis na pasta `data/`:

| Arquivo | Formato | Descrição |
|----------|----------|------------|
| `extrato.csv` | CSV | Histórico de transações do usuário |
| `categorias.json` | JSON | Regras para categorização automática |
| `perfil_usuario.json` | JSON | Informações básicas do usuário (opcional) |

O foco é a análise comportamental de gastos, não produtos financeiros.

📄 `docs/02-base-conhecimento.md`

---

### 3️⃣ Prompts do Agente

Documente os prompts que definem o comportamento do agente:

- **System Prompt**
  - Proibido inventar dados  
  - Sempre basear respostas no extrato  
  - Linguagem clara e acessível  
  - Recomendações práticas e objetivas  

- **Exemplos de Interação**
  - “Quanto eu gastei com alimentação este mês?”  
  - “Estou gastando muito com delivery?”  
  - “Se continuar assim, vou fechar no vermelho?”  
  - “Quais são meus gastos fixos?”  

- **Tratamento de Edge Cases**
  - Extrato incompleto  
  - Dados duplicados  
  - Valores inconsistentes  
  - Perguntas fora do escopo financeiro  

📄 `docs/03-prompts.md`

---

### 4️⃣ Aplicação Funcional

Desenvolva um protótipo funcional:

- Interface simples (ex: Streamlit)  
- Upload de extrato em CSV  
- Processamento automático das transações  
- Integração com LLM  
- Geração de resumo financeiro e diagnóstico mensal  

📁 `src/`

---

### 5️⃣ Avaliação e Métricas

Descreva como você avalia a qualidade do agente.

**Métricas sugeridas:**

- 📊 Precisão nos cálculos  
- 🔒 Zero alucinação financeira  
- 🧠 Coerência com os dados fornecidos  
- 📉 Capacidade de identificar padrões reais  
- 🧾 Clareza das recomendações  

📄 `docs/04-metricas.md`

---

### 6️⃣ Pitch

Grave um pitch de até 3 minutos apresentando:

- Qual problema real do brasileiro o agente resolve?  
- Como ele transforma extrato em inteligência?  
- Por que essa solução é útil no dia a dia?  
- Qual o diferencial (linguagem próxima + foco no cotidiano)?  

📄 `docs/05-pitch.md`

---

## 🛠 Ferramentas Sugeridas

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | ChatGPT, Gemini, Claude, Copilot, Ollama |
| **Desenvolvimento** | Streamlit, Gradio, Google Colab |
| **Orquestração** | LangChain, LangFlow, CrewAI |
| **Diagramas** | Mermaid, Draw.io, Excalidraw |

---

## 🗂 Estrutura do Repositório

