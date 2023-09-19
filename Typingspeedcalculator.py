from time import *
import random 


def mistake(paragraph,userinput):
    error =0
    for i in range(len(userinput)):
        try:
            if userinput[i] != paragraph[i]:
                error = error + 1
        except:
            error = error + 1
    return error


def speedtime(time_start,time_end,user_input):
    time_delay=time_end - time_start
    time_round=round(time_delay,2)
    speed = len(user_input) / time_round
    return round(speed)

test =["i am batman","i am iron man"]
test1=random.choice(test)
print("****** typing speed ******")
print(test1)
print()
time1=time()
testinput=input(" Enter : ")
time2=time()

print('speed :', speedtime(time1,time2,testinput),"W/sec" )
print("Error :" ,mistake(test1,testinput))

