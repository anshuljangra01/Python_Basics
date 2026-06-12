def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal server Error"
        case _:
            return "Unknown Error"
        
print (http_status(200))        
print (http_status(404))        
print (http_status(500))        
print (http_status(403))        