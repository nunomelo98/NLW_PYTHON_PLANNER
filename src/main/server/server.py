from flask import Flask
from src.main.routes.trips_routes import trips_reoutes_bp
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

#configuration of swagger
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Trip Planner app"
    }
)

app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

# @app.route('/api/docs/swagger.json')
# def swagger_json():
#     return send_from_directory(app.static_folder, 'swagger.json')
# Registrar seu blueprint
app.register_blueprint(trips_reoutes_bp)


