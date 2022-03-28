# Admin-UI
O objetivo desse projeto e oferecer uma interface para criacao de notícias.

# Tecnologia
Python 3.6 ou superior. Link para donwload e instalação: https://www.python.org/downloads/

# Montando um Ambiente
Esses procedimentos devem ser feitos na raiz do projeto, e são exemplos em ambiente `Unix/Mac`.
1. Como criar [virtual environments](https://docs.python.org/3/library/venv.html)  
    ```
    python3 -m pip install virtualenv
    ```
2. Criando um ambiente virtual   
    ```
    python3 -m venv venv && source venv/bin/activate
    ```
3. Instalando dependências
    ```
    pip install -r requirements.txt
    ```
    As dependências usanda nesse projeto são:
    ```
    click==8.0.4
    distlib==0.3.4
    filelock==3.6.0
    Flask==2.0.3
    gunicorn==20.1.0
    itsdangerous==2.1.1
    Jinja2==3.0.3
    MarkupSafe==2.1.1
    platformdirs==2.5.1
    six==1.16.0
    virtualenv==20.13.4
    Werkzeug==2.0.3
    ```

# Desenvolvimento
```
python run.py
```

# Produção
```
gunicorn --bind 0.0.0.0:5000 "run:admin_ui_service" --worker-class=gthread --threads=4 -w 4
```
