purity = float(input())

if purity >= 99.9:
    print('24K')
elif purity >= 91.7:
    print('22K')
elif purity >= 83.3:
    print('20K')
elif purity >= 75.0:
    print('18K')
else:
    print('Not enough K')
