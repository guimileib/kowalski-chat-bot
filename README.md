# Chatbot Kowalski - Agente de Suporte da ASCII EJ

> Um agente de IA para responder dúvidas sobre a ASCII, desenvolvido com Python e a API de alta velocidade da Groq.

Este projeto implementa um chatbot conversacional chamado "Kowalski", projetado para ser o primeiro ponto de contato para clientes e interessados nos serviços da ASCII, a Empresa Júnior de Computação da UFU.

O objetivo do Kowalski é fornecer respostas rápidas a perguntas frequentes e redirecionar de forma eficiente as solicitações comerciais e técnicas para a equipe humana, garantindo que nenhum lead seja perdido e que a equipe possa focar em tarefas de maior valor.

## Funcionalidades Principais

*   **Respostas Instantâneas:** Fornece informações sobre a ASCII, seus serviços, estrutura e contatos com base em uma base de conhecimento pré-definida.
*   **Redirecionamento Inteligente:** Identifica automaticamente perguntas sobre orçamentos, sugestões e projetos específicos, e encaminha o usuário para os canais de contato corretos.
*   **Personalidade Definida:** Opera com a persona "Kowalski", um agente militar preciso, objetivo e com um humor sutil.
*   **Manutenção de Contexto:** Lembra do histórico da conversa atual para fornecer respostas mais coesas e naturais.
*   **Fácil de Executar:** Pode ser iniciado com um único comando no terminal.

## Tecnologias Utilizadas

*   **Linguagem:** Python 3
*   **Motor de IA:** [Groq API](https://groq.com/)
*   **Modelo de Linguagem:** Llama 3 (8B-8192)
*   **Gerenciamento de Chaves:** `python-dotenv`

## Configuração e Instalação

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```
### 2. Crie um Ambiente Virtual
python -m venv venv

#### Ativar no Windows
.\venv\Scripts\activate

#### Ativar no macOS/Linux
source venv/bin/activate
