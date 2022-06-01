from app import *
#from dbmodels import *
import unittest

client = app.test_client()

class TestApp(unittest.TestCase):
#    def test_db():

    def test_flask(self):
        resp = client.get('/')
        self.assertEqual(resp._status_code, 200)    

if __name__ == '__main__':
    unittest.main()
