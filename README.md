THREADS VS. PROCESSES IN PYTHON
========================================
This small example compares multithreading and multiprocessing.

To test multi-threading, which works better for I/O-bound applications due to the Global Interpreter Lock:

    $ time python test-thread.py

To test multi-processing, which works better for CPU-bound applications:

    $ time python test-multiproc.py

Source: http://www.martinkral.sk/blog/2011/03/python-multicore-vs-threading-example/
