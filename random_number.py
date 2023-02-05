import random
while True:
    
    try:
        a = input('请输入随机数个数:')
        b = input('请输入随机数范围最小值:')
        c = input('请输入随机数范围最大值:')
        a = int(a)
        b = int(b)
        c = int(c)
    
    except ValueError:
        print('输入类型有误，请输入一个整数。')
    except:
        print('遇到未知错误。')
    
    else: 
        try:
            for i in range(a):
                d = random.randint(b, c)
                print(d)
        except ValueError:
            print('随机数范围最小值大于了随机数范围最大值，请输入正确的内容。')
        except:
            print('遇到未知错误。')
    
    finally:
        print('---------------------')