f=open("input3.txt","r")
import numpy as np
list=f.readlines()
f.close()
Si,Smax,T,D=list[0].split()
fragList=[]
Sc=[] 
Tr=[]
Sr=[]
Na=[]
isinList=[]
for line in list[1:]: #each line represents a demon
    x= line.split()
    Sc.append(int(x[0])) #stamina to spent to fight
    Tr.append(int(x[1])) #turns recovering stamina
    Sr.append(int(x[2])) #recover per round
    Na.append(int(x[3])) #Turns getting rewards
    temp = [int(item) for item in x[4:]]
    fragList.append(temp) #reward for each turn

Si,Smax,T,D=int(Si),int(Smax),int(T),int(D)
stamina=Si
fragments=0
pick=[] #list of picked demons at each turn
turn=0
stam=np.zeros(3*T, int) #here we store the stamina that we will gain in next rounds
frag=np.zeros(3*T, int) #here we store the fragments that we will gain in next rounds



while turn<T:
    #step 1: recover stamina
    stamina=stamina+stam[turn]
    if stamina>Smax:
        stamina=Smax
    #step 2: find demon and fight him
    rem=T-turn
    MaxReward=0
    fight=0
    if len(pick)<D: #fight demon 
        for j in range(D):
            if Na[j]==0:
                continue
            if j not in pick and Sc[j]<=stamina:
                recoverFor=Tr[j]
                maxRecover=(Sr[j])*(recoverFor-rem)
                Reward=sum(fragList[j][:(rem)]) #demon that will give max reward at current step
                Penalized=Reward/Sc[j] #use this for better results
                if Penalized>MaxReward:
                    maxrewdemon=j
                    MaxReward=Penalized
                    fight=1
                
    if fight==1:       
        j=maxrewdemon 
        pick.append(j)
        stamina=stamina-Sc[j] #stamina lost fighting
        arr = np.array(fragList[j])
        frag[turn+1:turn+Na[j]+1]=np.add(frag[turn+1:turn+Na[j]+1],arr)
        temps=np.array([Sr[j]]*Na[j])
        #stam[turn+1:turn+Tr[j]]=stam[turn+1:turn+Na[j]]+temps
        stam[turn+1:turn+Na[j]+1]=np.add(frag[turn+1:turn+Na[j]+1],temps)
    #step 3: collect fragments
    fragments=fragments+frag[turn]
    #step 4: next turn
    turn=turn+1
print(fragments)


filename = "output_numbers.txt"

#w tells python we are opening the file to write into it
outfile = open('output3.txt', 'w')
for number in pick:
	outfile.write(str(number)+'\n')
outfile.close() #Close the file when we’re done!