from flask import url_for
from henryjh import create_app
from henryjh.models import About

app = create_app()

@app.context_processor
def about_me():
    about = About.query.filter_by(id=1).first()
    image_file = url_for('static', filename='profile_pics/' + about.image_file)
    return {'about': about,'image_file':image_file}

if __name__ == '__main__':
    app.run(debug=True) 