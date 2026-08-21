import numpy as np
//<img SRC="data:image/png;base64,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
w0 = np.zeros((25))

# набор данных для обучения
D = np.array([
    [1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,],

    [1, 1, 1, 1, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 0, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 1, 1,],

    [1, 1, 1, 1, 1,
    1, 0, 0, 0, 1,
    1, 1, 0, 1, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 0,
     1, 0, 0, 1, 1,
     1, 1, 0, 1, 1,
     1, 1, 0, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
    0, 0, 0, 0, 1,
    0, 1, 1, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,],

    [0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,],

    [1, 1,1, 1, 1,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,],

    [1, 1, 1, 1, 1,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 1, 1,],

    [1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 0, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     0, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 0,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 0, 1, 1,
     1, 1, 1, 0, 1,
     1, 0, 1, 1, 0,
     1, 1, 1, 1, 1,
     1, 0, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 0, 1, 1, 1,
     1, 1, 0, 1, 1, ],

    [1, 1, 1, 1, 0,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 0,
     1, 0, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     0, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     1, 1, 0, 1, 1,
     1, 0, 1, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 0,
     1, 1, 1, 1, 1,
     1, 1, 0, 1, 1,
     1, 0, 1, 1, 1,
     0, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     0, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 0, ],

    [0, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 0, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 0, 1, 0, 1,
     1, 1, 1, 1, 1, ],

    [0, 0, 0, 0, 0,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     0, 0, 0, 0, 0, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 0, 0, 0, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 0, 1, 1,
     1, 0, 1, 0, 1,
     1, 1, 0, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 0, 1, 1,
     1, 0, 0, 0, 1,
     1, 1, 0, 1, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 0,
     1, 1, 1, 1, 0,
     0, 0, 0, 0, 0,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 0,
     1, 1, 1, 0, 0,
     0, 0, 0, 0, 0,
     1, 1, 1, 1, 1, ],

    [0, 1, 1, 1, 0,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 0, 0, 0, 1,
     0, 1, 1, 1, 0, ],

    [0, 1, 1, 1, 0,
     1, 1, 0, 1, 1,
     1, 1, 1, 0, 1,
     1, 0, 0, 0, 1,
     0, 1, 1, 1, 0, ],

    [0, 1, 1, 1, 0,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     0, 1, 1, 1, 0, ],

    [0, 1, 1, 1, 0,
     1, 1, 0, 1, 1,
     1, 1, 1, 0, 1,
     1, 0, 0, 0, 1,
     0, 1, 1, 1, 0, ],

    [1, 0, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,],

    [1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 0, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,],

    [1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1,0,  1, 1,
    1, 1, 1, 1, 1,],

    [1, 0, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,],

    [1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 0,
     1, 1, 1, 1, 1],

    [1, 0, 1, 0, 1,
     0, 1, 0, 1, 0,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 0,
     1, 1, 1, 1, 1]
])
print(len(D))
# желаемые результаты от входных данных для обучения
Y0 = np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])
print(len(Y0))

α =  0.3  # скорость обучения
β = -0.4 
σ = lambda x: 1 if x > 0 else 0  # функция активации нейрона

def f(x, _w):
    s = β + np.sum(x @ _w)
    return σ(s)

def train(w, D, Y):
    _w = w.copy()
    for x, y in zip(D, Y):
        w += α * (y - f(x, w)) * x
    return (w != _w).any()

while train(w0, D, Y0) :
    print(w0)

D = np.array([


    [1, 1, 1, 1, 1,
     1, 0, 0, 0, 1,
     1, 1, 1, 0, 1,
     1, 0, 0, 0, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 0,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 0, 0, 0, 1,
     1, 1, 1, 1, 1,
     1, 0, 0, 0, 1,
     1, 1, 1, 1, 1, ],

    [1, 1, 1, 1, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 0, 1,
     1, 1, 1, 1, 1],

    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1],

    [1, 0, 1, 0, 1,
     0, 1, 0, 1, 0,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 0,
     1, 1, 1, 1, 1]

])
print("вход                               результат")
for x in D:
    print(x, "  ", f(x, w0))
