



class IntValidator:

    # this method will check for the inputValue if is a number, and between
    # rangeLeft & rangeRight (inclusive), and if not, it will be returned false
    @staticmethod
    def valid(inputValue,rangeLeft,rangeRight):
        try:
            integer=int(inputValue)
            return integer >= rangeLeft and integer <= rangeRight
        except:
            return False
