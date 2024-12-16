
dic={}
grid=[]
with open("input.txt") as f:
    for i,line in enumerate(f.readlines()):
        grid.append(list(line.strip()))
        for j,ch in enumerate(line.strip()):
            if ch!='.':
                if ch in dic:
                    dic[ch].append((i,j))
                else:
                    dic[ch]=[(i,j)]

# print(dic)
# print(len(grid),len(grid[0]))

def inside_grid(x,y):
    return 0<=x<len(grid) and 0<=y<len(grid[0])


valid_nodes=set()
for key in dic:
    for i in range(len(dic[key])):
        for j in range(i+1,len(dic[key])):
            #Find the two antinodes that are formed by this pair
            #An antinode is a point that is colinear to the two points and is twice as far away from one point as the other

            #The two points are at dic[key][i] and dic[key][j]
            #The antinode is at (x,y)
            x1,y1=dic[key][i]
            x2,y2=dic[key][j]

            dx,dy = x1-x2, y1-y2
            node1x,node1y = x1+dx,y1+dy
            node2x,node2y = x2-dx,y2-dy

            if node1x==x1 and node1y==y1:
                print("ISSUE:",node1x,node1y,node2x,node2y)
            if node2x==x2 and node2y==y2:
                print("ISSUE:",node1x,node1y,node2x,node2y)

            if inside_grid(node1x,node1y):
                valid_nodes.add((node1x,node1y))
            
            if inside_grid(node2x,node2y):
                valid_nodes.add((node2x,node2y))

# print(valid_nodes)
print(len(valid_nodes))
