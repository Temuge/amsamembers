import datetime;

MAX_TIME_TO_BE_SCHOOL = 10
MAX_TIME_GRADUATED_AGO = 20
MAX_AGE = 100

def getPossibleYearsToBorn():
    now = datetime.datetime.now()
    return range(now.year-MAX_AGE, now.year+1)

def getPossibleYearsToGraduate():
    now = datetime.datetime.now()
    return range(now.year-MAX_TIME_GRADUATED_AGO, now.year+MAX_TIME_TO_BE_SCHOOL+1)
    
def getMonthsList():
    return range(1, 13)

def getDaysList():
    return range(1,32)

def getDateTimeContext():
    context = {}
    context['possibleYearsToBorn']=getPossibleYearsToBorn()
    context['possibleYearsToGraduate']=getPossibleYearsToGraduate()
    context['months']=getMonthsList()
    context['days']=getDaysList()

    return context;

