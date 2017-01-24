import pyximport
import numpy as np
pyximport.install(setup_args={'include_dirs': np.get_include()})
import cython_random


cython_random.py_seed_random(1234)

for i in range(1000):
    cython_random.py_rand_int()

assert ( cython_random.py_rand_int() == 15529542738993802093 )


for i in range(1000):
    cython_random.py_rand_int()

assert ( cython_random.py_rand_int() == 13925894414736521713 )


for i in range(1000):
    cython_random.py_rand_int()

assert ( np.abs(0.3677696173800852341706502 - cython_random.py_uniform_rv() )< 1E-10 )

for i in range(1000):
    cython_random.py_rand_int()

assert ( np.abs( 0.3083103800285806328496108 - cython_random.py_uniform_rv() ) < 1E-10 )


print('If you get to this message with no errors, you have installed correctly :-)')


