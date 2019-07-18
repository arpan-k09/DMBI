import math

def min_max(li):
    max_v = max(li)
    #print(max_v)
    min_v = min(li)
    #print(min_v)
    new_li_m = []
    le_m = len(li)
    count = 0
    
    new_min = float(input("Enter new_min "))
    new_max = float(input("Enter new_max "))
    
    v_bar = 0
    while count != le_m:
    
        v_bar = ((float(li[count]) - float(min_v))/(float(max_v)- float(min_v)))*(float(new_max) - float(new_min))+float(new_min)
        
        #s = str(v_bar)
        new_li_m = new_li_m + [v_bar]
        
        
        
            
        count = count + 1
    
    return new_li_m
    


def deciscale(li):
    count=0
    leng_m=len(li)
    max_v = max(li)
    #temp = 1
    new_li_m = []
    
    count = 0
    while max_v >= 1:
        max_v = max_v / 10
        count = count + 1
        
    fin = 1
    while count != 0:
        fin = fin * 10
        count = count - 1
        
    count1 = 0
    while count1 != leng_m:
        
        v_bar =  float(li[count1])/float(fin)
        new_li_m = new_li_m + [v_bar]
        count1 = count1 + 1

    return new_li_m


def z_score(li):
    count=0
    leng_m=len(li)
    max_v = max(li)
    #temp = 1
    new_li_m = []
    
    total = 0
    while count != leng_m:
        total = total + li[count]
        count = count + 1
    
    mean = float(total)/leng_m
    
    count1 = 0
    total_v = 0.0
    while count1 != leng_m:
        squ = (float(li[count1]) - float(mean))*(float(li[count1]) - float(mean))
        total_v = total_v + squ
        count1 = count1 + 1
        
    va = total_v / leng_m
    variance = math.sqrt(va)
    count2 = 0 
    new_li_m = []
    v_bar = 0
    while count2 != leng_m:
        v_bar = (float(li[count2]) - float(mean))/float(variance)
        new_li_m = new_li_m + [v_bar]
        count2 = count2 + 1
        
    return new_li_m


li = [10,12,3,6,5,25,17,100,1000,98,11,27,78,33,9,18,23,44,690,200]

#print(deciscale(li))
#print(min_max(li))        
print(z_score(li))
