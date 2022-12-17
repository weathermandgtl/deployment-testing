from app import app
from app.routes import home
import os
# from dotenv import load_dotenv
#
# load_dotenv()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


