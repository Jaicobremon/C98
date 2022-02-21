#Defining the file
def swapFileData ():

    #Small introduction to what the program deos
    print("Hi, I'm SWITCHER a program amde to switch the content of two files.")

    #Asking for the names of the files. 
    file1 = input("What is the name of file 1 ?:")
    file2 = input("What is the name of file 2 ?")

    #Getting data from file 1
    with open(file1,'r') as a:
        data_a = a.read()

    #Getting data from file 2
    with open(file2,'r') as b:
        data_b = b.read()

    #Replacing data in file 1
    with open(file1,'w') as a:
        a.write(data_b)

    #Replacing data in file 2
    with open(file2,'w') as b:
        b.write(data_a)

    #Declaring that the task has been completing
    print("I have switched the content of both of these files.")

#Calling the function
swapFileData()
