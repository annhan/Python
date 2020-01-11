# -*- coding: utf8 -*-

from MySQL import *
from webflask import runningFlask , app
#import Variable

if __name__ == '__main__':
    load_database()
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0',port=8080,debug=True,use_reloader=False)
    #runningFlask()