import statistics
def make_bin(li):
    leng = len(li)
    count = 0
    final_bin = []
    bin_size = int(input("Enter bin size : - "))
    rem = leng % bin_size

    if rem != 0:
        while(count < leng - rem):
            temp_li = []
            temp = 0
            while temp != bin_size:
                if li[temp + count] is None:
                    break
                else:
                    temp_li = temp_li + [li[temp + count]]
                temp = temp + 1
            final_bin.append(temp_li)
            count = count + bin_size

        count1 = 0
        temp_li = []

        while count1 != rem:
            temp_li = temp_li + [li[count]]

            count = count + 1
            count1 = count1 + 1
    else:
        while (count != leng):
            temp_li = []
            temp = 0
            while temp != bin_size:
                if li[temp + count] is None:
                    break
                else:
                    temp_li = temp_li + [li[temp + count]]
                temp = temp + 1
            final_bin.append(temp_li)
            count = count + bin_size
    final_bin.append(temp_li)

    return final_bin

def mean_bi(bi):
    l = len(bi)
    count = 0
    fi = []
    while count != l:
        temp = []
        le = len(bi[count])
        total = 0
        count2 = 0
        while count2 != le:
            total = total + bi[count][count2]
            count2 = count2 +1

        me = float(total / le)
        count3 = 0
        while count3 != le:
            temp = temp + [me]
            count3 = count3 + 1
        fi.append(temp)
        count = count + 1
    return fi


def median_bi(bi):
    l = len(bi)
    count = 0
    fi = []
    while count != l:
        temp = []

        le = len(bi[count])
        me = statistics.median(bi[count])
        count3 = 0
        while count3 != le:
            temp = temp + [me]
            count3 = count3 + 1
        fi.append(temp)
        count = count + 1
    return fi

def range_bi(bi):

    l = len(bi)
    count = 0
    fi = []
    while count != l:
        temp = []
        max_bi = max(bi[count])
        min_bi = min(bi[count])
        le = len(bi[count])

        count3 = 0
        while count3 != le:
            mi = abs(bi[count][count3]-min_bi)
            ma = abs(max_bi-bi[count][count3])
            if mi <= ma :
                temp = temp + [min_bi]
            elif mi > ma :
                temp = temp + [max_bi]

            count3 = count3 + 1
        fi.append(temp)
        count = count + 1
    return fi


li = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 5, 35, 35, 36, 40, 45, 46, 52, 70 ]
bi = make_bin(li)
mean_bi(bi)
median_bi(bi)
range_bi(bi)

