from flask import redirect, render_template
from app import admin_ui_service

@admin_ui_service.route('/')
def index():
    return redirect('/login')


@admin_ui_service.route('/login')
def login():
    return render_template('login.html')
