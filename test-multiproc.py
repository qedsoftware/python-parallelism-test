#!/usr/bin/python
from multiprocessing import Process
import random

times = 20000000

def process(count, jobid, output):
    pom = []
    for i in range(count):
        pom.append(random.random())
    print "Job ", jobid, " finished!"

out1 = list()
out2 = list()

job = []
job.append(Process(target=process, args=(times, 'A', out1)))
job.append(Process(target=process, args=(times, 'B', out2)))
job.append(Process(target=process, args=(times, 'C', out2)))

for j in job:
    j.start()
for j in job:
    j.join()

print "Finished!"
