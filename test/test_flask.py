import unittest
from app import app
from flask_testing  import TestCase


# this is the Test that we want to run it 
class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dika.db'
        # what we used for the test 
        self.app = app.test_client()
        
    def tearDown(self):
        pass
    
    # List   
    def test_showAll(self):
        response = self.app.get('/shift/list', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    # Add Function Get / Post 
    def test_add_Get(self):
        response = self.app.get('/shift/add', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_add_Post(self):
        response = self.app.post('/shift/add', follow_redirects=True)
        self.assertEqual(response.status_code, 200) 
    
    # delete Function Found
    def test_delete_get_Found(self):
        response = self.app.delete('/shift/delete/', query_string={'id': 2}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
    def test_Insert_Correctly(self):
        testApp = app.test_client(self)
        response = testApp.post('/shift/add', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
    # edit Function found
    def test_edit_get_Found(self,):
        response = self.app.delete('/shift/edit', query_string={'id': 2}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
  
        
# run Test         
if __name__ == "__main__":
    unittest.main()

