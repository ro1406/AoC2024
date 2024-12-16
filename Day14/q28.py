from sklearn.cluster import DBSCAN
import pandas as pd
from tqdm import tqdm
W=101
H=103
num_steps=10_000
input_list = []
with open("input.txt",'r') as f:
    for line in f.readlines():
        p,v = line.strip().split(" ")
        posx,posy = map(int,p.split('=')[-1].split(','))
        velx,vely = map(int,v.split('=')[-1].split(','))
        # print(f'{posx=}, {posy=}, {velx=}, {vely=}')

        #save pos and vel into list
        input_list.append((posx,posy,velx,vely))


with open("grid.txt","w") as f:
    pass

write_to_file=False
#Find final position after 100 steps
for i in tqdm(range(num_steps)):
    temp_list = []
    grid=[['.' for _ in range(W)] for _ in range(H)]
    # dic={'row':[],'col':[]}

    for posx,posy,velx,vely in input_list:
        posx = (posx+velx)%W
        posy = (posy+vely)%H
        temp_list.append((posx,posy,velx,vely))
        grid[posy][posx]='#'
        # dic['row'].append(posy)
        # dic['col'].append(posx)
    input_list=temp_list.copy()
    
    #Make dataset with x,y coordinates and use DBSCAN for number of clusters
    # df = pd.DataFrame(dic)
    # model = DBSCAN()
    # model.fit(df)
    # labels = model.labels_
    # n_clusters = len(set(labels))
    # # print(f'Number of clusters: {n_clusters}')
    # if n_clusters>1:
    #     write_to_file=True
    #     print(f"FOUND IT!! IT WAS STEP NUMBER {i+1}")

    if any('#########' in ''.join(grid[row]) for row in range(H)):
        write_to_file=True
        print(f"FOUND IT!! IT WAS STEP NUMBER {i+1}")
        

    if write_to_file:
        with open("grid.txt","a") as f:
            f.write(f'STEP NUMBER {i+1}'+'\n')
            for x in grid:
                f.write(''.join(x))
                f.write('\n')
            f.write("="*100)
            f.write('\n')
            f.write('\n')
        write_to_file=False
        
    

   
    
        
