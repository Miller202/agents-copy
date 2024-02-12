from flask import Flask, request, jsonify
from agents import get_crew
from crewai import Task
from langchain.agents import Tool
from langchain_community.tools import DuckDuckGoSearchRun
import os

app = Flask(__name__)
crew = get_crew()
search_tool = DuckDuckGoSearchRun()

@app.route('/request-copy', methods=['POST'])
def request_copy():
    data = request.get_json()
    user_request = data.get('user_request')

    if not user_request:
        return jsonify({"error": "Por favor, forneça o pedido de copy como 'user_request'."}), 400

    crew.tasks = [
        Task(description=f"Coletar informações relevantes sobre o contexto: {user_request}.", agent=crew.agents[0], tools=[search_tool]),
        Task(description=f"Extrair ideias valiosas a partir dos dados coletados no contexto: {user_request}.", agent=crew.agents[1]),
        Task(description=f"Desenvolver Big Ideas para o contexto: {user_request}.", agent=crew.agents[2]),
        Task(description=f"Criar Headlines impactantes para o contexto: {user_request}.", agent=crew.agents[3]),
        Task(description=f"Escrever Leads envolventes do contexto: {user_request}.", agent=crew.agents[4]),
        Task(description=f"Produzir roteiros para VSL do contexto: {user_request}.", agent=crew.agents[5]),
        Task(description=f"Elaborar ofertas irresistíveis para o contexto: {user_request}.", agent=crew.agents[6]),
        Task(description="Revisão final de todo o conteúdo.", agent=crew.agents[7])
    ]

    result = crew.kickoff()

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
