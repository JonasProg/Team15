import area as a
import circumference as c

x = input('Choose: square or circle')
if x == 'square':
    x = input('area or circumference?')
    if x == 'area':
        x = input('length of side?')
        return a.area_square(x)
if x == 'circle':

else:
    print('Idiot')

