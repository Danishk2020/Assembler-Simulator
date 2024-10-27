flag=True
count=0
kul=[]
hlt_count=0
# num=0
import sys
dict={"add":"00000","sub":"00001","mov":"00011","ld":"00100","st":"00101","mul":"00110","div":"00111","rs":"01000","ls":"01001",
"xor":"01010","or":"01011","and":"01100","not":"01101","cmp":"01110","jmp":"01111","jlt":"10000","jgt":"1001","je":"10010","hlt":"10011"}
l=['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp', 'jlt', 'jgt', 'je', 'hlt']
rd={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","R7":"111"}
rer_p=["000","001","010","011","100","101","110","111"]

def op_check(opcode):
    for i in l:
        if i==opcode:
            return True   
    return False


def reg_check(reg):
    for i in rd:
        if i==reg:
            return True
    return False

def op_to_bin(opcode):
    return dict[opcode]

def rg_to_bin(rgcode):
    return rd[rgcode]

def imm_to_bin(no):
    b=(bin(no))[2:]       ##no is int value
    return "0"*(8-len(b))+b

def mem_addr_valid(add):
    if len(add)==8:
        return True
    else:
        return False

def error_in_register_nameor_instructions_name():
    print("error in register name  ")
def use_of_underfined_var():
    print("use of undefined variables")
def use_of_underfined_label():
    print("use of undefined label")
def illegal_use_of_flags_register():
    print("use of flag register")
def illegal_immediate_values():
    print("illegal immediate values")
def misuse_of_labels():
    print("Misuse of labels or vice versa")
def variables_not_declared_at_the_begining():
    print("variables not declared at the begining")
def missing_hlt_instructions():
    print("missing hlt instructions")
def hlt_not_being_used_as_instructions():
    print("hlt not being used as last instructions")

def wrong_syntax_used_for_instructions():
    print(" wrong syntax used for instructions")
def mem_add_out_of_range():
    print("memory adress out of range")
def general_error():
    print("general error")








def main(a):
    #to read input
    
    # a= input("input de:")
    z=a.split(" ")
    # count={}
    # count[num]=z
    # mum=num+1
    # print(z)


    # print(op_check(z[0]))
    if op_check(z[0])==False:
        wrong_syntax_used_for_instructions()
        

   
    if(z[0]=="add"):
        # print("ok")
        if  reg_check(z[1]):
            #  print("ok")
             if reg_check(z[2]):
                #  print("ok")
                 if reg_check(z[3]):
                    #  print("ok")
                     print(op_to_bin(z[0])+"00"+rg_to_bin(z[1])+rg_to_bin(z[2])+rg_to_bin(z[3]))

                 else:
                    error_in_register_nameor_instructions_name()
             else:
                error_in_register_nameor_instructions_name()
        else:
            error_in_register_nameor_instructions_name()
    # else:
    #     print("bhaag jaa")

    elif(z[0]=="sub"):
        if  reg_check(z[1]):
            #  print("ok")
             if reg_check(z[2]):
                #  print("ok")
                 if reg_check(z[3]):
                    #  print("ok")
                     print(op_to_bin(z[0])+"00"+rg_to_bin(z[1])+rg_to_bin(z[2])+rg_to_bin(z[3]))
                 else:
                    error_in_register_nameor_instructions_name()
             else:
                error_in_register_nameor_instructions_name()
        else:
            error_in_register_nameor_instructions_name()


    elif(z[0]=="mul"):
        if  reg_check(z[1]):
            #  print("ok")
             if reg_check(z[2]):
                #  print("ok")
                 if reg_check(z[3]):
                    #  print("ok")
                     print(op_to_bin(z[0])+"00"+rg_to_bin(z[1])+rg_to_bin(z[2])+rg_to_bin(z[3]))
                 else:
                    error_in_register_nameor_instructions_name()
             else:
                error_in_register_nameor_instructions_name()
        else:
            error_in_register_nameor_instructions_name()

    elif(z[0]=="xor"):
        if  reg_check(z[1]):
            #  print("ok")
             if reg_check(z[2]):
                #  print("ok")
                 if reg_check(z[3]):
                    #  print("ok")
                     print(op_to_bin(z[0])+"00"+rg_to_bin(z[1])+rg_to_bin(z[2])+rg_to_bin(z[3]))
                 else:
                    error_in_register_nameor_instructions_name()
             else:
                error_in_register_nameor_instructions_name()
        else:
            error_in_register_nameor_instructions_name()

    elif(z[0]=="or"):
        if  reg_check(z[1]):
            #  print("ok")
             if reg_check(z[2]):
                #  print("ok")
                 if reg_check(z[3]):
                    #  print("ok")
                     print(op_to_bin(z[0])+"00"+rg_to_bin(z[1])+rg_to_bin(z[2])+rg_to_bin(z[3]))
                 else:
                    error_in_register_nameor_instructions_name()
             else:
                error_in_register_nameor_instructions_name()
        else:
            error_in_register_nameor_instructions_name()

    elif(z[0]=="and"):
        if  reg_check(z[1]):
            #  print("ok")
             if reg_check(z[2]):
                #  print("ok")
                 if reg_check(z[3]):
                    #  print("ok")
                     print(op_to_bin(z[0])+"00"+rg_to_bin(z[1])+rg_to_bin(z[2])+rg_to_bin(z[3]))
                 else:
                    error_in_register_nameor_instructions_name()
             else:
                error_in_register_nameor_instructions_name()
        else:
            error_in_register_nameor_instructions_name()

    elif(z[0]=="hlt"):                                                    ###hlt function
        print(op_to_bin(z[0])+"00000000000")
    
    
    elif(z[0]=="mov"):
        d=z[2]
        if d[0]=="$":
            if reg_check(z[1]):
                if int( d[1:])<=255 and int(d[1:])>=0:
                    print("00010"+rg_to_bin(z[1])+imm_to_bin(int(d[1:])))
                else:
                    illegal_immediate_values()
            else:
                error_in_register_nameor_instructions_name()
        

        else:
            if reg_check(z[1]):
                if reg_check(z[2]):
                    print(op_to_bin(z[0])+"00000"+rg_to_bin(z[1])+rg_to_bin(z[2]))
                else:
                    error_in_register_nameor_instructions_name()
            else:
                error_in_register_nameor_instructions_name()
        


    elif(z[0]=="div"):
        if reg_check(z[1]):
            if reg_check(z[2]):
                    print(op_to_bin(z[0])+"00000"+rg_to_bin(z[1])+rg_to_bin(z[2]))
            else:
                error_in_register_nameor_instructions_name()
        else:
            error_in_register_nameor_instructions_name()

    elif(z[0]=="not"):
        if reg_check(z[1]):
            if reg_check(z[2]):
                print(op_to_bin(z[0])+"00000"+rg_to_bin(z[1])+rg_to_bin(z[2]))
            else:
                error_in_register_nameor_instructions_name()
        else:
            error_in_register_nameor_instructions_name()
    
    elif(z[0]=="cmp"):
        if reg_check(z[1]):
            if reg_check(z[2]):
                print(op_to_bin(z[0])+"00000"+rg_to_bin(z[1])+rg_to_bin(z[2]))
            else:
                error_in_register_nameor_instructions_name()
        else:
            error_in_register_nameor_instructions_name()

    elif(z[0]=="rs"):
        if reg_check(z[1]):
            d=z[2]
            if d[0]=="$":
                if int( d[1:])<=255 and int(d[1:])>=0:
                    print(op_to_bin(z[0])+rg_to_bin(z[1])+imm_to_bin(int(d[1:])))
                else:
                    illegal_immediate_values()
            else:
                wrong_syntax_used_for_instructions()
        else:
            error_in_register_nameor_instructions_name()

    elif(z[0]=="ls"):
        if reg_check(z[1]):
            d=z[2]
            if d[0]=="$":
                if int( d[1:])<=255 and int(d[1:])>=0:
                    print(op_to_bin(z[0])+rg_to_bin(z[1])+imm_to_bin(int(d[1:])))
                else:
                    illegal_immediate_values()
            else:
                wrong_syntax_used_for_instructions()
        else:
            error_in_register_nameor_instructions_name()




    elif(z[0]=="jmp"):
        if (mem_addr_valid(z[1])):
            print(op_to_bin(z[0])+z[1])
        else:
            mem_add_out_of_range()

    elif(z[0]=="jlt"):
        if (mem_addr_valid(z[1])):
            print(op_to_bin(z[0])+z[1])
        else:
            mem_add_out_of_range()

    elif(z[0]=="jgt"):
        if (mem_addr_valid(z[1])):
            print(op_to_bin(z[0])+z[1])
        else:
            mem_add_out_of_range()

    elif(z[0]=="je"):
        if (mem_addr_valid(z[1])):
            print(op_to_bin(z[0])+z[1])
        else:
            mem_add_out_of_range()


    elif(z[0]=="ld"):
        if (reg_check(z[1])):
            if(mem_addr_valid(z[2])):
                print(op_to_bin(z[0])+rg_to_bin(z[1])+z[2])
            else:
                mem_add_out_of_range()
        else:
            error_in_register_nameor_instructions_name()

    elif(z[0]=="st"):
        if (reg_check(z[1])):
            if(mem_addr_valid(z[2])):
                print(op_to_bin(z[0])+rg_to_bin(z[1])+z[2])
            else:
                mem_add_out_of_range()
        else:
            error_in_register_nameor_instructions_name()

    # else:
    #   print("bhaag jaa")












while True:
    a= input()
    # if hlt_count>1:
    #     general_error()
    #     break
    if a=="":
        continue
    else:
        if (a=="hlt"):
            hlt_count+=1
            kul.append(a)
            # kul[count]=a
            count+=1
            break
        else:
            if (":" in a):
                c,d=a.split(":")
                kul.append(a)
                # kul[count]=d
                # main(a)
                if d=="hlt":
                    hlt_count+=1
                    kul.append(a)
                    # kul[count]=d
                    count+=1
                    break
            else:
                kul.append(a)
                # kul[count] = a
                count+=1
                
                # main(a)
    
# while True:
#      a= input()
#      if a!="":
#          general_error()
#          flag=False
#          break
#      else:
#         break
# r,s,k,l=0,0,0,0

for  g in range(1,len(kul)):

    r=kul[g].split(" ")
    if (r[0]=="var"):
        r=kul[g-1].split(" ")
        if r[0]=="var":
            continue
        else:
            variables_not_declared_at_the_begining()
            flag=False
            break
    else:
        continue

if flag:
    for p in kul:
        main(p)


    



# if kul[kul.length]=="hlt":
#     while True:

    
# main(a)






# a = sys.stdin.read()
# for line in stdin:
#     main(line) 


# print(imm_to_bin(4))

# X=input()
# print(len(X))
# print(op_check(z[0]))
# print(reg_check(z[1]))
# # print( bin("1"))
# for i in range(9):
#     print(bin(i))
# print(a["add"])
# print(x)
# def error_typo:
#     print("typo in opcoed")
