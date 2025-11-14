# test_examples
Some examples how to test using pytest

## Installation
```bash
git clone https://github.com/Practical-Python-Development/test_examples.git
cd test_examples
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Just run tests
```bash
pytest
```

Check how much code is covered by tests
```bash
pytest --cov
```

Generate an interactive website to check which part of the code is not tested
```bash
pytest --cov --cov-report=html
```