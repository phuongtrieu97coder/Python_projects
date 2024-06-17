COOKIE_SAMPLE_NUMBER = 48
cupSugarSample = 1.5
cupButterSample = 1.0
cupFlourSample = 2.75

numCookies = input('Enter number of cookies:')
outputCupSugar = 1.5/48*int(numCookies)
outputCupButter = 1.0/48*int(numCookies)
outputCupFlour = 2.75/48*int(numCookies)
print(f'You need {outputCupSugar} cups of sugar, {outputCupButter} cups of butter, and {outputCupFlour} cups of flour.')
print("\n")
print(f'You need {outputCupSugar} cups of sugar, '
f'{outputCupButter} cups of butter, '
f'and {outputCupFlour} cups of flour.')
