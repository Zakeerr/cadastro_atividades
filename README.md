# OrganizaJá

Integrantes
Isaque Ferreira — RGM: 43660126
Lukas Paulo — RGM: 47763311
Ruan Abner — RGM: 43095097

Sistema de gerenciamento de tarefas acadêmicas desenvolvido para a disciplina Estruturas de Dados I.

---

# Tecnologias utilizadas

- Python 3
- Flask
- PostgreSQL
- HTML
- CSS
- JavaScript

---

# Estruturas de dados utilizadas

## Lista
Utilizada para armazenar todas as tarefas cadastradas.

## Fila
Utilizada para controle de tarefas pendentes seguindo FIFO.

## Pilha
Utilizada para histórico e desfazer ações seguindo LIFO.

---

# Estrutura do projeto

```text
src/
├── core/
│   ├── fila.py
│   ├── lista.py
│   ├── pilha.py
│   └── tarefa.py
│
├── service/
│   └── gerenciador_service.py
│
├── ui/
│   ├── main.py
│   └── menu.py
│
├── database/
│   ├── conexao.py
│   └── tarefa_repository.py
│
├── tests/
├── data/
└── README.md
