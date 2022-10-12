from web import create_app
from flasgger import Swagger

app = create_app()
app.config['SWAGGER'] = {
    'title': 'Crypto server',
    'uiversion': 3,
    'openapi': '3.0.3',
    'template_file': 'swagger.yml',
}
Swagger(app, template_file='swagger.yml')

if __name__ == '__main__':
    app.run(host="localhost", port=8005)