"""The computer riddling a number, and our algorithm trying to guess it and calculate avg number of tryies"""

import numpy

def GuessAlgorythm(numb : int = 1) -> int:
    """The Algorythm for guessing unknown number
    Args:
        numb (int, optional): It takes the number that computer riddled . Defaults to 1.
    Returns:
        int: numer of passes
    """
    leftEdge = 0
    rightEdge = 101
    middle = rightEdge // 2
    passes = 0 # number of passes
    
    while middle != numb:
        if numb > middle: # if our numb more than 'middle', we're moving 'leftEdge' to 'middle' and calculating new 'middle' 
            leftEdge = middle 
            middle += (rightEdge - middle) // 2
            passes += 1            
        else: # the same, but with 'rightEdge', if our' numb' less than 'middle'
            rightEdge = middle
            middle -= (middle - leftEdge) //2
            passes += 1
    #print(f'Number {middle} guessed in {passes} tryies')        
    return passes

def Average():
    """ Void function which calculating avg number of tryies
    Returns:
        Nothing
    """
    attempts_list = [] #creating list, which will contain attempts
    num_list = numpy.random.randint(1, 101, 1000) # list with random numbers
    
    for number in num_list:
        attempts_list.append(GuessAlgorythm(number)) # Calling 'GuessAlgorythm' for every element form 'num_list' 
    avg = int(numpy.mean(attempts_list)) # With 'numpy.mean' calculating average number of tryies
    print(f"On average, Algorytm guesses number in {avg} tryies")
    
if __name__ == "__main__":
    numpy.random.seed(1)
    Average()