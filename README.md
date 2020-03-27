D_Day_Code for Python
================
# Composed by
### Project File(.sln)
### Python code file(.py)

# Preview
#### this is sample of day calculate
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
* * *
# Tools
### Visual Studio Community 2019 version 16.5.0
### (Python - 16.5.20041.1)
	