import json

def GetBody(request):
    #decode request
    unicode = request.body.decode('utf-8')
    # turn unicode string into dict
    return json.loads(unicode)