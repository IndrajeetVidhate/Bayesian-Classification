import pandas as p
import numpy as num
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 00:12:28 2018

@author: Indrajeet Vidhate
"""

def read():
    d = p.read_csv("q2.csv")
    x1 = 0
    x2n1_yn0 = 0
    x2n1_yn1 = 0
    x2n0_yn0 = 0
    x2n0_yn1 = 0
    x3 = 0
    yn1_x1n0x3n0 = 0
    yn1_x1n1x3n0 = 0
    yn1_x1n0x3n1 = 0
    yn1_x1n1x3n1 = 0
    x2 = 0
    yn0_x1n0x3n0 = 0
    yn0_x1n1x3n0 = 0
    yn0_x1n0x3n1 = 0
    yn0_x1n1x3n1 = 0
    
    x3n0_x2n0 = 0
    x3n0_x2n1 = 0
    x3n1_x2n0 = 0
    x3n1_x2n1  = 0
    
    count = 0
    
    tempx10_x30 = 0
    tempx10_x31 = 0
    tempx11_x30 = 0
    tempx11_x31 = 0
    for i in range (200):
        
        
         if(d["x1"][i] == True and d["x2"][i] == True  ):
             tempx11_x31 +=1

         
         if(d["x1"][i] == True and d["x2"][i] == False  ):
             tempx11_x30 +=1
             
         
         if(d["x1"][i] == False and d["x2"][i] == True  ):
             tempx10_x31 +=1
             
         
         if(d["x1"][i] == False and d["x2"][i] == False  ):
             tempx10_x30 +=1
             
             
         if(d["x3"][i] == True and d["x2"][i] == True  ):
             x3n1_x2n1 +=1
         
         if(d["x3"][i] == False and d["x2"][i] == True  ):
             x3n0_x2n1 +=1
             
         if(d["x3"][i] == True and d["x2"][i] == False  ):
             x3n1_x2n0 +=1
             
         if(d["x3"][i] == False and d["x2"][i] == False  ):
             x3n0_x2n0 +=1
        

         if(d["x1"][i] == True):
             x1= x1 + 1
             
         if(d["x3"][i] == True):
             x3+=1
             
         if(d["x2"][i] == True):
             x2+=1
         
         if(d["y"][i] == True and d["x1"][i] == False and d["x3"][i] == False  ):
             yn1_x1n0x3n0 +=1
             
         if(d["y"][i] == False and d["x1"][i] == False and d["x3"][i] == False  ):
             yn0_x1n0x3n0 +=1
             
         if(d["y"][i] == True and d["x1"][i] == True and d["x3"][i] == False  ):
             yn1_x1n1x3n0+=1
             
         if(d["y"][i] == False and d["x1"][i] == True and d["x3"][i] == False  ):
             yn0_x1n1x3n0+=1
                     
         if(d["y"][i] == True and d["x1"][i] == False and d["x3"][i] == True  ):
             yn1_x1n0x3n1+=1
             
             
         if(d["y"][i] == False and d["x1"][i] == False and d["x3"][i] == True  ):
             yn0_x1n0x3n1+=1
             
             
         if(d["y"][i] == True and d["x1"][i] == True and d["x3"][i] == True  ):
             yn1_x1n1x3n1+=1
             
         if(d["y"][i] == False and d["x1"][i] == True and d["x3"][i] == True  ):
             yn0_x1n1x3n1+=1
             
         if(d["x2"][i] == True and d["y"][i] == True  ):
             x2n1_yn1 +=1
         
         if(d["x2"][i] == False and d["y"][i] == True  ):
             x2n0_yn1 +=1
             
         if(d["x2"][i] == True and d["y"][i] == False  ):
             x2n1_yn0 +=1
             
         if(d["x2"][i] == False and d["y"][i] == False  ):
             x2n0_yn0 +=1    
             
         # Calculating actual CPT entries for parameters
         
    P_x1_t = x1/200     
    P_x1_f = 1 - P_x1_t
    print(P_x1_t)
    print(P_x1_f)
    
    P_x3_t = x3/200
    P_x3_f = 1 - P_x3_t
    print(P_x3_t)
    print(P_x3_f)
    
    print("2nd")
    P_x2_t = x2/200
    P_x2_f = 1 - P_x2_t
    print(P_x2_t)
    print(P_x2_f)
    
    
    Px3t_x2t = x3n1_x2n1/(x3n1_x2n1 + x3n0_x2n1)
    print(Px3t_x2t)
    Px3f_x2t = 1 - Px3t_x2t
    print(Px3f_x2t)
    Px3t_x2f = x3n1_x2n0 /(x3n1_x2n0 + x3n0_x2n0)
    print(Px3t_x2f)
    Px3f_x2f = 1 - Px3t_x2f
    print(Px3f_x2f)
    
    print("ans")
    
    tempx11_x31 = tempx11_x31/(tempx10_x31)
    print(tempx11_x31)
    
    print(1-tempx11_x31)
    
    tempx11_x30 = tempx11_x30/(tempx11_x30 + tempx10_x30)
    print(tempx11_x30)
    print(1-tempx11_x30)
    
    print("ans")
    print("2nd end")
    
    Px2t_Yt = x2n1_yn1/(x2n1_yn1 + x2n0_yn1)
    print(Px2t_Yt)
    Px2f_Yt = 1 - Px2t_Yt
    print(Px2f_Yt)
    Px2t_Yf = x2n1_yn0/(x2n1_yn0 + x2n0_yn0)
    print(Px2t_Yf)
    Px2f_Yf = 1 -Px2t_Yf
    print(Px2f_Yf)
    
    
    P_YT_x1T_x3T = yn1_x1n1x3n1/(yn1_x1n1x3n1 + yn0_x1n1x3n1)
    print(P_YT_x1T_x3T)
    P_YF_x1T_x3T = 1 - P_YT_x1T_x3T
    print(P_YF_x1T_x3T )
    
    
    P_YT_x1F_x3T = yn1_x1n0x3n1 / (yn1_x1n0x3n1 + yn0_x1n0x3n1)
    print(P_YT_x1F_x3T)
    P_YF_x1F_x3T = 1 - P_YT_x1F_x3T
    print(P_YF_x1F_x3T)
    
    P_YT_x1T_x3F = yn1_x1n1x3n0 / (yn1_x1n1x3n0 + yn0_x1n1x3n0)
    print(P_YT_x1T_x3F)
    P_YF_x1T_x3F = 1 - P_YT_x1T_x3F
    print(P_YF_x1T_x3F)
    
    P_YT_x1F_x3F = yn1_x1n0x3n0 / (yn1_x1n0x3n0 + yn0_x1n0x3n0 )
    print(P_YT_x1F_x3F)
    P_YF_x1F_x3F = 1 - P_YT_x1F_x3F
    print(P_YF_x1F_x3F)
   
           


def main():
    read()
    
if __name__ == "__main__":
    main()