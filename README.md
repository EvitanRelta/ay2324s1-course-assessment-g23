# Assignment 2

## Setup instructions

### Setup database
- Install Postgres 14.9
- Start up and login to postgres (either psql or pgAdmin 4)
- Create a database named `cs3219-assignment-2`
- In the created database, run the query file: `database/init.sql`
- Update the values in the repo's `.env` file to match your Postgres configuration. \
  Specifically, these Postgres env variables:
  ```properties
  POSTGRES_HOST
  POSTGRES_PORT
  POSTGRES_USER
  POSTGRES_PASSWORD
  ```

<br>

### Setup/Start backend
- Install Python 3.11.5.

  If you're using Anaconda, create and activate a new Python 3.11.5 environment:
  ```bash
  conda create -n assignment-2-env python=3.11.5
  conda activate assignment-2-env
  ```

- Install backend dependencies found in `api/requirements.txt`

  ```bash
  pip install -r api/requirements.txt
  ```

- Start backend server using `api/app/start.py` script.

  ```bash
  python api/app/start.py
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
After setting up and starting the database, backend and frontend, the web app will be accessible at: `http://localhost`.
