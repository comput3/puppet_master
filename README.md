# Puppet_Master

Puppet_Master is an advanced Ansible Python project designed for interacting with Oracle databases. It automates the execution of SQL (DML) scripts, leveraging Python for database operations and Ansible for orchestration.

## Project Structure

- `src/`: Contains Python modules for database interactions.
- `sql_scripts/dml/`: Stores individual DML files for database operations.
- `config/`: Configuration files for database settings and DML script variables.
- `ansible/`: Contains Ansible playbooks and roles for orchestrating database operations.
- `logs/`: Output logs of operations.

## Setup

1. **Install Dependencies**:
   - Install Python dependencies listed in `requirements.txt`.
   - Set up Ansible on the control machine.

2. **Configure Database Settings**:
   - Edit `config/db_config.json` with your Oracle database credentials.
   - Note: Do not commit sensitive data to version control.

3. **Configure DML Scripts and Variables**:
   - Place your DML scripts in the `sql_scripts/dml/` directory.
   - Define necessary variables for your DML scripts in `config/dml_variables.json`.

## Running the Project

To run a database operation using Ansible:

1. Navigate to the `ansible/` directory.
2. Execute the Ansible playbook:
   ```bash
   ansible-playbook playbooks/db_update_playbook.yml
