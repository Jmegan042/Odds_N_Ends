import time

now = time.time()
print('Hit enter to stop timer:')
input()
then = time.time()
Time_Spent = then-now
Minutes = Time_Spent/60
Hours = Minutes/60
print('Total time spent is ',Time_Spent,'seconds.')
print('This translates to %s hours or %s minutes' % (round(Hours,2),round(Minutes,2)))