def split (string):
    LR = []
    block = ""

    for c in string:
        if c != " ":
            block += c
        else:
            if block: 
                LR.append(block)
                block = ""
    
    if block:
        LR.append(block)
    
    return LR

string = "ab c     d ef"
res = split(string)
print(res)


def capitalize (sentence):
    res = ""
    indicator = True

    for c in sentence:
        if indicator and c.isalpha():
            res += c.upper()
            indicator = False
        else:
            res += c

        if c in [".","!","?","..."]:
            indicator = True
    
    return res

sentence = "should we have lunch together? no... ok fine! bye."
res = capitalize(sentence)
print(res)

database = {"mom":"eunsun72","dad":"sungjo68","bro":"jooyoung00","sis":"jiwon03"}

def base(id, password):
    if id in database and database[id] == password:
        print("Database found")
    else:
        print("Incorrect id or password.")

id = "sis" 
password = "jiwon03"
res = base(id,password)
