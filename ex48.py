class Lexicon(object):
    def scan(self, userinput):
        # First split up the input into a list of words
        words = userinput.split()
        output = []
        # Next go through the list, for each word give it a label from a list of words for each label
        for item in words:
            result = self.label(item) # return a nice tuple - needs to be "self.", because it's a clas
            output.append(result)
        # return a list of all of these labled words
        return output

    def label(self, item):
        # label the item and packacge it up in a tuple
        if item in ['north', 'south', 'east']:
            return ('direction', item)
        # test if it's a verb
        elif item in ['go', 'kill', 'eat']:
            return ('verb', item)
        # test if it's a stop
        elif item in ['the', 'in', 'of']:
            return ('stop', item)
        # test if it's a noun
        elif item in ['bear', 'princess']:
            return ('noun', item)
        # test if it's a number
        # test if it's crap
        else:
            try:
                number = int(item) # it's possible the item is not an int
                return ('number', number)
            except ValueError: # catches up  the posible error of ValueError
                # what if the item is not a number?
                return('error', item)


lexicon = Lexicon()
