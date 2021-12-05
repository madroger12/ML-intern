def queue_to_processed()
    import io

    import mysql.connector
    import shutil
    import glob

    source = 'C:/Users/e1p4ch0/PycharmProjects/internship/queue/'
    destination = 'C:/Users/e1p4ch0/PycharmProjects/internship/processed/'

    db = mysql.connector.connect(host="localhost",
                                 user="e1p4ch0",
                                 password="Xerx3s1921",
                                 database="internship"
                                 )

    # cursor obj
    mycursor = db.cursor()

    files = [file for file in glob.glob(source)]
    for file_name in files:
        with io.open(file_name, 'r') as curr_file:
            file_content = curr_file.read()
            curr_file.close()
            query = "INSERT INTO table Values (%s) "
            mycursor.execute(query, (file_content,))
            shutil.move(source + file_name, destination + file_name)

    db.close()

