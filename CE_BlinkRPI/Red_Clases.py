import numpy as np
def red_Clases(Fk):
    Dist1=Fk[0]
    Dist2=Fk[1]
    Dist3=Fk[2]
    Dist4=Fk[3]
    Energia=Fk[4]
    Picos=Fk[5]
    Desv_std=Fk[6]
    Varianza=Fk[7]

    xmin_D1=0.0
    xmax_D1=2584.0

    xmin_D2=0.0
    xmax_D2=938.0

    xmin_D3=0.0
    xmax_D3=1355.0

    xmin_D4=0.0
    xmax_D4=844.0

    xmin_Energia=59.723193144710663
    xmax_Energia=429.71271750465553

    xmin_Picos=1.0
    xmax_Picos=7.0

    xmin_Desv=0.18040662850042705
    xmax_Desv=0.37168930882141671

    xmin_Var=0.0325465516068911
    xmax_Var=0.13815294229214248

    ymin=-1.0
    ymax=1.0

    E1 = ((ymax-ymin)*(Dist1-xmin_D1))/(xmax_D1-xmin_D1) + ymin
    E2 = ((ymax-ymin)*(Dist2-xmin_D2))/(xmax_D2-xmin_D2) + ymin
    E3 = ((ymax-ymin)*(Dist3-xmin_D3))/(xmax_D3-xmin_D3) + ymin
    E4 = ((ymax-ymin)*(Dist4-xmin_D4))/(xmax_D4-xmin_D4) + ymin
    E5 = ((ymax-ymin)*(Energia-xmin_Energia))/(xmax_Energia-xmin_Energia) + ymin
    E6 = ((ymax-ymin)*(Picos-xmin_Picos))/(xmax_Picos-xmin_Picos) + ymin
    E7 = ((ymax-ymin)*(Desv_std-xmin_Desv))/(xmax_Desv-xmin_Desv) + ymin
    E8 = ((ymax-ymin)*(Varianza-xmin_Var))/(xmax_Var-xmin_Var) + ymin

    N1=((E1*-1.0113031979780174)+(E2*0.098187742376040374)+(E3*-2.6582584540485885)+(E4*0.76390381463773416)+
        (E5*0.77319129911241691)+(E6*2.9437137917062697)+(E7*1.158902654215211)+(E8*1.8661908803532641)+(1.1266830744486385))
    
    N2=((E1*-0.85867341647244044)+(E2*1.0303611483421935)+(E3*1.5292406898795798)+(E4*-1.0802223519553726)+
        (E5*-0.29938120558971115)+(E6*-5.8344498296640053)+(E7*0.050831956775358421)+(E8*0.092006735370762135)+(0.57810614657969317))
    
    N3=((E1*-3.155611325206332)+(E2*6.1081698509508637)+(E3*-0.47951281933582657)+(E4*-0.56400329403721361)+
        (E5-1.8248402379449189)+(E6*-1.0295244772876992)+(E7*-0.52915383218966416)+(E8*0.47412687090609323)+(-1.0190126376589934))


    Fun_Net1 =  2/(1+np.exp(-2*N1))-1
    Fun_Net2 =  2/(1+np.exp(-2*N2))-1
    Fun_Net3 =  2/(1+np.exp(-2*N3))-1

##    Salida_1= ((Fun_Net1*-0.89794713035091611)+(Fun_Net2*-4.2405871585736712)+(Fun_Net3*13.906716908198963)+(-6.5358046846950204))
    Salida_1=((Fun_Net1*-4.3915511318331673)+(Fun_Net2*0.32182213080635103)+(Fun_Net3*-3.0511514059846703)+(4.6404873558255719))
##    Salida_2= ((Fun_Net1*1.9458161604383357)+(Fun_Net2*1.4629255109072001)+(Fun_Net3*-1.2608732993196365)+(-2.9629892305791228))
    Salida_2=((Fun_Net1*0.94494993055185705)+(Fun_Net2*4.3126516807222259)+(Fun_Net3*3.4594716662851739)+(-1.0927748024785633))
##    Salida_3= ((Fun_Net1*-0.2934533110259307)+(Fun_Net2*-0.46430368270129896)+(Fun_Net3*0.068326097344357239)+(-0.83067443909282845))
    Salida_3=((Fun_Net1*0.25727235983981483)+(Fun_Net2*-1.7655518173828233)+(Fun_Net3*5.6333182490920128)+(-0.93441784986661414))
##    Salida_4= ((Fun_Net1*0.61135649944358961)+(Fun_Net2*-4.5331516837760386)+(Fun_Net3*0.83846582844112494)+(-2.2656245372016035))
    Salida_4=((Fun_Net1*-0.65033368611878184)+(Fun_Net2*-6.6949592390017729)+(Fun_Net3*2.8854603801783605)+(-1.4083877483113796))
##    Salida_5= ((Fun_Net1*-3.5376918196783946)+(Fun_Net2*2.9393244962589873)+(Fun_Net3*-0.77384162115315502)+(-2.1136574787091269))
    Salida_5=((Fun_Net1*-0.13100509506157998)+(Fun_Net2*0.78440662310312326)+(Fun_Net3*-3.4403791829792816)+(1.235362587611786))
##    Salida_6= ((Fun_Net1*-4.2253929580672249)+(Fun_Net2*-2.3623541342402361)+(Fun_Net3*-0.55312881368534539)+(-0.98219258818716071))
    Salida_6=((Fun_Net1*-0.074731745251750928)+(Fun_Net2*-3.1246814071400033)+(Fun_Net3*-3.2368351515942941)+(-0.61724323476404563))
##    Salida_7= ((Fun_Net1*1.1699128255692197)+(Fun_Net2*1.2247626044961148)+(Fun_Net3*6.4683943218135829)+(0.38437610916893244))
    Salida_7=((Fun_Net1*0.2795199182900589)+(Fun_Net2*6.8013655826914983)+(Fun_Net3*-2.2907457786793426)+(-1.0894835828786622))

    Vector_salida=[Salida_1,Salida_2,Salida_3,Salida_4,Salida_5,Salida_6,Salida_7]
    Salida =  (np.exp(Vector_salida))/sum(np.exp(Vector_salida))
    print(Salida)
##    FunS_Net2 =  2/(1+np.exp(-2*Salida_2))-1
##    FunS_Net3 =  2/(1+np.exp(-2*Salida_3))-1
##    FunS_Net4 =  2/(1+np.exp(-2*Salida_4))-1
##    FunS_Net5 =  2/(1+np.exp(-2*Salida_5))-1
##    FunS_Net6 =  2/(1+np.exp(-2*Salida_6))-1
##    FunS_Net7 =  2/(1+np.exp(-2*Salida_7))-1
##
    xmi_S=0.0
    xma_S=+1.0
    ymi_S=-1.0
    yma_S=+1.0
##
    y1_S=Salida+(-ymi_S)
    k_S=((xma_S-xmi_S)/(yma_S-ymi_S))*(y1_S)
##    
##    y2_S=FunS_Net2+(-ymi_S)
##    k2_S=((xma_S-xmi_S)/(yma_S-ymi_S))*(y2_S)
##
##    y3_S=FunS_Net3+(-ymi_S)
##    k3_S=((xma_S-xmi_S)/(yma_S-ymi_S))*(y3_S)
##    
##    y4_S=FunS_Net4+(-ymi_S)
##    k4_S=((xma_S-xmi_S)/(yma_S-ymi_S))*(y4_S)
##    
##    y5_S=FunS_Net5+(-ymi_S)
##    k5_S=((xma_S-xmi_S)/(yma_S-ymi_S))*(y5_S)
##    
##    y6_S=FunS_Net6+(-ymi_S)
##    k6_S=((xma_S-xmi_S)/(yma_S-ymi_S))*(y6_S)
##
##    y7_S=FunS_Net7+(-ymi_S)
##    k7_S=((xma_S-xmi_S)/(yma_S-ymi_S))*(y7_S)
##    
##
    return (k_S)
