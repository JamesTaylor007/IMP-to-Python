p_X=1
p_Y=1
p_Result=0
p_Count=0
while ((p_Count<100)):
    p_Result=p_X+p_Y
    p_X=p_Y
    p_Y=p_Result
    p_Count=p_Count+1
    print(p_Result)