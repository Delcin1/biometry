from app import *
from dbmodels import *
import unittest
from sqlalchemy import create_engine
client = app.test_client()

class TestApp(unittest.TestCase):
    def test_db(self):
        conn = create_engine("postgresql://user:example@localhost/biometry")
        self.assertIsNotNone(conn.connect())

    def test_flask(self):
        resp = client.get('/')
        self.assertEqual(resp._status_code, 200)    

if __name__ == '__main__':
    unittest.main()