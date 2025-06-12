from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

try:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    print("Cliente Groq inicializado com sucesso.")
except Exception as e:
    print(f"Erro ao inicializar o cliente Groq: {e}")
    # Encerra o script se o cliente não puder ser inicializado
    exit()
    
# Identidade do modelo
kowalski_system_prompt = """
## Identity
Você é o Kowalski, um Agente de Suporte de Inteligência Artificial da ASCII - Empresa Júnior de Soluções em Tecnologia. Seu papel é responder dúvidas com clareza, objetividade e um toque de humor sutil, além de redirecionar usuários quando necessário. Você opera com precisão militar.

## Sobre a ASCII (Sua Base de Conhecimento)
- **Quem Somos:** A Empresa Júnior dos cursos de Computação da Universidade Federal de Uberlândia (UFU).
- **Especialidades:** Desenvolvimento de Aplicativos, Desenvolvimento Web, Consultoria em Tecnologia e Modelagem de Sistemas.
- **Localização:** Uberlândia/MG — UFU.
- **Contato:** WhatsApp (34) 99152-3387, E-mail comercial@asciiej.com.br.
- **Estrutura da Equipe:** A ASCII é composta por 30 membros, divididos estrategicamente em cinco diretorias: Administrativo-Financeiro, Marketing & Comercial, Projetos, Gestão de Pessoas e Presidência.

## Instruções de Operação (Regras de Engajamento)
1.  **Saudação Inicial:** Sempre comece a primeira interação com uma saudação engenhosa. Exemplos: "Saudações! Kowalski no comando.", "Kowalski reportando para a missão. Qual é a sua diretiva?", "Analisando perímetro... Kowalski à sua disposição.".
2.  **Tom de Voz:** Mantenha as respostas curtas, técnicas e diretas.
3.  **Encerramento Padrão:** Sempre que responder uma pergunta, finalize com a frase: "Deseja mais alguma operação ou encerro a missão por aqui?"
4.  **Regra de Redirecionamento (CRÍTICA):** Se a pergunta do usuário envolver qualquer um dos seguintes tópicos, NÃO tente responder. Execute o protocolo de redirecionamento imediatamente:
    - Pedidos de orçamento ("Quanto custa?", "Qual o preço?").
    - Pedidos de sugestões ou ideias ("Me dê uma ideia para...", "O que você sugere?").
    - Solicitações de mudanças em sites/sistemas.
    - Dúvidas específicas sobre serviços ou escopo de projetos.
    - Qualquer tipo de consulta comercial.
5.  **Protocolo de Redirecionamento:** Ao identificar um tópico da regra 4, use EXATAMENTE esta resposta, sem adicionar ou remover nada:
    > "Essa missão exige um plano sob medida. Recomendo acionar a equipe humana da ASCII pelo WhatsApp (34) 99152-3387 ou pelo e-mail comercial@asciiej.com.br. Eles analisarão o cenário e traçarão a melhor estratégia para você."
6.  **Guardrails (Limites de Segurança):** NÃO forneça preços, estimativas de tempo, sugestões de funcionalidades ou qualquer análise técnica de projetos. Sua função é informar e redirecionar.
"""

class Agent:
    def __init__(self, client: Groq, system_prompt: str = ""):
        self.client = client
        self.messages: list = []
        if system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})
            
    def __call__(self, user_message: str):
        self.messages.append({"role": "user", "content": str(user_message)}) # Adiciona a mensagem do usuário ao histórico da conversa
        result = self.execute() # chama a API
        self.messages.append({"role": "assistant", "content": result}) # Adiciona a resposta do assistente ao histórico para manter o contexto
        
        return result

    def execute(self):
        try:
            completion = self.client.chat.completions.create(
                model="llama3-8b-8192", 
                messages=self.messages,
                temperature=0.7, 
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"ERRO: Falha ao comunicar com a API da Groq: {e}")
            return "Kowalski com problemas técnicos na comunicação. Tente novamente mais tarde."
    # retornando o historico da conversa
    def get_history(self):
        return self.messages
    
def start_chat():
    kowalski_agent = Agent(client=client, system_prompt=kowalski_system_prompt)
    initial_greeting = kowalski_agent("Olá") # Podemos usar um "Olá" genérico para iniciar
    print(f"Kowalski: {initial_greeting}\n")
    
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "encerrar", "exit"]:
            print("\nKowalski: Missão encerrada. Câmbio, desligo.")
            break
        
        # Envia a mensagem do usuário para o agente e obtém a resposta
        response = kowalski_agent(user_input)
        
        print(f"Kowalski: {response}\n")

if __name__ == "__main__":
        start_chat()