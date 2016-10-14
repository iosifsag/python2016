from datetime import date
import urllib2
import json

def getNumbers():
    while True:
        numbers = raw_input("Enter numbers separated by ',' (up to 12 numbers):")
        if len(numbers.split(',')) > 12:
            print "You can enter up to 12 numbers"
        else:
            numbers_list = []
            for number in numbers.split(','):
                numbers_list.append(int(number))
            return numbers_list

def getKinoData(date):
    url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/"+str(date)+".json"
    response = urllib2.urlopen(url)
    data = response.read()
    data = json.loads(data)
    response.close()
    return data

def CheckForWins(data, nums, date):
    win = False
    for draw in data["draws"]["draw"]:
        numbers_found = []
        for num in nums:
            if num in draw["results"]:
             numbers_found.append(num)
             win = True
        if win:
            print "(Date: " + date + ", Draw Number:" + str(draw["drawNo"]) + ") -> Numbers found: ",
            print numbers_found
            win = False

numbers = getNumbers()
for day in range(1, date.today().day + 1):
    Date = str(day) + "-" + str(date.today().month) + "-" + str(date.today().year) 
    CheckForWins(getKinoData(Date), numbers, Date)
