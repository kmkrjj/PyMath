# Write code below 💖




class trapezium():
  def __init__(self):
    def a():
      print(' ')
      print('           \/           ')
      print('    ________________    ')
      print('   /                \   ')
      print('  /                  \  ')
      print(' /                    \ ')
      print(' ---------------------- ')

    def b():
      print('  ')
      print('    ________________    ')
      print('   /                \   ')
      print('  /                  \  ')
      print(' /                    \ ')
      print(' ---------------------- ')
      print('           /\           ')

    def heightTrapezium():
      print('  ')
      print('    ________________    ')
      print('   /       ---      \   ')
      print('  /         | <--    \  ')
      print(' /         ---        \ ')
      print(' ---------------------- ')
    try:
      a()
      a = float(input('What is the top width of your shape in centimeter?  : '))
      b()
      b = float(input('What is the bottom width of your shape in centimeter?  : '))
      heightTrapezium()
      heightTrapezium = float(input('What is the height of your shape in centimeter?  : '))

      AnsOne = a + b

      Ans = f'The area of this shape is {heightTrapezium*AnsOne/2}'
    except ValueError:
      print('an error has occurred, please enter a numeric value')
    print(Ans + ' square centimeters')
    input('press Enter to exit...')

class triangle():
  def __init__(self):
    def heightTriangle():
      print('           /\           ')
      print('          /  \          ')
      print('         / ---\         ')
      print('        /   |  \        ')
      print('       /    |   \       ')
      print('      /     |    \      ')
      print('     /      | <-- \     ')
      print('    /       |      \    ')
      print('   /        |       \   ')
      print('  /         |        \  ')
      print(' /         ---        \ ')
      print(' ---------------------- ')

    def baseTriangle():
      print('           /\           ')
      print('          /  \          ')
      print('         /    \         ')
      print('        /      \        ')
      print('       /        \       ')
      print('      /          \      ')
      print('     /            \     ')
      print('    /              \    ')
      print('   /                \   ')
      print('  /                  \  ')
      print(' /                    \ ')
      print(' ---------------------- ')
      print(' |--------------------| ')
      print('           /\           ')
    try:
      baseTriangle()
      a = float(input('What is the bottom width of your shape in centimeter (numeric only)?  : '))
      heightTriangle()
      b = float(input('What is the height of your shape in centimeter (numeric only)?  : '))

      Ans = f'The area of this shape is {a*b/2}'
    except ValueError:
      print('an error has occurred, please enter a numeric value')
    print(Ans + ' square centimeters')
    input('press Enter to exit...')




def setup():
  print('PyMath 1.0.0')
  print('')
  print('use your numeric keys to select')
  print('1. trapezium 2. Triangle')
  print('')
  math = input('PyMath\Home>  ')
  if math == '1':
    trapezium()
  if math == '2':
    triangle()


setup()



