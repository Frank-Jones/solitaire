# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:44:26 2016

@author: Frank
"""
import sys

board=[1]*37
board[18]=0

progress=[-1]*36

moves=([0,2,1],[0,10,4],[1,11,5],[2,0,1],[2,12,6],[3,16,9],[3,5,4],[4,17,10],
[4,6,5],[5,3,4],[5,18,11],[5,7,6],[6,4,5],[6,19,12],[7,5,6],[7,20,13],
[8,22,15],[8,10,9],[9,23,16],[9,11,10],[10,8,9],[10,24,17],[10,12,11],[10,0,4],
[11,9,10],[11,25,18],[11,13,12],[11,1,5],[12,10,11],[12,26,19],[12,14,13],
[12,2,6],[13,11,12],[13,27,20],[14,12,13],[14,28,21],[15,17,16],[16,29,23],
[16,18,17],[16,3,9],[17,15,16],[17,30,24],[17,19,18],[17,4,10],[18,16,17],
[18,31,25],[18,20,19],[18,5,11],[19,17,18],[19,32,26],[19,21,20],[19,6,12],
[20,18,19],[20,33,27],[20,7,13],[21,19,20],[22,24,23],[22,8,15],[23,25,24],
[23,9,16],[24,22,23],[24,34,30],[24,26,25],[24,10,17],[25,23,24],[25,35,31],
[25,27,26],[25,11,18],[26,24,25],[26,36,32],[26,28,27],[26,12,19],[27,25,26],
[27,13,20],[28,26,27],[28,14,21],[29,31,30],[29,16,23],[30,32,31],[30,17,24],
[31,29,30],[31,33,32],[31,18,25],[32,30,31],[32,19,26],[33,31,32],[33,20,27],
[34,36,35],[34,24,30],[35,25,31],[36,34,35],[36,26,32])

step=0

def reset_progress():
    progress=[-1]*36
    return;

def ascending_board():    
    board[0]=0
    board[1]=1
    board[2]=2
    board[3]=3
    board[4]=4
    board[5]=5
    board[6]=6
    board[7]=7
    board[8]=8
    board[9]=9
    board[10]=10
    board[11]=11
    board[12]=12
    board[13]=13
    board[14]=14
    board[15]=15
    board[16]=16
    board[17]=17
    board[18]=18
    board[19]=19
    board[20]=20
    board[21]=21
    board[22]=22
    board[23]=23
    board[24]=24
    board[25]=25
    board[26]=26
    board[27]=27
    board[28]=28
    board[29]=29
    board[30]=30
    board[31]=31
    board[32]=32
    board[33]=33
    board[34]=34
    board[35]=35
    board[36]=36
    return;

def reset_board():
    board[0]=1
    board[1]=1
    board[2]=1
    board[3]=1
    board[4]=1
    board[5]=1
    board[6]=1
    board[7]=1
    board[8]=1
    board[9]=1
    board[10]=1
    board[11]=1
    board[12]=1
    board[13]=1
    board[14]=1
    board[15]=1
    board[16]=1
    board[17]=1
    board[18]=0
    board[19]=1
    board[20]=1
    board[21]=1
    board[22]=1
    board[23]=1
    board[24]=1
    board[25]=1
    board[26]=1
    board[27]=1
    board[28]=1
    board[29]=1
    board[30]=1
    board[31]=1
    board[32]=1
    board[33]=1
    board[34]=1
    board[35]=1
    board[36]=1
    return;

def print_board():
    
    print(
    "         ",board[0:3],'\n',
    "     ",board[3:8],'\n',
    "  ",board[8:15],'\n',
    "  ",board[15:22],'\n',
    "  ",board[22:29],'\n',
    "     ",board[29:34],'\n',
    "        ",board[34:37],'\n')
    return;
    
def make_move(cat_no,step):
    #print ("Entered make_move with step = ", step, " and cat_no = ", cat_no)
    board[moves[cat_no][0]]=0
    board[moves[cat_no][1]]=1
    board[moves[cat_no][2]]=0
    progress[step]=cat_no
    return;
    
def undo_move(x_cat_no,x_step):
    #print ("Entered undo_move with step = ", x_step, " and cat_no = ", x_cat_no)
    if x_cat_no==91:
        progress[x_step]=0
        board[moves[x_cat_no][0]]=1
        board[moves[x_cat_no][1]]=0
        board[moves[x_cat_no][2]]=1
        x_step -= 1
        undo_move (progress[x_step], x_step)
    else:    
        board[moves[x_cat_no][0]]=1
        board[moves[x_cat_no][1]]=0
        board[moves[x_cat_no][2]]=1
        progress[x_step]+=1
    #print ("Leaving undo_move with step = ", x_step, " and cat_no = ", x_cat_no)
    return x_cat_no, x_step;

def undo_last_move():
    progress_count=0
    while progress[progress_count] != -1:
        progress_count+=1
    cat_no=progress[progress_count-1]
    progress[progress_count-1]=-1
    board[moves[cat_no][0]]=1
    board[moves[cat_no][1]]=0
    board[moves[cat_no][2]]=1
    #print ("From undo_last_move",progress)
    #print_board()
    #x=input("Pause on exit of undo_last_move:")
    return;
    
def validate_move(cat_no):
    if (board[moves[cat_no][0]]==1) and (board[moves[cat_no][1]]==0) and (board[moves[cat_no][2]]==1):
        return True
    else:
        return False
        
def count_untakeables():
    untakeables=0
    if board[0]==1:
        untakeables+=1
    if board[2]==1:
        untakeables+=1
    if board[3]==1:
        untakeables+=1
    if board[7]==1:
        untakeables+=1
    if board[8]==1:
        untakeables+=1
    if board[14]==1:
        untakeables+=1
    if board[22]==1:
        untakeables+=1
    if board[28]==1:
        untakeables+=1
    if board[29]==1:
        untakeables+=1
    if board[33]==1:
        untakeables+=1
    if board[34]==1:
        untakeables+=1
    if board[36]==1:
        untakeables+=1
    return untakeables;
    
def count_greens():
    greens=0
    if board[1]==1:
        greens+=1
    if board[9]==1:
        greens+=1
    if board[11]==1:
        greens+=1
    if board[13]==1:
        greens+=1
    if board[23]==1:
        greens+=1
    if board[25]==1:
        greens+=1
    if board[27]==1:
        greens+=1
    if board[35]==1:
        greens+=1       
    return greens;
   
def count_blues():
    blues=0
    if board[4]==1:
        blues+=1
    if board[6]==1:
        blues+=1
    if board[15]==1:
        blues+=1
    if board[17]==1:
        blues+=1
    if board[19]==1:
        blues+=1
    if board[21]==1:
        blues+=1
    if board[30]==1:
        blues+=1
    if board[32]==1:
        blues+=1
    return blues;
     
def fail_test1():
    untakeable_count=count_untakeables()
    green_count=count_greens()
    blue_count=count_blues()
    if untakeable_count>(green_count+blue_count):
        return True;
    else:
        return False;    
        
def count_moves():
    no_of_moves=0
    if fail_test1()==True:
        print ("FT",progress)
        return no_of_moves;
    cat_no=0
    while cat_no!=92:    
        if (board[moves[cat_no][0]]==1) and (board[moves[cat_no][1]]==0) and (board[moves[cat_no][2]]==1):
            no_of_moves+=1
            #print("Candidate move is ",cat_no)
        cat_no+=1
    #print("Number of moves from within count_moves ",no_of_moves)
    return no_of_moves;

def get_first_move():
    count=0
    while count!=92:
        if (board[moves[count][0]]==1) and (board[moves[count][1]]==0) and (board[moves[count][2]]==1):        
            return count;
        count+=1
        
def get_subs_move():
    progress_count=0
    while progress[progress_count] != -1:
        progress_count+=1
    count=progress[progress_count-1]+1
    #print ("First while in get_subs_move ends with progress_count at ", progress_count, " and count at ",count)
    undo_last_move()    
    while count!=92:
        if (board[moves[count][0]]==1) and (board[moves[count][1]]==0) and (board[moves[count][2]]==1):        
            return count;
        count+=1
    print ("Something went wrong! count in get_subs_move got to 92")
    return
            
def make_first_move(cat_no):
    board[moves[cat_no][0]]=0
    board[moves[cat_no][1]]=1
    board[moves[cat_no][2]]=0
    progress_count=0
    while progress[progress_count] != -1:
        progress_count+=1
    progress[progress_count]=cat_no
    if progress_count>=33:
        print (progress)
    if progress_count==34:
        print_board()
        print (progress)
        sys.exit()
    return;
    
def make_subs_move(cat_no):
    board[moves[cat_no][0]]=0
    board[moves[cat_no][1]]=1
    board[moves[cat_no][2]]=0
    progress_count=0
    while progress[progress_count] != -1:
        progress_count+=1
    progress[progress_count-1]=cat_no
    return;

def process_node():
    #x=input("Pause inside process node:")
    #print ("From entry of process_node ",progress)
    #print_board()
    num_branches=count_moves()
    #print (num_branches)
    if num_branches!=0:
        attempts=0
        #print("No of attempts in process node ",attempts)
        while attempts!=num_branches:
            if attempts==0:
                next_move=get_first_move()
                make_first_move(next_move)
            else:
                next_move=get_subs_move()
                #print ("next_move from inside the subs branch ", next_move)
                make_first_move(next_move)
            process_node()
            attempts+=1
            #print("attempts was incremented to ", attempts, "num_branches is currently ",num_branches)
            if attempts==num_branches:
                undo_last_move()
                return;
    else:
        return;
        
process_node()
