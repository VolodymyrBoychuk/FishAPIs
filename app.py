from flask import Flask
from flask_smorest import Api
from resources.session import blp as SessionBlueprint
from resources.statistic import blp as StatisticBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Session REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)


api.register_blueprint(SessionBlueprint)
api.register_blueprint(StatisticBlueprint)


if __name__ == "__main__":
    app.run(debug=True)