from datetime import datetime

# initial value
fut = [2025,3,29] # if you use this code, just change this variable [year,month,day]
now = [datetime.today().year,datetime.today().month,datetime.today().day]
d_day = 0

def yearCalculate(nowyear,futyear,nowmonth,nowday) :
    year_Cal = 0
    
    for i in range(nowyear,futyear) :
        temp = i
        if nowmonth <= 2 and nowday <= 28 and nowyear == temp and leapyear(temp) == True :
            year_Cal = year_Cal+366
        elif nowyear != temp and leapyear(temp) == True :
            year_Cal = year_Cal+366
        else :
            year_Cal = year_Cal+365
    return year_Cal

def monthCalculate(nowday,nowmonth,nowyear,futmonth) :
    month_Cal = [0,0] # [caculate day of month, calculate year]
    if nowmonth == futmonth :
        month_Cal[0] = 0
        month_Cal[1] = nowyear
        return month_Cal
    if nowmonth >> futmonth :
        for i in range(nowmonth,13) :
            temp = i
            if temp == 2 and nowday <= 28 and leapyear(nowyear) == True :
                month_Cal[0] = month_Cal[0] + 29
            else :
                month_Cal[0] = month_Cal[0] + howMonth(temp,nowyear)
        nowmonth = 1
        nowyear = nowyear + 1
    for i in range(nowmonth, futmonth) :
        temp = i
        if temp == 2 and nowday <= 28 and leapyear(nowyear) == True :
            month_Cal[0] = month_Cal[0] + 29
        else :
            month_Cal[0] = month_Cal[0] + howMonth(temp,nowyear)
    month_Cal[1] = nowyear
    return month_Cal

def dayCalculate (nowyear,nowmonth,nowday,futday) :
    day_Cal = [0,0,0] # [calculate day, calculate future year, calculate future month]
    day_Cal[0] = futday - nowday;
    if nowday >> futday :
        day_Cal[0] = (howMonth(nowmonth,nowyear) - nowday) + futday
        nowmonth = nowmonth + 1;
        if nowmonth >> 12 :
            nowyear = nowyear +1
            nowmonth = nowmonth -1

    day_Cal[2] = nowmonth
    day_Cal[1] = nowyear
    return day_Cal


def howMonth(month,year) : # Return month of day
    
    if month in [1,3,5,7,8,10,12] :
        monthday = 31
    elif month in [4,6,9,11] :
        monthday = 30
    else :
        if leapyear(year) :
            monthday = 29
        else:
            monthday = 28
    return monthday

def leapyear(year) : # Check leap year
    if year%4 == 0 :
        return True
        if year%100 == 0 and year%400 != 0 :
            return False
    else :
        return False

# code start
cal_1 = dayCalculate(now[0],now[1],now[2],fut[2])
d_day = cal_1[0]
now[0] = cal_1[1]
now[1] = cal_1[2]
print(now[1])

cal_2 = monthCalculate(now[2],now[1],now[0],fut[1])
d_day = d_day + cal_2[0]
now[0] = cal_2[1]
print(now[0])

d_day = d_day + yearCalculate(now[0],fut[0],now[1],now[2])
print(d_day+1)

