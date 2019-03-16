import pandas as p
import numpy as num
from scipy.stats import norm
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:18:31 2018

@author: Indrajeet Avinash Vidhate

"""
# ============================================================================= 
# Actual model parameters which will be trained
# Decalred globally for access in all actual classification function
# =============================================================================


Yn1_S = [] 
Yn0_S = []

Yn1_W = [] 
Yn0_W = []

# =============================================================================
# CPT table for P(html| is Spam)
# =============================================================================
PhtmlT_YT = 0
PhtmlF_YT = 0
PhtmlT_YF = 0
PhtmlF_YF = 0

# =============================================================================
# CPT table for P( is emoji| is Spam)
# =============================================================================

PemojiT_YT = 0
PemojiF_YT = 0
PemojiT_YF = 0
PemojiF_YF = 0

# =============================================================================
# CPT table for P(  sent to list| is Spam)
# =============================================================================

PslT_YT = 0
PslF_YT = 0
PslT_YF = 0
PslF_YF = 0

# =============================================================================
# CPT table for P(  sent to list| is Spam)
# =============================================================================


PcomT_YT = 0
PcomF_YT = 0
PcomT_YF = 0
PcomF_YF = 0
# =============================================================================
# CPT table for P(  name| is Spam)
# =============================================================================

PnameT_YT = 0
PnameF_YT = 0
PnameT_YF = 0
PnameF_YF = 0

# =============================================================================
# CPT table for P(  sign | is Spam)
# =============================================================================

PsigT_YT = 0
PsigF_YT = 0
PsigT_YF = 0
PsigF_YF = 0


# =============================================================================
# individual probability for Spam
# =============================================================================
PSpam_T =0
PSpam_F =0

# =============================================================================
# Mean and Standard deviation for calculation PDF (Probaiblity distribution function) for 
# continuous variables
# =============================================================================

SpamT_MuSnt =0
SpamT_SdSnt = 0
SpamF_MuSnt =0
SpamF_SdSnt = 0


SpamT_MuW =0
SpamT_SdW = 0
SpamF_MuW =0
SpamF_SdW = 0

def train(Train_Data):
   
    
    Yt = 0
# =============================================================================
# 
#     calculating occurance of each configurations for given P(x|y), where each x, and y 
#     has 2 states each hence 4 entries for each CPT table
# =============================================================================
    yn1_html1 = 0
    yn0_html1 = 0
    yn1_html0 = 0
    yn0_html0 = 0
    
    yn1_emoji1 = 0
    yn0_emoji1 = 0
    yn1_emoji0 = 0
    yn0_emoji0 = 0
    
    yn1_sl1 = 0
    yn0_sl1 = 0
    yn1_sl0 = 0
    yn0_sl0 = 0
    
    yn1_com1 = 0
    yn0_com1 = 0
    yn1_com0 = 0
    yn0_com0 = 0
    
    yn1_name1 = 0
    yn0_name1 = 0
    yn1_name0 = 0
    yn0_name0 = 0
    
    yn1_sig1 = 0
    yn0_sig1 = 0
    yn1_sig0 = 0
    yn0_sig0 = 0

    htmlt = 0
    emojit =0
    slt =0
    comt =0
    namet =0
    sigt =0
    
    data = p.read_csv(Train_Data)
    count1 = 0
# =============================================================================
#     
#     Scanning the X vectors from training data and calcualting
#     Maximum likelihood based on counting intuition presented in 9.3 of
#     Bayesian Reasoning and Machine learning
# =============================================================================
    
    for i in range(500):
        
        if(data[" is spam"][i] ==  True):
            Yt +=1;
            
        if(data["in html"][i] ==  True):
            htmlt +=1;
         
        if(data[" has emoji"][i] ==  True):
            emojit +=1;
            
        if(data[" sent to list"][i] ==  True):
            slt +=1;
            
        if(data[" from .com"][i] ==  True):
            comt +=1;
        
        if(data[" has my name"][i] ==  True):
            namet +=1;
            
        if(data[" has sig"][i] ==  True):
            sigt +=1;    
            
        if((data[" is spam"][i] == True)):
            Yn1_S.append(int(data[" # sentences"][i]))
            Yn1_W.append(int(data[" # words"][i]))    
                       
                    
        if((data[" is spam"][i] == False)):
            Yn0_S.append(float(data[" # sentences"][i]))
            Yn0_W.append(float(data[" # words"][i]))
            
        if(data[" is spam"][i] == True and data["in html"][i] == True ):
            yn1_html1 += 1
            
        if(data[" is spam"][i] == False and data["in html"][i] == True ):
            yn0_html1 += 1
    
        if(data[" is spam"][i] == True and data["in html"][i] == False ):
            yn1_html0 += 1
            
        if(data[" is spam"][i] == False and data["in html"][i] == False ):
            yn0_html0 += 1 
            
        if(data[" is spam"][i] == True and data[" has emoji"][i] == True ):
            yn1_emoji1 += 1
            
        if(data[" is spam"][i] == False and data[" has emoji"][i] == True ):
            yn0_emoji1 += 1
    
        if(data[" is spam"][i] == True and data[" has emoji"][i] == False ):
            yn1_emoji0 += 1
            
        if(data[" is spam"][i] == False and data[" has emoji"][i] == False ):
            yn0_emoji0 += 1
            
            
        if(data[" is spam"][i] == True and data[" sent to list"][i] == True ):
            yn1_sl1 += 1
            
        if(data[" is spam"][i] == False and data[" sent to list"][i] == True ):
            yn0_sl1 += 1
    
        if(data[" is spam"][i] == True and data[" sent to list"][i] == False ):
            yn1_sl0 += 1
            
        if(data[" is spam"][i] == False and data[" sent to list"][i] == False ):
            yn0_sl0 += 1    
    
    #
        if(data[" is spam"][i] == True and data[" from .com"][i] == True ):
            yn1_com1 += 1
            
        if(data[" is spam"][i] == False and data[" from .com"][i] == True ):
            yn0_com1 += 1
    
        if(data[" is spam"][i] == True and data[" from .com"][i] == False ):
            yn1_com0 += 1
            
        if(data[" is spam"][i] == False and data[" from .com"][i] == False ):
            yn0_com0 += 1
            
     #
        if(data[" is spam"][i] == True and data[" has my name"][i] == True ):
           yn1_name1 += 1
            
        if(data[" is spam"][i] == False and data[" has my name"][i] == True ):
           yn0_name1 += 1

        if(data[" is spam"][i] == True and data[" has my name"][i] == False ):
           yn1_name0 += 1
           
        if(data[" is spam"][i] == False and data[" has my name"][i] == False ):
           yn0_name0 += 1
           
           
           
        if(data[" is spam"][i] == True and data[" has sig"][i] == True ):
           yn1_sig1 += 1
           count1 += 1
        if(data[" is spam"][i] == False and data[" has sig"][i] == True ):
           yn0_sig1 += 1
           count1 += 1
        if(data[" is spam"][i] == True and data[" has sig"][i] == False ):
           yn1_sig0 += 1
           count1 += 1
        if(data[" is spam"][i] == False and data[" has sig"][i] == False ):
           yn0_sig0 += 1      
           count1 += 1
# =============================================================================
#            
# Actual Maximum Likelihood as trained parameters      
# and assesing global model parameters to train and make them available 
# =============================================================================

    
    global SpamT_MuSnt
    global SpamT_SdSnt
    global SpamF_MuSnt
    global SpamF_SdSnt
    
    
    global SpamT_MuW
    global SpamT_SdW
    global SpamF_MuW
    global SpamF_SdW
    
    global PhtmlT_YT 
    global PhtmlF_YT 
    global PhtmlT_YF 
    global PhtmlF_YF 
    
    global PemojiT_YT 
    global PemojiF_YT 
    global PemojiT_YF 
    global PemojiF_YF 
    
    global PslT_YT 
    global PslF_YT 
    global PslT_YF 
    global PslF_YF 
    
    global PcomT_YT 
    global PcomF_YT 
    global PcomT_YF 
    global PcomF_YF 
    
    global PnameT_YT 
    global PnameF_YT 
    global PnameT_YF 
    global PnameF_YF 
    
    global PsigT_YT 
    global PsigF_YT 
    global PsigT_YF 
    global PsigF_YF 
    
    global PSpam_T 
    global PSpam_F 
    
# =============================================================================
#     
#     Calculating mean and standard deviation for continuous variables
#     by their occurance in different class 
# =============================================================================
    SpamT_MuSnt  = num.mean(num.asarray(Yn1_S))
    SpamT_SdSnt = num.std(num.asarray(Yn1_S))
    SpamF_MuSnt  = num.mean(num.asarray(Yn0_S))
    SpamF_SdSnt = num.std(num.asarray(Yn0_S))
    
    SpamT_MuW  = num.mean(num.asarray(Yn1_W))
    SpamT_SdW = num.std(num.asarray(Yn1_W))
    SpamF_MuW  = num.mean(num.asarray(Yn0_W))
    SpamF_SdW = num.std(num.asarray(Yn0_W))
# =============================================================================
# 
#     calculating CPT tables by maximum likelihood for
#     remaining 6 Decreste features
# =============================================================================
    
   
    
    
    PSpam_T = (Yt/500)
    PSpam_F = 1 - PSpam_T     
   
    
    PhtmlT_YT = yn1_html1/( yn1_html1 + yn1_html0 )
    PhtmlF_YT = 1 - PhtmlT_YT
    PhtmlT_YF = yn0_html1/(yn0_html1 + yn0_html0 )
    PhtmlF_YF = 1 - PhtmlT_YF
    

    
    PemojiT_YT = yn1_emoji1/( yn1_emoji1 + yn1_emoji0 )
    PemojiF_YT = 1 - PemojiT_YT
    PemojiT_YF = yn0_emoji1/(yn0_emoji1 + yn0_emoji0 )
    PemojiF_YF = 1 - PemojiT_YF
    
    
    PslT_YT = yn1_sl1/( yn1_sl1 + yn1_sl0 )
    PslF_YT = 1 - PslT_YT
    PslT_YF = yn0_sl1/(yn0_sl1 + yn0_sl0 )
    PslF_YF = 1 - PslT_YF
    
    
    PcomT_YT = yn1_com1/( yn1_com1 + yn1_com0 )
    PcomF_YT = 1 - PcomT_YT
    PcomT_YF = yn0_com1/(yn0_com1 + yn0_com0 )
    PcomF_YF = 1 - PcomT_YF
    
    

    PnameT_YT = yn1_name1/( yn1_name1 + yn1_name0 )
    PnameF_YT = 1 - PnameT_YT
    PnameT_YF = yn0_name1/(yn0_name1 + yn0_name0 )
    PnameF_YF = 1 - PnameT_YF

    
    
    PsigT_YT = yn1_sig1/( yn1_sig1 + yn1_sig0 )
    PsigF_YT = 1 - PsigT_YT
    PsigT_YF = yn0_sig1/(yn0_sig1 + yn0_sig0 )
    PsigF_YF = 1 - PsigT_YF
    

    

def classify(Test_Data):
    
# =============================================================================
#   Accesing trained parameters by use of MLE  
# =============================================================================
    global SpamT_MuSnt
    global SpamT_SdSnt
    global SpamF_MuSnt
    global SpamF_SdSnt
    

    global SpamT_MuW
    global SpamT_SdW
    global SpamF_MuW
    global SpamF_SdW
    
    global PhtmlT_YT 
    global PhtmlF_YT 
    global PhtmlT_YF 
    global PhtmlF_YF 
    
    global PemojiT_YT 
    global PemojiF_YT 
    global PemojiT_YF 
    global PemojiF_YF 
    
    global PslT_YT 
    global PslF_YT 
    global PslT_YF 
    global PslF_YF 
    
    global PcomT_YT 
    global PcomF_YT 
    global PcomT_YF 
    global PcomF_YF 
    
    global PnameT_YT 
    global PnameF_YT 
    global PnameT_YF 
    global PnameF_YF 
    
    global PsigT_YT 
    global PsigF_YT 
    global PsigT_YF 
    global PsigF_YF 
    
    global PSpam_T 
    global PSpam_F
    data = p.read_csv(Test_Data)
    
    x1_y = 0
    x2_y = 0
    x3_y = 0
    x4_y = 0
    x5_y = 0
    x6_y = 0
    x7_y = 0
    x8_y = 0
    
    x1_y_neg = 0
    x2_y_neg = 0
    x3_y_neg = 0
    x4_y_neg = 0
    x5_y_neg = 0
    x6_y_neg = 0
    x7_y_neg = 0
    x8_y_neg = 0
    
    
    
# =============================================================================
#      
#     Actual CPT table correct extractions for given states of discrete variables and pdf for
#     continuous features 
# =============================================================================
    
   
    counter = 0
    for i in range(200):
        
        if(data["in html"][i] == True):
            x1_y = PhtmlT_YT
            x1_y_neg = PhtmlT_YF
         
        if(data["in html"][i] == False):
            x1_y = PhtmlF_YT
            x1_y_neg = PhtmlF_YF
            
            
        if(data[" has emoji"][i] == True):
            x2_y = PemojiT_YT
            x2_y_neg = PemojiT_YF
            
        if(data[" has emoji"][i] == False):
            x2_y = PemojiF_YT
            x2_y_neg = PemojiF_YF
            
            
        if(data[" sent to list"][i] == True):
            x3_y = PslT_YT
            x3_y_neg = PslT_YF
          
        if(data[" sent to list"][i] == False):
            x3_y = PslF_YT
            x3_y_neg = PslF_YF
            
            
        if(data[" from .com"][i] == True):
            x4_y = PcomT_YT
            x4_y_neg = PcomT_YF
            
        if(data[" from .com"][i] == False):
            x4_y = PcomF_YT
            x4_y_neg = PcomF_YF
            
            
        if(data[" has my name"][i] == True):
            x5_y = PnameT_YT
            x5_y_neg = PnameT_YF
            
        if(data[" has my name"][i] == False):
            x5_y = PnameF_YT
            x5_y_neg = PnameF_YF
            
            
        if(data[" has sig"][i] == True):
            x6_y = PsigT_YT
            x6_y_neg = PsigT_YF
            
        if(data[" has sig"][i] == False):
            x6_y = PsigF_YT
            x6_y_neg = PsigF_YF
            
            
        x7_y = norm.pdf(data[" # sentences"][i],SpamT_MuSnt,SpamT_SdSnt)
        x7_y_neg = norm.pdf(data[" # sentences"][i],SpamF_MuSnt,SpamF_SdSnt)
        
                                 
        x8_y = norm.pdf(data[" # words"][i],SpamT_MuW,SpamT_SdW)
        x8_y_neg = norm.pdf(data[" # words"][i],SpamF_MuW,SpamF_SdW)                     
        
# =============================================================================
#         calculating actual estimation using trained parameteres by use of equation 10.2.16 from Bayesian reasoning
#         and machine learning by David Barber        
# =============================================================================
        numerator = x1_y * x2_y* x3_y* x4_y* x5_y* x6_y* x7_y* x8_y * PSpam_T
        
        sub_denomenator  = x1_y_neg * x2_y_neg* x3_y_neg* x4_y_neg* x5_y_neg* x6_y_neg* x7_y_neg* x8_y_neg * PSpam_F
        
        denomenator = numerator + sub_denomenator
        
        value = numerator/denomenator

# =============================================================================
#         if actual Y is False and my hypothesis gives True then error count is increased
# =============================================================================
               
        if (value>0.5 and data[" is spam"][i] == False):
            counter += 1
        
# =============================================================================
#         if actual Y is True and my hypothesis gives False then error count is increased
# =============================================================================
        if (value<0.5 and data[" is spam"][i] == True):
            counter += 1
            
      
    print("The classification error by considering all parameteres",( 200-counter)/200 ,' error = ', 1-( 200-counter)/200 )    
                  
def play_improvisation(Test_Data):
    
# =============================================================================
#   Accesing trained parameters by use of MLE  
# =============================================================================

    
    global SpamT_MuSnt
    global SpamT_SdSnt
    global SpamF_MuSnt
    global SpamF_SdSnt
    

    
    global SpamT_MuW
    global SpamT_SdW
    global SpamF_MuW
    global SpamF_SdW
    
    global PhtmlT_YT 
    global PhtmlF_YT 
    global PhtmlT_YF 
    global PhtmlF_YF 
    
    global PemojiT_YT 
    global PemojiF_YT 
    global PemojiT_YF 
    global PemojiF_YF 
    
    global PslT_YT 
    global PslF_YT 
    global PslT_YF 
    global PslF_YF 
    
    global PcomT_YT 
    global PcomF_YT 
    global PcomT_YF 
    global PcomF_YF 
    
    global PnameT_YT 
    global PnameF_YT 
    global PnameT_YF 
    global PnameF_YF 
    
    global PsigT_YT 
    global PsigF_YT 
    global PsigT_YF 
    global PsigF_YF 
    
    global PSpam_T 
    global PSpam_F
    data = p.read_csv(Test_Data)
    
    
# =============================================================================
#      declaring container variables to pick appropriate entries from CPT tables
#      based on truth and continuous values of given data vector  
# =============================================================================
    x1_y = 0
    x2_y = 0
    x3_y = 0
    x4_y = 0
    x5_y = 0
    x6_y = 0
    x7_y = 0
    x8_y = 0
    
    x1_y_neg = 0
    x2_y_neg = 0
    x3_y_neg = 0
    x4_y_neg = 0
    x5_y_neg = 0
    x6_y_neg = 0
    x7_y_neg = 0
    x8_y_neg = 0
    
# =============================================================================
#      
#     Actual CPT table correct extractions for given states of discrete variables and pdf for
#     continuous features 
# =============================================================================
    
   
    counter = 0
    for i in range(200):
        
        if(data["in html"][i] == True):
            x1_y = PhtmlT_YT
            x1_y_neg = PhtmlT_YF
           
        if(data["in html"][i] == False):
            x1_y = PhtmlF_YT
            x1_y_neg = PhtmlF_YF
            
            
        if(data[" has emoji"][i] == True):
            x2_y = PemojiT_YT
            x2_y_neg = PemojiT_YF
            
        if(data[" has emoji"][i] == False):
            x2_y = PemojiF_YT
            x2_y_neg = PemojiF_YF
            
            
        if(data[" sent to list"][i] == True):
            x3_y = PslT_YT
            x3_y_neg = PslT_YF
            
        if(data[" sent to list"][i] == False):
            x3_y = PslF_YT
            x3_y_neg = PslF_YF
            
            
        if(data[" from .com"][i] == True):
            x4_y = PcomT_YT
            x4_y_neg = PcomT_YF
            
        if(data[" from .com"][i] == False):
            x4_y = PcomF_YT
            x4_y_neg = PcomF_YF
            
            
        if(data[" has my name"][i] == True):
            x5_y = PnameT_YT
            x5_y_neg = PnameT_YF
            
        if(data[" has my name"][i] == False):
            x5_y = PnameF_YT
            x5_y_neg = PnameF_YF
            
            
        if(data[" has sig"][i] == True):
            x6_y = PsigT_YT
            x6_y_neg = PsigT_YF
            
        if(data[" has sig"][i] == False):
            x6_y = PsigF_YT
            x6_y_neg = PsigF_YF
            
            
        x7_y = norm.pdf(data[" # sentences"][i],SpamT_MuSnt,SpamT_SdSnt)
        x7_y_neg = norm.pdf(data[" # sentences"][i],SpamF_MuSnt,SpamF_SdSnt)
        
                                 
        x8_y = norm.pdf(data[" # words"][i],SpamT_MuW,SpamT_SdW)
        x8_y_neg = norm.pdf(data[" # words"][i],SpamF_MuW,SpamF_SdW)                     
        
                
# =============================================================================
#        
#         To ignore a particular parameter remove the variable from below equation
# =============================================================================
        numerator =  x1_y*x2_y * x3_y * x4_y* x5_y* x7_y* x8_y * PSpam_T
        
        sub_denomenator  =x1_y_neg* x2_y_neg* x3_y_neg* x4_y_neg* x5_y_neg*  x7_y_neg* x8_y_neg * PSpam_F
        
        denomenator = numerator + sub_denomenator
        value = numerator/denomenator               
        if (value>0.5 and data[" is spam"][i] == False):
            counter += 1
        
# =============================================================================
#         if actual Y is True and my hypothesis gives False then error count is increased
# =============================================================================
        if (value<0.5 and data[" is spam"][i] == True):
            counter += 1
            
    print("Best achieved classification by ignoring sign and error with ignoring ",( 200-counter)/200, " e = ", 1-( 200-counter)/200  )
      
     
    
def main():
    train("q3.csv")
    classify("q3b.csv")
    play_improvisation("q3b.csv")
    
if __name__ == "__main__":
    main()