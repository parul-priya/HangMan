from random import randint
class word_guess() :
    def __init__(self) :
        print "Life's a game! Wanna Play??"
        print " 1 : Let's play  OR  2 : No thanks! "

        i = raw_input( ' : ' )
    
        if i == '1' :
            self.play()
        elif i == '2' :
            exit()

        else :
          print 'Enter 1 or 2 only!'

    def play(self) :
        print 'Okay! Buckle Up!'
        self.game()


    def game(self) :
        words = ['cheerful', 'cheery', 'merry', 'joyful', 'jovial', 'jolly', 'jocular', 'gleeful', 'carefree', 'untroubled', 'delighted', 'smiling', 'beaming', 'grinning', 'lighthearted', 'pleased', 'contented', 'content', 'satisfied', 'gratified', 'buoyant', 'radiant', 'sunny', 'blithe', 'joyous', 'beatific']
        wrong_tries = 0
        used_let = ''
        word = words[randint(0,len(words)-1)]
        so_far = ['_ ' for i in range(len(word))]

        while wrong_tries < 5 :
        
            guess = raw_input('Enter your letter : ')

            if guess in used_let : print 'Letter already used, try again'

            else :
                used_let += guess
                if guess not in word :
                    wrong_tries += 1
                print '----------------------------------------'
                self.show(wrong_tries,word)
                print '----------------------------------------'
                self.update(guess, word, so_far)
                print 'So far : ' + ''.join(so_far)
                

    def update(self, guess, word, so_far) :
        for i,let in enumerate(word) :
            if guess == let :
                so_far[i] = let
        if ''.join(so_far) == word :
            print ('You guessed it!').upper()
            self.__init__()
        return so_far


    def show(self, w, word) :
        if w == 0 :
            print '-----'
            print '  |  '

        if w == 1 :
            print '-----'
            print '  |  '
            print '  0  '

        if w == 2 :
            print '-----'
            print '  |  '
            print '  0  '
            print '  |  '

        if w == 3 :
            print '-----'
            print '  |  '
            print '  0  '
            print ' /|\  '

        if w == 4 :
            print '-----'
            print '  |  '
            print '  0  '
            print ' /|\ '
            print '  |  '

        if w == 5 :
            print '-----'
            print '  |  '
            print '  0  '
            print ' /|\ '
            print ' /|\ '
            print 'Game Over'
            print 'Shoot! The word was : ' + word.upper()
            print '---------------------------------------------'
            self.__init__()


new = word_guess()

            
            








    
    
               
                
                
