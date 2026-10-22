# Booking API Test Framework

[![CI](https://github.com/lytvakdmytro/booking-api-test-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/lytvakdmytro/booking-api-test-framework/actions/workflows/ci.yml)

API test automation framework for [Restful Booker](https://restful-booker.herokuapp.com/), built with Python, pytest and Requests.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/lytvakdmytro/booking-api-test-framework.git
   cd booking-api-test-framework
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate it:
   ```bash
   # Windows
   .venv\Scripts\activate

   # macOS / Linux
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Tests run against the public Restful Booker instance by default. To point them at another instance, set the `BASE_URL` environment variable:

```bash
# Windows (PowerShell)
$env:BASE_URL = "http://localhost:3001"

# macOS / Linux
export BASE_URL=http://localhost:3001
```

## How to run the full suite

```bash
pytest
```

## How to run specific tests

Run a single file:
```bash
pytest tests/api/test_health.py
```

Run a single test:
```bash
pytest tests/api/test_health.py::TestHealth::test_health
```

Run tests matching a keyword:
```bash
pytest -k health
```

## Linting with ruff

Check for issues:
```bash
ruff check .
```

Auto-fix what can be fixed safely:
```bash
ruff check . --fix
```

Format the code:
```bash
ruff format .
```

## Known issues

- `GET /ping` returns `201 Created`, although `200 OK` would be the expected status for a health check that creates nothing. The docs are inconsistent too: the section header says "Success 200", while the field description and the response example say 201. Tests assert the actual behavior (201).