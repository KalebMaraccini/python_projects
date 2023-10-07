import datetime, random 

def getBirthdays(numOfBirthdays):
    """returns a list of number random date objects"""
    birthdays = []
    for i in range(numOfBirthdays):
        # we're assuming a single year, so it is unimportant
        startOfYear = datetime.date(2001,1,1)

        #get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays
def getMatch(birthdays):
        """returns the date object of a birthday that occurs more than once in the birthdays list."""
        if len(birthdays) == len(set(birthdays)):
             return None #all birthdays are unique 
        
        for a, birthdayA in enumerate(birthdays):
             for b, birthdayB in enumerate(birthdays[a+1:]):
                  if birthdayA == birthdayB:
                       return birthdayA
                  
# display intro
print(('''
Birthday Paradox, by Al Sweigart al@inventwithpython.com
 
 The birthday paradox shows us that in a group of N people, the odds
 that two of them have matching birthdays is surprisingly large.
 This program does a Monte Carlo simulation (that is, repeated random
 simulations) to explore this concept.
  
 (It's not actually a paradox, it's just a surprising result.)
 '''))
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
     print('How many birthdays shill I generate? (Max 100)')
     response = input('> ')
     if response.isdecimal and (0< int(response) <= 100):
          numBDays = int(response)
          break
print()

# generate and display the birthdays:
print('Here are',numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
     if i != 0:
          #display a comma for each birthday after teh first birthday.
          print(', ', end='')
     monthName = months[birthday.month -1]
     dateText = '{} {}'.format(monthName, birthday.day)
     print(dateText, end='')
print()
print()

# determine if there are two birthdays that match.
match = getMatch(birthdays)

#display the results
print('In this simulation, ',end='')
if match != None:
     monthname= months[match.month -1]
     dateText = '{} {}'.format(monthName, match.day)
     print('multiple people have a birthday on', dateText)
else:
     print('there are no matching birthdays.')
print()

# run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0
for i in range(100000):
     #report the progress every 10,000 simulations:
     if i % 10000 == 0:
          print(i,'simulations run...')
     birthdays= getBirthdays(numBDays)
     if getMatch(birthdays) != None:
         simMatch = simMatch + 1
print('100,000 simulations run.')
 
# Display simulation results:
probability = round(simMatch / 100000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
