#!/usr/bin/python
import random
import threading

times = 20000000

def process(count, jobid, output):
    pom = []
    for i in range(count):
        pom.append(random.random())
    print "Job ", jobid, " finished!"

out1 = list()
out2 = list()

thread1 = threading.Thread(target=process(times, 'A', out1))
thread2 = threading.Thread(target=process(times, 'B', out2))
thread3 = threading.Thread(target=process(times, 'C', out2))

job = []
job.append(thread1)
job.append(thread2)
job.append(thread3)

for i in job:
    i.start()
for i in job:
    i.join()

print "Finished!"
