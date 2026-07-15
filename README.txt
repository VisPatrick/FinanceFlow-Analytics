# 💰 FinanceFlow Analytics

> Projeto completo de Engenharia e Análise de Dados desenvolvido para simular um ambiente financeiro corporativo, abrangendo desde a modelagem do banco de dados até a construção de dashboards executivos em Power BI.

---

## 📌 Sobre o Projeto

O **FinanceFlow Analytics** foi desenvolvido com o objetivo de reproduzir um cenário real de gestão financeira empresarial, permitindo análises estratégicas sobre receitas, despesas, pagamentos, recebimentos e fluxo de caixa.

O projeto contempla todas as etapas de um pipeline moderno de dados:

- Levantamento de requisitos
- Documentação funcional
- Modelagem de dados
- Banco de Dados Relacional
- Geração de dados sintéticos
- ETL (em desenvolvimento)
- Data Warehouse (em desenvolvimento)
- Dashboards no Power BI (em desenvolvimento)

---

## 🎯 Objetivos

- Simular um ambiente financeiro corporativo.
- Aplicar conceitos de Engenharia de Dados.
- Desenvolver um pipeline completo de Analytics.
- Criar dashboards executivos para tomada de decisão.
- Demonstrar habilidades em Python, SQL, MySQL e Power BI.

---

# 🏗 Arquitetura da Solução

```text
                  Documentação
                        │
                        ▼
               Banco de Dados (MySQL)
                        │
                        ▼
           Geradores de Dados (Python)
                        │
                        ▼
               Arquivos CSV (RAW)
                        │
                        ▼
                 Pipeline ETL
                        │
                        ▼
                 Data Warehouse
                        │
                        ▼
                   Power BI
                        │
                        ▼
             Dashboards Executivos
```

---

# 🛠 Tecnologias Utilizadas

| Tecnologia | Utilização |
|------------|------------|
| Python | Geração de dados e ETL |
| MySQL | Banco de Dados |
| SQL | Modelagem e consultas |
| Pandas | Manipulação de dados |
| Faker | Dados sintéticos |
| Power BI | Dashboards |
| Git | Versionamento |
| GitHub | Portfólio |

---

# 📁 Estrutura do Projeto

```text
FinanceFlow-Analytics/

docs/
database/
generator/
etl/
data/
powerbi/
dashboard/

README.md

---

# 📚 Documentação

O projeto possui documentação completa contendo:

- ✅ Entendimento do Negócio
- ✅ Regras de Negócio
- ✅ Dicionário de Dados
- ✅ Modelo Entidade-Relacionamento (DER)
- ✅ Modelo Dimensional
- ✅ Arquitetura da Solução
- ✅ Especificação Funcional dos Dashboards

---

# 🗄 Banco de Dados

O projeto utiliza **MySQL** como banco de dados relacional.

Principais tabelas:

### Financeiro

- Clientes
- Fornecedores
- Contas a Pagar
- Pagamentos
- Contas a Receber
- Recebimentos

---

# ⚙ Geração de Dados

Os dados são gerados automaticamente através de scripts Python.

Atualmente o projeto possui:

```
✔ generate_clientes.py

✔ generate_fornecedores.py

✔ generate_contas_pagar.py

✔ generate_pagamentos.py

✔ generate_contas_receber.py

✔ generate_recebimentos.py

✔ generate_all.py
```

Todos os registros são gerados respeitando regras de negócio previamente documentadas.

---

# 📊 Dados Gerados

A execução do projeto gera automaticamente aproximadamente:

| Tabela | Registros |
|---------|----------:|
| Clientes | 500 |
| Fornecedores | 500 |
| Contas a Pagar | 15.000 |
| Pagamentos | ~10.000 |
| Contas a Receber | 15.000 |
| Recebimentos | ~10.000 |

Mais de **50 mil registros** são criados automaticamente.

---


## ✅ Concluído

- Documentação
- Banco de Dados
- Modelagem
- Scripts de geração
- Pipeline de geração

---

## 🚧 Em desenvolvimento

- Pipeline ETL
- Importação automática para MySQL
- Data Warehouse
- Views SQL
- Dashboards Power BI

---

## 🔮 Futuras melhorias

- Docker
- Testes automatizados
- Integração com APIs
- Deploy em Cloud
- Machine Learning para previsão de fluxo de caixa

---

# 💼 Competências Demonstradas

Este projeto evidencia conhecimentos em:

- Engenharia de Dados
- Modelagem Relacional
- Modelagem Dimensional
- SQL
- Python
- Pandas
- ETL
- Business Intelligence
- Power BI
- Git
- GitHub

---

# 📸 Preview

Em breve serão adicionadas imagens dos dashboards desenvolvidos no Power BI.

---

# 👨‍💻 Autor

**Patrick**

Tecnólogo em Sistemas de Computação — UFF

Analista de Dados | Business Intelligence | Engenharia de Dados

GitHub:
https://github.com/VisPatrick

LinkedIn:
https://www.linkedin.com/in/patrick-nascimento-b2960b236/

---

# ⭐ Projeto em evolução

Este projeto faz parte do meu portfólio profissional e continuará recebendo novas funcionalidades relacionadas à Engenharia de Dados, Business Intelligence e Analytics.