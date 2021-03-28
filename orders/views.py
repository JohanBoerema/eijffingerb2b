from django.shortcuts import render
import json
import requests


def get_orderlines(request):
  s = requests.Session()
  s.post('https://ebv.ignitar.com:50000/b1s/v2/Login', json={'UserName':'manager1', 'Password': 'Domani01', 'CompanyDB': 'TEST_EIJFFINGER_LOG'}, verify=False)

  result_orderlines = s.get('https://ebv.ignitar.com:50000/b1s/v2/Orders?$select=DocNum,DocDate&$filter=CardCode eq \'538490000\' and DocumentStatus eq \'bost_Open\'', verify=False)
  orderlines = result_orderlines.json().get("value")

  context = {"orders" : orderlines}
  return render(request, "orders/orderlines.html", context)

