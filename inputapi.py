class SmartInput():
    def inputInt(msg):
        """
        Input validation as an int.
        :return: only returns valid int values
        """
        while True:
            try:
                n = int(input(msg))
                return n
            except:
                print("error, try again")

    def posFloat(msg):
        """
        Input validation as an float.
        :return: only returns valid float values
        """
        while True:
            try:
                n = float(input(msg))
                if n<0:
                    print("error, try again")
                    continue
                return n
            except:
                print("error, try again")



if __name__ == "__main__":  #if this file is run, it is called '__main__' regardless of filename
    print ("hello")

if __name__ == "inputapi":  #if run as imported, called like this.
    print ("api")
