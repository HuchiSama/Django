from django.http import HttpResponseRedirect, JsonResponse
from django.utils.deprecation import MiddlewareMixin


class Middleware(MiddlewareMixin):

    def process_request(self, request):
        print('process_request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('process_view')
        return self.checkUser(request=request)

    def process_response(self, request, response):
        print('process_response')
        return response
    def process_exception(self, request, exception):
        print('process_exception')
        return JsonResponse({'message': str(exception)}, status=500)

    def checkUser(self, request):
        #cookie方法
        # uid = request.COOKIES.get('uid')
        #session方法
        uid = request.session.get('uid')
        path = request.path
        print(path, 'path')
        if (not uid and 'login' not in path):
            return HttpResponseRedirect('/login')
        return None
