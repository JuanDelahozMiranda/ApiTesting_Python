"""
Creado por: Juan Pablo De la Hoz Miranda
https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index
"""
import unittest 
import requests
import json

class ApiTestingCase(unittest.TestCase):
    global BASE_URL
    global ORDEN_SUCCESS
    global PARAMETER

    BASE_URL = "https://petstore.swagger.io/v2/store/order/"
    ORDEN_SUCCESS = "77"
    PARAMETER = {'id': ORDEN_SUCCESS,'petId': ORDEN_SUCCESS, 'quantity': '3','shipDate': '2021-03-17','status': 'placed', 'complete': 'false'}

    def testRequestPostSuccess(self):
        print('Prueba 1 - consumo API Post \n')
        lenBase = len(BASE_URL)-1

        response = requests.post(url=BASE_URL[0:lenBase], json=PARAMETER, headers={"Content-Type":"application/json"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')


class ApiTestingCase2(unittest.TestCase):

    global BASE_URL
    global ORDEN_FAIL
    global ORDEN_SUCCESS

    BASE_URL = "https://petstore.swagger.io/v2/store/order/"
    ORDEN_FAIL = "70"
    ORDEN_SUCCESS = "70"
    
    def testGet1_Success(self):
        print('Prueba 2 - consumo API Get Success + Body \n')
        response = requests.get(BASE_URL+ORDEN_SUCCESS)
        response_body = response.json()

        self.assertEqual(response_body["id"], int(ORDEN_SUCCESS))
        self.assertEqual(response_body["petId"], int(ORDEN_SUCCESS))
        self.assertEqual(response_body["quantity"], 3)
        self.assertEqual(response_body["shipDate"][0:10], '2021-03-17')
        self.assertEqual(response_body["status"], 'placed')
        self.assertFalse(response_body["complete"])

    def testGet2_Fail(self):
        print('Prueba 3 - consumo API GET Fail \n')
        response = requests.get(BASE_URL+ORDEN_FAIL)
        response_body = response.json()
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_body["code"], 1)
        self.assertEqual(response_body["type"], 'error')
        self.assertEqual(response_body["message"], 'Order not found')

    def testRequestDelete1(self):
        print('Prueba 4 - consumo API Delete Success + Body \n')
        response = requests.delete(BASE_URL+ORDEN_SUCCESS)
        response_body = response.json()

        self.assertEqual(response_body["code"], 200)
        self.assertEqual(response_body["type"], 'unknown')
        self.assertEqual(response_body["message"], ORDEN_SUCCESS)

    def testRequestDelete2(self):
        print('Prueba 5 - consumo API Delete Fail + Body \n')
        response = requests.delete(BASE_URL+ORDEN_FAIL)
        response_body = response.json()

        self.assertEqual(response_body["code"], 404)
        self.assertEqual(response_body["type"], 'unknown')
        self.assertEqual(response_body["message"], 'Order Not Found')

if __name__ == '__main__':
    unittest.main(verbosity=2)
