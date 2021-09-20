from django.shortcuts import render
from django.views import View
import json
from .models import requestForm, responseForm
from form import models
from . import validation

class Registration(View):
    def get(self,request):
        return render(request, 'home.html', {'name':'welcome to request submission form'})
    def post(self,request):

        req = requestForm()
        res = responseForm()
        data= []
        data.append(request.POST['f1'])
        data.append(request.POST['f2'])
        data.append(request.POST['f3'])
        data.append(request.POST['f4'])
        data.append(request.POST['f5'])
        data.append(request.POST['f6'])
        data.append(request.POST['f7'])
        data.append(request.POST['f8'])
        data.append(request.POST['f9'])
        data.append(request.POST['f10'])
        data.append(request.POST['f11'])
        user = validation.UserDataInput(data)
        user.validate_details()
        req.first_name = user.data[0]
        req.last_name = user.data[1]
        req.DOb = user.data[2]
        req.gender = user.data[3]
        req.Nationality = user.data[4]
        req.State = user.data[5]
        req.Current_city = user.data[6]
        req.pin_code = user.data[7]
        req.Qualification = user.data[8]
        req.salary = user.data[9]
        req.pan_number = user.data[10]
        req.save()

        res.request_id = requestForm.objects.latest('id').id
        res.response = user.result
        res.reason = user.reason

        res.save()

        response_dict = {}
        if res.response == "success":
            response_dict["Request_id"] = res.request_id
            response_dict["Response"] = res.response
        elif res.response == "failure":
            response_dict["Request_id"] = res.request_id
            response_dict["Response"] = res.response
            response_dict["Reason"] = res.reason
        json_dump = json.dumps(response_dict)


        return render(request, 'result.html', {'json': json_dump})