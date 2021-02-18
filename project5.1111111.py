

"""Author: Henry Gyamfi

  Date-Written: 11/1/2020

  Date-Modified: 11/6/2020

  Description: In this program, I created a GUI that has two Buttons, a Text Box, and a Label.
  I took a data file and used Control Break logic on it to produce a report to the screen.The control break was on the Year the file was created.
  Try except is used to display an error if the file does not work. I used control break logic to help me read one line at a time. The PhotoReport
  is later written to an html file and displayed on internet explorer.

  Variables Used:

     TotalBytes - gives the total amount of Bytes after each year

     allBytes - gives total amount of bytes after all the years

     textHeader - helps to display my various subheadings

     currentYear - 2019"""
















from breezypythongui import EasyFrame

class PhotoLibrary(EasyFrame):

    def __init__(self):
        """Sets up the window and widgets"""
        EasyFrame.__init__(self, title = "Photo Library Report")
       

        self.addLabel(text = "Enter File: ", row = 0, column = 0)
        self.inputFile = self.addTextField(text="",row = 0, column = 1)
                                    
        self.Button1 = self.addButton(text = "Write Photo Report",
                              row = 1, column = 0,command=self.writeReport)
                            
        self.Button2 = self.addButton(text = "Write Photo Report to html",
                                      row = 1, column = 1, command=self.htmlReport)


    def writeReport(self):
        textHeader = ""
        textHeader = textHeader + "File Name                      Date Created           Number of Bytes\n"
        
        try:
            readFile = open(self.inputFile.getText())
        except FileNotFoundError:
            self.messageBox(title ="File not known",message ="File not found")
            return

        print(textHeader)
        currentYear = 2019
        TotalBytes = 0
        allBytes = 0

        allDone = False

        
        while not allDone:
            previousYear = currentYear
            while previousYear == currentYear:
                date = readFile.readline().split("\n")[0]
                if date == "":
                    print("Total bytes for all files is: ", allBytes)
                    allDone = True
                    break
                fileName = readFile.readline().split("\n")[0]
                byteTotal = readFile.readline().split("\n")[0]
                currentYear = date[6:10]
                #print(byteTotal)
                TotalBytes+=int(byteTotal)
                allBytes += int(byteTotal)
                #print("duifjiosdfiojio"+str(TotalBytes))
                print(f"{fileName:<30}{date:^12}{byteTotal:>20}\n")
                if previousYear == currentYear:
                    print ("Total bytes for " + currentYear + " is: ", int(TotalBytes))
                else:
                    break
                TotalBytes = 0

    def htmlReport(self):
        f = open("PhotoReport.htm", "w")
        
   
        textHeader = ""
        textHeader = textHeader + "<DOCTYPE html>\n<html>\n<head><title>Photo Report</title></head>\n<body>\n<h1><font color=0000FF>Photo Report</font></h1>" 
        textHeader = textHeader + "<h3><font color=FF0000>File Name                      Date Created           Number of Bytes</font></h3>\n"
        
        try:
            readFile = open(self.inputFile.getText())
        except FileNotFoundError:
            self.messageBox(title ="File not known",message ="File not found")
            return

        f.write(textHeader)
        currentYear = 2019
        TotalBytes = 0
        allBytes = 0

        allDone = False

        
        while not allDone:
            previousYear = currentYear
            while previousYear == currentYear:
                date = readFile.readline().split("\n")[0]
                if date == "":
                    f.write("<p>Total bytes for all files is: " + str(allBytes)+"</p></body></html>")
                    f.close()
                    allDone = True
                    break
                fileName = readFile.readline().split("\n")[0]
                byteTotal = readFile.readline().split("\n")[0]
                currentYear = date[6:10]
                #print(byteTotal)
                TotalBytes+=int(byteTotal)
                allBytes += int(byteTotal)
                #print("duifjiosdfiojio"+str(TotalBytes))
                f.write(f"{fileName:<30}{date:^12}{byteTotal:>20}<br>\n")
                if previousYear == currentYear:
                    f.write ("<h4>Total bytes for " + currentYear + " is: " + str(TotalBytes)+"</h4>\n")
                else:
                    break
                TotalBytes = 0
                      
            
            
        
        
            
        
    
    

    
        


PhotoLibrary().mainloop()
        
        
