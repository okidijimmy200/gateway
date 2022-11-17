from flask import Flask
from routers.auth_router import auth_api


app = Flask(__name__) 

app.register_blueprint(auth_api, name='signup')
app.register_blueprint(auth_api, name='login')

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)