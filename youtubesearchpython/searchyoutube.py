import youtubesearchpython.main

def searchyoutube(keyword, offset = 1):

    #########https://github.com/alexmercerind#########
    
    result = youtubesearchpython.main.exec(keyword, offset)
    
    if result == "Network Error!":
        return "Network Error!"
    else:
        if len(result[0]) == 0:
            result = searchyoutube(keyword, offset)
        
        return result
