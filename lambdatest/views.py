from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import InputParam

def index(request):

    params = {
        'htitle':'ichiA Django',
        'title':'Lambda接続テスト',
        'message':'Lamda戻り',
        'content_text': 'ボタンを押すとlambdaの戻り値が来ます',
        'form1' : InputParam(),
        }

    if (request.method == 'POST'):

        headers = {'x-api-key': 'aspijTnwG7MXJwVBzAbM3IxJ8Vp73AI2Ya5OSEv5'}
        x = request.POST['Param1']
        y = request.POST['Param2']
        val = {"x" : x , "y" : y}
        url = "https://3dul2tnnsg.execute-api.us-east-2.amazonaws.com/KK_Test/HelloLambda"

        #api_val = requests.get(url, params = val , headers=headers)
        api_val = requests.post(url, params = val , headers=headers)

        params['content_text'] = api_val.text
        params['form1'] = InputParam()
        return render(request, 'lambdatest/index.html',params) 

    else:
        params['content_text'] = 'ボタンを押すとlambdaの戻り値が来ます（未呼び出し）'
        return render(request, 'lambdatest/index.html',params) 
        
