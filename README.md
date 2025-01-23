# Python in CI/CD Github Action

```yaml
name: Python

on:
  push:
    branches:
      - master

jobs:
  run-python-script:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v5 
        with:
          python-version: '3.10'
      
      - name: Run Python script
        run: python main.py
```
