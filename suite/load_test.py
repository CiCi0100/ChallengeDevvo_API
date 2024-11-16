import requests
import time
import concurrent.futures
import logging
import os
from datetime import datetime
from html import escape

# URL da API que será testada
API_URL = "https://official-joke-api.appspot.com/jokes/ten"

# Configuração do logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()

# Função para realizar a requisição e medir o tempo de resposta
def make_request(user_id):
    try:
        start_time = time.time()
        response = requests.get(API_URL)
        end_time = time.time()

        # Tempo de resposta
        response_time = end_time - start_time

        # Verifica a consistência da resposta (id único e não vazio)
        if response.status_code == 200:
            data = response.json()

            # Verificar se o 'id' está presente e é único
            ids = [joke["id"] for joke in data]
            if len(ids) == len(set(ids)):  # Todos os ids são únicos
                # Distribuição dos tipos de piadas e tamanho das respostas
                joke_types = [joke["type"] for joke in data]
                response_sizes = [len(str(joke)) for joke in data]  # Tamanho das respostas

                logger.info(f"Usuário {user_id}: Requisição bem-sucedida em {response_time:.2f}s")
                return response_time, True, joke_types, response_sizes
            else:
                logger.error(f"Usuário {user_id}: IDs não são únicos.")
                return response_time, False, [], []
        else:
            logger.error(f"Usuário {user_id}: Erro na requisição - Status {response.status_code}")
            return None, False, [], []

    except Exception as e:
        logger.error(f"Usuário {user_id}: Erro ao fazer a requisição - {e}")
        return None, False, [], []

# Função para simular 10 usuários simultâneos
def load_test():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        user_ids = range(1, 11)  # Simula 10 usuários
        results = list(executor.map(make_request, user_ids))

    return results

# Função para gerar o relatório HTML
def generate_html_report(results):
    # Criação do nome do arquivo de relatório com base na data e hora atual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"load_test_report_{timestamp}.html"

    # Cabeçalho do relatório HTML
    report_content = f"""
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Relatório de Teste de Carga - {timestamp}</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .success {{ color: green; }}
        .error {{ color: red; }}
    </style>
    </head>
    <body>
        <h1>Relatório de Teste de Carga - {timestamp}</h1>
        <p>O teste foi realizado com 10 usuários simultâneos. Abaixo está o resumo dos resultados:</p>
        <table>
            <thead>
                <tr>
                    <th>ID Usuário</th>
                    <th>Tempo de Resposta (s)</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
    """

    # Adicionando os resultados no corpo da tabela
    for user_id, (response_time, success, joke_types, response_sizes) in enumerate(results, 1):
        status = "Sucesso" if success else "Falha"
        status_class = "success" if success else "error"
        response_time_str = f"{response_time:.2f}" if response_time else "N/A"
        
        report_content += f"""
        <tr>
            <td>{user_id}</td>
            <td>{response_time_str}</td>
            <td class="{status_class}">{status}</td>
        </tr>
        """

    # Adicionando resumo do relatório
    success_count = sum(1 for _, success, _, _ in results if success)
    total_time = sum(response_time for response_time, _, _, _ in results if response_time is not None)
    average_time = total_time / success_count if success_count > 0 else 0

    # Distribuição dos tipos de piadas
    joke_type_counts = {}
    total_response_size = 0
    total_jokes = 0

    for _, _, joke_types, response_sizes in results:
        for joke_type in joke_types:
            joke_type_counts[joke_type] = joke_type_counts.get(joke_type, 0) + 1
        total_response_size += sum(response_sizes)
        total_jokes += len(response_sizes)

    average_response_size = total_response_size / total_jokes if total_jokes > 0 else 0

    report_content += f"""
            </tbody>
        </table>
        <h2>Resumo</h2>
        <p>Total de requisições bem-sucedidas: {success_count}</p>
        <p>Tempo médio de resposta: {average_time:.2f}s</p>
        <p>Taxa de sucesso: {success_count / 10 * 100:.2f}%</p>
        <p>Tamanho médio das respostas: {average_response_size:.2f} caracteres</p>
        <p>Distribuição dos tipos de piadas:</p>
        <ul>
    """

    for joke_type, count in joke_type_counts.items():
        report_content += f"<li>{joke_type}: {count} piadas</li>"

    report_content += f"""
        </ul>
        <p>O teste foi concluído com {'sucesso' if success_count == 10 else 'falha'}.</p>
    </body>
    </html>
    """

    # Configuração do caminho para salvar o relatório na pasta 'relatórios'
    directory = "relatorios"
    os.makedirs(directory, exist_ok=True)  # Cria o diretório 'relatórios' se não existir

    # Caminho completo do arquivo de relatório
    report_filename = os.path.join(directory, f"load_test_report_{timestamp}.html")

    # Salvando o relatório HTML em um arquivo
    with open(report_filename, "w", encoding="utf-8") as file:
        file.write(report_content)

    logger.info(f"Relatório gerado: {report_filename}")

# Função principal para executar o teste
def run_load_test():
    logger.info("Iniciando teste de carga...")
    results = load_test()

    # Gerar o relatório HTML
    generate_html_report(results)

    # Analisando resultados
    success_count = sum(1 for _, success, _, _ in results if success)
    total_time = sum(response_time for response_time, _, _, _ in results if response_time is not None)
    average_time = total_time / success_count if success_count > 0 else 0

    logger.info(f"Total de requisições bem-sucedidas: {success_count}")
    logger.info(f"Tempo médio de resposta: {average_time:.2f}s")

    # Verifica se todas as requisições foram bem-sucedidas
    if success_count == 10:
        logger.info("Teste de carga concluído com sucesso!")
    else:
        logger.error(f"Falha no teste de carga, {10 - success_count} requisições falharam.")

# Executando o teste de carga
if __name__ == "__main__":
    run_load_test()
