# 180s
from re import L


TOTAL_TIME = 180000
offset = 1
count = 1
curr_time = 1

while(1):
    for j in range(offset):
        curr_time += 1
        print(count)

    count=count+1
    # if(count):
    offset=offset*10

    if(curr_time>TOTAL_TIME):
        break