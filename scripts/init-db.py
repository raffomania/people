import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from people import db
from people.models import User, Profile
from werkzeug.security import generate_password_hash

db.drop_all()
db.create_all()

user = User("00admin", "Admin", "Account", generate_password_hash("plaintextpassword"))
profile = Profile("00admin")
db.session.add(user)
db.session.add(profile)

db.session.commit()