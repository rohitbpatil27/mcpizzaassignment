## McPizzaAssignment Test Suite

This repository contains automated tests for the McPizzaAssignment project.

**Requirements:**

* Python 3.x
* pip

**Installation:**

1. Clone this repository to your local machine:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd McPizzaAssignment
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

**Running Tests:**

To run the tests, execute the following command:

```bash
pytest -v
```

By default, pytest will discover all files named `test_*.py` or `*_test.py` in the current directory and its subdirectories and execute them.

**Test Reports:**

To generate an HTML test report, you can use the following command:

```bash
pytest --html=report.html
```

This will create an HTML report named `report.html` in the project directory.

**Structure:**

- `conftest.py`: Contains fixtures and configuration settings for the test suite.
- `tests`: Directory containing test cases.
- `pages`: Directory containing page objects and helper functions.
- `utils`:
- `locators.py`: Defines locator constants.
- `logger.py`: Contains logging configuration.
