# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

input_ = input().split()
print(list(calendar.day_name)[calendar.weekday(int(input_[2]),int(input_[0]),int(input_[1]))].upper())
