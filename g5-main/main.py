from website import create_app
#from . import db

#db.create_all()
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


