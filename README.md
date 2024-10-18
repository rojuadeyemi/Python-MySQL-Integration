# Python-MySQL Integration

The aim of this project is to demonstrate how Python can be integrated with a MySQL to perform various operations such as database creation, data retrieval, manipulation, and analysis. This will involve creating a MySQL database, setting up tables, inserting data, and using Python to query and update the database.


The Program:

1. Connects to a database.
1. Does all form of query statements.
1. Imports csv data into a database.


## Installation

### Prerequisites

- Python 3.10 - 3.13
- Pip (Python package installer)

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/rojuadeyemi/Python-MySQL-integration.git
    cd Python-MySQL-integration
    ```

2. **Create a virtual environment:**

You can use the provided `Makefile` to create a virtual environment by running `make` or `make all`.

You can also create a virtual environment manually using the following approach.

For *Linux/Mac*:

```sh
python -m venv .venv
source .venv/bin/activate 
```

For *Windows*:
    
```sh
python -m venv .venv
.venv\Scripts\activate
```

3. **Install the required dependencies:**

    ```sh
    pip install -U pip
    pip install -r requirements.txt
    ```
*Note: if you use `make`, you do not need to run the above*

4. **Activate the environment:**

Run the below, to activate the environment

    make activate
    

## Usage

### Running the Program

To run the *Program*, you can use the command `make run`. You can also use the following commands:

```sh
python main.py
```
