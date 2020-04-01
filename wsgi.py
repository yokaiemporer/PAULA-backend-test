from plotdt import app
from waitress import serve
import os
port = int(os.environ.get('PORT', 5000))
if __name__ == "__main__":
    #app.run()
    serve(app, host='0.0.0.0', port=port)