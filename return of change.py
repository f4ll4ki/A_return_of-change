money = int( input('거스름돈 입력 : ') )
 
if money <= 0:
    print('거스름돈 없음')
    import sys
    sys.exit()
 
y50000 = money//50000; money %= 50000
y10000 = money//10000; money %= 10000
y5000 = money//5000; money %= 5000
y1000 = money//1000; money %= 1000
y100 = money//100; money %= 100
 
print('50000원\t:', y50000, '개')
print('10000원\t:', y10000, '개')
print('5000원\t:', y5000, '개')
print('1000원\t:', y1000, '개')
print('100원\t:', y100, '개')
