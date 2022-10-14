from operator import add, sub, mul, truediv

ERROR_ZERO_DIV = 'Division by zero'
ERROR_UNDEFINED = 'Result is undefined'

DEFAULT_FONT_SIZE = 16
DEFAULT_ENTRY_FONT_SIZE = 40

DIGIT_BUTTONS = [f'btn_{num}' for num in range(10)]
MATH_OPERATIONS = ['btn_add', 'btn_sub', 'btn_mul', 'btn_div']
BUTTONS_TO_DISABLE = [
    'btn_calc', 'btn_add', 'btn_sub',
    'btn_mul', 'btn_div', 'btn_neg', 'btn_point'
]

OPERATIONS = {
    '+': add,
    '−': sub,
    '×': mul,
    '/': truediv
}
