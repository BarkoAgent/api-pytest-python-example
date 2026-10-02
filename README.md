# api-pytest-python-example

Training example: API test automation with Python, pytest and Allure. Runs against the public [Restful-Booker](https://restful-booker.herokuapp.com/apidoc/index.html) API. **No account, sign-up or API key needed.**

This is a teaching project and may contain defects.

## Requirements
- Python 3.9+
- pip
- [Allure](https://allurereport.org/docs/install/) (only to view the report)

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Optional: `cp .env.example .env` to override defaults.

| Variable | Default | Meaning |
|---|---|---|
| `BASE_URL` | `https://restful-booker.herokuapp.com` | API under test |
| `AUTH_USERNAME` | `admin` | Public demo user from the API docs |
| `AUTH_PASSWORD` | `password123` | Public demo password from the API docs |

## Covered
- List booking ids
- Create a booking, validate response against a JSON schema, read it back, delete it (token auth), confirm 404

Every run creates its own uniquely named booking, so parallel and repeated runs do not collide.

## Structure
- `endpoints/` - one class per API area, inherits `APIRequests`
- `helpers/requests.py` - HTTP methods, auth token, schema validation
- `helpers/data_factory.py` - builds per-run test data
- `helpers/configuration.py` - environment-based config
- `test_data/schemas/` - JSON schemas
- `test_booking.py` - tests

## Run
```bash
pytest test_booking.py --alluredir=allure-report/
```

## Report
```bash
allure serve allure-report
```
