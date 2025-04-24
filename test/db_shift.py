import unittest
from app import app 
from app.model.shift import Shift


class MyTestDiKa(unittest.TestCase):

    # 200
    def test_add(self):
        testApp = app.test_client(self)
        response = testApp.get('/shift/add', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_Insert_Correctly(self):
        testApp = app.test_client(self)
        response = testApp.post('/shift/add',
                               shift=Shift(stype=3 , status='online' , start='2022-05-09 13:15:13' , end='2022-05-09 16:15:13'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    # 404
    def tset_Edite_Correctly(self):
        testApp = app.test_client(self)
        response = testApp.post('/shift/edit', query_string={'id': 20}, follow_redirects=True)  
        # shift=Shift(stype=3 , status='online' , start='2022-05-09 13:15:13' , end='2022-05-09 16:15:13'),    
        
        self.assertEqual(response.status_code, 404)
        

if __name__ == "__main__":
    unittest.main()
