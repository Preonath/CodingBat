def alarm_clock(day, vacation):
    if(not vacation):
        if(day<=5 and day>=1 ):
            return "7:00"
        return "10:00"
    if(vacation):
        if (day <= 5 and day >= 1):
            return "10:00"
    return  "off"

