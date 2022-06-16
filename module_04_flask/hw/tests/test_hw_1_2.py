"""
Для каждого поля и валидатора в endpoint /registration напишите по unit-тесту,
    который проверит, что валидатор и правда работает (т.е. мы должны проверить,
    что существует набор данных, которые проходят валидацию, и такие,
    которые валидацию не проходят)
"""
import unittest
from python_advanced.module_04_flask.hw.hw_1_2 import registration, app
import requests
import os



class TestRegistration(unittest.TestCase):
    def setUp(self):
        app.config["WTF_CSRF_ENABLED"] = False
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'
        self.app = app.test_client()


    def test_missing_field_user_registration_error(self):

        upload_url = '/registration'
        post_data = {'name':'sss','phone':2122,'address':'hhhh','email':'ssss@mail.ru','index':22,'comment':"sdsd"}
        #Правильный вариант(тест когда все правильно)
        response1 = self.app.post('/registration',data=dict(name='sss',phone=9282221212,address='hhhh',email='george_dyatchkov@mail.ru',index=22,comment="sdsd"))
        response1_text = response1.data.decode()
        #далее тесты с неправильными значениями
        #Нет комента,адрес и имя по аналогии
        response2 = self.app.post('/registration', data=dict(name='sss', phone=9282221212, address='hhhh',
                                                             email='george_dyatchkov@mail.ru', index=22))
        response2_text = response2.data.decode()
#Неправильный телефон
        response3 = self.app.post('/registration',data=dict(name='sss',phone=9282221212222,address='hhhh',email='george_dyatchkov@mail.ru',index=22,comment="sdsd"))
        response3_text = response3.data.decode()
#Неправильный эмейл
        response4 = self.app.post('/registration', data=dict(name='sss', phone=9282221212, address='hhhh',
                                                             email='gssssss', index=22,
                                                             comment="sdsd"))
        response4_text = response4.data.decode()




        self.assertEqual(str(response1_text),f'Successfully registered user george_dyatchkov@mail.ru with phone +79282221212')
        self.assertNotEqual(str(response2_text),
                        f'Successfully registered user george_dyatchkov@mail.ru with phone +79282221212')
        self.assertNotEqual(str(response3_text),
                          f'Successfully registered user george_dyatchkov@mail.ru with phone +79282221212')
        self.assertNotEqual(str(response4_text),
                            f'Successfully registered user george_dyatchkov@mail.ru with phone +79282221212')







if __name__ == '__main__':
    unittest.main()