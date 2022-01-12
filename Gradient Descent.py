


def step_gradient(points,learning_rate,m,c):
    slope_m=0
    slope_c=0
    M=len(points)
    for i in range(M):
        x=points[i,0]
        y=points[i,1]
        slope_m += (-2/M)*(y-m*x-c)(x) 
        slope_c += (-2/M)*(y-m*x-c)    
    new_m=m-learning_rate*slope_m
    new_c=c-learning_rate*slope_c
    return new_m,new_c




def gd(points,learning_rate,no_of_iter):
    m=0
    c=0
    for i in range(no_of_iter):
        m,c=step_gradient(points,learning_rate,m,c)
        print(i,"cost : ",cost(points,m,c))
return m,c





def run():
    np.loadtxt("data.csv",delimeter=",")
    learning_rate=0.001
    no_of_iter=100
    m,c=gd(data,learning_rate,no_of_iter);
    print(m,c)



def cost(points,m,c):
    total_cost=0
    M=len(points)
    for i in range(M):
        x=points[i,0]
        y=points[i,1]
        total_cost += (1/M)*(y-m*x-c)**2
return total_cost






