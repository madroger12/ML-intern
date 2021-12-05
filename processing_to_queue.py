def processing_to_queue():
    import os
    import time
    import shutil
    source = 'C:/Users/e1p4ch0/PycharmProjects/internship/Processing/'
    destination = 'C:/Users/e1p4ch0/PycharmProjects/internship/queue/'

    while not os.listdir(destination):
        allfiles = os.listdir(source)

        for f in allfiles:
            shutil.move(source + f, destination + f)
        time.sleep(5)






