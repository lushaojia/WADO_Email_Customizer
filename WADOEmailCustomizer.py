"""Taking an email template I wrote for WADO's workshop reminder emails and splitting it by paragraphs. Things inside brackets are to be
customized based on user input. Each variable stores the list of strings resulting from splitting each paragraph by spaces."""

wadoEmailP1 = ["Hello!"]
wadoEmailP2 = """This is a friendly reminder that you have signed up for WADO's [WORKSHOP_NAME] [dance] workshop on
                [DATE] (this coming [SAT/SUN]) from [TIME_DURATION] PM EST @ Tishman Commons/Zoom! Tishman Commons
                is on the lowest level of Lulu; the Zoom link can be found here. This workshop will be taught by our
                lovely act [leaders] [NAMES]!""".split()

wadoEmailP3 = """Please come in clothes that you can easily dance in, bring a water bottle,
                    and be prepared to have some fun!""".split()
wadoEmailP4 = """If you are going to be late or absent, please let the act [leaders]
                know at least 24 hours in advance with an e-mail and remove your name from
                the sign-up sheet (if absent). [NAME1] username is [UN1] [NAME2] username is [UN2]""".split()

wadoEmailP5 = """Lastly, as you head into this workshop, we want you to think about if you would like to
                    participate in WADO's Spring Showcase. Spring Showcase this year will be virtual, consisting
                    of a YouTube live stream of all the dances taught this spring. If you choose to participate in
                    Spring Showcase, we ask that you look over the filming/outfit requirements for the dance(s) that
                    you wish to submit a video for. The sign-up sheet can be found here; please note that this sheet
                    is binding (you will be expected to submit a video by the deadline and attend the review session
                    hosted at a later time by the act leader if you put your name down). The deadline to sign-up to
                    participate in Spring Showcase for [WORKSHOP_NAME] is [DEADLINE] at 11:59 PM EST. For all T4
                    dances, the deadline to submit videos is Saturday, June 5th at 11:59 PM EST.""".split()

wadoEmailP6 = """<3,""".split()
wadoEmailP7 = """WADO""".split()

#Each variable below stores the index of customizable elements in each paragraph. Technically, I can figure out each customizable element's
#index, but I am too lazy to count.

#Paragraph 2
workshopNameP2Index = wadoEmailP2.index("[WORKSHOP_NAME]")
danceP2Index = wadoEmailP2.index('[dance]')
dateP2Index = wadoEmailP2.index('[DATE]')
sat_SunP2Index = wadoEmailP2.index('[SAT/SUN])')
timeDurationP2Index = wadoEmailP2.index('[TIME_DURATION]')
leadersP2Index = wadoEmailP2.index('[leaders]')
namesP2Index = wadoEmailP2.index('[NAMES]!')

#Paragraph 4
leadersP4Index = wadoEmailP4.index('[leaders]')
name1P4Index = wadoEmailP4.index("[NAME1]")
UN1P4Index = wadoEmailP4.index("[UN1]")
name2P4Index = wadoEmailP4.index("[NAME2]")
UN2P4Index = wadoEmailP4.index("[UN2]")

#Paragraph 5
workshopNameP5Index = wadoEmailP5.index('[WORKSHOP_NAME]')
deadlineP5Index = wadoEmailP5.index("[DEADLINE]")


#defining a literal dictionary with 12 key:value pairs where keys are integers ranging from 1 to 12 and corresponding values are lists containing two elements where the first
#is the name of a month spelled out in English and the second is the number of days in that month. Assuming a common year, February has 28 days.
monthDict = {1:['January', 31], 2:['February', 28], 3:['March', 31], 4:['April', 30], 5:['May', 31], 6:['June', 30],
             7:['July', 31], 8:['August', 31], 9:['September', 30], 10:['October', 31], 11:['November', 30], 12:['December', 31]}

def addOneDay(date):
    """a function that takes an input of a date in the format of M/DD (e.g. 4/12) as a string, adds one day to this input, and return it in the format of "Month DD" where
    the Month is written out in English (e.g. March) and the Day is an integer (23).
    This function is necessary for customizing the [DEADLINE] element in the fifth paragraph. The deadline to sign up to participate in WADO's Spring Showcase
    for all dances is always the Sunday of the weekend when the workshop was held. If the workshop was held on 3/27 (Saturday), then the deadline is March, 28 (Sunday).
    If the workshop was held on 3/28 (Sunday), the deadline is also 3/28 (Sunday)."""
    
    splitDateBySlash = date.split('/')
    # using the monthDict dictionary, if input is the last day of a month, then the function returns the first day of the next month in the format of Month DD
    intMonth = int(splitDateBySlash[0])
    intDay = int(splitDateBySlash[1])
    if monthDict[intMonth][1] == intDay:
        if monthDict[intMonth][0] != 'December':
            intMonthPlusOne = intMonth + 1
        else:
            intMonthPlusOne = intMonth - 11
        nextMonthEnglish = monthDict[intMonthPlusOne][0]
        return str(nextMonthEnglish) + " " + str(1)
    # using the monthDict dictionary, if input is not the last day of a month, the function adds one day to the input date and returns that in the format of Month DD
    else:
        monthEnglish = monthDict[intMonth][0]
        intNextDay = intDay + 1
        return str(monthEnglish) + ' ' + str(intNextDay)

def dateInEnglish(date):
    """a function that takes a input of a date in the format of M/DD (e.g. 4/12) as a string and
    returns a string of the same date in the format of Month DD (e.g. April 12)"""
    
    splitDateBySlash = date.split('/')
    intMonth = int(splitDateBySlash[0])
    intDay = int(splitDateBySlash[1])
    monthEnglish = monthDict[intMonth][0]
    
    return monthEnglish + " " + str(intDay)

def alterP2EmailList(workshopName, date, satOrSun, timeDuration, ALName1, ALName2):
    """This function takes the name, date, duration of the workshop and whether the workshop happens on a Saturday or Sunday as strings.
    The name of the workshop have the appropriate number of spaces separating the words. The date should be in the format of M/DD (e.g. 5/15). Workshop duration
    should be in a format like 1-2. Names of act leaders should be full names and capitalized appropriately. If there is only one act leader, ALName1 should be the full name of the
    act leader and ALName2 should be an empty string.
    
    This function then makes changes to the list stored in wadoEmailP2 accordingly and returns the new list.
    """
    #Each variable below stores the index of customizable elements in each paragraph. Technically, I can figure out each customizable element's
    #index, but I am too lazy to count.

    #index of customizable elements before [dance]
    workshopNameP2Index = wadoEmailP2.index("[WORKSHOP_NAME]")
    danceP2Index = wadoEmailP2.index('[dance]')
    
    wadoEmailP2[workshopNameP2Index] = workshopName
    if workshopName.split()[-1] == "Dance":
        # if the word "Dance" is in the name of the workshop, then the string 'dance' at index 13 will be popped from the list.
        wadoEmailP2.pop(danceP2Index)
    else:
        wadoEmailP2[danceP2Index] = 'dance'
    
    #index of customizable elements after [dance]
    dateP2Index = wadoEmailP2.index('[DATE]')
    sat_SunP2Index = wadoEmailP2.index('[SAT/SUN])')
    timeDurationP2Index = wadoEmailP2.index('[TIME_DURATION]')
    leadersP2Index = wadoEmailP2.index('[leaders]')
    namesP2Index = wadoEmailP2.index('[NAMES]!')
    
    wadoEmailP2[dateP2Index] = date
    if satOrSun == "Saturday":
        wadoEmailP2[sat_SunP2Index] = 'Saturday)'
    else:
        wadoEmailP2[sat_SunP2Index] = 'Sunday)'
    wadoEmailP2[timeDurationP2Index] = timeDuration
    if ALName2 != '':
        # if there are two act leaders, then the word "leaders" will be plural and both act leaders' names will be added to the list separated by 'and'
        # an exclammation mark will follow the name of the first/second act leader
        wadoEmailP2[leadersP2Index] = 'leaders'
        wadoEmailP2.pop(namesP2Index)
        wadoEmailP2.append(ALName1)
        wadoEmailP2.append('and')
        wadoEmailP2.append(ALName2 + '!')
    else:
        wadoEmailP2[leadersP2Index] = 'leader'
        wadoEmailP2.pop(namesP2Index)
        wadoEmailP2.append(ALName1 + '!')
    return wadoEmailP2

#print(alterP2EmailList("Vietnamese Lotus Dance", '3/25', "Saturday", "2-3", 'Katie Toye', 'Lucinda Li'))
    

def alterP4EmailList(ALName1, ALName2, UN1, UN2):
    """This function takes the names of act leaders (up to 2) and the usernames for their email addresses (up to 2) as strings. If there is only
    one act leader, ALName2 and UN2 should be empty strings.
    
    This function makes changes to the list stored in wadoEmailP4 accordingly and returns the new list"""
    
    # indices of customizable elements in paragraph 4
    leadersP4Index = wadoEmailP4.index('[leaders]')
    name1P4Index = wadoEmailP4.index("[NAME1]")
    UN1P4Index = wadoEmailP4.index("[UN1]")
    name2P4Index = wadoEmailP4.index("[NAME2]")
    UN2P4Index = wadoEmailP4.index("[UN2]")
    
    if ALName2 != '':
        # if there are two act leaders, both of their first names and usernames will be added to the list with an apostre s added after
        # leaders will remain as a plural word
        wadoEmailP4[leadersP4Index] = 'leaders'
        wadoEmailP4[name1P4Index] = ALName1.split()[0] + "'s"
        wadoEmailP4[UN1P4Index] = UN1 + ';'
        wadoEmailP4[name2P4Index] = ALName2.split()[0] + "'s"
        wadoEmailP4[UN2P4Index] = UN2 + "."
        return wadoEmailP4
    else:
        wadoEmailP4[leadersP4Index] = 'leader'
        wadoEmailP4[name1P4Index] = ALName1.split()[0] + "'s"
        wadoEmailP4[UN1P4Index] = UN1 + '.'
        return wadoEmailP4[0:UN1P4Index + 1]

        
#print(alterP4EmailList('Katie Toye', 'Lucinda Li', 'ktoye', 'lli5'))
#print(alterP4EmailList('Anika Luo', '', 'aluo8', ''))
    
def alterP5EmailList(workshopName, date, satOrSun):
    """This functions takes the name of the workshop, the date of the workshop in the format of M/DD (e.g. 3/29), and whether the workshop is held on a Sat or Sun as strings.
    The deadline to sign-up to participate in Spring Showcase for all dances is the Sunday of the weekend during which their workshop was held.
    If the workshop was held on a Saturday, this function invokes the addOneDay function to replace [DEADLINE] (from the list stored in wadoEmailP5) with the following day's date in
    Month DD format (e.g. April 4). If the workshop was held on a Sunday, this function invokes the dateInEnglish function to replace [DEADLINE] with the input date in
    Month DD format."""
    
    #indices for customizable elements in paragraph 5
    workshopNameP5Index = wadoEmailP5.index('[WORKSHOP_NAME]')
    deadlineP5Index = wadoEmailP5.index("[DEADLINE]")
    
    wadoEmailP5[workshopNameP5Index] = workshopName
    if satOrSun == "Saturday":
        wadoEmailP5[deadlineP5Index] = addOneDay(date)
    elif satOrSun == "Sunday":
        wadoEmailP5[deadlineP5Index] = dateInEnglish(date)
    return wadoEmailP5



def makeCompleteEmail():
    """
    Asks for user input on the name, date, and duration of the workshop, whether the workshop is held on a Saturday or Sunday, the name(s) of the act leaders and their username(s),
    then invokes previously defined functions to alter the template paragraphs accordingly.
    Lastly, takes all the paragraphs, altered (paragraphs 2, 4, 5) and unaltered (paragraphs 1, 3, 6, 7), inserts empty
    lists between paragraphs 1, 2, 3, 4, and 5 (representing line breaks), and returns a list of these lists."""
    
    
    workshopName = input('What is the name of the workshop? ')
    date = input("What is the date of the workshop? (Please enter it in the format of M/DD where M and DD are all integers) ")
    timeDuration = input('What is the duration of the workshop? (Please enter it in the format of START TIME - END TIME) ')
    satOrSun = input('Does the workshop happen on a Saturday or Sunday? ')
    ALName1 = input('What is the full name of the first act leader? ')
    UN1 = input('What is their Wellesley email address username? ')
    ALName2 = input('What is the full name of the second act leader? (If there is only one Act Leader, please hit return.) ')
    UN2 = input('What is their Wellesley email address username? (If there is only one Act Leader, please hit return.) ')
    
    alteredP2 = alterP2EmailList(workshopName, date, satOrSun, timeDuration, ALName1, ALName2)
    alteredP4 = alterP4EmailList(ALName1, ALName2, UN1, UN2)
    alteredP5 = alterP5EmailList(workshopName, date, satOrSun)
    
    completeEmailList = [wadoEmailP1, alteredP2, wadoEmailP3, alteredP4, alteredP5, wadoEmailP6, wadoEmailP7]
    
    counter = 0
    emailListWithSpaces = []
    for paragraphList in completeEmailList:

        if counter <= 4:
            emailListWithSpaces.append(paragraphList)
            emailListWithSpaces.append([])
            counter += 1
        else:
            emailListWithSpaces.append(paragraphList)
            counter += 1
    return emailListWithSpaces

#makeCompleteEmail()

def printCompleteEmail():
    """Prints out the final, customized email message with spaces added in between words and line breaks."""
    completedEmailList = makeCompleteEmail()
    for paragraphList in completedEmailList:
        paragraphStr = ''
        for word in paragraphList:
            paragraphStr += word + ' '
        print(paragraphStr)
        
printCompleteEmail()

    
        
    