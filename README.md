# Threats Assignment

- The frontend UI is served by React + Vite
  - It calls the backend API and tries to render the returned paginated records
- The backend API is served by Python + Flask
  - It has an endpoint `GET /api/threats/` with optional params `?page=<int>&limit=<int>`
  - Calls the urlhaus-api and returns extracted threat data as a list

## Setup & Installation

**Ensure python3, pip, and npm are installed in your Linux environment.**

Clone the repository:

```bash
git clone https://github.com/Brochin5671/threats-assignment.git
cd threats-assignment
```

Install requirements for the frontend:

```bash
cd frontend
npm install
cd ..
```

Create and activate a virtual environment for the backend API:

```bash
cd backend
python3 -m venv env
source env/bin/activate
```

Install requirements for the backend API:

```bash
pip install -r requirements.txt
cd ..
```

Run the backend API in a seperate terminal:

```bash
cd backend
python3 main.py
```

The backend will be available at `localhost:5000`.

Run the frontend in a seperate terminal:

```bash
cd frontend
npm run build
npm run preview
```

The frontend will be available at `localhost:8000`.

### Tests

Run tests for the frontend:

```bash
cd frontend
npm run test
cd ..
```

Run tests for the backend API:

```bash
cd backend
pytest
cd ..
```

## Assumptions & Limitations

- Assuming a Linux environment with `python3`, `pip`, and `npm` installed.
- Backend API:
  - Rate-limit of 1 request per second
  - Assuming I will be dealing with a small amount of data from urlhaus-api (states limit is 1000 records)
- Frontend:
  - Not optimized to cache requests or serve the UI from build
