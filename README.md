# DUAD Bootcamp Exercises

My coursework from the **DUAD** software development bootcamp: Python fundamentals, object-oriented programming, data structures and algorithms, unit testing, web/HTTP fundamentals, and SQL. Each module was delivered on its own branch and merged into the default branch through a pull request.

> Some code comments and module notes are in Spanish (the bootcamp language); code and identifiers are mostly in English.

## Highlights

- **Gestor Finanzas**: a desktop personal-finance manager with a FreeSimpleGUI interface, JSON persistence, and unit tests. It later became my web app **[finance-tracker-flask](https://github.com/coderblockch/finance-tracker-flask)** (Flask + SQLite + pytest).
- **Student Control System**: a menu-driven CLI app (procedural version, then refactored to OOP) with input validation and CSV import/export.
- **Data structures from scratch**: stack, deque, and binary tree built with linked nodes.
- **31 unit tests** with `unittest` across the testing modules, all passing.
- **SQL**: an e-commerce schema (MySQL) and a SQLite database with `CREATE`, `INSERT`, `ALTER`, and `SELECT` exercises.

## Repository Structure

```
duad-exercises/
├── DUAD/
│   ├── Python Basico/
│   │   ├── CSV/                    # write video-game records to CSV (comma and tab delimited)
│   │   ├── JSON/                   # read, append, and save Pokémon data in a JSON file
│   │   └── Proyecto Final/         # Student Control System (CLI)
│   ├── Python Intermedio/
│   │   ├── bus.py, circle.py, human.py, student.py   # intro OOP: classes and composition
│   │   ├── EOOP/                   # OOP, data structures, algorithms
│   │   ├── Unit Tests/             # small functions + unittest test suites
│   │   ├── Proyecto Estudiantes OOP/   # Student Control System refactored with a Student class
│   │   └── Gestor Finanzas/        # Personal finance manager (GUI + JSON + tests)
│   └── El Internet/
│       └── fundamentos-internet/   # written report on HTTP, DNS, APIs + Postman collection
└── bases-de-datos/
    ├── ecommerce.sql               # MySQL e-commerce schema with foreign keys
    └── sql-exercises/              # SQLite: create, insert, alter, select (+ store.db)
```

## Modules

### Python Basics (`DUAD/Python Basico`)

| Folder | What it covers |
|--------|----------------|
| `CSV/` | Reading user input and writing records with the `csv` module, including a tab-delimited version and a refactor into functions |
| `JSON/` | Loading a JSON file, adding a new Pokémon from user input, and saving it back (`json.load` / `json.dump`) |
| `Proyecto Final/` | **Student Control System**: add students with grades for four subjects, list all students, view the top 3, compute the general average, and export/import CSV. Input validation for grades (0–100) and counts. Split into `main.py`, `menu.py`, `actions.py`, and `data.py`. |

### Intermediate Python (`DUAD/Python Intermedio`)

| Folder / file | What it covers |
|---------------|----------------|
| `bus.py`, `circle.py`, `human.py`, `student.py` | First classes: a bus with a passenger limit, a circle's area, composition (a human built from head, torso, arms, and legs), and a student's grade average |
| `EOOP/bank_account.py` | Inheritance: `BankAccount` and a `SavingsAccount` that enforces a minimum balance |
| `EOOP/shapes.py` | Abstract base class `Shape` (`abc`) with `Square`, `Circle`, and `Rectangle` |
| `EOOP/multiple_inheritance.py` | Multiple inheritance: a `Smartphone` that combines email, push, and messenger classes |
| `EOOP/decorators.py` | Decorators: debug logging, a numbers-only argument check, and an adults-only check |
| `EOOP/stack.py`, `deque.py`, `binary_tree.py` | Data structures built from scratch with node classes |
| `EOOP/bubble_sort.py`, `bubble_sort_reverse.py` | Bubble sort with list-type validation, plus a variant that scans from right to left |
| `EOOP/big_o_analysis.py` | Big O analysis of several functions, with the reasoning written in comments |
| `Unit Tests/` | Functions (sum a list, reverse a string, count upper/lower case, sort hyphen-separated words, find primes) plus bubble sort, each with a `unittest` suite |
| `Proyecto Estudiantes OOP/` | The Student Control System refactored to use a `Student` class |
| `Gestor Finanzas/` | **Personal Finance Manager**: `Category`, `Movement`, and `FinanceManager` classes (income, expenses, balance), a FreeSimpleGUI desktop interface, JSON persistence, and tests for the logic |

### Internet Fundamentals (`DUAD/El Internet/fundamentos-internet`)

A written report (in Spanish) explaining what happens between typing a URL and seeing the page (DNS, TCP, TLS/HTTPS, HTTP request/response), how frontend and backend communicate, REST vs SOAP vs GraphQL, and a hands-on API exploration with **Postman** (GET, POST, PUT, and DELETE against JSONPlaceholder). The exported Postman collection is included.

### Databases (`bases-de-datos`)

- `ecommerce.sql`: MySQL schema for an online store (products, invoices, products per invoice, shopping cart, cart products) with foreign-key constraints.
- `sql-exercises/`: the same model in **SQLite**: `01_create_tables.sql`, `02_insert_data.sql`, `03_alter_tables.sql` (adds buyer phone and cashier code to invoices), and `04_selects.sql` (filters, `GROUP BY` with `SUM`, `ORDER BY`, and lookups). `store.db` is the resulting database.

## Running the Code

Requires **Python 3.10+**.

```bash
git clone https://github.com/coderblockch/duad-exercises.git
cd duad-exercises

# Run a CLI project (scripts read and write files in their own folder)
cd "DUAD/Python Basico/Proyecto Final"
python3 main.py
```

Run the unit tests from inside each folder:

```bash
cd "DUAD/Python Intermedio/Unit Tests" && python3 -m unittest      # 19 tests
cd "../EOOP" && python3 -m unittest                                # 4 tests
cd "../Gestor Finanzas" && python3 -m unittest                     # 8 tests
```

The finance manager's GUI needs FreeSimpleGUI:

```bash
pip install FreeSimpleGUI
cd "DUAD/Python Intermedio/Gestor Finanzas"
python3 interface.py
```

Try the SQL exercises with the SQLite CLI:

```bash
cd bases-de-datos/sql-exercises
sqlite3 store.db < 04_selects.sql
```

## Author

**David Jimenez**, Sacramento, CA · [GitHub @coderblockch](https://github.com/coderblockch) · [Portfolio](https://portfolio-bay-nine-59.vercel.app)
