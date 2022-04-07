a=int(input())
if (0==a%400):
    print('윤년')
elif (0==a%100):
    print('평년')
elif (0==a%4):
    print('윤년')
else:
    print('평년')