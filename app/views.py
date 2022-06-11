from re import sub
from app.utils.logger import logger
from flask import redirect, render_template, request
from app import admin_ui_service
import requests as req


# ======================= index =======================
@admin_ui_service.route('/')
def index():
    return redirect('/login')


# ======================= login =======================
@admin_ui_service.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        logger.info({**request.form})
        response = req.post('http://127.0.0.1:5002/authenticate', json={
            "email": username, 
            "password": password
        })

        print(response)
        print(response.status_code)

        if response.status_code == 200: 
            return redirect('/criar-noticias')
        else:
            return redirect('/login')
            
        

    return render_template('login.html')


# ======================= criar-noticias =======================
@admin_ui_service.route('/criar-noticias', methods=('GET', 'POST'))
def postar_noticia():
    if request.method == 'POST':
        title = request.form['title']
        type = request.form['type']
        image = request.form['image']
        content = request.form['content']
        logger.info({**request.form})
        print(title, type, image, content)
        response = req.post('http://127.0.0.1:5002/news/', json={
            "title": title,
            "type": type,
            "image": image,
            "content": content
        })
        print(response.status_code)

        if response.status_code == 201: 
            return redirect('/criar-noticias')
        else:
            return redirect('/login')
    
    return render_template('create_news.html')


# ======================= updel-noticias =======================
@admin_ui_service.route('/updel-noticias', methods=('GET', 'POST'))
def atualiza_deletar_noticias():

    response = req.get('http://127.0.0.1:5002/news/', timeout=3)
    data = response.json()
    print(data)

    if request.method == 'POST':
        logger.info({**request.form})
        id = request.form['id']
        title = request.form['title']
        type = request.form['type']
        image = request.form['image']
        content = request.form['content']
        submit = request.form['submit']
        logger.info({**request.form})
        print(title, type, image, content)
        if submit == 'delete':
            response = req.delete(f'http://127.0.0.1:5002/news/{id}')
            print(response.status_code)
            return redirect('/updel-noticias')
        else:
            response = req.put(f'http://127.0.0.1:5002/news/{id}', json={
            "title": title,
            "type": type,
            "image": image,
            "content": content
            })
            print(response)
            return redirect('/updel-noticias')
        
    return render_template('update_delete_news.html', **data)

