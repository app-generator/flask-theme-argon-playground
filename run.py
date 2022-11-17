# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# from apps import app
from argon_app import app

DEBUG = app.config['DEBUG'] 

app.logger.info('DEBUG            = ' + str( DEBUG )                 )
app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE' )

if __name__ == "__main__":
    app.run()
