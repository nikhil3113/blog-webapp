from os import environ # this line should go at the top of your file
from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)