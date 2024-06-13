# FastAPI Configuration Management 

## Setup

### Installation

1. Clone the repository and navigate to the project directory:

    ```bash
    git clone https://github.com/yourusername/fastapi-configuration-management.git
    cd fastapi-configuration-management
    ```

2. Create and activate a virtual environment (Linux/macOS):

    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Update the database URL in your environment configuration file:

    ```
    postgresql://postgres:mysecretpassword@localhost/cogoport
    ```

Replace `username`, `password`, and `dbname` with your actual database credentials.

### Running the Application

To start the FastAPI application with automatic reloading during development, use the following command:

```bash
uvicorn main:app --reload
