import random


def letters():
    return ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def symbols():
    return ["~","!","@","#","$","%","^","&","*","(",")","_","-","=","+","<",">",".","/","?",";",":","[","]","{","}"]


def nums():
    return list(range(0,10))

def small():
    smletters =[]
    for i in letters():
        smletters.append(i.lower())
    return smletters


passcode1 = random.sample(letters(),1) +  random.sample(symbols(),3)+ random.sample(nums(),2)+random.sample(small(),2)
passcode2 = random.sample(letters(),3) +  random.sample(symbols(),6)+ random.sample(nums(),5) + random.sample(small(),3)
passcode3 = random.sample(letters(),4) +  random.sample(symbols(),9)+ random.sample(nums(),8)+random.sample(letters(),4)+ random.sample(small(),2) +  random.sample(symbols(),9)+ random.sample(nums(),8)+random.sample(small(),2)



def password(x):
    try:
        x=int(x)
        if x <5:
            return "Password can not be less than 5"
        elif x <8:
            return "%s" % ','.join(map(str,random.sample(passcode1,x))).replace(',',"")
        elif x < 11:
            return "%s" % ','.join(map(str,random.sample(passcode2,x))).replace(',',"")
        elif x >=11 and x <= 15:
            return "%s" % ','.join(map(str,random.sample(passcode3,x))).replace(',',"")
        elif x > 15:
            return "Enter a number less than 12"
    except:
        return "Invalid Input"