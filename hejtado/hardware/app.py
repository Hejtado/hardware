import os
import connexion

def create_app():
    """Create Flask (connexion) app"""

    spec_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'openapi')
    app = connexion.FlaskApp(__name__, specification_dir=spec_dir)
    app.add_api('openapi.yaml')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run

