import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics

df = pd.read_csv('18.csv')
fig = ff.create_distplot([df['Weight(Pounds)'].tolist()],['Weight'],show_hist=False)

heightList = df['Height(Inches)'].tolist()
weightList = df['Weight(Pounds)'].tolist()

hMean = statistics.mean(heightList)
wMean = statistics.mean(weightList)

hMode = statistics.mode(heightList)
wMode = statistics.mode(weightList)

hMedian = statistics.median(heightList)
wMedian = statistics.median(weightList)

hstandardDeviation = statistics.stdev(heightList)
wstandardDeviation = statistics.stdev(weightList)

height1sdStart,height1sdEnd = hMean - hstandardDeviation,hMean + hstandardDeviation
weight1sdStart,weight1sdEnd = wMean - wstandardDeviation,wMean + wstandardDeviation

height2sdStart,height2sdEnd = hMean - (2*hstandardDeviation),hMean + (2*hstandardDeviation)
weight2sdStart,weight2sdEnd = wMean - (2*wstandardDeviation),wMean + (2*wstandardDeviation)

height3sdStart,height3sdEnd = hMean - (3*hstandardDeviation),hMean + (3*hstandardDeviation)
weight3sdStart,weight3sdEnd = wMean - (3*hstandardDeviation),wMean + (3*wstandardDeviation)

heightListOfData1sd = [result for result in heightList  if result > height1sdStart and result < height1sdEnd]
heightListOfData2sd = [result for result in heightList  if result > height2sdStart and result < height2sdEnd]
heightListOfData3sd = [result for result in heightList  if result > height3sdStart and result < height3sdEnd]

weightListOfData1sd = [result for result in weightList  if result > weight1sdStart and result < weight1sdEnd]
weightListOfData2sd = [result for result in weightList  if result > weight2sdStart and result < weight2sdEnd]
weightListOfData3sd = [result for result in weightList  if result > weight3sdStart and result < weight3sdEnd]

print('Mean, median, mode of weight is {} ,{} , {} '.format(wMean,wMode,wMedian))
print('Mean, median, mode of height is {} ,{} , {} '.format(hMean,hMode,hMedian))

print('{} % of data for height lies within one sd'.format(len(heightListofData1sd)*100.0/len(heightList)))
print('{} % of data for height lies within the second sd'.format(len(heightListofData2sd)*100.0/len(heightList)))
print('{} % of data for height lies within the third sd'.format(len(heightListofData3sd)*100.0/len(heightList)))

print('{} % of data for weight lies within one sd'.format(len(weightListofData1sd)*100.0/len(weightList)))
print('{} % of data for weight lies within the second sd'.format(len(weightListofData2sd)*100.0/len(weightList)))
print('{} % of data for weight lies within the third sd'.format(len(weightListofData2sd)*100.0/len(weightList)))