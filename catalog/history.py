from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        recent_list= request.session.get('last_five',[])
        request.last_five=[]

        for p in recent_list:
            request.last_five.append(cmod.Product.Objects.get(id=p))

        response = self.get_response(request)

    

        last_five_ids = []
        for r in request.last_five:
            last_five_ids.append(r.id)

        request.session['last_five'] = last_five_ids



        return response
