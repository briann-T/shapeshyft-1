#takes in parameters such as age, gender, fitness goals, bmi, sleep and water log
def water_rec(w_in_glass):
    if(w_in_glass<3):
        rec="It is highly recommended to add more glasses of water into your daily activities."
    elif(3<=w_in_glass<5):
        rec="You're making good progress, keep drinking more glasses of water."
    elif(5<=w_in_glass<7):
        rec="Almost there! Drink some more water."
    elif(7<=w_in_glass<=9):
        rec="Good job! You have met the daily recommended amount of water"
    elif(w_in_glass>9):
        rec="Be careful, drinking too much water can cause hyponatremia. You should only drink water when you are feeling thirsty." 
    return rec

def sleep_rec(age,hrs):
    if(6<=age<=12):
        #9-12 hrs
        if(0<=hrs<7):
            rec="It is highly recommended that you should get more hours of sleep."
        elif(7<=hrs<9):
            rec="You may need more hours of sleep."
        elif(9<=hrs<=12):
            rec="You are getting a sufficient amount of sleep."
        else:
            rec="You are getting more hours of sleep than recommended for your age."
        return 
    elif(13<=age<=18):
        #8-10 hrs
        if(0<=hrs<5):
            rec="It is highly recommended that you should get more hours of sleep."
        elif(5<=hrs<8):
            rec="You may need more hours of sleep."
        elif(8<=hrs<=10):
            rec="You are getting a sufficient amount of sleep."
        else:
            rec="You are getting more hours of sleep than recommended for your age."
    elif(age>18):
        #7-9 hrs
        if(0<=hrs<5):
            rec="It is highly recommended that you should get more hours of sleep."
        elif(5<=hrs<7):
            rec="You may need more hours of sleep."
        elif(7<=hrs<=9):
            rec="You are getting a sufficient amount of sleep."
        else:
            rec="You are getting more hours of sleep than recommended for your age."

    return rec