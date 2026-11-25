[🇧🇷 Português](README.pt-BR.md) | 🇺🇸 English

# LoginSystem

A simple command-line authentication system built with Python and SQLite. The project implements user registration, authentication, password hashing, and a basic role-based access control structure for administrator accounts.

## Features

- **User Registration:** Create accounts with unique usernames and passwords.
- **Authentication:** Verify user credentials during login.
- **Password Hashing:** Store passwords as SHA-256 hashes combined with individual salts and a pepper.
- **SQLite Database:** Persist user credentials and account information locally.
- **Role Management:** Support for administrator privileges.
- **CLI Interface:** Interactive terminal-based interface.
- **Cross-platform Terminal:** Terminal clearing support for Windows and Unix-like systems.

## Technologies

- Python 3
- SQLite3
- SHA-256
- Git

## Project Structure

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

| File | Description |
|---|---|
| `main.py` | Main application loop and authentication workflow. |
| `authentication.py` | User verification and authentication logic. |
| `database.py` | Database operations and account management. |
| `hashutils.py` | Password hashing and salt generation utilities. |
| `cli.py` | Terminal interface and input handling. |
| `config.py` | Configuration constants. |
| `utils.py` | General utility functions. |
| `adduser.py` | Administrator privilege modification script. |
| `removeuser.py` | User removal utility script. |

## Getting Started

### Prerequisites

- Python 3.10+ (or a compatible Python version)

No external Python packages are required. The project uses Python's standard library.

### Installation

Clone the repository:

```bash
git clone https://github.com/Agst2k7/loginSystem.git
```

Navigate to the project directory:

```bash
cd loginSystem
```

### Running the Application

Run the main script:

```bash
python main.py
```

The application will initialize the SQLite database and display the main menu.

## Database

The application uses SQLite to store user information.

The database contains the following fields:

| Field | Description |
|---|---|
| `id` | Unique user identifier. |
| `username` | Unique username. |
| `salt` | Individual salt associated with the user's password. |
| `password_hash` | Hashed password. |
| `admin` | Indicates whether the user has administrator privileges. |

The database is automatically initialized when the application starts.

## Security Considerations

This project was developed as a learning exercise in authentication, database management, and password handling.

- Passwords are not directly stored in plaintext.
- Individual salts are generated for user passwords.
- A pepper is used as an additional hashing input.
- SQLite parameterized queries are used for database operations.

**This project is not intended for production use.**

The current implementation uses SHA-256 directly for password hashing, which is not suitable for modern production authentication systems. Password storage should use dedicated password hashing algorithms such as Argon2id, bcrypt, or scrypt. Additionally, the pepper should be stored outside the source code.

## Purpose

This project was developed to practice Python programming, modular code organization, database integration, authentication workflows, and basic security concepts.

---

Developed by [Agst2k7](https://github.com/Agst2k7)
