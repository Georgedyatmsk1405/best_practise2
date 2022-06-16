import unittest
import datetime
from python_advanced.module_03_ci_culture_beginning.homework.hw_3_2 import app

storagetest={}
storagetest[1]={'year':2022,'month':'12','day':13,'finance':123}

class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/add/'+str(storagetest[1]['year'])+str(storagetest[1]['month'])\
                        +str(storagetest[1]['day'])+'/'+str(storagetest[1]['finance'])

    def test_url(self):
        urlfirst='/add/'+str(storagetest[1]['year'])+str(storagetest[1]['month'])\
                        +str(storagetest[1]['day'])+'/'+str(storagetest[1]['finance'])
        failurl='add/22222222/22/22'
        urlsecond = '/calculate/'+str(storagetest[1]['year'])
        urlthird='/calculate/'+str(storagetest[1]['year'])+'/'+str(storagetest[1]['month'])

        response1 = self.app.get(urlfirst)
        response2 = self.app.get(urlsecond)
        response3 = self.app.get(urlthird)

        self.assertEqual(str(response1),'<Response streamed [200 OK]>')
        self.assertEqual(str(response2), '<Response streamed [200 OK]>')
        self.assertEqual(str(response3), '<Response streamed [200 OK]>')
        datachek=self.base_url.split('/')
        datachekyear=datachek[2]
        self.assertTrue(len(datachekyear[0:4])==4)
        self.assertTrue(len(datachekyear[4:6]) == 2)
        self.assertTrue(int(datachekyear[4:6])>0 and int(datachekyear[4:6])<13)
        self.assertTrue(len(datachekyear[6:8]) == 2)
        self.assertTrue(int(datachekyear[6:8]) > 0 and int(datachekyear[6:8]) < 31)







if __name__ == '__main__':
    unittest.main()