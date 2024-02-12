from langchain.chat_models.openai import ChatOpenAI
from crewai import Agent, Crew, Task, Process
import os

default_llm = ChatOpenAI(
    openai_api_base=os.getenv('OPENAI_API_BASE_URL'),
    openai_api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0.1,
    model_name=os.getenv('MODEL_NAME'),
    top_p=0.3
)

def create_agent(role, goal, backstory):
    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        verbose=True,
        llm=default_llm
    )

def get_crew():

    agente_de_pesquisa = create_agent(role='Agente de Pesquisa', goal='Coletar informações que servirão de base para a criação de copy.', 
        backstory='Especialista em buscar dados e tendências de mercado relevantes.')
    extrator_de_boas_ideias = create_agent(role='Extrator de Boas Ideias', goal='Identificar insights valiosos a partir do material coletado.', 
        backstory='Analisa informações para encontrar ideias inovadoras.')
    criador_de_big_ideas = create_agent(role='Criador de Big Ideas', goal='Desenvolver conceitos centrais que servirão como a base das campanhas.', 
        backstory='Transformar insights em conceitos centrais impactantes.')
    criador_de_headlines = create_agent(role='Criador de Headlines', goal='Gerar títulos que atraiam a atenção do público.', 
        backstory='Especializado em criar títulos envolventes e memoráveis.')
    criador_de_lead = create_agent(role='Criador de Lead', goal='Construir a introdução e argumento inicial das copies.', 
        backstory='Desenvolve introduções que capturam o interesse dos leitores.')
    criador_de_vsl = create_agent(role='Criador de VSL', goal='Produzir roteiros para vídeos de vendas eficazes.', 
        backstory='Cria roteiros persuasivos para vídeos que convertem.')
    criador_de_ofertas = create_agent(role='Criador de Ofertas', goal='Elaborar ofertas irresistíveis para o cliente.', 
        backstory='Desenvolve propostas de valor que destacam os produtos, persuadindo o cliente.')
    head_de_copy = create_agent(role='Head de Copy', goal='Liderar a estratégia de conteúdo e garantir a qualidade do material produzido.', 
        backstory='Responsável pela direção criativa e estratégica do conteúdo, para organizar tudo o que foi elaborado no projeto final com a copy completa.')

    crew = Crew(
        agents=[
            agente_de_pesquisa, extrator_de_boas_ideias, criador_de_big_ideas,
            criador_de_headlines, criador_de_lead, criador_de_vsl, 
            criador_de_ofertas, head_de_copy
        ],
        tasks=[],
        process=Process.sequential,
        verbose=True
    )

    return crew