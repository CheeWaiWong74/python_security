python -m venv venv
.\venv\scripts\activate

Power shell:
Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope LocalMachine
Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser

pip install:
pip install cryptography
pip install gmpy2

pip freeze > requirements.txt

Reference:
https://cryptography.io/en/latest/

https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm