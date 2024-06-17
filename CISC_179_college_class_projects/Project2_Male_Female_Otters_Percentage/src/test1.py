numOttersMale = int(input('Enter number of males:'))
numOttersFemale = int(input('Enter number of females:'))

percentOttersMale = numOttersMale/(numOttersMale+numOttersFemale)*100
percentOttersFemale = numOttersFemale/(numOttersMale+numOttersFemale)*100

print(f'Percent males: {percentOttersMale:.0f}%')
print(f'Percent females: {percentOttersFemale:.0f}%')
