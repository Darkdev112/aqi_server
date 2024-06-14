def calc_aqi(conc):
    pm_conc = conc[0]
    co_conc = conc[1]
    o3_conc = conc[2]
    min_aqi = [0,51,101,201,301,401]
    max_aqi = [50,100,200,300,400,500]
    min_pm_conc = [0,31,61,91,121,251]
    max_pm_conc = [30,60,90,120,250,500]
    min_co_conc = [0,1.1,2.1,10.1,17.1,34.1]
    max_co_conc = [1,2,10,17,34,50]
    min_o3_conc = [0,51,101,169,209,748]
    max_o3_conc = [50,100,168,208,747,1000]


    for index,min_pm_val in enumerate(min_pm_conc):
        if pm_conc > min_pm_val:
            pm_aqi = ( (max_aqi[index] - min_aqi[index])/(max_pm_conc[index]-min_pm_val) ) * (pm_conc - min_pm_val) + min_aqi[index]
        else:
            break

    for index,min_co_val in enumerate(min_co_conc):
        if co_conc > min_co_val:
            co_aqi = ( (max_aqi[index] - min_aqi[index])/(max_co_conc[index]-min_co_val) ) * (co_conc - min_co_val) + min_aqi[index]
        else:
            break

    for index,min_o3_val in enumerate(min_o3_conc):
        if o3_conc > min_o3_val:
            o3_aqi = ( (max_aqi[index] - min_aqi[index])/(max_o3_conc[index]-min_o3_val) ) * (o3_conc - min_o3_val) + min_aqi[index]
        else : 
            break
    
    return max(pm_aqi,max(co_aqi,o3_aqi))