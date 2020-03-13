from flask_testing import TestCase

from Blogger import create_app as application
from Blogger import db


class BaseTestCase(TestCase):
    """ A Base Test Case"""

    def create_app(self):
        app = application(**{
            'SECRET_KEY': "mysuppersecretkey",
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///blogger.db'
        })
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
