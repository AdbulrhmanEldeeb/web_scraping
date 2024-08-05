from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pickle 
#  الخطوات : 
# هيفتح واخليه ينام لحد ما احمل كل المتاجر يديويا 
# هخليه يسحب الأسماء و التقييم 
# Initialize ChromeOptions
# ########################################alarabya#######################################
# locations={ 'riyadh':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@24.7025527,46.5573589,11z/data=!3m1!4b1?entry=ttu',
#             'mekka':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@21.4365243,39.5346827,11z/data=!3m1!4b1?entry=ttu',
#             'tabouk':'https://www.google.com/maps/place/%D8%AA%D8%A8%D9%88%D9%83+%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9%E2%80%AD/@28.3986991,36.5659024,12z/data=!3m1!4b1!4m9!1m2!2m1!1z2KfZhNi52LHYqNmK2Kkg2YTZhNi52YjYrw!3m5!1s0x15a9ad0594132365:0x6f40e3c6b6139acf!8m2!3d28.3835079!4d36.5661908!16zL20vMDNuNTF0?entry=ttu',
#             'tymaa':'https://www.google.com/maps/place/%D8%AA%D9%8A%D9%85%D8%A7%D8%A1+%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9%E2%80%AD/@27.6223611,38.5355759,13z/data=!3m1!4b1!4m9!1m2!2m1!1z2KfZhNi52LHYqNmK2Kkg2YTZhNi52YjYrw!3m5!1s0x15a729e2f13118a7:0x3850fff5d162f2c7!8m2!3d27.6121695!4d38.5165234!16zL20vMDU3dnpz?entry=ttu',
#             'madina':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@24.470952,38.9935839,10z/data=!3m1!4b1?entry=ttu',
#             'jeddah':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF+%E2%80%AD%E2%80%AD/@21.4500838,38.5516446,9z?entry=ttu',
#             'abha':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@18.2422705,42.2365515,11z/data=!3m1!4b1?entry=ttu',
#             'dammam':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF+%E2%80%AD%E2%80%AD/@26.4137458,49.512705,9.5z?entry=ttu',
#             'hfouf':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF+%E2%80%AD%E2%80%AD/@25.2516889,49.2758302,10z/data=!3m1!4b1?entry=ttu',
#             'hail':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF+%E2%80%AD%E2%80%AD/@27.5262431,41.3629755,11z/data=!3m1!4b1?entry=ttu',
#             'buraidah':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF+%E2%80%AD%E2%80%AD/@26.3483212,43.7586115,11z/data=!3m1!4b1?entry=ttu',
#             'khamis_mushiat':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF+%E2%80%AD%E2%80%AD/@18.2874034,42.6650181,12z/data=!3m1!4b1?entry=ttu',
#             'jubil':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@27.0232326,49.1196207,10z?entry=ttu',
#             'yanbu':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF+%E2%80%AD%E2%80%AD/@24.0458747,37.9623781,11z/data=!3m1!4b1?entry=ttu',
#             'khobar':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD%E2%80%AD/@26.2004797,49.881781,11z/data=!3m1!4b1?entry=ttu',
#             'najran':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF+%E2%80%AD/@17.5379759,44.1108025,12z/data=!3m1!4b1?entry=ttu',
#             'jazan':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@16.8992649,42.5060555,12z?entry=ttu', 
#             'arar':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@30.9475503,40.9756099,12z?entry=ttu',
#             'taif':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@21.4639677,39.5996244,9.5z?entry=ttu',
    # }
#  ############################## daraa ########################
# locations={ 'riyadh':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@24.701359,46.5423729,11z?entry=ttu',
#             'mekka':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@21.4367323,39.6817318,11z/data=!3m1!4b1?entry=ttu',
#             'tymaa':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@27.6186946,37.2160265,8z/data=!3m1!4b1?entry=ttu',
#             'madina':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@24.4717418,39.4527431,11z/data=!3m1!4b1?entry=ttu',
#             'jeddah':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@21.4500838,38.5516446,9z/data=!3m1!4b1?entry=ttu',
#             'abha':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@18.2422705,42.2365515,11z/data=!3m1!4b1?entry=ttu',
#             'dammam':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@26.3632034,49.8277264,11z/data=!3m1!4b1?entry=ttu',
#             # 'hfouf':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@25.3061226,49.5309114,12z/data=!3m1!4b1?entry=ttu',
#             'hail':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@27.5264937,41.5100194,11z/data=!3m1!4b1?entry=ttu',
#             'buraidah':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@26.3483212,43.7586115,11z/data=!3m1!4b1?entry=ttu',
#             'khamis_mushiat':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@18.2874034,42.6650181,12z/data=!3m1!4b1?entry=ttu',
#             'jubil':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@26.984844,49.2185016,10z/data=!3m1!4b1?entry=ttu',
#             'najran':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@17.5379759,44.1108025,12z/data=!3m1!4b1?entry=ttu',
#             'arar':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@30.9475503,40.9756099,12z/data=!3m1!4b1?entry=ttu',
#             'taif':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@21.3838756,39.2562989,8z/data=!3m1!4b1?entry=ttu',
#             'tabouk':'https://www.google.com/maps/search/%D8%AF%D8%B1%D8%B9%D9%87%E2%80%AD/@28.3990778,36.4835003,12z/data=!3m1!4b1?entry=ttu',
#             }
#  ############################## abdelsamad elkourashi ########################
# locations={ 'riyadh':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@24.705156,46.5285266,11z/data=!3m1!4b1?entry=ttu',
#             'mekka':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@21.4367323,39.6817318,11z/data=!3m1!4b1?entry=ttu',
#             'tymaa':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@27.6187475,37.1425299,8z/data=!3m1!4b1?entry=ttu',
#             'madina':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@24.4618519,39.5464907,13z/data=!3m1!4b1?entry=ttu',
#             'jeddah':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@21.4500838,38.5516446,9z/data=!3m1!4b1?entry=ttu',
#             'abha':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@18.2421216,42.4660155,12z/data=!3m1!4b1?entry=ttu',
#             'dammam':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@26.3632034,49.8277264,11z/data=!3m1!4b1?entry=ttu',
#             'hfouf':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@25.3061226,49.5309114,12z/data=!3m1!4b1?entry=ttu',
#             'hail':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@27.5264937,41.5100194,11z/data=!3m1!4b1?entry=ttu',
#             'buraidah':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@26.3483212,43.7586115,11z/data=!3m1!4b1?entry=ttu',
#             'khamis_mushiat':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@18.2874034,42.6650181,12z/data=!3m1!4b1?entry=ttu',
#             # 'jubil':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@26.980921,48.2286059,8z/data=!3m1!4b1?entry=ttu',
#             # 'najran':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@17.5379759,44.1108025,12z/data=!3m1!4b1?entry=ttu',
#             # 'arar':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@30.9430856,39.7385125,8z/data=!3m1!4b1?entry=ttu',
#             # 'taif':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@21.3867933,40.2462619,10z/data=!3m1!4b1?entry=ttu',
#             'tabouk':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@28.3990778,36.4835003,12z/data=!3m1!4b1?entry=ttu',
#             }
#  ############################## almaged ########################

# locations={ 'riyadh':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@24.6921232,46.5578042,11z/data=!3m1!4b1?entry=ttu',
#             'mekka':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@21.4367323,39.6817318,11z?entry=ttu',
#             'tymaa':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@27.6186946,37.2160265,8z/data=!3m1!4b1?entry=ttu',
#             'madina':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@24.4717418,39.4527431,11z/data=!3m1!4b1?entry=ttu',
#             'jeddah':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@21.4500838,38.5516446,9z/data=!3m1!4b1?entry=ttu',
#             'abha':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@18.2421216,42.4660155,12z/data=!3m1!4b1?entry=ttu',
#             'dammam':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@26.3632034,49.8277264,11z/data=!3m1!4b1?entry=ttu',
#             'hfouf':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@25.3061226,49.5309114,12z/data=!3m1!4b1?entry=ttu',
#             'hail':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@27.5264937,41.5100194,11z/data=!3m1!4b1?entry=ttu',
#             'buraidah':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@26.3483212,43.7586115,11z/data=!3m1!4b1?entry=ttu',
#             'khamis_mushiat':'https://www.google.com/maps/search/%D8%A7%D9%84%D9%85%D8%A7%D8%AC%D8%AF+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@18.2874034,42.6650181,12z/data=!3m1!4b1?entry=ttu',
#             ##لسا متعدلوش  'jubil':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@26.980921,48.2286059,8z/data=!3m1!4b1?entry=ttu',
#             ## 'najran':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@17.5379759,44.1108025,12z/data=!3m1!4b1?entry=ttu',
#             ## 'arar':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@30.9430856,39.7385125,8z/data=!3m1!4b1?entry=ttu',
#             ## 'taif':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@21.3867933,40.2462619,10z/data=!3m1!4b1?entry=ttu',
#             # 'tabouk':'https://www.google.com/maps/place/Almajed+For+Oud/@28.3910088,36.4937393,11.5z/data=!4m10!1m2!2m1!1z2KfZhNmF2KfYrNiv!3m6!1s0x15a9b3ab260184bf:0x197b4ecd91d8671c!8m2!3d28.430344!4d36.572342!15sCgzYp9mE2YXYp9is2K8iA4gBAVoOIgzYp9mE2YXYp9is2K-SAQ1wZXJmdW1lX3N0b3Jl4AEA!16s%2Fg%2F11pwy10766?entry=ttu',
#             }
# #  ############################## أجمل ########################

# locations={ 'riyadh':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@24.7020972,46.5634085,11z/data=!3m1!4b1?entry=ttu',
#             'mekka':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@21.4367323,39.6817318,11z/data=!3m1!4b1?entry=ttu',
#             'tymaa':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@27.8144324,36.2937806,8z/data=!3m1!4b1?entry=ttu',
#             'madina':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@24.4717418,39.4527431,11z/data=!3m1!4b1?entry=ttu',
#             'jeddah':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@21.4500838,38.5516446,9z/data=!3m1!4b1?entry=ttu',
#             'abha':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@18.2421216,42.4660155,12z/data=!3m1!4b1?entry=ttu',
#             'dammam':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@26.3632034,49.8277264,11z/data=!3m1!4b1?entry=ttu',
#             'hfouf':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@25.3061226,49.5309114,12z/data=!3m1!4b1?entry=ttu',
#             # 'hail':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84%E2%80%AD/@27.5264937,41.5100194,11z/data=!3m1!4b1?entry=ttu',
#             'buraidah':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@26.0588411,42.9212702,8z/data=!3m1!4b1?entry=ttu',
#             'khamis_mushiat':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@18.2874034,42.6650181,12z/data=!3m1!4b1?entry=ttu',
#             ##لسا متعدلوش  'jubil':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@26.980921,48.2286059,8z/data=!3m1!4b1?entry=ttu',
#             ## 'najran':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@17.5379759,44.1108025,12z/data=!3m1!4b1?entry=ttu',
#             ## 'arar':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@30.9430856,39.7385125,8z/data=!3m1!4b1?entry=ttu',
#             ## 'taif':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@21.3867933,40.2462619,10z/data=!3m1!4b1?entry=ttu',
#             # 'tabouk':'https://www.google.com/maps/place/Almajed+For+Oud/@28.3910088,36.4937393,11.5z/data=!4m10!1m2!2m1!1z2KfZhNmF2KfYrNiv!3m6!1s0x15a9b3ab260184bf:0x197b4ecd91d8671c!8m2!3d28.430344!4d36.572342!15sCgzYp9mE2YXYp9is2K8iA4gBAVoOIgzYp9mE2YXYp9is2K-SAQ1wZXJmdW1lX3N0b3Jl4AEA!16s%2Fg%2F11pwy10766?entry=ttu',
#             }
# #  ############################## الرصاصي ########################

# locations={ 'riyadh':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B1%D8%B5%D8%A7%D8%B5%D9%8A+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@24.6578841,46.6980673,13z/data=!3m1!4b1?entry=ttu',
#             'mekka':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B1%D8%B5%D8%A7%D8%B5%D9%8A+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@21.4364811,39.1870577,9z/data=!3m1!4b1?entry=ttu',
#             # 'tymaa':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@27.8144324,36.2937806,8z/data=!3m1!4b1?entry=ttu',
#             'madina':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B1%D8%B5%D8%A7%D8%B5%D9%8A+%D9%84%D9%84%D8%B9%D9%88%D8%AF%E2%80%AD/@24.4592639,39.5554485,14z/data=!3m1!4b1?entry=ttu',
#             'jeddah':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B1%D8%B5%D8%A7%D8%B5%D9%8A+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@21.4500838,38.5516446,9z/data=!3m1!4b1?entry=ttu',
#             'abha':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B1%D8%B5%D8%A7%D8%B5%D9%8A+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@18.2421216,42.4660155,12z/data=!3m1!4b1?entry=ttu',
#             'dammam':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B1%D8%B5%D8%A7%D8%B5%D9%8A+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD%E2%80%AD/@26.3632034,49.8277264,11z/data=!3m1!4b1?entry=ttu',
#             'hfouf':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B1%D8%B5%D8%A7%D8%B5%D9%8A+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@25.3061226,49.5309114,12z/data=!3m1!4b1?entry=ttu',
#             # 'hail':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84%E2%80%AD/@27.5264937,41.5100194,11z/data=!3m1!4b1?entry=ttu',
#             'buraidah':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B1%D8%B5%D8%A7%D8%B5%D9%8A+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@25.6498499,35.4384362,6z?entry=ttu',
#             'khamis_mushiat':'https://www.google.com/maps/search/%D8%A7%D9%84%D8%B1%D8%B5%D8%A7%D8%B5%D9%8A+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@18.2874034,42.6650181,12z/data=!3m1!4b1?entry=ttu',
#             ##لسا متعدلوش  'jubil':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@26.980921,48.2286059,8z/data=!3m1!4b1?entry=ttu',
#             ## 'najran':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@17.5379759,44.1108025,12z/data=!3m1!4b1?entry=ttu',
#             ## 'arar':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@30.9430856,39.7385125,8z/data=!3m1!4b1?entry=ttu',
#             ## 'taif':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@21.3867933,40.2462619,10z/data=!3m1!4b1?entry=ttu',
#             # 'tabouk':'https://www.google.com/maps/place/Almajed+For+Oud/@28.3910088,36.4937393,11.5z/data=!4m10!1m2!2m1!1z2KfZhNmF2KfYrNiv!3m6!1s0x15a9b3ab260184bf:0x197b4ecd91d8671c!8m2!3d28.430344!4d36.572342!15sCgzYp9mE2YXYp9is2K8iA4gBAVoOIgzYp9mE2YXYp9is2K-SAQ1wZXJmdW1lX3N0b3Jl4AEA!16s%2Fg%2F11pwy10766?entry=ttu',
#             }
# #  ############################## ريف ########################

# locations={ 'riyadh':'https://www.google.com/maps/search/%D8%B1%D9%8A%D9%81+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@24.7012213,46.5335951,11z/data=!3m1!4b1?entry=ttu',
#             'mekka':'https://www.google.com/maps/search/%D8%B1%D9%8A%D9%81+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@21.4367323,39.6817318,11z/data=!3m1!4b1?entry=ttu',
#             # 'tymaa':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@27.8144324,36.2937806,8z/data=!3m1!4b1?entry=ttu',
#             'madina':'https://www.google.com/maps/search/%D8%B1%D9%8A%D9%81+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@24.4717418,39.4527431,11z/data=!3m1!4b1?entry=ttu',
#             'jeddah':'https://www.google.com/maps/search/%D8%B1%D9%8A%D9%81+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@21.4500838,38.5516446,9z/data=!3m1!4b1?entry=ttu',
#             'abha':'https://www.google.com/maps/search/%D8%B1%D9%8A%D9%81+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@18.2421216,42.4660155,12z/data=!3m1!4b1?entry=ttu',
#             'dammam':'https://www.google.com/maps/search/%D8%B1%D9%8A%D9%81+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@26.3632034,49.8277264,11z/data=!3m1!4b1?entry=ttu',
#             'hfouf':'https://www.google.com/maps/search/%D8%B1%D9%8A%D9%81+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@25.3061226,49.5309114,12z/data=!3m1!4b1?entry=ttu',
#             # 'hail':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84%E2%80%AD/@27.5264937,41.5100194,11z/data=!3m1!4b1?entry=ttu',
#             'buraidah':'https://www.google.com/maps/search/%D8%B1%D9%8A%D9%81+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@26.3483212,43.7586115,11z/data=!3m1!4b1?entry=ttu',
#             'khamis_mushiat':'https://www.google.com/maps/search/%D8%B1%D9%8A%D9%81+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@18.2874034,42.6650181,12z/data=!3m1!4b1?entry=ttu',
#             ##لسا متعدلوش  'jubil':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@26.980921,48.2286059,8z/data=!3m1!4b1?entry=ttu',
#             ## 'najran':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@17.5379759,44.1108025,12z/data=!3m1!4b1?entry=ttu',
#             ## 'arar':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@30.9430856,39.7385125,8z/data=!3m1!4b1?entry=ttu',
#             ## 'taif':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@21.3867933,40.2462619,10z/data=!3m1!4b1?entry=ttu',
#             # 'tabouk':'https://www.google.com/maps/place/Almajed+For+Oud/@28.3910088,36.4937393,11.5z/data=!4m10!1m2!2m1!1z2KfZhNmF2KfYrNiv!3m6!1s0x15a9b3ab260184bf:0x197b4ecd91d8671c!8m2!3d28.430344!4d36.572342!15sCgzYp9mE2YXYp9is2K8iA4gBAVoOIgzYp9mE2YXYp9is2K-SAQ1wZXJmdW1lX3N0b3Jl4AEA!16s%2Fg%2F11pwy10766?entry=ttu',
#             }
# #  ############################## ابراهيم القرشي ########################

locations={ 'riyadh':'https://www.google.com/maps/search/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@24.72461,46.1630327,9z/data=!3m1!4b1?entry=ttu',
            'mekka':'https://www.google.com/maps/search/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@21.4367323,39.6817318,11z/data=!3m1!4b1?entry=ttu',
            # 'tymaa':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84+%D9%84%D9%84%D8%B9%D8%B7%D9%88%D8%B1%E2%80%AD/@27.8144324,36.2937806,8z/data=!3m1!4b1?entry=ttu',
            'madina':'https://www.google.com/maps/search/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@24.4717418,39.4527431,11z/data=!3m1!4b1?entry=ttu',
            'jeddah':'https://www.google.com/maps/search/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@21.4500838,38.5516446,9z/data=!3m1!4b1?entry=ttu',
            'abha':'https://www.google.com/maps/search/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@18.2421216,42.4660155,12z/data=!3m1!4b1?entry=ttu',
            'dammam':'https://www.google.com/maps/search/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@26.3632034,49.8277264,11z/data=!3m1!4b1?entry=ttu',
            'hfouf':'https://www.google.com/maps/search/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@25.7621168,44.4253872,7z/data=!3m1!4b1?entry=ttu',
            # 'hail':'https://www.google.com/maps/search/%D8%A3%D8%AC%D9%85%D9%84%E2%80%AD/@27.5264937,41.5100194,11z/data=!3m1!4b1?entry=ttu',
            'buraidah':'https://www.google.com/maps/search/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@26.3483212,43.7586115,11z/data=!3m1!4b1?entry=ttu',
            # 'khamis_mushiat':'https://www.google.com/maps/search/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@18.2874034,42.6650181,12z/data=!3m1!4b1?entry=ttu',
            ##لسا متعدلوش  'jubil':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@26.980921,48.2286059,8z/data=!3m1!4b1?entry=ttu',
            ## 'najran':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@17.5379759,44.1108025,12z/data=!3m1!4b1?entry=ttu',
            ## 'arar':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A+%E2%80%AD/@30.9430856,39.7385125,8z/data=!3m1!4b1?entry=ttu',
            ## 'taif':'https://www.google.com/maps/search/%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B5%D9%85%D8%AF+%D8%A7%D9%84%D9%82%D8%B1%D8%B4%D9%8A%E2%80%AD/@21.3867933,40.2462619,10z/data=!3m1!4b1?entry=ttu',
            # 'tabouk':'https://www.google.com/maps/place/Almajed+For+Oud/@28.3910088,36.4937393,11.5z/data=!4m10!1m2!2m1!1z2KfZhNmF2KfYrNiv!3m6!1s0x15a9b3ab260184bf:0x197b4ecd91d8671c!8m2!3d28.430344!4d36.572342!15sCgzYp9mE2YXYp9is2K8iA4gBAVoOIgzYp9mE2YXYp9is2K-SAQ1wZXJmdW1lX3N0b3Jl4AEA!16s%2Fg%2F11pwy10766?entry=ttu',
            }


chrome_options = Options()
chrome_options.add_argument("--incognito")  # تمكين وضع التصفح الخفي

chrome_options.add_experimental_option('detach', True)

# إعداد Selenium WebDriver
driver = webdriver.Chrome(options=chrome_options)

driver.get(locations['buraidah'])

# # ابحث عن المتجر
# search_box = driver.find_element(By.CLASS_NAME, 'fontBodyMedium.searchboxinput.xiQnY')

# # search_box.send_keys("السعودية")
# # search_box.send_keys(Keys.RETURN)

# time.sleep(4)
# search_box.clear()

# search_box.send_keys('العربية للعود')
# search_box.send_keys(Keys.ENTER)
print('sleep for 25 seconds')
time.sleep(25)
print('unsleep')
anchors=driver.find_elements(By.CLASS_NAME,'hfpxzc')

i=0
print(f'{len(anchors)} stores were found')
stores_info=[]
for anchor in anchors : 
    i+=1
    driver.execute_script("arguments[0].scrollIntoView();", anchor)
    time.sleep(1)
    
    try :
        anchor.click() 
        time.sleep(5)
        print(i)
        store_info={}
        store_name=driver.find_element(By.CLASS_NAME,'DUwDvf.lfPIob')
        # print(1)
        if store_name : 
            # print(2)
            store_name=store_name.text
            # print(3)
            store_info['store_name']=store_name
            print(store_name)
        rating=driver.find_element(By.CLASS_NAME,"ceNzKf")
        
        if rating : 
            rating=rating.get_attribute('aria-label')
            store_info['rating']=rating
            print(rating)
        else : 
            print('No rating was found')
            store_info['rating']=' '    
        # else :
        #     rating=driver.find_element(By.CSS_SELECTOR,"span[aria-hidden='true']")   
        #     rating=rating.text
        #     store_info['rating']=rating
        #     print(rating)
        
        location=driver.find_element(By.CLASS_NAME,"Io6YTe.fontBodyMedium.kR99db")
        if location :
            location=location.text
            store_info['location']=location
            print(location)
        print('#'*50)
        stores_info.append(store_info)
        pickle.dump(stores_info,open('ebrahim_pkl\\ebrahim_buraidah.pkl','wb'))

    except Exception as e : 
        print(f'Exception {e} occured at {i}')


