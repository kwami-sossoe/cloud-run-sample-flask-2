import logging
import os
from flask import Flask
from secure import require_apikey


app = Flask(__name__)

@app.route('/health')
def health():
    return 'It is alive!\n'


@app.route('/hello')
@require_apikey
def hello():
    return {'hello': 'world; on the way for leveraging myself on CI/CD pipeline ! '}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
