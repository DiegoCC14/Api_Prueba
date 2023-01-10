import pathlib

from .Service.jsonSMS_service import save_json_data

from django.http import JsonResponse
from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


DIR_ACTUAL = pathlib.Path(__file__).parent.absolute() #La direccion actual


@method_decorator( csrf_exempt , name='dispatch' )
class Entrada_Mensajes( View ):
    
    def post( self , request ):
        
        dicc_request = request.POST.dict()

        save_json_data( dicc_request , "fileSMS" , DIR_ACTUAL/"Service" )
        return JsonResponse( {} )
