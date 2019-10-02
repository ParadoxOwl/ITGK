from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display
import ipywidgets as widgets
from string import ascii_uppercase, ascii_lowercase


def f( x ):
    return x


def g( x ):
    return x**2 + 10


def reverse_caps( statement ):
    tmp = ''
    if statement is '':
        return tmp
    for c in statement:
        if c in ascii_lowercase:
            tmp += c.upper()
        elif c in ascii_uppercase:
            tmp += c.lower()
        else:
            tmp += c
    return tmp


@interact( a=1, b=1, c=1, x=1, reverse=False, statement='' )
def equation( a, b, c, x, reverse, statement ):
    if reverse:
        a = -a
        statement = reverse_caps( statement )
    ans = a*(x**2) + b*x + c
    return statement, ans


def is_correct( b ):
    question.disabled = True
    if question.value is 'True':
        print('Correct answer')
    else:
        print('Wrong Answer')


question = widgets.RadioButtons(
    options = [ 'True', 'False' ],
#    description = 'test',
    disabled = False
)

button = widgets.Button(
    description='Submit',
    disabled=False,
)

print('test')
button.on_click(is_correct)
display( question )
display( button )
#interact(f, x=10)
#interact(g, x=widgets.FloatSlider(min = -15, max = 20, step = 0.2, value =3))
