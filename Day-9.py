'''List comprs'''

'''1D 2D list '''
# row =[]
# for i in range(8):
#     row.append("white_PAWN")


# row = ["WHITE_PAWN" for i in range(8)]
# squares =[index **2 for index in range(1,11)]
# two = [2 **index for index in range(8)]


# print(row)
# print(squares)
# print(two)

# squares =[index **2 for index in range(1,11)]
# odds = [f'{element}:Is odd Number' for element in squares if element%2 != 0]
# print(odds)

'''chess board'''

# board = []

# for i in range(8):
#      row = ["EMPTY" for i in range(8)]
#      board.append(row)
# # print(board)    #board size will be 8 here
# for element in board:
#      print(element)
# #print(len(board))
# board[0][0] = "ROOK"
# board[0][7] = "ROOK"
# board[7][0] = "ROOK"
# board[7][7] = "ROOK"

# print("---------------")
# for element in board:
#     print(element)

# board[0][1] = "Knight"
# board[0][6] = "Knight"
# board[7][1] = "Knight"
# board[7][6] = "Knight"

# print("---------------")
# for element in board:
#     print(element)


# board[0][2] = ""
# board[0][5] = ""
# board[7][2] = ""
# board[7][5] = ""

# print("---------------")
# for element in board:
#     print(element)

''' **weather station'''
# 24 hours , 31 days in month

# temps =[[0.0 for h in range(24)] for d in range(31)]
# temp1 = 19
# temp2 = 32
# temp3 = 33
# count = 0

# for days  in temps:
#   if count == 0:
#     days[11] = temp1
#     count = 1
#   elif count == 1:
#     days[11] = temp3
#     count = 2
#   else:
#    days[11] = temp2
#    count =0

# for element in temps:
#   print(element)

# total = 0.0
# for days in temps:
#     total += days[11]
# average = total/31
# print("average temperature at noon:",average)

# higesht = -100.0
# for days in temps:
#      for temp in days:
#         if temp > higesht:
#            higesht = temp
# print("highest temp was : ",higesht)


# Grm_din = 00
# for day in temps:
#    if day[11] > 20.0:
#       Grm_din += 1
# print(Grm_din,"days were hot days in the month")





'''3D 3building 15 floor 20 room/floor '''
# here false means all are empty initialy
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)] # this is the 3 D list which consist 3 building which have 15 floors and which have 20 rooms in each floor
print(rooms)

rooms [1] [9][13] =True
rooms [1] [9][1] = True

vacancy = 0
for room_num in range(20):
    if not rooms[1][9][room_num]:
        vacancy += 1
print("vacancy in 10th floor, of 3rd building is",vacancy)
