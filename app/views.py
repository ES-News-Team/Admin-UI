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
        return redirect('/crud-noticias')

    return render_template('login.html')


# ======================= crud-noticias =======================
@admin_ui_service.route('/crud-noticias', methods=('GET', 'POST'))
def postar_noticia():
    if request.method == 'POST':
        logger.info({**request.form})

    return render_template('post_news.html')

