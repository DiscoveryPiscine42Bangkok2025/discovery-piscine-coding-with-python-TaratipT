from checkmate import checkmate

def main():
##### Success (Pawn Checkmate)
    board = """\
R...
.K..
..P.
....\
"""

# ##### Success (Rook Checkmate)
#     board = """\
# ......
# .K....
# ....P.
# ......
# .R....
# ...B..\
# """

# ##### Success (Bishop Checkmate)
#     board = """\
# .....Q
# K.....
# ....P.
# ......
# ...B..
# .R....\
# """

# ##### Success (Queen Checkmate)
#     board = """\
# K....Q
# ......
# ....P.
# ......
# ...B..
# .R....\
# """

# ##### Fail (Not Checkmate)
#     board = """\
# ........
# .....P..
# ...R....
# ........
# ........
# .K......
# ........
# ....Q...\
# """

# ##### Error (Size Not Correct [Column > Row])
#     board = """\
# R...
# .K.....
# ..P.
# ....\
# """    

# ##### Error (Size Not Correct [Row > Column])
#     board = """\
# R...
# .K..
# ..P.
# ....
# ....
# ....\
# """    

# ##### Error (Character not allowed [Row > Column])
#     board = """\
# ...Z
# .K..
# ..P.
# ,...\
# """    

# ##### Error (Double King)
#     board = """\
# R.K.
# .K..
# ..P.
# ....\
# """

# ##### Rook can attack King (but blocked by Pawn)
#     board = """\
# ..K..
# ..P..
# .....
# ..R..
# .....\
# """
    checkmate(board)

if __name__ == "__main__":
    main()
