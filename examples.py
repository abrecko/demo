from calc import multiply, divide, plus, minus, safe_div

if __name__ == '__main__':
    a, b = 10, 2
    print('multiply({}, {}) ='.format(a, b), multiply(a, b))
    print('divide({}, {}) ='.format(a, b), divide(a, b))
    print('plus({}, {}) ='.format(a, b), plus(a, b))
    print('minus({}, {}) ='.format(a, b), minus(a, b))
    print('safe_div({}, {}) ='.format(a, b), safe_div(a, b))
