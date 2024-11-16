### README: Teste de Carga com Python Requests e Relatório HTML

---

## **Descrição**

Este projeto realiza testes de cargae funcionais. Ele mede o tempo de resposta de cada requisição, garante que tudo esteja funcionando corretamente e gera um relatório detalhado em formato HTML para facilitar a análise dos resultados.

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
     git clone https://github.com/seu-usuario/teste-carga-api.git
     ```
   - Ou baixe os arquivos manualmente e extraia-os.

2. **Execute o Script**
   - No terminal, navegue até o diretório onde o arquivo `suite` está localizado.
     ```bash
     cd ./suite
     ```
   - Execute o script:
     ```bash
     python load_test.py
     ```
     ou
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

1. **Simulação de Teste de Carga**:
   - O script utiliza `concurrent.futures` para simular 10 usuários simultâneos.
   - Cada usuário faz uma requisição à API definida (`https://official-joke-api.appspot.com/jokes/ten`).
   - O tempo de resposta e a consistência das respostas retornadas são validados.

2. **Validação de Resultados**:
   - Verifica se:
     - O status HTTP é 200 (OK).
     - Os IDs retornados são únicos.

3. **Geração de Relatório HTML**:
   - Um relatório detalhado é gerado automaticamente após os testes.
   - Inclui:
     - Tempo de resposta para cada requisição.
     - Status de sucesso ou falha.
     - Resumo geral com número de requisições bem-sucedidas e o tempo médio de resposta.

---

## **Premissas**

- A API alvo está funcional e responde às requisições.
- Cada resposta da API contém um conjunto de piadas com IDs únicos.
- O ambiente de execução possui conectividade com a Internet.
- O Python 3.7 ou superior está instalado corretamente no sistema.

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

# Relatórios de Teste

Aqui estão os relatórios detalhados sobre os testes realizados:

1. [Relatório de Teste - API de Piadas](./docs/Relatório%20de%20Teste%20-%20API%20de%20Piadas.pdf)  
   Descreve os testes funcionais e de carga realizados na API de piadas, incluindo falhas identificadas e recomendações.

2. [Análise dos Resultados](./docs/Análise%20dos%20Resultados.pdf)  
   Detalha os padrões de erros observados, melhorias sugeridas e possíveis riscos encontrados durante os testes.

3. [Documentação para relatar os bugs encontrados, com base no relatório de Testes 01](./docs/Documentação%20para%20relatar%20os%20bugs%20encontrados,%20com%20base%20no%20relatório%20de%20Testes%2001.pdf)  
   Lista os bugs encontrados, passos para reproduzir os problemas e evidências coletadas durante os testes.

4. [Documentação de bugs baseado no relatório de teste de carga 01](./docs/Documentação%20de%20bugs%20baseado%20no%20relatório%20de%20teste%20de%20carga%2001.pdf)  
   Detalha os problemas identificados durante os testes de carga, incluindo falhas de infraestrutura e inconsistências nas respostas da API.
---

---

## **Licença**

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## **Autor**

Criado por [Ciara/CiCi0100].  

LinkedIn: [Seu LinkedIn](https://www.linkedin.com/in/ciaradepaulanascimento0206/)  
GitHub: [Seu GitHub](https://github.com/CiCi0100)  

--- 

Se precisar de mais ajuda ou informações, abra uma **Issue** no repositório.
