# Assignment 3

## Setup instructions

- Download the `.env` file that we've submitted to Canvas CS3219's "Sharing Assignment Private Info" assignment, and place it in the root of the repo.
- Ensure the ports `80`, `8000` and `8001` are available.

<br>

### Setup databases
- Install Postgres 14.9
- Start up and login to postgres (either psql or pgAdmin 4)
- Update the values in the repo's `backend.conf` and `.env` file to match your Postgres configuration. \
  Specifically, these Postgres env variables:
  ```properties
  # In `backend.conf`:
  POSTGRES_HOST
  POSTGRES_PORT
  POSTGRES_USER

  # In `.env`:
  POSTGRES_PASSWORD
  ```

<br>

#### Setup database for questions
- In the Postgres interface (either psql or pgAdmin 4) create a database named `cs3219-assignment-3-questions`
- In the created database, run the query file: `backend_services/questions_service/database/init.sql`

<br>

#### Setup database for users
- In the Postgres interface (either psql or pgAdmin 4) create a database named `cs3219-assignment-3-users`
- In the created database, run the query file: `backend_services/users_service/database/init.sql`

<br>

### Setup/Start backend
- Install Python 3.11.5.

  If you're using Anaconda, create and activate a new Python 3.11.5 environment:

  ```bash
  conda create -n assignment-3-env python=3.11.5
  conda activate assignment-3-env
  ```

- Install backend dependencies found in `backend_services/requirements.txt`:

  ```bash
  pip install -r backend_services/requirements.txt
  ```

- Install the local package found in the `backend_services/shared_definitions` dir:

  ```bash
  pip install ./backend_services/shared_definitions
  ```

<br>

#### Start questions API server
- Start the questions API server using `backend_services/questions_service/api/app/start.py` script.

  ```bash
  python backend_services/questions_service/api/app/start.py
  ```

<br>

#### Start users API server
- Start the users API server using `backend_services/users_service/api/app/start.py` script.

  ```bash
  python backend_services/users_service/api/app/start.py
  ```

<br>

### Setup/Start frontend
- Install NodeJS 16.13.1

- Navigate to the `frontend` dir

  ```bash
  cd frontend
  ```

- Install frontend dependencies found in `frontend` dir

  ```bash
  npm install
  ```
 
- Start frontend development server:

  ```bash
  npm run dev
  ```

<br>

### Accessing the web app
After setting up and starting the database, API servers and frontend, the web app will be accessible at: `http://localhost`.
