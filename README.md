# Mini Data Warehouse - Vendas

A small data warehouse implementation for sales analysis using Python and PostgreSQL.

## Project Structure
```
mini_dw_vendas/
├── data/             
├── etl/               
├── sql/              

## Prerequisites
- Python 3.8+
- PostgreSQL
- pip

## Installation

1. Clone the repository
```bash
git https://github.com/ismaelfranklin/data-warehouse-creation.git
cd mini_dw_vendas
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
Create a `.env` file with:
```
DB_HOST=localhost
DB_NAME=dw_vendas
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432
```

## Usage

1. Create database schema:
```bash
psql -U postgres -d dw_vendas -f sql/schema.sql
```

2. Run ETL process:
```bash
python etl/etl_runner.py
```


## Database Model

```mermaid
flowchart TD
    CSV1[(clientes.csv)]
    CSV2[(produtos.csv)]
    CSV3[(vendas.csv)]
    E1[Extract Data]
    T1[Transform Cliente]
    T2[Transform Produto]
    T3[Transform Vendas]
    V1{Validate}
    L1[Load Dimensions]
    L2[Load Facts]
    DB[(PostgreSQL DB)]
    END[Complete]

    CSV1 & CSV2 & CSV3 --> E1
    E1 --> T1 & T2 & T3
    T1 & T2 & T3 --> V1
    V1 -->|Valid| L1
    V1 -->|Invalid| END
    L1 --> L2
    L2 --> DB
    L2 --> END
```

## License
MIT
