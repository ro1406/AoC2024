
W=101
H=103
num_steps=100
q1,q2,q3,q4=0,0,0,0

with open("input.txt",'r') as f:
    for line in f.readlines():
        p,v = line.strip().split(" ")
        posx,posy = map(int,p.split('=')[-1].split(','))
        velx,vely = map(int,v.split('=')[-1].split(','))
        # print(f'{posx=}, {posy=}, {velx=}, {vely=}')
        #Find final position after 100 steps
        for i in range(num_steps):
            posx = (posx+velx)%W
            posy = (posy+vely)%H
        # print(f'Final pos: {posx=}, {posy=}')
        
        #check which quadrant the robot ended up in:
        if posx<W//2 and posy<H//2:
            q1+=1
        elif posx<W//2 and posy>H//2:
            q2+=1
        elif posx>W//2 and posy<H//2:
            q3+=1
        elif posx>W//2 and posy>H//2:
            q4+=1

        # print(f"{q1=}, {q2=}, {q3=}, {q4=}")

print(q1*q2*q3*q4)