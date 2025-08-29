import numpy
import random as rt
def neurons(a):
    return round(eval(a),10)

# li  = [i for i in range(1,100)]
def sampleneurons(target) :
    li_op = ["-","+","*","%","/"]
    li_op1 = ["-","+","*","%","/"]
    operations = 0
    while True:
        op_ran = rt.randint(0,len(li_op)-1)
        op_ran1 = rt.randint(0,len(li_op)-1)
        ran =str(rt.randint(1,100))
        ran1 =str(rt.randint(1,100))
        ran2 =str(rt.randint(1,100))
        operations_vec = neurons(ran+li_op[op_ran]+ran1+li_op1[op_ran1]+ran2)
        print(operations_vec)
        operations = operations + 1 
        if operations_vec == target :
            print(f"expression : {str(ran)+str(li_op[op_ran]+str(ran1))+str(li_op1[op_ran1]+str(ran2))}")
            print(f"operations : {operations}")
            break


    
