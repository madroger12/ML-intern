def create_dir():
    import os
    dir = ['Processing','processed','queue']
    for i in dir:
        if not os.path.exists(i):
            os.makedirs(i)
    create_file()

def create_file():
    import time
    count =1
    while True:
        f_name = "file"+ str(count)
        f = open("C:/Users/e1p4ch0/PycharmProjects/internship/Processing/f_name.txt","w+")
        count +=1
        time.sleep(1)


if __name__ == '__main__':
    create_dir()

