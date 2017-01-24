# cython_random
Cython library for random number generation

This library uses a 64 bit Mersenne Twister algorithm to provide a fast and high resolution random number generation library for people coding in Cython. The code should be platform independent and has been tested on Windows 10, Ubuntu 16.04, and multiple versions of macOS. However, you must be using a 64 bit version of Python for this.

Only the Cython source and header file are provided. You can install it however you like (i.e. using pyximport or distutils).

The code for random number generation and seeding was lifted directly from the C implementation of the code created by Matsumoto and Nishimura.

References:
   T. Nishimura, ``Tables of 64-bit Mersenne Twisters''
     ACM Transactions on Modeling and 
     Computer Simulation 10. (2000) 348--357.
   M. Matsumoto and T. Nishimura,
     ``Mersenne Twister: a 623-dimensionally equidistributed
       uniform pseudorandom number generator''
     ACM Transactions on Modeling and 
     Computer Simulation 8. (Jan. 1998) 3--30.
 

# Testing

The script test_cython_random.py tests out if the library installed properly. Simply run it. If you get any errors, the installation failed. If you get a message saying it has installed correctly, you are fine. These tests were created to ensure that this library produces the same output as the implementation from Nishimura and Matsumoto above.


