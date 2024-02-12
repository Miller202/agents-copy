from langchain.chat_models.openai import ChatOpenAI
from crewai import Agent, Crew, Task, Process
from agents_backstories import (
    get_agente_de_pesquisa_backstory,
    get_extrator_de_boas_ideias_backstory,
    get_criador_de_big_ideas_backstory,
    get_criador_de_headlines_backstory,
    get_criador_de_lead_backstory,
    get_criador_de_vsl_backstory,
    get_criador_de_ofertas_backstory,
    get_head_de_copy_backstory
)
import os

default_llm = ChatOpenAI(
    openai_api_base=os.getenv('OPENAI_API_BASE_URL'),
    openai_api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0.1,
    model_name=os.getenv('MODEL_NAME'),
    max_tokens=128
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

    agente_de_pesquisa = create_agent(role='Agente de Pesquisa', 
        goal='Coletar informações que servirão de base para a criação de copy.', 
        backstory=get_agente_de_pesquisa_backstory())

    extrator_de_boas_ideias = create_agent(role='Extrator de Boas Ideias', 
        goal='Identificar insights valiosos a partir do material coletado.', 
        backstory=get_extrator_de_boas_ideias_backstory())

    criador_de_big_ideas = create_agent(role='Criador de Big Ideas', 
        goal='Desenvolver conceitos centrais que servirão como a base das campanhas.', 
        backstory=get_criador_de_big_ideas_backstory())

    criador_de_headlines = create_agent(role='Criador de Headlines', 
        goal='Gerar títulos que atraiam a atenção do público.', 
        backstory=get_criador_de_headlines_backstory())

    criador_de_lead = create_agent(role='Criador de Lead', 
        goal='Construir a introdução e argumento inicial das copies.', 
        backstory=get_criador_de_lead_backstory())
        
    criador_de_vsl = create_agent(role='Criador de VSL', 
        goal='Produzir roteiros para vídeos de vendas eficazes.', 
        backstory=get_criador_de_vsl_backstory())

    criador_de_ofertas = create_agent(role='Criador de Ofertas', 
        goal='Elaborar ofertas irresistíveis para o cliente.', 
        backstory=get_criador_de_ofertas_backstory())

    head_de_copy = create_agent(role='Head de Copy', 
        goal='Liderar a estratégia de conteúdo e garantir a qualidade do material produzido.', 
        backstory=get_head_de_copy_backstory())

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