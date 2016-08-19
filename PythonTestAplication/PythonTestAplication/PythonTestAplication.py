#Just a test application. 

def infinity():
    x=0
    while(True):
        x = int(x) +1
        print(x)

def main():
    list1=[4,2,3,4,5,6,7,8,9,0,1]
    list2 =['db','az','bz']
    print("hello")
    print("test List")
    print(list1[1:6])
    list1.sort()
    print("Sorted List") 
    list1 = list1*5

    list1.sort()
    print("Sorted List") 
    print( list1)
    print("give me a list")
    list4 = [int(x) for x in input().split()]
    print(list4)
    list4.sort()
    print(list4)
    tup1 = (2,1,3);
    print(tup1)
    print(tup1.index(2))
    dict = {'name':'steven' 'jordan', 'age': 24, 'class':'Graduate'}

    print(dict.keys)
    print("type the key you want")
    keyboard = input()
    print(dict.get(keyboard))
    print("update dir key name")
    keyboard = input()
    print("at")
    keyboard1 = input()
    dict.update(keyboard)

    
    return(0)

main()