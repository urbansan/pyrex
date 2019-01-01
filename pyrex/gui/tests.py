from pyrex import gui
import unittest
import bottle
import os
import webtest
test_app = webtest.TestApp(gui.web_frontend)

routes = {
    'index': '/',
    'contract_list': '/contracts',
    'contract_details': '/contract/1230123',
    'contract_trade_details': '/contract/1230123/trade/1230123',
}


def route_test_wrapper(route):
    def fixture(self):
        resp = test_app.get(route)
        assert resp.status_int == 200
        assert resp.content_type == 'text/html'
        assert resp.content_length > 0
    return fixture


class RoutesTest(unittest.TestCase):
    pass


for route_name, route in routes.items():
    setattr(RoutesTest, f'test_{route_name}', route_test_wrapper(route))

#
# class WebappTest(unittest.TestCase):
#     def test_index(self):
#         a = gui.routes.index()
#         print(a)


if __name__ == '__main__':
    unittest.main()