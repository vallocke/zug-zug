# Name: Peter Kelt
# Date: 01/27/2013
# nims.py

def check_input(ans, max_take, on_pile):
    if (ans > 0 and ans <= max_take and on_pile >= ans):
        return True
    else:
        print "Invalid response!"
        return False

def get_input(player, max_take, on_pile):
    return int(raw_input('Player %d, choose # of stones to take (1-%d): ' %
                         (player, min(max_take, on_pile))))
               
def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''
    cur_pile = pile
    valid_ans = False
    player = 1
    while(cur_pile > 0):
        while(valid_ans == False):
            answer = get_input(player, max_stones, cur_pile)
            valid_ans = check_input(answer, max_stones, cur_pile)

        if cur_pile - answer != 0:
            if player == 1:
                player = 2
            else:
                player = 1
            valid_ans = False
            
        cur_pile = cur_pile - answer
        print "Only %d stone remaining." % cur_pile

    print "Player %d is the Winner!" % player

play_nims(100, 5)
