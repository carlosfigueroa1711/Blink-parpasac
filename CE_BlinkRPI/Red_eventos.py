import numpy as np
def red_eventos(Fk):
    Var_E1=Fk[0]
    Med_E2=Fk[1]
    xmin_E1=0.129702712
    xmax_E1=40020.525009999998
    xmin_E2=24.382416540000001
    xmax_E2=64.714482779999997
    ymin=-1.0
    ymax=1.0
    E1 = ((ymax-ymin)*(Var_E1-xmin_E1))/(xmax_E1-xmin_E1) + ymin
    E2 = ((ymax-ymin)*(Med_E2-xmin_E2))/(xmax_E2-xmin_E2) + ymin

    N1=(E1*2.117802805381106) + (2.541343706991428*E2) + (2.3226996879829755)
    N2=(E1*-1.4493275812458262) + (-0.48061247528058715*E2) + (0.46089055219010766)
    N3=(E1*-2.8000319408679317) + (-0.0015080782642618242*E2) + (-2.2076993331047148)

    Fun_Net1 =  2/(1+np.exp(-2*N1))-1
    Fun_Net2 =  2/(1+np.exp(-2*N2))-1
    Fun_Net3 =  2/(1+np.exp(-2*N3))-1

    Salida_1= (Fun_Net1*1.1804204024320994)+(Fun_Net2*1.0331050441000629)+(-5.8312130179308435*Fun_Net3)+(-1.591405231443094)
    Salida_2=(Fun_Net1*-0.67464524415127902)+(Fun_Net2*1.8342369707295685)+(4.8694889488137578*Fun_Net3)+(-1.2609957459283423)

    FunS_Net1 =  2/(1+np.exp(-2*Salida_1))-1
    FunS_Net2 =  2/(1+np.exp(-2*Salida_2))-1

    xmi_S=0.0
    xma_S=+1.0
    ymi_S=-1.0
    yma_S=+1.0

    y1_S=FunS_Net1+(-ymi_S)
    k1_S=((xma_S-xmi_S)/(yma_S-ymi_S))*(y1_S)
    
    y2_S=FunS_Net2+(-ymi_S)
    k2_S=((xma_S-xmi_S)/(yma_S-ymi_S))*(y2_S)

    return (k1_S,k2_S)
