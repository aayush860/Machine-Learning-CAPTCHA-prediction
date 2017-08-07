import urllib as ul
from selenium import webdriver
import time
from sklearn.externals import joblib
import numpy as np
import pandas as pd
import cv2


               #importing trained letter file
filename = 'D:/build/pickelfrpython2710.sav'
clf = joblib.load(filename)

st_rno="0812EC141073"
end_rno="0812EC1410120"

st=int(st_rno[9:])
end=int(end_rno[9:])
sem_no="6"

driver=webdriver.Chrome("C:/chromedriver.exe")

sttime=time.time()

for iterat in range(st,((end+1))):
   # print iterat
    driver.get('http://result.rgpv.ac.in/Result/BErslt.aspx')
    semx='//*[@id="ctl00_ContentPlaceHolder1_drpSemester"]/option'
    semxp=semx+"["+str(sem_no)+"]"
    semxpp=driver.find_element_by_xpath(semxp)
    semxpp.click()
                    ##ENROLLMENT NAME       (to be iterated)
    epthh='//*[@id="ctl00_ContentPlaceHolder1_txtrollno"]'
    epth=driver.find_element_by_xpath(epthh)
    epth.clear()
#    time.sleep(1)
    if len(str(iterat))==1:
        tex_inp=st_rno[:11]+str(iterat)
        epth.send_keys(tex_inp)
    elif len(str(iterat))==2:
        tex_inp=st_rno[:10]+str(iterat)
        epth.send_keys(tex_inp)
    else:
        tex_inp=st_rno[:9]+str(iterat)
        epth.send_keys(tex_inp)
    counterr=0
    print (tex_inp)
    while(True):
            #epth.send_keys(tex_inp)
            print("st iteration")
                    # get the image source
            img = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_pnlCaptcha"]/table/tbody/tr[1]/td/div/img')
            src = img.get_attribute('src')
        
                    ##download the image
            ul.urlretrieve(src, "D:/typ1.png")
            time.sleep(2)
        
                    ##image preprocessing
            address='D:/typ1.png'
            ff=open('D:/cpt/ccc.txt','w')
            img=cv2.imread(address,0)
            img=cv2.resize(img,(1000,500))
            li=list()
            lisr=list()
            yui=str('label,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900')
            ff.write(yui+'\n')
            ret,threshold=cv2.threshold(img,129,255,0)
            laplacian=cv2.Laplacian(threshold,cv2.CV_64F)
            edges=cv2.Canny(img,700,700)
            kernel=np.ones((5,5),np.uint8)
            threshold=cv2.erode(threshold,kernel,iterations=1)
            
            im2, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            
            lisr1=list()
            x=list()
            
            for i in range(0,len(contours)):
                x.append(i)
            
            for z in x:
                cnt=contours[z]
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                x,y,w,h=cv2.boundingRect(cnt)
                roi=threshold[y:y+h,x:x+w]
                dd=cv2.contourArea(cnt)
            
                if dd>9500 and dd<450000:
                    lisr.append(x)
                    lisr.append(y)
                    lisr.append(w)
                    lisr.append(h)
                    
            
            for i in range(0, len(lisr), 4):
                lisr1.append(lisr[i:i + 4])
            lisr1.sort()
            x=list()
            
            wer=1
            for ttt in lisr1:
         #       print ttt[1]
            
                rect1 = cv2.minAreaRect(cnt)
                box1 = cv2.boxPoints(rect1)
                roi1=threshold[ttt[1]:ttt[1]+ttt[3],ttt[0]:ttt[0]+ttt[2]]
                retval,frame=cv2.threshold(roi1,129,255,0)
                frame=cv2.resize(frame,(30,30))
                blur = cv2.GaussianBlur(frame,(5,5),0)
                ret3,frame = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                kernel = np.ones((5,5),np.uint8)
                frame = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)
                ar=np.array(frame)
                d=ar.tolist()
                w=str(d)
                w=w.replace("]","",10000)
                w=w.replace("[","",10000)
                w=w.replace(" ","",10000)
                w=w.replace("255","1",100000)
                w=w.strip()
                outpt=str(w)+'\n'
                ff.write(outpt)
                #print w
                #cv2.imshow(str(wer),frame)
                wer=wer+1
            
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            ff.close()
            
            #time.sleep(2)
            #print("sleeping")
            preadd=pd.read_csv("D:/cpt/ccc.txt",'r')
            kf=np.array(preadd)
            
            ii=open('C:/Users/new/Desktop/tempo2.txt','w')
            ii.write("")
            ii.close()
            #print(len(lisr))
            try:
                print(wer-1)
                for dd in range(0,(5)):
                    ee=str(kf[dd]).replace("[","",1000)
                    ee=ee.replace("\n","",1000)
                    ee=ee.replace("]","",1000)
                    ee=ee.replace("'","",1000)
                    ee=ee.strip()
                    #print (ee)
                    ee=tuple(list(ee.split(",")))
                    prevar=np.array([ee])
                    prevar=prevar.reshape(1,-1)
                    #print(prevar)
                    #kf[dd]=kf[dd].reshape(1,-1)
                    g=clf.predict(prevar)
                #    acc=clf.score(X,y)
                #    print(acc*100)
                    #############print("The letter u drew is"+":"+chr(g))
                    ii=open('C:/Users/new/Desktop/tempo2.txt','a')
                #    pi.append(g)
                    ii.write(chr(g))
                    ii.close()
                
                            
            
                            ##AFTER MACHINE LEARNING PREDICTION
                ii=open('C:/Users/new/Desktop/tempo2.txt','r')
                sm=str(ii.read())
                ii.close()
            
                            ##CAPTCHA BOX           (to be iterated)
                cpthh='//*[@id="ctl00_ContentPlaceHolder1_TextBox1"]'
                cpth=driver.find_element_by_xpath(cpthh)
                cpth.clear()
                cpth.send_keys(sm)
                time.sleep(1)
                
                            ##VIEW RESULT
                            
                vr='//*[@id="ctl00_ContentPlaceHolder1_btnviewresult"]'
                vrr=driver.find_element_by_xpath(vr)
                vrr.click()
                print("cccccccccccccccccccccc")
                if counterr>0:
                    vrr.click()
                ###else:
                ###    vrr.click()
                ##########    print("Clicking")
                #time.sleep(1)
                
                #print("res sucessfully displayed")
                
                try:
                    alert = driver.switch_to_alert()
                    if alert.text=="Result for this Enrollment No. not Found":
                        alert.accept()
                        #alert.dismiss()
                        #driver.get('http://result.rgpv.ac.in/Result/BErslt.aspx')
                        counterr=counterr+1
                        print("-------------------------------")
                        break
                        #time.sleep(1)
                    elif alert.text=="you have entered a wrong text":
                        alert.accept()
                        counterr=counterr+1
                        time.sleep(1)
                        print("entred")
                   
                    
                except:
                    #time.sleep(1)
                   # if counterr>0:
                    #    vrr.click()
                    datastore=open('D:/EC_B_sem6.txt','a')
                    
                    print("entering except")
                    name_pth='//*[@id="ctl00_ContentPlaceHolder1_lblNameGrading"]'
                    nmpth=driver.find_element_by_xpath(name_pth)
                    
                    rno_xpthh='//*[@id="ctl00_ContentPlaceHolder1_lblRollNoGrading"]'
                    rno_xpth=driver.find_element_by_xpath(rno_xpthh)
                    
                    sta_xpthh='//*[@id="ctl00_ContentPlaceHolder1_lblResultNewGrading"]'
                    sta_xpth=driver.find_element_by_xpath(sta_xpthh)
                    
                    sgpa_xpthh='//*[@id="ctl00_ContentPlaceHolder1_lblSGPA"]'
                    sgpa_xpth=driver.find_element_by_xpath(sgpa_xpthh)
                    
                    cgpa_xpthh='//*[@id="ctl00_ContentPlaceHolder1_lblcgpa"]'
                    cgpa_xpth=driver.find_element_by_xpath(cgpa_xpthh)
                    
                    branch_xpthh='//*[@id="ctl00_ContentPlaceHolder1_lblBranchGrading"]'
                    branch_xpth=driver.find_element_by_xpath(branch_xpthh)
                                     
                    print(str(nmpth.text))
                    
                    inpstr=str(nmpth.text)+"\t"+str(rno_xpth.text)+"\t"+str(branch_xpth.text)+"\t"+str(sta_xpth.text)+"\t"+str(sgpa_xpth.text)+"\t"+str(cgpa_xpth.text)+"\n"
                    datastore.write(inpstr)
                    datastore.close()
                    break
            except:
                pass
tinmin=time.time()-sttime                
print(tinmin/60)
