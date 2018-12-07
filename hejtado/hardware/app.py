import os
import connexion

from connexion.resolver import RestyResolver


#SETTINGS = os.path.join(os.path.dirname(__file__), 'settings.ini')

#if settings is None:
#    settings = SETTINGS


app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('openapi.yaml')
app.run(port=5000, host='127.0.0.1', debug='true')


