#get stats from two data frames and output comparison
import statistics
import pandas as pd

def calcTBStats(df_1, df_2):
    '''
    Calculate summary statistics of two tables 
    to extract the min, max, Avg and Sum

    Parameters:
        df_1:
            Dataframe representing first table

        df_2:
            Dataframe representing second table

    Returns:
        df_out:
            Output dataframe containing df_1, 
            df_2 and summary stats

    '''

    #find indices of min and max
    min1_i = df_1[['total']].idxmin()[0]
    min2_i = df_2[['total']].idxmin()[0]
    max1_i = df_1[['total']].idxmax()[0]
    max2_i = df_2[['total']].idxmax()[0]

    
    #calc averages
    avg1 = df_1["total"].mean()
    avg2 = df_2["total"].mean()

    #calc sums
    sum1 = round(df_1["total"].sum(),2)
    sum2 = round(df_2["total"].sum(),2)

    #Populate new output table for table 1 summary stats
    df_1_out = pd.DataFrame({"Table":str(1)
                             , "sum_load":sum1
                             , "avg_load":avg1                             
                             , "min_load":[df_1.loc[min1_i,"total"]]
                             , "max_load":[df_1.loc[max1_i,"total"]]                             
                             , "min_load_t":[df_1.loc[min1_i,"hour_ending"]]
                             , "max_load_t":[df_1.loc[max1_i,"hour_ending"]]                       
                             })
    #Populate new output table for table 2 summary stats
    df_2_out = pd.DataFrame({"Table":str(2)
                             , "sum_load":sum2                             
                             , "avg_load":avg2                             
                             , "min_load":[df_2.loc[min2_i,"total"]]
                             , "max_load":[df_2.loc[max2_i,"total"]]                             
                             , "min_load_t":[df_2.loc[min2_i,"hour_ending"]]
                             , "max_load_t":[df_2.loc[max2_i,"hour_ending"]]                             
                             })    

    #Populate new output table for TOTAL summary stats
    df_out = df_1_out.append(df_2_out)
    totalMin = df_out["min_load"].min()
    totalMax = df_out["max_load"].max()
    totalAvg = statistics.mean([avg1, avg2])
    
    df_sum = pd.DataFrame({"Table":"Summary:"
                             , "sum_load":sum1+sum2                           
                             , "avg_load":[totalAvg]                           
                             , "min_load":[totalMin]    
                             , "max_load":[totalMax]
                             , "min_load_t":[""]                           
                             , "max_load_t":[""]
                             })
    df_out = df_out.append(df_sum)
    
    return df_out


