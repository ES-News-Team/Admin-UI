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
        # response = req.post('', data={
        #     "username": request.form['username'], 
        #     "password": request.form['password']
        # })

        # if response.status_code == '200':
        #     # YEAH!!!
        #     pass 
        return redirect('/criar-noticias')

    return render_template('login.html')


# ======================= criar-noticias =======================
@admin_ui_service.route('/criar-noticias', methods=('GET', 'POST'))
def postar_noticia():
    if request.method == 'POST':
        logger.info({**request.form})

    return render_template('create_news.html')


# ======================= updel-noticias =======================
@admin_ui_service.route('/updel-noticias', methods=('GET', 'POST'))
def atualiza_deletar_noticias():
    if request.method == 'POST':
        logger.info({**request.form})

    return render_template('update_delete_news.html', list_of_news = [
        {
            "id": "ec5c011a-6478-4def-99e1-ed58bee20b47",
            "assunto": 'artes',
            "title": "art TITLE",
            "conteudo": "TEXTOTEXTOTEXTOTEXTO..."
        },
        {
            "id": "ceb82e0a-d086-4111-b558-8ce5db910b51",
            "assunto": 'pets',
            "title": "pet TITLE",
            "conteudo": "TEXTOTEXTOTEXTOTEXTO..."
        },
        {
            "id": "54b5ff2b-1f41-4880-8b17-5e78c613f3ba",
            "assunto": 'ciencia',
            "title": "ciencia TITLE",
            "conteudo": "TEXTOTEXTOTEXTOTEXTO..."
        }
    ])

