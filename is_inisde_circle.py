import math
def is_inside_circle(point,radius):
    #the center of the circle will always be in C(1,1)
    x=[0,0]
    y=[0,0]
    x0=point[0]
    y0=point[1]
    try:
        x[0]=-1*math.sqrt(math.pow(radius,2)-math.pow(y0,2))
        x[1]=math.sqrt(math.pow(radius,2)-math.pow(y0,2))
    except:
        return False
    
    try:
        y[0]=-1*math.sqrt(math.pow(radius,2)-math.pow(x0,2))
        y[1]=math.sqrt(math.pow(radius,2)-math.pow(x0,2))
    except:
        return False

    x_isin=False
    if x0>=x[0] and x0<=x[1]:
        x_isin=True

    y_isin=False
    if y0>=y[0] and y0<=y[1]:
        y_isin=True

    return x_isin and y_isin