import math,sys


def get_more(wrappers,remaining_wrappers):
    total_wrappers = wrappers + remaining_wrappers
    new_chocolates = total_wrappers/wrapper_discount
    if new_chocolates >= 1:
        return int(new_chocolates) + \
               get_more(int(new_chocolates),total_wrappers%wrapper_discount)
    else:
        return 0

if __name__ == "__main__":
    #fo = open('D:\\Lebara\\output.txt','w+')
    #fo = open(sys.stdout)
    with open('D:\\Lebara\\input_data.txt') as f:
        for x in f.readlines():
            dollars,price,wrapper_discount = list(map(int,x.split(' ')))
            #fo.writelines(str(int((dollars/price) + get_more(int(dollars/price),int(dollars%price))))+'\n')
            #print(str(int((dollars/price) + get_more(int(dollars/price),int(dollars%price))))+'\n')
            print(str(int((dollars/price) + get_more(int(dollars/price),0))))
    f.close()
    #fo.close()


