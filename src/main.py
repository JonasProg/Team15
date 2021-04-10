""" Interaktive Konsole für area.py und circumference.py
"""
import area as a
import circumference as c

shape = input('Choose: square or circle: ')
if shape == 'square':
    y = input('area or circumference?: ')
    if y == 'area':
        length = input('enter length of side in cm: ')
        output = a.area_square(float(length))
        print('The area of your square is {:.2f} cm².'.format(output))
    elif y == 'circumference':
        length = input('enter length of side in cm: ')
        output = c.circ_square(float(length))
        print('The circumference of your square is {:.2f} cm.'.format(output))
    else:
        print('Please restart with correct syntax.')
elif shape == 'circle':
    y = input('area or circumference?: ')
    if y == 'area':
        radius = input('enter radius in cm: ')
        output = a.area_circle(float(radius))
        print('The area of your circle is {:.2f} cm².'.format(output))
    elif y == 'circumference':
        radius = input('enter radius in cm: ')
        output = c.circ_circle(float(radius))
        print('The circumference of your circle is {:.2f} cm.'.format(output))
    else:
        print('Please restart with correct syntax.')
else:
    print('Please restart with correct syntax.')
