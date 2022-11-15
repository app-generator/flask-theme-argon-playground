# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# App modules
from apps import app

@app.route('/')
def hello_world():
    return 'Hello, World!'

