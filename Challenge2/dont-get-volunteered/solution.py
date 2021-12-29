def solution(src,dest):
    #Source and Destination Index find out
    def find_index(num):
        row = int(num/8)
        col = num - row*8
        return row,col


    src_index = find_index(src)
    dest_index = find_index(dest)

    visited = []


    def check_valid_moves(moves):
        valid = []
        for i in moves:
            if i in visited:                                     # Check if the node is already visited or not
                continue
            if(i[0]>=0 and i[0]<=7 and i[1]>=0 and i[1]<=7):            # Checking if the move is inside the matrix
                valid.append(i)
        return valid
            
            



    def get_possible_moves(index):
        r,c = index
        all_moves = []

        # 8 possible moves of the knight
        all_moves.append((r+2,c-1))
        all_moves.append((r-2,c-1))
        all_moves.append((r+2,c+1))
        all_moves.append((r-2,c+1))
        all_moves.append((r-1,c+2))
        all_moves.append((r-1,c-2))
        all_moves.append((r+1,c+2))
        all_moves.append((r+1,c-2))
        valid_moves = check_valid_moves(all_moves)
        return valid_moves


    q = []
    q.append(src_index)
    visited.append(src_index)

    # Level Flag
    q.append(1)
    level = 0

    if(src == dest):                         # If both same, no cost 
        return level
    else:
        flag = 0                             # Destination flag
        while q and flag == 0:
            current = q.pop(0)               # dequeing from list
            if current==1:
                level += 1
                q.append(1)
                continue
            else:
                moves = get_possible_moves(current)
                for next in moves:
                    if (next!=dest_index):
                        q.append(next)
                        visited.append(next)
                    else:
                        flag = 1
                        level += 1
                        return level
    
print(solution(10,10))