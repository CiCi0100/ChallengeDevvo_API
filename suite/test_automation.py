from concurrent.futures import ThreadPoolExecutor
import requests
import json
import logging
from datetime import datetime, time
from collections import Counter
import concurrent.futures
import os

# Configuração do logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_automation.log"),
        logging.StreamHandler()
    ]
)

# URL do endpoint que será testado
BASE_URL = "https://official-joke-api.appspot.com/jokes/random"

# Lista para armazenar resultados dos testes
test_results = []

# Função para registrar os resultados dos testes
def log_result(test_name, status, details=""):
    test_results.append({
        "test_name": test_name,
        "status": status,
        "details": details,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# Funções dos casos de teste
def ct01_verify_expected_fields():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        joke = response.json()
        expected_fields = {"id", "type", "setup", "punchline"}
        missing_fields = expected_fields - joke.keys()
        assert not missing_fields, f"Campos ausentes: {', '.join(missing_fields)}"
        log_result("CT01: Verificar campos esperados", "PASS")
    except Exception as e:
        log_result("CT01: Verificar campos esperados", "FAIL", str(e))

def ct02_verify_json_format():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        assert response.headers["Content-Type"] == "application/json", "Resposta não está em JSON"
        log_result("CT02: Verificar formato JSON", "PASS")
    except Exception as e:
        log_result("CT02: Verificar formato JSON", "FAIL", str(e))

def ct03_verify_id_numeric_and_unique():
    try:
        ids = set()
        for _ in range(10):  # Testar 10 requisições
            response = requests.get(BASE_URL)
            response.raise_for_status()
            joke = response.json()
            assert isinstance(joke["id"], int), "ID não é numérico"
            assert joke["id"] not in ids, "ID duplicado encontrado"
            ids.add(joke["id"])
        log_result("CT03: Verificar ID numérico e único", "PASS")
    except Exception as e:
        log_result("CT03: Verificar ID numérico e único", "FAIL", str(e))

def ct04_verify_type_string():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        joke = response.json()
        assert isinstance(joke["type"], str), "Type não é string"
        log_result("CT04: Verificar se Type é string", "PASS")
    except Exception as e:
        log_result("CT04: Verificar se Type é string", "FAIL", str(e))

def ct05_verify_setup_and_punchline_length():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        joke = response.json()
        assert isinstance(joke["setup"], str) and len(joke["setup"]) <= 255, "Setup inválido"
        assert isinstance(joke["punchline"], str) and len(joke["punchline"]) <= 255, "Punchline inválido"
        log_result("CT05: Verificar comprimento de Setup e Punchline", "PASS")
    except Exception as e:
        log_result("CT05: Verificar comprimento de Setup e Punchline", "FAIL", str(e))

def ct06_simultaneous_requests():
    try:
        with ThreadPoolExecutor(max_workers=100) as executor:
            responses = list(executor.map(lambda _: requests.get(BASE_URL), range(10)))
        jokes = [resp.json() for resp in responses if resp.status_code == 200]
        assert len(jokes) == 10, "Falha ao obter todas as respostas"
        log_result("CT06: Verificar consistência com requisições simultâneas", "PASS")
    except Exception as e:
        log_result("CT06: Verificar consistência com requisições simultâneas", "FAIL", str(e))

def ct07_verify_response_time():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        elapsed = response.elapsed.total_seconds() * 1000  # Converter para ms
        assert elapsed <= 2000, f"Tempo de resposta alto: {elapsed}ms"
        log_result("CT07: Verificar tempo de resposta", "PASS")
    except Exception as e:
        log_result("CT07: Verificar tempo de resposta", "FAIL", str(e))

def ct08_verify_unique_ids_in_sequence():
    try:
        ids = set()
        for _ in range(100):
            response = requests.get(BASE_URL)
            response.raise_for_status()
            joke = response.json()
            assert joke["id"] not in ids, f"ID duplicado: {joke['id']}"
            ids.add(joke["id"])
        log_result("CT09: Verificar IDs únicos em sequência", "PASS")
    except Exception as e:
        log_result("CT09: Verificar IDs únicos em sequência", "FAIL", str(e))

def ct09_to_ct11_field_not_empty(field_name, test_name):
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        joke = response.json()
        assert joke[field_name], f"Campo {field_name} está vazio"
        log_result(test_name, "PASS")
    except Exception as e:
        log_result(test_name, "FAIL", str(e))

def ct12_verify_sensitive_data():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        joke = response.json()
        sensitive_keywords = ["password", "credit", "card", "ssn", "security", "auth", "key", "token"]
        exposed_data = [key for key in joke.keys() if any(word in key.lower() for word in sensitive_keywords)]
        assert not exposed_data, f"Dados sensíveis expostos: {', '.join(exposed_data)}"
        log_result("CT13: Verificar exposição de dados sensíveis", "PASS")
    except Exception as e:
        log_result("CT13: Verificar exposição de dados sensíveis", "FAIL", str(e))

# Função para calcular taxa de sucesso
def calculate_success_rate():
    passed_tests = sum(1 for result in test_results if result["status"] == "PASS")
    total_tests = len(test_results)
    success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    return success_rate

# Função para calcular distribuição dos tipos de piadas
def calculate_joke_type_distribution():
    joke_types = []
    for _ in range(50):  # Amostra maior para análise
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            joke = response.json()
            joke_types.append(joke.get("type", "Unknown"))
    return Counter(joke_types)

# Função para calcular tamanho médio das respostas
def calculate_average_response_length():
    setups = []
    punchlines = []
    for _ in range(50):  # Amostra maior para análise
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            joke = response.json()
            setups.append(len(joke.get("setup", "")))
            punchlines.append(len(joke.get("punchline", "")))
    avg_setup_length = sum(setups) / len(setups) if setups else 0
    avg_punchline_length = sum(punchlines) / len(punchlines) if punchlines else 0
    return avg_setup_length, avg_punchline_length

# Função para gerar relatório HTML e salvar na pasta 'relatorios'
def generate_html_report():
    # Cria a pasta 'relatorios' caso ela não exista
    os.makedirs('relatorios', exist_ok=True)
    
    # Nome do relatório com timestamp
    report_name = f"test_automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    
    # Caminho completo para salvar o relatório na pasta 'relatorios'
    report_path = os.path.join('relatorios', report_name)
    
    logging.info(f"Gerando relatório: {report_path}")
    
    # Criação e escrita no arquivo HTML
    with open(report_path, "w", encoding="utf-8") as report:
        report.write("<html><head>")
        report.write("<meta charset='UTF-8'>")
        report.write("<title>Test Report</title></head><body>")
        report.write("<h1>Relatório de Testes Automatizados</h1>")
        report.write(f"<p>Data e Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")
        
        # Taxa de sucesso
        success_rate = calculate_success_rate()
        report.write(f"<p><b>Taxa de Sucesso:</b> {success_rate:.2f}%</p>")
        
        # Distribuição dos tipos de piadas
        joke_type_distribution = calculate_joke_type_distribution()
        report.write("<h2>Distribuição dos Tipos de Piadas</h2>")
        report.write("<ul>")
        for joke_type, count in joke_type_distribution.items():
            report.write(f"<li>{joke_type}: {count}</li>")
        report.write("</ul>")
        
        # Tamanho médio das respostas
        avg_setup_length, avg_punchline_length = calculate_average_response_length()
        report.write("<h2>Tamanho Médio das Respostas</h2>")
        report.write(f"<p>Setup: {avg_setup_length:.2f} caracteres</p>")
        report.write(f"<p>Punchline: {avg_punchline_length:.2f} caracteres</p>")
        
        # Resultados dos testes
        report.write("<h2>Resultados dos Testes</h2>")
        report.write("<table border='1'><tr><th>Teste</th><th>Status</th><th>Detalhes</th><th>Timestamp</th></tr>")
        for result in test_results:
            status_color = "green" if result["status"] == "PASS" else "red"
            report.write(
                f"<tr><td>{result['test_name']}</td>"
                f"<td style='color: {status_color}'>{result['status']}</td>"
                f"<td>{result['details']}</td>"
                f"<td>{result['timestamp']}</td></tr>"
            )
        report.write("</table>")
        report.write("</body></html>")
    
    logging.info(f"Relatório gerado com sucesso e salvo em: {report_path}")

# Atualizando o fluxo principal
if __name__ == "__main__":
    logging.info("Iniciando execução de todos os casos de teste...")
    ct01_verify_expected_fields()
    ct02_verify_json_format()
    ct03_verify_id_numeric_and_unique()
    ct04_verify_type_string()
    ct05_verify_setup_and_punchline_length()
    ct06_simultaneous_requests()
    ct07_verify_response_time()
    ct08_verify_unique_ids_in_sequence()
    ct09_to_ct11_field_not_empty("id", "CT09: Verificar campo ID não vazio")
    ct09_to_ct11_field_not_empty("type", "CT10: Verificar campo Type não vazio")
    ct09_to_ct11_field_not_empty("setup", "CT11: Verificar campo Setup não vazio")
    ct12_verify_sensitive_data()
    generate_html_report()
    logging.info("Execução finalizada.")