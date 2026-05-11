def dictt():
    
    di = {}
    
    comments = {
        "hello": "hy",
        "how are you": "i am fine",
        "what are doing": "nothing",
        "acha": "hmm"
    }
    
    for idx, val in enumerate(comments.values()):
        
        di[idx] = val   # index key ban gaya
        
    print(di)

dictt()