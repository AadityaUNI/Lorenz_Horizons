class InputTaker:
    
    @staticmethod
    def validifyRange(inputs, validRange):
        if inputs not in validRange:
            print("Invalid input, please try again.")
            return False
        return True
    
    
    @classmethod
    def readInt(cls, prompt="> ", validRange=None):
        while True:
            try:
                value = int(input(prompt))
            except (EOFError, KeyboardInterrupt):
                return None
            except ValueError:
                print("Invalid input, please try again.")
                continue

            if validRange is not None and not cls.validifyRange(value, validRange):
                continue

            return value


    @classmethod
    def readFloat(cls, prompt="> ", validRange=None):
        while True:
            try:
                value = float(input(prompt))
            except (EOFError, KeyboardInterrupt):
                return None
            except ValueError:
                print("Invalid input, please try again.")
                continue

            if validRange is not None and not cls.validifyRange(value, validRange):
                continue

            return value
