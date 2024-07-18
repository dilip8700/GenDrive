from flask import Blueprint
from app.main import main

@main.route('/')
def index():
    return "Welcome to the API"
