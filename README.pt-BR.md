🇧🇷 Português | [🇺🇸 English](README.md)

# LoginSystem

Um sistema simples de autenticação via terminal desenvolvido em Python e SQLite. O projeto implementa cadastro de usuários, autenticação, hash de senhas e uma estrutura básica de controle de acesso baseada em privilégios de administrador.

## Funcionalidades

- **Cadastro de usuários:** Criação de contas com nomes de usuário e senhas únicos.
- **Autenticação:** Verificação das credenciais dos usuários durante o login.
- **Hash de senhas:** Armazenamento de senhas como hashes SHA-256 combinados com salts individuais e um pepper.
- **Banco de dados SQLite:** Persistência local de credenciais e informações das contas.
- **Gerenciamento de privilégios:** Suporte a contas com privilégios de administrador.
- **Interface CLI:** Interface interativa baseada no terminal.
- **Compatibilidade entre sistemas:** Suporte para limpeza do terminal em Windows e sistemas Unix-like.

## Tecnologias utilizadas

- Python 3
- SQLite3
- SHA-256
- Git

## Estrutura do projeto

```text
loginSystem/
├── adduser.py
├── authentication.py
├── cli.py
├── config.py
├── database.py
├── hashutils.py
├── main.py
├── metas.txt
├── removeuser.py
├── step.py
├── users.db
└── utils.py
```

| Arquivo | Descrição |
|---|---|
| `main.py` | Loop principal da aplicação e fluxo de autenticação. |
| `authentication.py` | Lógica de verificação e autenticação de usuários. |
| `database.py` | Operações com o banco de dados e gerenciamento de contas. |
| `hashutils.py` | Utilitários para hash de senhas e geração de salts. |
| `cli.py` | Interface de terminal e tratamento de entradas. |
| `config.py` | Constantes e configurações do projeto. |
| `utils.py` | Funções utilitárias gerais. |
| `adduser.py` | Script para alteração de privilégios de administrador. |
| `removeuser.py` | Utilitário para remoção de usuários. |

## Como começar

### Pré-requisitos

- Python 3.10+ (ou uma versão compatível)

Nenhuma biblioteca externa de Python é necessária. O projeto utiliza apenas a biblioteca padrão do Python.

### Instalação

Clone o repositório:

```bash
git clone https://github.com/Agst2k7/loginSystem.git
```

Entre no diretório do projeto:

```bash
cd loginSystem
```

### Executando a aplicação

Execute o script principal:

```bash
python main.py
```

A aplicação inicializará o banco de dados SQLite e exibirá o menu principal.

## Banco de dados

A aplicação utiliza SQLite para armazenar as informações dos usuários.

O banco de dados contém os seguintes campos:

| Campo | Descrição |
|---|---|
| `id` | Identificador único do usuário. |
| `username` | Nome de usuário único. |
| `salt` | Salt individual associado à senha do usuário. |
| `password_hash` | Hash da senha. |
| `admin` | Indica se o usuário possui privilégios de administrador. |

O banco de dados é inicializado automaticamente quando a aplicação é executada.

## Considerações sobre segurança

Este projeto foi desenvolvido como um exercício de aprendizado sobre autenticação, gerenciamento de banco de dados e armazenamento de senhas.

- As senhas não são armazenadas diretamente em texto puro.
- Salts individuais são gerados para as senhas dos usuários.
- Um pepper é utilizado como entrada adicional no processo de hashing.
- Consultas parametrizadas do SQLite são utilizadas nas operações com o banco de dados.

**Este projeto não foi desenvolvido para uso em produção.**

A implementação atual utiliza SHA-256 diretamente para hashing de senhas, o que não é adequado para sistemas modernos de produção. O armazenamento de senhas deve utilizar algoritmos especificamente projetados para esse propósito, como Argon2id, bcrypt ou scrypt. Além disso, o pepper deve ser armazenado fora do código-fonte.

## Objetivo

Este projeto foi desenvolvido para praticar programação em Python, organização modular de código, integração com banco de dados, fluxos de autenticação e conceitos básicos de segurança.

---

Desenvolvido por [Agst2k7](https://github.com/Agst2k7)
