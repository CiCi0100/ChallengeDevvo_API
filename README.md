### README: Testes Automatizado em API-Risadas, com Python Requests e Relatório HTML

---

## **Descrição**

Este projeto realiza testes de carga e funcionais. Ele mede o tempo de resposta de cada requisição, garante que tudo esteja funcionando corretamente e gera um relatório detalhado em formato HTML para facilitar a análise dos resultados.

---

## **Instruções de Instalação e Uso**

### **1. Pré-requisitos**

- **Python 3.7+**: Certifique-se de que o Python está instalado em sua máquina.
  - Verifique sua versão com:
    ```bash
    python --version
    ```

- **Pip**: O gerenciador de pacotes do Python deve estar instalado.
  - Verifique com:
    ```bash
    pip --version
    ```

### **2. Dependências**

As principais bibliotecas utilizadas neste projeto são:

- **requests**: Para fazer as requisições HTTP.
- **concurrent.futures**: Para gerenciar requisições simultâneas (embutido no Python).
- **datetime**: Para gerar timestamps nos relatórios (embutido no Python).
- **logging**: Para registrar logs de execução (embutido no Python).

Instale a única dependência externa com:
```bash
pip install requests
```

---

## **Como Executar**

1. **Clone ou Baixe o Repositório**
   - Clone o repositório:
     ```bash
     git clone https://github.com/CiCi0100/ChallengeDevvo_API.git
     ```
   - Ou baixe os arquivos manualmente e extraia-os.

2. **Execute o Script**
   - No terminal, navegue até o diretório onde o arquivo `suite` está localizado.
     ```bash
     cd ./suite
     ```
   - Execute o teste de carga:
     ```bash
     python load_test.py
     ```
   - Execute os testes funcionais:
     ```bash
     python test_automation.py
     ```

3. **Verifique o Relatório**
   - Após a execução, será gerado um arquivo de relatório HTML no mesmo diretório do script, na pasta ***relatorios***.
   - O arquivo será nomeado no formato `load_test_report_YYYYMMDD_HHMMSS.html`
`test_automation_report_YYYYMMDD_HHMMSS.html`.
   - Abra o arquivo em qualquer navegador para visualizar os resultados.

---

## **Funcionamento do Script**

Este script automatiza a execução de testes de API e gera relatórios detalhados com métricas e informações úteis. Abaixo estão os passos e funcionalidades principais:

**1. Execução de Testes**

Os testes utilizam a API de piadas disponível no endpoint https://official-joke-api.appspot.com/jokes/random.

Cada teste faz uma requisição à API, valida campos esperados e calcula métricas como tempo de resposta e tamanho da resposta.

Todos os resultados dos testes (sucesso ou falha) são armazenados em uma lista de resultados, com detalhes como:

Nome do teste.

Status (PASS ou FAIL).

Detalhes do erro (em caso de falha).

Data e hora do teste.



**2. Métricas Coletadas**

Durante a execução dos testes, o script calcula as seguintes métricas:

Tempo médio de resposta: tempo médio de processamento da API em milissegundos.

Tamanho médio das respostas: tamanho médio das respostas da API em bytes.

Taxa de sucesso: percentual de testes concluídos com sucesso.

Distribuição dos tipos de piadas: contagem de piadas categorizadas por tipo.


**3. Geração de Relatório**

Após a execução dos testes, um relatório em formato HTML é gerado.

O relatório inclui:

Data e hora da execução.

Métricas gerais.

Detalhes dos testes realizados.


O relatório é salvo automaticamente em uma pasta chamada relatórios, que é criada automaticamente caso não exista.


**4. Logs**

Todas as ações e eventos importantes são registrados em um arquivo de log chamado test_automation.log, incluindo:

Erros encontrados durante a execução.

Informações sobre a geração do relatório.



**5. Estrutura do Projeto**

relatórios/: pasta onde os relatórios gerados serão salvos.

test_automation.log: arquivo de log com os eventos do script.



---

## **Premissas**

A API alvo está operacional e responde às requisições dentro de tempos aceitáveis.

Cada resposta da API contém uma piada com um ID único e os campos esperados (ex.: id, type, setup, punchline).

O ambiente de execução possui acesso à Internet estável para realizar as requisições.

O Python 3.7 ou superior está instalado e configurado corretamente no sistema.

---

## **Exemplo de Saída**

### **Log no Terminal**
```plaintext
2024-11-16 14:35:25 - Iniciando teste de carga...
2024-11-16 14:35:26 - Usuário 1: Requisição bem-sucedida em 0.22s
2024-11-16 14:35:26 - Usuário 2: Requisição bem-sucedida em 0.20s
2024-11-16 14:35:26 - Total de requisições bem-sucedidas: 10
2024-11-16 14:35:26 - Tempo médio de resposta: 0.21s
2024-11-16 14:35:26 - Relatório gerado: load_test_report_20241116_143526.html
```

### **Relatório HTML**
O relatório HTML gerado será salvo no mesmo diretório e exibirá:
- Tabela com o tempo de resposta e status de cada requisição.
- Resumo com o total de sucessos e o tempo médio de resposta.

### **Documentação, Relatórios e Análise dos resultados Disponíveis**

## Relatórios de Testes

- [Relatório de Teste - API de Piadas](https://docs.google.com/document/d/1NmxhKje6i41G64J4319cuSx1m23UwfZBT5vpjw_4xXA/edit?usp=drivesdk)  
  Descreve os testes funcionais e de carga realizados na API de piadas, incluindo falhas identificadas e recomendações.

- [Análise dos Resultados](https://docs.google.com/document/d/1hEOmjIEzU4qRVKS6w607_Jc5Qj1-dZa49FbnbeRRJp4/edit?usp=drivesdk)  
  Detalha os padrões de erros observados, melhorias sugeridas e possíveis riscos encontrados durante os testes.

- [Documentação para relatar os bugs encontrados, com base no relatório de Testes 01](https://docs.google.com/document/d/149U0eBfemnh5eaPDsXfGuzGX8jqI6uH-wguRN-cIxpQ/edit?usp=drivesdk)  
  Lista os bugs encontrados, passos para reproduzir os problemas, e evidências coletadas durante os testes.

- [Documentação de bugs baseado no relatório de teste de carga 01](https://docs.google.com/document/d/1I19g6yZJS2PVz9oAojd3h8KVG0prPNhh8zG8PYzsTIA/edit?usp=drivesdk)  
  Detalha os problemas identificados durante os testes de carga, incluindo falhas de infraestrutura e inconsistências nas respostas da API.

---

## **Autor**

Criado por [Ciara/CiCi0100].  

LinkedIn: [Seu LinkedIn](https://www.linkedin.com/in/ciaradepaulanascimento0206/)  
GitHub: [Seu GitHub](https://github.com/CiCi0100)  

--- 

Se precisar de mais ajuda ou informações, abra uma **Issue** no repositório.
