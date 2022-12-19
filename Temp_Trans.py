#溫度轉換程式
#請輸入要轉換的溫度單位
print ('請輸入要轉換的溫度單位: ')
print ('1: 華氏')
print ('2: 攝氏')
temp = input ()
temp = int (temp)

if temp == 1 or temp == 2 :
    
    if temp == 1:
        fah = input ('請輸入要轉換的華氏溫度數值: ')
        fah = int(fah)
        temp_c = 5/9 * (fah-32)
        print ('攝氏溫度為: ', temp_c)
    
    if temp == 2:
        cels = input ('請輸入要轉換的攝氏溫度數值: ')
        cels = int(cels)
        temp_f = 9/5 * cels +32
        print ('華氏溫度為: ', temp_f)
else:
    print('請重新輸入')