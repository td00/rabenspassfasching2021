import os

class Picture:
    def __init__(self, fullName, directory):
        self.fullName = fullName
        self.variables = []

    def doMagic(self,p):
        if(self.getVariables(p) < 0):
            return
        return self.generateString()

    def getVariables(self,p):
        #cut string in pieces and fill the variables set accordingly
        #put -1 if non existant
        index = 0
        workingArray = self.fullName.split('_')

        #kindergarten
        if(workingArray[index][0:2].lower()== 'kg' and workingArray[index][2].isnumeric()):
            self.variables.append(workingArray[index].lower())
            index += 1
        else:
            outStr = "there is no ID for " + str(self.fullName) + "\n"
            p.write(outStr)
            return -1


        #firstName (if there is none, ist -1)
        if(workingArray[index].lower () == 'v'):
            #firstname exist, fill till last name
            firstname = ''
            index += 1
            while( not (workingArray[index].lower() == 'n' )):
                if(firstname ==''):
                    firstname = workingArray[index].upper()
                else:
                    firstname = firstname + ' ' + workingArray[index].upper()
                index += 1

            if(not( firstname == '')):
                self.variables.append(firstname)
            else:
                self.variables.append('-1')
        else:
            self.variables.append('-1')

        #familyName (if there is none, its -1)
        if(workingArray[index].lower () == 'n'):
            #firstname exist, fill till last name
            familyName = ''
            index += 1
            while(( not (workingArray[index].lower() == 'a' )) or (workingArray[index][-4:-3] == '.')):
                if(familyName == ''):
                    familyName = workingArray[index].upper()
                else:
                    familyName = familyName + ' ' + workingArray[index].upper()
                index += 1

            if(workingArray[index][-4:-3] == '.' and ( not workingArray[index][0] == '.')):
                name, fileEnd = workingArray[index].split('.')
                familyName = familyName + name

            if(not( familyName == '')):
                self.variables.append(familyName)
            else:
                self.variables.append('-1')
        else:
            self.variables.append('-1')

        #age (if there is none, its -1)
        if(workingArray[index].lower() =='a'):
            age, fileEnd = workingArray[index+1].split('.')
            if(age.isnumeric()):
                self.variables.append(age)
            else:
                #age was not a number
                self.variables.append('-1')
        else:
            self.variables.append('-1')
        
        return 0


    def generateString(self):
        #alwasy when enty exists, add that to string
        output = "<li class=\"grid-item " + str(self.variables[0]) + "\">\n    <a href=\"grossesbild.php?"
        output = output + "bild=" + str(self.fullName)
        if(not self.variables[1] == '-1'):
            output = output + "&vorname=" + str(self.variables[1])
        if(not self.variables[2] == '-1'):
            output = output + "&nachname=" + str(self.variables[2]) + "."
        if(not self.variables[3] == '-1'):
            output = output + "&alter=" + str(self.variables[3])
        output = output + "&kg=" + str(self.variables[0])
        output = output + "\"><img src=\"zeichnungen/"+ str(self.fullName)
        output = output +"\" alt=\"\" />\n    <div class=\"mask\"></div></a>"
        return output




if __name__ == "__main__":

    dirPlace = r"./zeichnungen" #change path here (or maybe wherever the script lies? whatever)

    f = open("htmlCode.invalid", "w")
    p = open("InvalidPictures.csv", 'w')

    with os.scandir(dirPlace) as dirs:
        for entry in dirs:
        #read data name in
            #print(entry.name)
            picture = Picture(entry.name, dirPlace)
            #print("This is:", picture.fullName, 'path:', picture.path)
            string = picture.doMagic(p)
            if string == None :
                string = ''
            else:
                string = string + '\n'
            f.write(string)


