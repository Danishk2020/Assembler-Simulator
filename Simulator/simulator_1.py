
mem=[]
pc=-1
y_axis=[]
register = {"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"R7":0}
flags= {"V":0,"L":0,"G":0,"E":0}
def find_register(s):
    if(s=="000"):
        return "R0"
    elif(s=="001"):
        return "R1"
    elif(s=="010"):
        return "R2"
    elif(s=="011"):
        return "R3"
    elif(s=="100"):
        return "R4"
    elif(s=="101"):
        return "R5"
    elif(s=="110"):
        return "R6"
    elif(s=="111"):
        return "R7"


def Move_Register(a):
    reg1 = find_register(a[10:13])
    reg2 = find_register(a[13:16])
    register[reg1]=register[reg2]
    global pc
    pc+=1
def Divide(a):
    reg1 = find_register(a[10:13])
    reg2 = find_register(a[13:16])
    register["R1"]=register[reg1]%register[reg2]
    register["R0"] = register[reg1] // register[reg2]
    global pc
    pc+=1
def compare(a) :
    reg1 = find_register(a[10:13])
    reg2 = find_register(a[13:16])
    if(register[reg1]<register[reg2]):
        flags["L"]=1
    elif(register[reg1]>register[reg2]):
        flags["G"] = 1
    elif(register[reg1]==register[reg2]) :
        flags["E"]=1
    global pc
    pc+=1

def invert(a):
    reg1 = find_register(a[10:13])
    reg2 = find_register(a[13:16])
    register[reg1] = ~register[reg2]
    global pc
    pc+=1

def binary_to_deci(s):
    k = 0
    g = len(s)-1
    for i in s:
         k = (2**g)*int(i)+k
         g = g-1
    return k
def dec_to_bina(k):
    s = ""
    if k==0:
        s = "0"
        return s
    else:
        while(k>0):
            t =k%2
            k = k//2
            s = s+ str(t)
    s=s[::-1]
    return s


def Unconditional_Jump(a):
    k = binary_to_deci(a[8:16])
    global pc
    pc = k

def Jump_If_Less_Than(a):
    if(flags["L"]==1):
        Unconditional_Jump(a)
    else:
        global pc
        pc+=1
        return
def Jump_If_Greater_Than(a) :
    if (flags["G"] == 1):
        Unconditional_Jump(a)
    else:
        global pc
        pc+=1
        return
def Jump_If_Equal(a):
    if (flags["E"] == 1):
        Unconditional_Jump(a)
    else:
        global pc
        pc+=1
        return


def reg_immediate_type(a):
    st_val=a[8:16]
    reg = find_register(a[5:8])
    store_val=binary_to_deci(st_val)
    register[reg]=store_val
    global pc
    pc+=1

def right_Shift(a):
    reg=find_register(a[5:8])
    t=binary_to_deci(a[8:16])
    w=register[reg]//2**t
    register[reg]=w
    global pc
    pc+=1

def left_Shift(a):
    reg=find_register(a[5:8])
    t=binary_to_deci(a[8:16])
    w=register[reg](2*t)
    register[reg]=w
    global pc
    pc+=1


   



def Addition(a):
    reg1 = find_register(a[7:10])
    reg2 = find_register(a[10:13])
    reg3 = find_register(a[13:16])
    register[reg1]=register[reg2]+register[reg3]
    if register[reg1]>255 or register[reg1]<0:
        flags["V"]=1
        register[reg1]=0

    global pc
    pc+=1

def Subtraction(a):
    reg1 = find_register(a[7:10])
    reg2 = find_register(a[10:13])
    reg3 = find_register(a[13:16])
    register[reg1]=register[reg2]-register[reg3]
    if register[reg1]>255 or register[reg1]<0:
        flags["V"]=1
        register[reg1]=0

    global pc
    pc+=1

def Multiply(a):
    reg1 = find_register(a[7:10])
    reg2 = find_register(a[10:13])
    reg3 = find_register(a[13:16])
    register[reg1]=register[reg2]*register[reg3]
    if register[reg1]>255 or register[reg1]<0:
        flags["V"]=1
        register[reg1]=0

    global pc
    pc+=1

def Exclusive_OR(a):
    reg1 = find_register(a[7:10])
    reg2 = find_register(a[10:13])
    reg3 = find_register(a[13:16])
    register[reg1]=register[reg2]^register[reg3]
    global pc
    pc+=1

def OR(a):
    reg1 = find_register(a[7:10])
    reg2 = find_register(a[10:13])
    reg3 = find_register(a[13:16])
    register[reg1]=register[reg2]|register[reg3]
    global pc
    pc+=1

def And(a):
    reg1 = find_register(a[7:10])
    reg2 = find_register(a[10:13])
    reg3 = find_register(a[13:16])
    register[reg1]=register[reg2]&register[reg3]
    global pc
    pc+=1

def Load(a):
    reg= find_register(a[5:8])
    mem_add=binary_to_deci(a[8:16])
    register[reg]=mem[mem_add]
    global pc
    pc+=1

def Store(a):
    reg= find_register(a[5:8])
    mem_add=binary_to_deci(a[8:16])
    mem[mem_add]=print_16_bit(register[reg])               
    global pc
    pc+=1
    
def flag_set():
    masla= binary_to_deci(str(flags["V"])+str(flags["L"])+str(flags["G"])+str(flags["E"]))
    register["R7"]=masla

def hlt(a):
    global pc
    pc+=1

def reset_flag():
    flags["V"]=0
    flags["L"]=0
    flags["G"]=0
    flags["E"]=0


def main(a):
    if a[:5]=="00000":
        Addition(a)

    elif a[:5]=="00001":
        Subtraction(a)

    elif a[:5]=="00110":
        Multiply(a)

    elif a[:5]=="01010":
        Exclusive_OR(a)

    elif a[:5]=="01011":
        OR(a)
    
    elif a[:5]=="01100":
        And(a)

    elif a[:5]=="00100":
        Load(a)

    elif a[:5]=="00101":
        Store(a)
    
    elif a[:5]=="10011":
        hlt(a)

    elif(a[:5]=="00011"):
        Move_Register(a)
    elif(a[:5]=="00111"):
        Divide(a)
    elif(a[:5]=="01101"):
        invert(a)
    elif(a[:5]=="01110"):
        compare(a)
    elif(a[:5]=="01111") :
        Unconditional_Jump(a)
    elif(a[:5]=="10000") :
        Jump_If_Less_Than(a)
    elif(a[:5]=="10001") :
        Jump_If_Greater_Than(a)
    elif(a[:5]=="10010") :
        Jump_If_Equal(a)

    elif a[:5]=="00010":
        reg_immediate_type(a)
    elif a[:5]=="01001":
        left_Shift(a)
    elif a[:5]=="01000":
        right_Shift(a)
            


def print_8_bit(a):
    s=dec_to_bina(a)
    len_of_zero=8-len(s)
    return "0"*len_of_zero+s

def print_16_bit(a):
    s=dec_to_bina(a)
    len_of_zero=16-len(s)
    return "0"*len_of_zero+s

def real_print():
    fl = binary_to_deci(str(flags["V"])+str(flags["L"])+str(flags["G"])+str(flags["E"]))
    result=print_8_bit(pc)+" "+print_16_bit(register["R0"])+" "+print_16_bit(register["R1"])+" "+print_16_bit(register["R2"])+" "+print_16_bit(register["R3"])+" "+print_16_bit(register["R4"])+" "+print_16_bit(register["R5"])+" "+print_16_bit(register["R6"])+" "+print_16_bit(fl)
    print(result)




while True:
    a=input()

    if a=="1001100000000000":
        #memory append
        mem.append(a)
        break
    else:
        #memory append
        mem.append(a)
        continue
main_code_length=len(mem)
bachi_hue_zero=256-len(mem)

for i in range(bachi_hue_zero):
    mem.append("0000000000000000")


for i in range(main_code_length):
    main(mem[pc+1])
    flag_set()
    y_axis.append(pc+1)
    real_print()
    reset_flag()

    

for i in mem:
    print(i)

for i in range(bachi_hue_zero):
    lul=main_code_length+1
    y_axis.append(lul)
    lul+=1


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
plt.show()



