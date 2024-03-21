import pandas as pd
import matplotlib.pyplot as plt

dfillnessoriginal = pd.read_csv(r'C:\Users\Monica\Desktop\UCLA Extension\Data Science Certificate\2 Exploratory Data Analysis and Visualization\Final Project\python\outbreaks.csv')
dfillnessoriginal.head()

#goes through each state in df state column and adds new instance to list alphabetically
#will be used to see which states need to be removed
state_list = []
for i in dfillnessoriginal['State']:
    if i not in state_list:
        state_list.append(i)
        state_list.sort()
print(state_list)

#will only look at 50 states plus DC
#remove rows in df where state is guam, puerto rico, republic of palau and write to new df
dfillness = (dfillnessoriginal[dfillnessoriginal.State != 'Guam'])
dfillness = (dfillness[dfillness.State != 'Puerto Rico'])
dfillness = (dfillness[dfillness.State != 'Republic of Palau'])

#goes through dfillness and makes a list of each unique state
state_list_clean = []
for x in dfillness['State']:
    if x not in state_list_clean:
        if x != 'Multistate' :
            state_list_clean.append(x)
            state_list_clean.sort()
print(state_list_clean)


#deleting rows that have nan location
dfillness = dfillness[pd.notnull(dfillness['Location'])]
dfillness.head()

#deleting rows that have nan food
dfillness = dfillness[pd.notnull(dfillness['Food'])]
dfillness.head()

#making df2 into a new csv file
dfillness.to_csv("outbreaksclean.csv")

#changing month names to month numbers
dfillness = dfillness.replace(to_replace = 'January', value = 1)
dfillness = dfillness.replace(to_replace = 'February', value = 2)
dfillness = dfillness.replace(to_replace = 'March', value = 3)
dfillness = dfillness.replace(to_replace =  'April', value = 4)
dfillness = dfillness.replace(to_replace = 'May', value = 5)
dfillness = dfillness.replace(to_replace = 'June', value = 6)
dfillness = dfillness.replace(to_replace = 'July', value = 7)
dfillness = dfillness.replace(to_replace = 'August', value = 8)
dfillness = dfillness.replace(to_replace = 'September', value = 9)
dfillness = dfillness.replace(to_replace = 'October', value = 10)
dfillness = dfillness.replace(to_replace = 'November', value = 11)
dfillness = dfillness.replace(to_replace = 'December', value = 12)

#separating dfillness by year
df1998 = dfillness[(dfillness['Year'] == 1998)]
df1999 = dfillness[(dfillness['Year'] == 1999)]
df2000 = dfillness[(dfillness['Year'] == 2000)]
df2001 = dfillness[(dfillness['Year'] == 2001)]
df2002 = dfillness[(dfillness['Year'] == 2002)]
df2003 = dfillness[(dfillness['Year'] == 2003)]
df2004 = dfillness[(dfillness['Year'] == 2004)]
df2005 = dfillness[(dfillness['Year'] == 2005)]
df2006 = dfillness[(dfillness['Year'] == 2006)]
df2007 = dfillness[(dfillness['Year'] == 2007)]
df2008 = dfillness[(dfillness['Year'] == 2008)]
df2009 = dfillness[(dfillness['Year'] == 2009)]
df2010 = dfillness[(dfillness['Year'] == 2010)]
df2011 = dfillness[(dfillness['Year'] == 2011)]
df2012 = dfillness[(dfillness['Year'] == 2012)]
df2013 = dfillness[(dfillness['Year'] == 2013)]
df2014 = dfillness[(dfillness['Year'] == 2014)]
df2015 = dfillness[(dfillness['Year'] == 2015)]

#turning dfyear into csv
df1998.to_csv("outbreaks1998.csv")
df1999.to_csv("outbreaks1999.csv")
df2000.to_csv("outbreaks2000.csv")
df2001.to_csv("outbreaks2001.csv")
df2002.to_csv("outbreaks2002.csv")
df2003.to_csv("outbreaks2003.csv")
df2004.to_csv("outbreaks2004.csv")
df2005.to_csv("outbreaks2005.csv")
df2006.to_csv("outbreaks2006.csv")
df2007.to_csv("outbreaks2007.csv")
df2008.to_csv("outbreaks2008.csv")
df2009.to_csv("outbreaks2009.csv")
df2010.to_csv("outbreaks2010.csv")
df2011.to_csv("outbreaks2011.csv")
df2012.to_csv("outbreaks2012.csv")
df2013.to_csv("outbreaks2013.csv")
df2014.to_csv("outbreaks2014.csv")
df2015.to_csv("outbreaks2015.csv")

#calculating TI (total illnesses) per year
TI1998 = df1998['Illnesses'].sum()
TI1999 = df1999['Illnesses'].sum()
TI2000 = df2000['Illnesses'].sum()
TI2001 = df2001['Illnesses'].sum()
TI2002 = df2002['Illnesses'].sum()
TI2003 = df2003['Illnesses'].sum()
TI2004 = df2004['Illnesses'].sum()
TI2005 = df2005['Illnesses'].sum()
TI2006 = df2006['Illnesses'].sum()
TI2007 = df2007['Illnesses'].sum()
TI2008 = df2008['Illnesses'].sum()
TI2009 = df2009['Illnesses'].sum()
TI2010 = df2010['Illnesses'].sum()
TI2011 = df2011['Illnesses'].sum()
TI2012 = df2012['Illnesses'].sum()
TI2013 = df2013['Illnesses'].sum()
TI2014 = df2014['Illnesses'].sum()
TI2015 = df2015['Illnesses'].sum()

#creates dict where years are keys and illness num are values
total_illness_data = {'1998':TI1998, '1999':TI1999, '2000':TI2000, '2001':TI2001, '2002':TI2002, '2003':TI2003, '2004':TI2004, '2005':TI2005,
                       '2006':TI2006, '2007':TI2007, '2008':TI2008, '2009':TI2009,  '2010': TI2010, '2011':TI2011, '2012':TI2012, '2013':TI2013,
                       '2014':TI2014, '2015':TI2015}
illness_year = list(total_illness_data.keys())
illness_num = list(total_illness_data.values())

#bar plot of total illnesses per year
total_illness_bar = plt.bar(range(len(total_illness_data)), illness_num, tick_label = illness_year)
plt.xticks(rotation = 45)
plt.ylim(ymax = 16000)
plt.xlabel('Year')
plt.ylabel('Illnesses')
plt.title('Total Foodborne Illnesses by Year')

#line plot
total_illness_line = plt.plot(illness_year, illness_num)
plt.xticks(rotation = 45)
plt.ylim(ymax = 16000)
plt.xlabel('Year')
plt.ylabel('Illnesses')
plt.title('Total Foodborne Illnesses by Year in the US')

#POPULATION STUFF

#loading population data csv
dfpoporiginal = pd.read_csv(r'C:\Users\Monica\Desktop\UCLA Extension\Data Science Certificate\2 Exploratory Data Analysis and Visualization\Final Project\popdata.csv')
dfpoporiginal.head()

#removing rows that have non states
dfpopclean = (dfpoporiginal[dfpoporiginal.NAME != 'United States'])
dfpopclean = (dfpopclean[dfpopclean.NAME != 'Northeast Region'])
dfpopclean = (dfpopclean[dfpopclean.NAME != 'Midwest Region'])
dfpopclean = (dfpopclean[dfpopclean.NAME != 'South Region'])
dfpopclean = (dfpopclean[dfpopclean.NAME != 'West Region'])
dfpopclean = (dfpopclean[dfpopclean.NAME != 'Puerto Rico'])

#keeping only desired columns in dfpopclean
dfpopclean = dfpopclean[['NAME', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']]

#replacing district of  columbia with washington dc to match other data set
dfpopclean = dfpopclean.replace(to_replace = 'District of Columbia', value = 'Washington DC')

#sorting dfpopclean from a-z
dfpopclean = dfpopclean.sort_values('NAME', ascending = True)

#resetting index because after changing to washington dc and sorting, index didn't change
dfpopclean = dfpopclean.reset_index(drop = True)
dfpopclean.head()

#converting to csv
dfpopclean.to_csv("popdataclean.csv")

#looking at minimum value in each column
#in name column alabama is min because it's first alphabetically but that's irrelevant
#pop estimates are 564487, 567299, 576305, 582122, 582531, 585613
#lowest population shows the lowest magnitude of population is 100,000
minpop = dfpopclean.min()

#new dict with years from 2010-2015 and corresponding total cases for eacy year
total_illness_data_cut = {'2010': TI2010, '2011':TI2011, '2012':TI2012, '2013':TI2013, '2014':TI2014, '2015':TI2015}
illness_year_cut = list(total_illness_data_cut.keys())
illness_num_cut = list(total_illness_data_cut.values())

#converting dict to df
dftotal_illness_cut = pd.DataFrame(total_illness_data_cut.items(), columns = ['Year', 'Total Illnesses'])

#creating a list of months
months_list = []
for i in dfillness['Month']:
    if i not in months_list:
        months_list.append(i)
print(months_list)

#cut df to only show columns month, state, illnesses
df2010cut = df2010[['Month', 'State', 'Illnesses']]
df2011cut = df2011[['Month', 'State', 'Illnesses']]
df2012cut = df2012[['Month', 'State', 'Illnesses']]
df2013cut = df2013[['Month', 'State', 'Illnesses']]
df2014cut = df2014[['Month', 'State', 'Illnesses']]
df2015cut = df2015[['Month', 'State', 'Illnesses']]

#sums illnesses grouped by month and state as LISTS
list2010TotalIllness = df2010.groupby(['Month', 'State'])['Illnesses'].sum()
list2011TotalIllness = df2011.groupby(['Month', 'State'])['Illnesses'].sum()
list2012TotalIllness = df2012.groupby(['Month', 'State'])['Illnesses'].sum()
list2013TotalIllness = df2013.groupby(['Month', 'State'])['Illnesses'].sum()
list2014TotalIllness = df2014.groupby(['Month', 'State'])['Illnesses'].sum()
list2015TotalIllness = df2015.groupby(['Month', 'State'])['Illnesses'].sum()

#makes df for each year where it sums all the illnesses in each state
df2010SumStateIllnesses = df2010.groupby('State', as_index = False)['Illnesses'].sum()
df2011SumStateIllnesses = df2011.groupby('State', as_index = False)['Illnesses'].sum()
df2012SumStateIllnesses = df2012.groupby('State', as_index = False)['Illnesses'].sum()
df2013SumStateIllnesses = df2013.groupby('State', as_index = False)['Illnesses'].sum()
df2014SumStateIllnesses = df2014.groupby('State', as_index = False)['Illnesses'].sum()
df2015SumStateIllnesses = df2015.groupby('State', as_index = False)['Illnesses'].sum()

#removes multistate rows from each
df2010SumStateIllnessesClean = (df2010SumStateIllnesses[df2010SumStateIllnesses.State != 'Multistate'])
df2011SumStateIllnessesClean = (df2011SumStateIllnesses[df2011SumStateIllnesses.State != 'Multistate'])
df2012SumStateIllnessesClean = (df2012SumStateIllnesses[df2012SumStateIllnesses.State != 'Multistate'])
df2013SumStateIllnessesClean = (df2013SumStateIllnesses[df2013SumStateIllnesses.State != 'Multistate'])
df2014SumStateIllnessesClean = (df2014SumStateIllnesses[df2014SumStateIllnesses.State != 'Multistate'])
df2015SumStateIllnessesClean = (df2015SumStateIllnesses[df2015SumStateIllnesses.State != 'Multistate'])

#converting to list of tuples
series2010listbystate = df2010SumStateIllnessesClean.values.tolist()
series2011listbystate = df2011SumStateIllnessesClean.values.tolist()
series2012listbystate = df2012SumStateIllnessesClean.values.tolist()
series2013listbystate = df2013SumStateIllnessesClean.values.tolist()
series2014listbystate = df2014SumStateIllnessesClean.values.tolist()
series2015listbystate = df2015SumStateIllnessesClean.values.tolist()

#separate population data by year and into its own df
pop2010 = dfpopclean[['NAME', 'POPESTIMATE2010']]
pop2011 = dfpopclean[['NAME', 'POPESTIMATE2011']]
pop2012 = dfpopclean[['NAME', 'POPESTIMATE2012']]
pop2013 = dfpopclean[['NAME', 'POPESTIMATE2013']]
pop2014 = dfpopclean[['NAME', 'POPESTIMATE2014']]
pop2015 = dfpopclean[['NAME', 'POPESTIMATE2015']]

#convert pop data into list of tuples
listpop2010 = pop2010.values.tolist()
listpop2011 = pop2011.values.tolist()
listpop2012 = pop2012.values.tolist()
listpop2013 = pop2013.values.tolist()
listpop2014 = pop2014.values.tolist()
listpop2015 = pop2015.values.tolist()

#function that combines two lists, adds to dictionary and appends with matching first value
import collections

def merge(lst1, lst2):
    dict1 = collections.defaultdict(list)
    for e in lst1 + lst2:
        dict1[e[0]].append(e[1])
    dictlist = list()
    
    for key, value in dict1.items():
        dictlist.append([key] + value)
    return(dictlist)

#combine two lists using function
list2010IllnessState = merge(listpop2010, series2010listbystate)
list2011IllnessState = merge(listpop2011, series2011listbystate)
list2012IllnessState = merge(listpop2012, series2012listbystate)
list2013IllnessState = merge(listpop2013, series2013listbystate)
list2014IllnessState = merge(listpop2014, series2014listbystate)
list2015IllnessState = merge(listpop2015, series2015listbystate)

#converting combined lists to df and 
dfIllnessCalc2010 = pd.DataFrame(list2010IllnessState, columns = ['State', 'Population', 'Illnesses'])
dfIllnessCalc2011 = pd.DataFrame(list2011IllnessState, columns = ['State', 'Population', 'Illnesses'])
dfIllnessCalc2012 = pd.DataFrame(list2012IllnessState, columns = ['State', 'Population', 'Illnesses'])
dfIllnessCalc2013 = pd.DataFrame(list2013IllnessState, columns = ['State', 'Population', 'Illnesses'])
dfIllnessCalc2014 = pd.DataFrame(list2014IllnessState, columns = ['State', 'Population', 'Illnesses'])
dfIllnessCalc2015 = pd.DataFrame(list2015IllnessState, columns = ['State', 'Population', 'Illnesses'])

#calculating illnesses per person = illnesses / population
dfIllnessCalc2010['Illnesses per Person'] = (dfIllnessCalc2010['Illnesses'] / dfIllnessCalc2010['Population'])
dfIllnessCalc2011['Illnesses per Person'] = (dfIllnessCalc2011['Illnesses'] / dfIllnessCalc2011['Population'])
dfIllnessCalc2012['Illnesses per Person'] = (dfIllnessCalc2012['Illnesses'] / dfIllnessCalc2012['Population'])
dfIllnessCalc2013['Illnesses per Person'] = (dfIllnessCalc2013['Illnesses'] / dfIllnessCalc2013['Population'])
dfIllnessCalc2014['Illnesses per Person'] = (dfIllnessCalc2014['Illnesses'] / dfIllnessCalc2014['Population'])
dfIllnessCalc2015['Illnesses per Person'] = (dfIllnessCalc2015['Illnesses'] / dfIllnessCalc2015['Population'])

#normalizing illnesses per person by the population, (illness/population) * 100,000
dfIllnessCalc2010['Illnesses per 100,000 People'] = (dfIllnessCalc2010['Illnesses per Person'] * 100000)
dfIllnessCalc2011['Illnesses per 100,000 People'] = (dfIllnessCalc2011['Illnesses per Person'] * 100000)
dfIllnessCalc2012['Illnesses per 100,000 People'] = (dfIllnessCalc2012['Illnesses per Person'] * 100000)
dfIllnessCalc2013['Illnesses per 100,000 People'] = (dfIllnessCalc2013['Illnesses per Person'] * 100000)
dfIllnessCalc2014['Illnesses per 100,000 People'] = (dfIllnessCalc2014['Illnesses per Person'] * 100000)
dfIllnessCalc2015['Illnesses per 100,000 People'] = (dfIllnessCalc2015['Illnesses per Person'] * 100000)

#converting to csv
dfIllnessCalc2010.to_csv('2010 illness calc.csv')
dfIllnessCalc2011.to_csv('2011 illness calc.csv')
dfIllnessCalc2012.to_csv('2012 illness calc.csv')
dfIllnessCalc2013.to_csv('2013 illness calc.csv')
dfIllnessCalc2014.to_csv('2014 illness calc.csv')
dfIllnessCalc2015.to_csv('2015 illness calc.csv')

#converting back to lists
listIllnessCalc2010 = dfIllnessCalc2010.values.tolist()
listIllnessCalc2011 = dfIllnessCalc2011.values.tolist()
listIllnessCalc2012 = dfIllnessCalc2012.values.tolist()
listIllnessCalc2013 = dfIllnessCalc2013.values.tolist()
listIllnessCalc2014 = dfIllnessCalc2014.values.tolist()
listIllnessCalc2015 = dfIllnessCalc2015.values.tolist()

#combining all years

#ADJUSTED POP
#makes list of adj illness rate for each year
adjillnessrate2010 = []
for i in listIllnessCalc2010:
    adjillnessrate2010.append(i[4])
    print(adjillnessrate2010)

adjillnessrate2011 = []
for i in listIllnessCalc2011:
    adjillnessrate2011.append(i[4])
    print(adjillnessrate2011)

adjillnessrate2012 = []
for i in listIllnessCalc2012:
    adjillnessrate2012.append(i[4])
    print(adjillnessrate2012)
    
adjillnessrate2013 = []
for i in listIllnessCalc2013:
    adjillnessrate2013.append(i[4])
    print(adjillnessrate2013)

adjillnessrate2014 = []
for i in listIllnessCalc2014:
    adjillnessrate2014.append(i[4])
    print(adjillnessrate2014)
    
adjillnessrate2015 = []
for i in listIllnessCalc2015:
    adjillnessrate2015.append(i[4])
    print(adjillnessrate2015)
    
#merges 7 lists together, used for adjusted illness rates for each year
def merge1(list1, list2, list3, list4, list5, list6, list7):
    merged_list = tuple(zip(list1, list2, list3, list4, list5, list6, list7))
    return merged_list

#merges illness rate for all six years with statelist
CombineAllYearsPopAdj = merge1(state_list_clean, adjillnessrate2010, adjillnessrate2011, adjillnessrate2012, adjillnessrate2013, adjillnessrate2014, adjillnessrate2015)

#convert combinedallyears to df and add column labels
dfCombineAllYearsPopAdj = pd.DataFrame(CombineAllYearsPopAdj, columns = ['State', '2010', '2011', '2012', '2013', '2014', '2015'])

#calculating sum for dfCombineAllYearsPopAdjdfCombineAllYearsPopAdj
dfCombineAllYearsPopAdj['Total'] = dfCombineAllYearsPopAdj[['2010', '2011', '2012', '2013', '2014', '2015']].sum(axis = 1)

#calculating mean for dfCombineAllYearsPopAdj
dfCombineAllYearsPopAdj['Mean'] = dfCombineAllYearsPopAdj[['2010', '2011', '2012', '2013', '2014', '2015']].mean(axis = 1)

#calculating stdev for dfCombineAllYearsPopAdj
dfCombineAllYearsPopAdj['Standard Deviation'] = dfCombineAllYearsPopAdj[['2010', '2011', '2012', '2013', '2014', '2015']].std(axis = 1)

#convert to csv
dfCombineAllYearsPopAdj.to_csv('Combined Illness Calculation Pop Adj.csv')

#TOTAL CASES NOT ADJ FOR POP
#makes list of illnessES for each year
illness2010 = []
for i in listIllnessCalc2010:
    illness2010.append(i[2])

illness2011 = []
for i in listIllnessCalc2011:
    illness2011.append(i[2])

illness2012 = []
for i in listIllnessCalc2012:
    illness2012.append(i[2])
    
illness2013 = []
for i in listIllnessCalc2013:
    illness2013.append(i[2])

illness2014 = []
for i in listIllnessCalc2014:
    illness2014.append(i[2])
    
illness2015 = []
for i in listIllnessCalc2015:
    illness2015.append(i[2])
    
#use merge1 function from above

#merges illness rate for all six years with statelist
CombineAllYears = merge1(state_list_clean, illness2010, illness2011, illness2012, illness2013, illness2014, illness2015)

#convert combinedallyears to df and add column labels
dfCombineAllYears = pd.DataFrame(CombineAllYears, columns = ['State', '2010', '2011', '2012', '2013', '2014', '2015'])

#calculating sum across years
dfCombineAllYears['Total'] = dfCombineAllYears[['2010', '2011', '2012', '2013', '2014', '2015']].sum(axis = 1)

#calculating mean for dfCombineAllYearsPopAdj
dfCombineAllYears['Mean'] = dfCombineAllYears[['2010', '2011', '2012', '2013', '2014', '2015']].mean(axis = 1)

#calculating stdev for dfCombineAllYearsPopAdj
dfCombineAllYears['Standard Deviation'] = dfCombineAllYears[['2010', '2011', '2012', '2013', '2014', '2015']].std(axis = 1)

#convert to csv
dfCombineAllYears.to_csv('Combined Illness Calculation.csv')

#calculating mean for dfpopclean
dfpopclean['Mean'] = dfpopclean.mean(axis = 1)

#calculating stdev for dfpopclean
dfpopclean['Standard Deviation'] = dfpopclean.std(axis = 1)

#converting to csv
dfpopclean.to_csv('popcalculations.csv')

#converting to csv
pop2010.to_csv('pop2010.csv')
pop2011.to_csv('pop2011.csv')
pop2012.to_csv('pop2012.csv')
pop2013.to_csv('pop2013.csv')
pop2014.to_csv('pop2014.csv')
pop2015.to_csv('pop2015.csv')

#in dfCombineAllYearsPopAdj return the max total with corresponding state
dfCombineAllYearsPopAdjMaxTotal = dfCombineAllYearsPopAdj[['State', 'Total']][dfCombineAllYearsPopAdj.Total == dfCombineAllYearsPopAdj['Total'].max()]

#in dfCombineAllYearsPopAdj return the max mean with corresponding state
dfCombineAllYearsPopAdjMeanTotal = dfCombineAllYearsPopAdj[['State', 'Mean']][dfCombineAllYearsPopAdj.Mean == dfCombineAllYearsPopAdj['Mean'].max()]

#converting to csv
dfCombineAllYearsPopAdjMaxTotal.to_csv('max total cases pop adj.csv')
dfCombineAllYearsPopAdjMeanTotal.to_csv('max mean cases pop adj.csv')

dfYear = pd.DataFrame({'Year': ['2010', '2011', '2012', '2013', '2014', '2015']})

#LOCATIONS
#RESTAURANT
#removed multistate
df2010CleanedState = (df2010[df2010.State != 'Multistate'])
df2011CleanedState = (df2011[df2011.State != 'Multistate'])
df2012CleanedState = (df2012[df2012.State != 'Multistate'])
df2013CleanedState = (df2013[df2013.State != 'Multistate'])
df2014CleanedState = (df2014[df2014.State != 'Multistate'])
df2015CleanedState = (df2015[df2015.State != 'Multistate'])


#created a dataframe from df2010cleanedstate column location where column contains restaurant
df2010Restaurant = df2010CleanedState[df2010CleanedState['Location'].str.contains('Restaurant')]
df2011Restaurant = df2011CleanedState[df2011CleanedState['Location'].str.contains('Restaurant')]
df2012Restaurant = df2012CleanedState[df2012CleanedState['Location'].str.contains('Restaurant')]
df2013Restaurant = df2013CleanedState[df2013CleanedState['Location'].str.contains('Restaurant')]
df2014Restaurant = df2014CleanedState[df2014CleanedState['Location'].str.contains('Restaurant')]
df2015Restaurant = df2015CleanedState[df2015CleanedState['Location'].str.contains('Restaurant')]

#summed illnesses in df2010restaurant
df2010RestaurantCases = df2010Restaurant['Illnesses'].sum()
df2011RestaurantCases = df2011Restaurant['Illnesses'].sum()
df2012RestaurantCases = df2012Restaurant['Illnesses'].sum()
df2013RestaurantCases = df2013Restaurant['Illnesses'].sum()
df2014RestaurantCases = df2014Restaurant['Illnesses'].sum()
df2015RestaurantCases = df2015Restaurant['Illnesses'].sum()


#make data frame of year and restaurant cases
dfTotalRestaurantCases = pd.DataFrame([('2010', df2010RestaurantCases), ('2011', df2011RestaurantCases), ('2012', df2012RestaurantCases), 
                        ('2013', df2013RestaurantCases), ('2014', df2014RestaurantCases), ('2015', df2015RestaurantCases)], 
                                    columns = ['Year', 'Illnesses'])

SumRestaurantCases = dfTotalRestaurantCases['Illnesses'].sum()

#convert to csv
dfTotalRestaurantCases.to_csv('total restaurant cases.csv')

#GROCERY STORE
#created a dataframe from df2010cleanedstate column location where column contains grocery store
df2010Grocery = df2010CleanedState[df2010CleanedState['Location'].str.contains('Grocery')]
df2011Grocery = df2011CleanedState[df2011CleanedState['Location'].str.contains('Grocery')]
df2012Grocery = df2012CleanedState[df2012CleanedState['Location'].str.contains('Grocery')]
df2013Grocery = df2013CleanedState[df2013CleanedState['Location'].str.contains('Grocery')]
df2014Grocery = df2014CleanedState[df2014CleanedState['Location'].str.contains('Grocery')]
df2015Grocery = df2015CleanedState[df2015CleanedState['Location'].str.contains('Grocery')]

#summed illnesses in df2010grocerystore
df2010GroceryCases = df2010Grocery['Illnesses'].sum()
df2011GroceryCases = df2011Grocery['Illnesses'].sum()
df2012GroceryCases = df2012Grocery['Illnesses'].sum()
df2013GroceryCases = df2013Grocery['Illnesses'].sum()
df2014GroceryCases = df2014Grocery['Illnesses'].sum()
df2015GroceryCases = df2015Grocery['Illnesses'].sum()

#make data frame of year and grocery store cases
dfTotalGroceryCases = pd.DataFrame([('2010', df2010GroceryCases), ('2011', df2011GroceryCases), ('2012', df2012GroceryCases), 
                        ('2013', df2013GroceryCases), ('2014', df2014GroceryCases), ('2015', df2015GroceryCases)], 
                                    columns = ['Year', 'Illnesses'])

SumGroceryCases = dfTotalGroceryCases['Illnesses'].sum()

#convert to csv
dfTotalGroceryCases.to_csv('total grocery cases.csv')

#PRIVATE HOME/RESIDENCE
#created a dataframe from df2010cleanedstate column location where column contains residence
df2010Residence = df2010CleanedState[df2010CleanedState['Location'].str.contains('Residence')]
df2011Residence = df2011CleanedState[df2011CleanedState['Location'].str.contains('Residence')]
df2012Residence = df2012CleanedState[df2012CleanedState['Location'].str.contains('Residence')]
df2013Residence = df2013CleanedState[df2013CleanedState['Location'].str.contains('Residence')]
df2014Residence = df2014CleanedState[df2014CleanedState['Location'].str.contains('Residence')]
df2015Residence = df2015CleanedState[df2015CleanedState['Location'].str.contains('Residence')]

#summed illnesses in df2010residence
df2010ResidenceCases = df2010Residence['Illnesses'].sum()
df2011ResidenceCases = df2011Residence['Illnesses'].sum()
df2012ResidenceCases = df2012Residence['Illnesses'].sum()
df2013ResidenceCases = df2013Residence['Illnesses'].sum()
df2014ResidenceCases = df2014Residence['Illnesses'].sum()
df2015ResidenceCases = df2015Residence['Illnesses'].sum()

#make data frame of year and residence cases
dfTotalResidenceCases = pd.DataFrame([('2010', df2010ResidenceCases), ('2011', df2011ResidenceCases), ('2012', df2012ResidenceCases), 
                        ('2013', df2013ResidenceCases), ('2014', df2014ResidenceCases), ('2015', df2015ResidenceCases)], 
                                    columns = ['Year', 'Illnesses'])

SumResidenceCases = dfTotalResidenceCases['Illnesses'].sum()


#convert to csv
dfTotalResidenceCases.to_csv('total residence cases.csv')

#CATERING SERVICE
#created a dataframe from df2010cleanedstate column location where column contains catering
df2010Catering = df2010CleanedState[df2010CleanedState['Location'].str.contains('Catering')]
df2011Catering = df2011CleanedState[df2011CleanedState['Location'].str.contains('Catering')]
df2012Catering = df2012CleanedState[df2012CleanedState['Location'].str.contains('Catering')]
df2013Catering = df2013CleanedState[df2013CleanedState['Location'].str.contains('Catering')]
df2014Catering = df2014CleanedState[df2014CleanedState['Location'].str.contains('Catering')]
df2015Catering = df2015CleanedState[df2015CleanedState['Location'].str.contains('Catering')]

#summed illnesses in df2010catering
df2010CateringCases = df2010Catering['Illnesses'].sum()
df2011CateringCases = df2011Catering['Illnesses'].sum()
df2012CateringCases = df2012Catering['Illnesses'].sum()
df2013CateringCases = df2013Catering['Illnesses'].sum()
df2014CateringCases = df2014Catering['Illnesses'].sum()
df2015CateringCases = df2015Catering['Illnesses'].sum()

#make data frame of year and catering cases
dfTotalCateringCases = pd.DataFrame([('2010', df2010CateringCases), ('2011', df2011CateringCases), ('2012', df2012CateringCases), 
                        ('2013', df2013CateringCases), ('2014', df2014CateringCases), ('2015', df2015CateringCases)], 
                                    columns = ['Year', 'Illnesses'])

SumCateringCases = dfTotalCateringCases['Illnesses'].sum()


#convert to csv
dfTotalCateringCases.to_csv('total catering cases.csv')

#BANQUET FACILITY
#created a dataframe from df2010cleanedstate column location where column contains banquet
df2010Banquet = df2010CleanedState[df2010CleanedState['Location'].str.contains('Banquet')]
df2011Banquet = df2011CleanedState[df2011CleanedState['Location'].str.contains('Banquet')]
df2012Banquet = df2012CleanedState[df2012CleanedState['Location'].str.contains('Banquet')]
df2013Banquet = df2013CleanedState[df2013CleanedState['Location'].str.contains('Banquet')]
df2014Banquet = df2014CleanedState[df2014CleanedState['Location'].str.contains('Banquet')]
df2015Banquet = df2015CleanedState[df2015CleanedState['Location'].str.contains('Banquet')]

#summed illnesses in df2010banquet
df2010BanquetCases = df2010Banquet['Illnesses'].sum()
df2011BanquetCases = df2011Banquet['Illnesses'].sum()
df2012BanquetCases = df2012Banquet['Illnesses'].sum()
df2013BanquetCases = df2013Banquet['Illnesses'].sum()
df2014BanquetCases = df2014Banquet['Illnesses'].sum()
df2015BanquetCases = df2015Banquet['Illnesses'].sum()

#make data frame of year and banquet cases
dfTotalBanquetCases = pd.DataFrame([('2010', df2010BanquetCases), ('2011', df2011BanquetCases), ('2012', df2012BanquetCases), 
                        ('2013', df2013BanquetCases), ('2014', df2014BanquetCases), ('2015', df2015BanquetCases)], 
                                    columns = ['Year', 'Illnesses'])

#convert to csv
dfTotalBanquetCases.to_csv('total banquet cases.csv')

#BEEF
#searching food column
beefwords = ['Beef', 'Hamburger', 'Carne Asada', 'Steak', 'Sloppy Joe']
beefjoinwords = '|'.join(beefwords)

df2010FoodBeef = df2010CleanedState[df2010CleanedState['Food'].str.contains(beefjoinwords)]
df2011FoodBeef = df2011CleanedState[df2011CleanedState['Food'].str.contains(beefjoinwords)]
df2012FoodBeef = df2012CleanedState[df2012CleanedState['Food'].str.contains(beefjoinwords)]
df2013FoodBeef = df2013CleanedState[df2013CleanedState['Food'].str.contains(beefjoinwords)]
df2014FoodBeef = df2014CleanedState[df2014CleanedState['Food'].str.contains(beefjoinwords)]
df2015FoodBeef = df2015CleanedState[df2015CleanedState['Food'].str.contains(beefjoinwords)]

Count2010FoodBeef = df2010FoodBeef['Illnesses'].sum()
Count2011FoodBeef = df2011FoodBeef['Illnesses'].sum()
Count2012FoodBeef = df2012FoodBeef['Illnesses'].sum()
Count2013FoodBeef = df2013FoodBeef['Illnesses'].sum()
Count2014FoodBeef = df2014FoodBeef['Illnesses'].sum()
Count2015FoodBeef = df2015FoodBeef['Illnesses'].sum()

dfTotalFoodBeef = pd.DataFrame([('2010', Count2010FoodBeef), ('2011', Count2011FoodBeef), ('2012', Count2012FoodBeef), 
                                ('2013', Count2013FoodBeef), ('2014', Count2014FoodBeef), ('2015', Count2015FoodBeef)],
                               columns = ['Year', 'Illnesses'])

SumBeefCases = dfTotalFoodBeef['Illnesses'].sum()

#FISH
#searching food column
fishwords = ['Fish', 'Tuna', 'Yellowtail', 'Grouper', 'Salmon', 'Sushi', 'Sashimi', 'Amberjack']
fishjoinwords = '|'.join(fishwords)

df2010FoodFish = df2010CleanedState[df2010CleanedState['Food'].str.contains(fishjoinwords)]
df2011FoodFish = df2011CleanedState[df2011CleanedState['Food'].str.contains(fishjoinwords)]
df2012FoodFish = df2012CleanedState[df2012CleanedState['Food'].str.contains(fishjoinwords)]
df2013FoodFish = df2013CleanedState[df2013CleanedState['Food'].str.contains(fishjoinwords)]
df2014FoodFish = df2014CleanedState[df2014CleanedState['Food'].str.contains(fishjoinwords)]
df2015FoodFish = df2015CleanedState[df2015CleanedState['Food'].str.contains(fishjoinwords)]

Count2010FoodFish = df2010FoodFish['Illnesses'].sum()
Count2011FoodFish = df2011FoodFish['Illnesses'].sum()
Count2012FoodFish = df2012FoodFish['Illnesses'].sum()
Count2013FoodFish = df2013FoodFish['Illnesses'].sum()
Count2014FoodFish = df2014FoodFish['Illnesses'].sum()
Count2015FoodFish = df2015FoodFish['Illnesses'].sum()

dfTotalFoodFish = pd.DataFrame([('2010', Count2010FoodFish), ('2011', Count2011FoodFish), ('2012', Count2012FoodFish), 
                                ('2013', Count2013FoodFish), ('2014', Count2014FoodFish), ('2015', Count2015FoodFish)],
                               columns = ['Year', 'Illnesses'])

SumFishCases = dfTotalFoodFish['Illnesses'].sum()

#PORK
porkwords = ['Pork', 'Carnitas', 'Hog', 'Pig', 'Ribs']
porkjoinwords = '|'.join(porkwords)

df2010FoodPork = df2010CleanedState[df2010CleanedState['Food'].str.contains(porkjoinwords)]
df2011FoodPork = df2011CleanedState[df2011CleanedState['Food'].str.contains(porkjoinwords)]
df2012FoodPork = df2012CleanedState[df2012CleanedState['Food'].str.contains(porkjoinwords)]
df2013FoodPork = df2013CleanedState[df2013CleanedState['Food'].str.contains(porkjoinwords)]
df2014FoodPork = df2014CleanedState[df2014CleanedState['Food'].str.contains(porkjoinwords)]
df2015FoodPork = df2015CleanedState[df2015CleanedState['Food'].str.contains(porkjoinwords)]

Count2010FoodPork = df2010FoodPork['Illnesses'].sum()
Count2011FoodPork = df2011FoodPork['Illnesses'].sum()
Count2012FoodPork = df2012FoodPork['Illnesses'].sum()
Count2013FoodPork = df2013FoodPork['Illnesses'].sum()
Count2014FoodPork = df2014FoodPork['Illnesses'].sum()
Count2015FoodPork = df2015FoodBeef['Illnesses'].sum()

dfTotalFoodPork = pd.DataFrame([('2010', Count2010FoodPork), ('2011', Count2011FoodPork), ('2012', Count2012FoodPork), 
                                ('2013', Count2013FoodPork), ('2014', Count2014FoodPork), ('2015', Count2015FoodPork)],
                               columns = ['Year', 'Illnesses'])

SumPorkCases = dfTotalFoodPork['Illnesses'].sum()

#test = df2010CleanedState[df2010CleanedState['Food'].str.contains('Chicken|Fish')]

#CHICKEN
chickenwords = ['Chicken', 'Wings']
chickenjoinwords = '|'.join(chickenwords)

df2010FoodChicken = df2010CleanedState[df2010CleanedState['Food'].str.contains(chickenjoinwords)]
df2011FoodChicken = df2011CleanedState[df2011CleanedState['Food'].str.contains(chickenjoinwords)]
df2012FoodChicken = df2012CleanedState[df2012CleanedState['Food'].str.contains(chickenjoinwords)]
df2013FoodChicken = df2013CleanedState[df2013CleanedState['Food'].str.contains(chickenjoinwords)]
df2014FoodChicken = df2014CleanedState[df2014CleanedState['Food'].str.contains(chickenjoinwords)]
df2015FoodChicken = df2015CleanedState[df2015CleanedState['Food'].str.contains(chickenjoinwords)]

Count2010FoodChicken = df2010FoodChicken['Illnesses'].sum()
Count2011FoodChicken = df2011FoodChicken['Illnesses'].sum()
Count2012FoodChicken = df2012FoodChicken['Illnesses'].sum()
Count2013FoodChicken = df2013FoodChicken['Illnesses'].sum()
Count2014FoodChicken = df2014FoodChicken['Illnesses'].sum()
Count2015FoodChicken = df2015FoodChicken['Illnesses'].sum()

dfTotalFoodChicken = pd.DataFrame([('2010', Count2010FoodChicken), ('2011', Count2011FoodChicken), ('2012', Count2012FoodChicken), 
                                ('2013', Count2013FoodChicken), ('2014', Count2014FoodChicken), ('2015', Count2015FoodChicken)],
                               columns = ['Year', 'Illnesses'])

SumChickenCases = dfTotalFoodChicken['Illnesses'].sum()

#SALAD
saladwords = ['Salad', 'Lettuce', 'Cabbage']
saladjoinwords = '|'.join(saladwords)

df2010FoodSalad = df2010CleanedState[df2010CleanedState['Food'].str.contains(saladjoinwords)]
df2011FoodSalad = df2011CleanedState[df2011CleanedState['Food'].str.contains(saladjoinwords)]
df2012FoodSalad = df2012CleanedState[df2012CleanedState['Food'].str.contains(saladjoinwords)]
df2013FoodSalad = df2013CleanedState[df2013CleanedState['Food'].str.contains(saladjoinwords)]
df2014FoodSalad = df2014CleanedState[df2014CleanedState['Food'].str.contains(saladjoinwords)]
df2015FoodSalad = df2015CleanedState[df2015CleanedState['Food'].str.contains(saladjoinwords)]

Count2010FoodSalad = df2010FoodSalad['Illnesses'].sum()
Count2011FoodSalad = df2011FoodSalad['Illnesses'].sum()
Count2012FoodSalad = df2012FoodSalad['Illnesses'].sum()
Count2013FoodSalad = df2013FoodSalad['Illnesses'].sum()
Count2014FoodSalad = df2014FoodSalad['Illnesses'].sum()
Count2015FoodSalad = df2015FoodSalad['Illnesses'].sum()

dfTotalFoodSalad = pd.DataFrame([('2010', Count2010FoodSalad), ('2011', Count2011FoodSalad), ('2012', Count2012FoodSalad), 
                                ('2013', Count2013FoodSalad), ('2014', Count2014FoodSalad), ('2015', Count2015FoodSalad)],
                               columns = ['Year', 'Illnesses'])

SumSaladCases = dfTotalFoodSalad['Illnesses'].sum()

#adding cases from each year to dataframe
dfAllCases = pd.concat([dfYear['Year'], dfTotalRestaurantCases['Illnesses'], dfTotalGroceryCases['Illnesses'],
                              dfTotalResidenceCases['Illnesses'], dfTotalBanquetCases['Illnesses'], dfTotalCateringCases['Illnesses'],
                              dfTotalFoodBeef['Illnesses'], dfTotalFoodFish['Illnesses'], dfTotalFoodPork['Illnesses'],
                              dfTotalFoodChicken['Illnesses'], dfTotalFoodSalad['Illnesses']], axis = 1)

dfAllCases.columns = ['Year', 'Restaurant', 'Grocery', 'Residence', 'Banquet', 'Catering', 'Beef', 'Fish', 'Pork', 'Chicken', 'Salad']

dfAllCases.to_csv('2010-2015 Location and Food Cases.csv')

#look at df2010, df2011, df2012, df2013, df2014, df2015
#make df for just california and minnesota

#restaurant california: 20, 19, 21, 22, 21, 

dfillness = dfillness[dfillness.State != 'Multistate']

#cases only with california and minnesota
dfCalifornia = dfillness[dfillness.State == 'California']
dfMinnesota = dfillness[dfillness.State == 'Minnesota']

#years needed
desiredyears = [2010, 2011, 2012, 2013, 2014, 2015]

#making df for california and minnesotta with desiredyears
dfCaliforniaAdjYears = dfCalifornia[dfCalifornia['Year'].isin(desiredyears)]
dfMinnesotaAdjYears = dfMinnesota[dfMinnesota['Year'].isin(desiredyears)]

#searches for most found value in location column
dfCaliforniaAdjYears.Location.mode()
dfMinnesotaAdjYears.Location.mode()

#getting total illnesses per month
dfillnesscleanyear = dfillness[dfillness['Year'].isin(desiredyears)]

dfJanuaryIllness = dfillnesscleanyear[dfillness['Month'] == 1]
dfFebruaryIllness = dfillnesscleanyear[dfillness['Month'] == 2]
dfMarchIllness = dfillnesscleanyear[dfillness['Month'] == 3]
dfAprilIllness = dfillnesscleanyear[dfillness['Month'] == 4]
dfMayIllness = dfillnesscleanyear[dfillness['Month'] == 5]
dfJuneIllness = dfillnesscleanyear[dfillness['Month'] == 6]
dfJulyIllness = dfillnesscleanyear[dfillness['Month'] == 7]
dfAugustIllness = dfillnesscleanyear[dfillness['Month'] == 8]
dfSeptemberIllness = dfillnesscleanyear[dfillness['Month'] == 9]
dfOctoberIllness = dfillnesscleanyear[dfillness['Month'] == 10]
dfNovemberIllness = dfillnesscleanyear[dfillness['Month'] == 11]
dfDecemberIllness = dfillnesscleanyear[dfillness['Month'] == 12]

JanuaryIllnessSum = dfJanuaryIllness['Illnesses'].sum()
FebruaryIllnessSum = dfFebruaryIllness['Illnesses'].sum()
MarchIllnessSum = dfMarchIllness['Illnesses'].sum()
AprilIllnessSum = dfAprilIllness['Illnesses'].sum()
MayIllnessSum = dfMayIllness['Illnesses'].sum()
JuneIllnessSum = dfJuneIllness['Illnesses'].sum()
JulyIllnessSum = dfJulyIllness['Illnesses'].sum()
AugustIllnessSum = dfAugustIllness['Illnesses'].sum()
SeptemberIllnessSum = dfSeptemberIllness['Illnesses'].sum()
OctoberIllnessSum = dfOctoberIllness['Illnesses'].sum()
NovemberIllnessSum = dfNovemberIllness['Illnesses'].sum()
DecemberIllnessSum = dfDecemberIllness['Illnesses'].sum()

dfIllnessPerMonth = pd.DataFrame([('January', JanuaryIllnessSum), ('February', FebruaryIllnessSum), ('March', MarchIllnessSum),
                                  ('April', AprilIllnessSum), ('May', MayIllnessSum), ('June', JuneIllnessSum),
                                  ('July', JulyIllnessSum), ('August', AugustIllnessSum), ('September', SeptemberIllnessSum),
                                  ('October', OctoberIllnessSum), ('November', NovemberIllnessSum), ('December', DecemberIllnessSum)],
                                 columns = ['Month', 'Illnesses'])

SumIllnesses = dfIllnessPerMonth['Illnesses'].sum()

dfIllnessPerMonth['Percentage'] = (dfIllnessPerMonth['Illnesses'] / SumIllnesses) * 100

dfIllnessPerMonth.to_csv('illnesses per month.csv')

#dftotal_illness_cut shows number of illnesses per year (2010-2015)

#get sum of population each year
sumpop2010 = pop2010['POPESTIMATE2010'].sum()
sumpop2011 = pop2011['POPESTIMATE2011'].sum()
sumpop2012 = pop2012['POPESTIMATE2012'].sum()
sumpop2013 = pop2013['POPESTIMATE2013'].sum()
sumpop2014 = pop2014['POPESTIMATE2014'].sum()
sumpop2015 = pop2015['POPESTIMATE2015'].sum()

YearlyPop = pd.DataFrame([('2010', sumpop2010), ('2011', sumpop2011), ('2012', sumpop2012),
                          ('2013', sumpop2013), ('2014', sumpop2014), ('2015', sumpop2015)], columns = ['Year', 'Population'])

YearlyPop.to_csv('US Yearly Population 2010-2015.csv')

dftotal_illness_cut.to_csv('Total Illnesses Per Year 2010-2015.csv')

#cases in california per month
dfCaliforniaJanuaryCases = dfJanuaryIllness[dfJanuaryIllness['State'] == 'California']
dfCaliforniaFebruaryCases = dfFebruaryIllness[dfFebruaryIllness['State'] == 'California']
dfCaliforniaMarchCases = dfMarchIllness[dfMarchIllness['State'] == 'California']
dfCaliforniaAprilCases = dfAprilIllness[dfAprilIllness['State'] == 'California']
dfCaliforniaMayCases = dfMayIllness[dfMayIllness['State'] == 'California']
dfCaliforniaJuneCases = dfJuneIllness[dfJuneIllness['State'] == 'California']
dfCaliforniaJulyCases = dfJulyIllness[dfJulyIllness['State'] == 'California']
dfCaliforniaAugustCases = dfAugustIllness[dfAugustIllness['State'] == 'California']
dfCaliforniaSeptemberCases = dfSeptemberIllness[dfSeptemberIllness['State'] == 'California']
dfCaliforniaOctoberCases = dfOctoberIllness[dfOctoberIllness['State'] == 'California']
dfCaliforniaNovemberCases = dfNovemberIllness[dfNovemberIllness['State'] == 'California']
dfCaliforniaDecemberCases = dfDecemberIllness[dfDecemberIllness['State'] == 'California']

#sum cases each month
SumCaliforniaJanuary = dfCaliforniaJanuaryCases['Illnesses'].sum()
SumCaliforniaFebruary = dfCaliforniaFebruaryCases['Illnesses'].sum()
SumCaliforniaMarch = dfCaliforniaMarchCases['Illnesses'].sum()
SumCaliforniaApril = dfCaliforniaAprilCases['Illnesses'].sum()
SumCaliforniaMay = dfCaliforniaMayCases['Illnesses'].sum()
SumCaliforniaJune = dfCaliforniaJuneCases['Illnesses'].sum()
SumCaliforniaJuly = dfCaliforniaJulyCases['Illnesses'].sum()
SumCaliforniaAugust = dfCaliforniaAugustCases['Illnesses'].sum()
SumCaliforniaSeptember = dfCaliforniaSeptemberCases['Illnesses'].sum()
SumCaliforniaOctober = dfCaliforniaOctoberCases['Illnesses'].sum()
SumCaliforniaNovember = dfCaliforniaNovemberCases['Illnesses'].sum()
SumCaliforniaDecember = dfCaliforniaDecemberCases['Illnesses'].sum()

#cases in minnesota per month
dfMinnesotaJanuaryCases = dfJanuaryIllness[dfJanuaryIllness['State'] == 'Minnesota']
dfMinnesotaFebruaryCases = dfFebruaryIllness[dfFebruaryIllness['State'] == 'Minnesota']
dfMinnesotaMarchCases = dfMarchIllness[dfMarchIllness['State'] == 'Minnesota']
dfMinnesotaAprilCases = dfAprilIllness[dfAprilIllness['State'] == 'Minnesota']
dfMinnesotaMayCases = dfMayIllness[dfMayIllness['State'] == 'Minnesota']
dfMinnesotaJuneCases = dfJuneIllness[dfJuneIllness['State'] == 'Minnesota']
dfMinnesotaJulyCases = dfJulyIllness[dfJulyIllness['State'] == 'Minnesota']
dfMinnesotaAugustCases = dfAugustIllness[dfAugustIllness['State'] == 'Minnesota']
dfMinnesotaSeptemberCases = dfSeptemberIllness[dfSeptemberIllness['State'] == 'Minnesota']
dfMinnesotaOctoberCases = dfOctoberIllness[dfOctoberIllness['State'] == 'Minnesota']
dfMinnesotaNovemberCases = dfNovemberIllness[dfNovemberIllness['State'] == 'Minnesota']
dfMinnesotaDecemberCases = dfDecemberIllness[dfDecemberIllness['State'] == 'Minnesota']

#sum cases each month
SumMinnesotaJanuary = dfMinnesotaJanuaryCases['Illnesses'].sum()
SumMinnesotaFebruary = dfMinnesotaFebruaryCases['Illnesses'].sum()
SumMinnesotaMarch = dfMinnesotaMarchCases['Illnesses'].sum()
SumMinnesotaApril = dfMinnesotaAprilCases['Illnesses'].sum()
SumMinnesotaMay = dfMinnesotaMayCases['Illnesses'].sum()
SumMinnesotaJune = dfMinnesotaJuneCases['Illnesses'].sum()
SumMinnesotaJuly = dfMinnesotaJulyCases['Illnesses'].sum()
SumMinnesotaAugust = dfMinnesotaAugustCases['Illnesses'].sum()
SumMinnesotaSeptember = dfMinnesotaSeptemberCases['Illnesses'].sum()
SumMinnesotaOctober = dfMinnesotaOctoberCases['Illnesses'].sum()
SumMinnesotaNovember = dfMinnesotaNovemberCases['Illnesses'].sum()
SumMinnesotaDecember = dfMinnesotaDecemberCases['Illnesses'].sum()

#make df with ca and mn sums each month
dfCasesPerMonth = pd.DataFrame([('January', SumCaliforniaJanuary, SumMinnesotaJanuary),
                                ('February', SumCaliforniaFebruary, SumMinnesotaFebruary),
                                ('March', SumCaliforniaMarch, SumMinnesotaMarch),
                                ('April', SumCaliforniaApril, SumMinnesotaApril),
                                ('May', SumCaliforniaMay, SumMinnesotaMay),
                                ('June', SumCaliforniaJune, SumMinnesotaJune),
                                ('July', SumCaliforniaJuly, SumMinnesotaJuly),
                                ('August', SumCaliforniaAugust, SumMinnesotaAugust),
                                ('September', SumCaliforniaSeptember, SumMinnesotaSeptember),
                                ('October', SumCaliforniaOctober, SumMinnesotaOctober),
                                ('November', SumCaliforniaNovember, SumMinnesotaNovember),
                                ('December', SumCaliforniaDecember, SumMinnesotaDecember)],
                               columns = ['Month', 'California', 'Minnesota'])

#retreiving ca and mn population each year
CaliforniaPop2010 = int(pop2010.loc[pop2010['NAME'] == 'California', 'POPESTIMATE2010'])
CaliforniaPop2011 = int(pop2011.loc[pop2011['NAME'] == 'California', 'POPESTIMATE2011'])
CaliforniaPop2012 = int(pop2012.loc[pop2012['NAME'] == 'California', 'POPESTIMATE2012'])
CaliforniaPop2013 = int(pop2013.loc[pop2013['NAME'] == 'California', 'POPESTIMATE2013'])
CaliforniaPop2014 = int(pop2014.loc[pop2014['NAME'] == 'California', 'POPESTIMATE2014'])
CaliforniaPop2015 = int(pop2015.loc[pop2015['NAME'] == 'California', 'POPESTIMATE2015'])

MinnesotaPop2010 = int(pop2010.loc[pop2010['NAME'] == 'Minnesota', 'POPESTIMATE2010'])
MinnesotaPop2011 = int(pop2011.loc[pop2011['NAME'] == 'Minnesota', 'POPESTIMATE2011'])
MinnesotaPop2012 = int(pop2012.loc[pop2012['NAME'] == 'Minnesota', 'POPESTIMATE2012'])
MinnesotaPop2013 = int(pop2013.loc[pop2013['NAME'] == 'Minnesota', 'POPESTIMATE2013'])
MinnesotaPop2014 = int(pop2014.loc[pop2014['NAME'] == 'Minnesota', 'POPESTIMATE2014'])
MinnesotaPop2015 = int(pop2015.loc[pop2015['NAME'] == 'Minnesota', 'POPESTIMATE2015'])

#calculating mean pop
CaliforniaMeanPop = (CaliforniaPop2010 + CaliforniaPop2011 + CaliforniaPop2012 +
                     CaliforniaPop2013 + CaliforniaPop2014 + CaliforniaPop2015) / 6

MinnesotaMeanPop = (MinnesotaPop2010 + MinnesotaPop2011 + MinnesotaPop2012 +
                     MinnesotaPop2013 + MinnesotaPop2014 + MinnesotaPop2015) / 6

#calculating cases per person
dfCasesPerMonth['California Cases Per Population'] = dfCasesPerMonth['California'] / CaliforniaMeanPop
dfCasesPerMonth['Minnesota Cases Per Population'] = dfCasesPerMonth['Minnesota'] / MinnesotaMeanPop

#calculating cases per person adj by population
dfCasesPerMonth['California Cases Per 100,000 People'] = dfCasesPerMonth['California Cases Per Population'] * 100000
dfCasesPerMonth['Minnesota Cases Per 100,000 People'] = dfCasesPerMonth['Minnesota Cases Per Population'] * 100000

#convert to csv
dfCasesPerMonth.to_csv('ca mn cases per month.csv')

#retrieving population values from each year
pop2010clean = dfpopclean[['POPESTIMATE2010']]
pop2011clean = dfpopclean[['POPESTIMATE2011']]
pop2012clean = dfpopclean[['POPESTIMATE2012']]
pop2013clean = dfpopclean[['POPESTIMATE2013']]
pop2014clean = dfpopclean[['POPESTIMATE2014']]
pop2015clean = dfpopclean[['POPESTIMATE2015']]

#making list of population values
listpop2010clean = pop2010clean.values.tolist()
listpop2011clean = pop2011clean.values.tolist()
listpop2012clean = pop2012clean.values.tolist()
listpop2013clean = pop2013clean.values.tolist()
listpop2014clean = pop2014clean.values.tolist()
listpop2015clean = pop2015clean.values.tolist()

#using merge1 function to make list of tuples in order by state and population
TotalPopByState = merge1(state_list_clean, listpop2010clean, listpop2011clean, listpop2012clean, listpop2013clean,
                         listpop2014clean, listpop2015clean)

#turning list into df and changing numbers from strings to int
dfTotalPopByState = pd.DataFrame(TotalPopByState, columns = ['State', '2010', '2011', '2012', '2013', '2014', '2015'])
dfTotalPopByState['2010'] = dfTotalPopByState['2010'].str[0]
dfTotalPopByState['2011'] = dfTotalPopByState['2011'].str[0]
dfTotalPopByState['2012'] = dfTotalPopByState['2012'].str[0]
dfTotalPopByState['2013'] = dfTotalPopByState['2013'].str[0]
dfTotalPopByState['2014'] = dfTotalPopByState['2014'].str[0]
dfTotalPopByState['2015'] = dfTotalPopByState['2015'].str[0]

#calculating average population by state
dfTotalPopByState['Average Population'] = (dfTotalPopByState['2010'] + dfTotalPopByState['2011'] + dfTotalPopByState['2012'] +
                                           dfTotalPopByState['2013'] + dfTotalPopByState['2014'] + dfTotalPopByState['2015']) / 6

#converting to csv
dfTotalPopByState.to_csv('population by state 2010-2015.csv')

#converting to csv
dfCaliforniaAdjYears.to_csv('california cases 2010-2015.csv')
dfMinnesotaAdjYears.to_csv('minnesota cases 2010-2015.csv')

#finding ca and mn cases that contain restaurant
dfCaliforniaRestaurant = dfCaliforniaAdjYears[dfCaliforniaAdjYears['Location'].str.contains('Restaurant')]
dfMinnesotaRestaurant = dfMinnesotaAdjYears[dfMinnesotaAdjYears['Location'].str.contains('Restaurant')]

#summing restaurant cases
CaliforniaRestaurantSum = dfCaliforniaRestaurant['Illnesses'].sum()
MinnesotaRestaurantSum = dfMinnesotaRestaurant['Illnesses'].sum()

#summing total illnesses in ca and mn
CaliforniaIllnessesSum = dfCaliforniaAdjYears['Illnesses'].sum()
MinnesotaIllnessesSum = dfMinnesotaAdjYears['Illnesses'].sum()

#making a df for ca and mn restaurant cases
dfRestaurantIllnesses = pd.DataFrame([('California', CaliforniaRestaurantSum, CaliforniaIllnessesSum),
                                    ('Minnesota', MinnesotaRestaurantSum, MinnesotaIllnessesSum)],
                                   columns = ['State', 'Restaurant Illnesses', 'Total Illnesses'])

#adding column calculating  % of illnesses from restaurants (restaurant illnesses / total)
dfRestaurantIllnesses['Percentage of Illnesses from Restaurants'] = (dfRestaurantIllnesses['Restaurant Illnesses'] 
                                                                      / dfRestaurantIllnesses['Total Illnesses'])
#converting to csv
dfRestaurantIllnesses.to_csv('ca mn restaurant.csv')

#converting to csv
dfCaliforniaAdjYears.to_csv('ca cases 2010-2015.csv')
dfMinnesotaAdjYears.to_csv('mn cases 2010-2015.csv')

#SALAD
#finding ca and mn cases that contain salad
dfCaliforniaSalad = dfCaliforniaAdjYears[dfCaliforniaAdjYears['Food'].str.contains(saladjoinwords)]
dfMinnesotaSalad = dfMinnesotaAdjYears[dfMinnesotaAdjYears['Food'].str.contains(saladjoinwords)]

#summing Salad cases
CaliforniaSaladSum = dfCaliforniaSalad['Illnesses'].sum()
MinnesotaSaladSum = dfMinnesotaSalad['Illnesses'].sum()

#making a df for ca and mn Salad cases
dfSaladIllnesses = pd.DataFrame([('California', CaliforniaSaladSum, CaliforniaIllnessesSum),
                                    ('Minnesota', MinnesotaSaladSum, MinnesotaIllnessesSum)],
                                   columns = ['State', 'Salad Illnesses', 'Total Illnesses'])

#adding column calculating  % of illnesses from Salads (Salad illnesses / total)
dfSaladIllnesses['Percentage of Illnesses from Salad'] = (dfSaladIllnesses['Salad Illnesses'] 
                                                                      / dfSaladIllnesses['Total Illnesses'])
#converting to csv
dfSaladIllnesses.to_csv('ca mn Salad.csv')

#Beef
#finding ca and mn cases that contain Beef
dfCaliforniaBeef = dfCaliforniaAdjYears[dfCaliforniaAdjYears['Food'].str.contains(beefjoinwords)]
dfMinnesotaBeef = dfMinnesotaAdjYears[dfMinnesotaAdjYears['Food'].str.contains(beefjoinwords)]

#summing Beef cases
CaliforniaBeefSum = dfCaliforniaBeef['Illnesses'].sum()
MinnesotaBeefSum = dfMinnesotaBeef['Illnesses'].sum()

#making a df for ca and mn Beef cases
dfBeefIllnesses = pd.DataFrame([('California', CaliforniaBeefSum, CaliforniaIllnessesSum),
                                    ('Minnesota', MinnesotaBeefSum, MinnesotaIllnessesSum)],
                                   columns = ['State', 'Beef Illnesses', 'Total Illnesses'])

#adding column calculating  % of illnesses from Beefs (Beef illnesses / total)
dfBeefIllnesses['Percentage of Illnesses from Beef'] = (dfBeefIllnesses['Beef Illnesses'] 
                                                                      / dfBeefIllnesses['Total Illnesses'])
#converting to csv
dfBeefIllnesses.to_csv('ca mn Beef.csv')

#Pork
#finding ca and mn cases that contain Pork
dfCaliforniaPork = dfCaliforniaAdjYears[dfCaliforniaAdjYears['Food'].str.contains(porkjoinwords)]
dfMinnesotaPork = dfMinnesotaAdjYears[dfMinnesotaAdjYears['Food'].str.contains(porkjoinwords)]

#summing Pork cases
CaliforniaPorkSum = dfCaliforniaPork['Illnesses'].sum()
MinnesotaPorkSum = dfMinnesotaPork['Illnesses'].sum()

#making a df for ca and mn Pork cases
dfPorkIllnesses = pd.DataFrame([('California', CaliforniaPorkSum, CaliforniaIllnessesSum),
                                    ('Minnesota', MinnesotaPorkSum, MinnesotaIllnessesSum)],
                                   columns = ['State', 'Pork Illnesses', 'Total Illnesses'])

#adding column calculating  % of illnesses from Porks (Pork illnesses / total)
dfPorkIllnesses['Percentage of Illnesses from Pork'] = (dfPorkIllnesses['Pork Illnesses'] 
                                                                      / dfPorkIllnesses['Total Illnesses'])
#converting to csv
dfPorkIllnesses.to_csv('ca mn Pork.csv')


#Chicken
#finding ca and mn cases that contain Chicken
dfCaliforniaChicken = dfCaliforniaAdjYears[dfCaliforniaAdjYears['Food'].str.contains(chickenjoinwords)]
dfMinnesotaChicken = dfMinnesotaAdjYears[dfMinnesotaAdjYears['Food'].str.contains(chickenjoinwords)]

#summing Chicken cases
CaliforniaChickenSum = dfCaliforniaChicken['Illnesses'].sum()
MinnesotaChickenSum = dfMinnesotaChicken['Illnesses'].sum()

#making a df for ca and mn Chicken cases
dfChickenIllnesses = pd.DataFrame([('California', CaliforniaChickenSum, CaliforniaIllnessesSum),
                                    ('Minnesota', MinnesotaChickenSum, MinnesotaIllnessesSum)],
                                   columns = ['State', 'Chicken Illnesses', 'Total Illnesses'])

#adding column calculating  % of illnesses from Chickens (Chicken illnesses / total)
dfChickenIllnesses['Percentage of Illnesses from Chicken'] = (dfChickenIllnesses['Chicken Illnesses'] 
                                                                      / dfChickenIllnesses['Total Illnesses'])
#converting to csv
dfChickenIllnesses.to_csv('ca mn Chicken.csv')


#Fish
#finding ca and mn cases that contain Fish
dfCaliforniaFish = dfCaliforniaAdjYears[dfCaliforniaAdjYears['Food'].str.contains(fishjoinwords)]
dfMinnesotaFish = dfMinnesotaAdjYears[dfMinnesotaAdjYears['Food'].str.contains(fishjoinwords)]

#summing Fish cases
CaliforniaFishSum = dfCaliforniaFish['Illnesses'].sum()
MinnesotaFishSum = dfMinnesotaFish['Illnesses'].sum()

#making a df for ca and mn Fish cases
dfFishIllnesses = pd.DataFrame([('California', CaliforniaFishSum, CaliforniaIllnessesSum),
                                    ('Minnesota', MinnesotaFishSum, MinnesotaIllnessesSum)],
                                   columns = ['State', 'Fish Illnesses', 'Total Illnesses'])

#adding column calculating  % of illnesses from Fishs (Fish illnesses / total)
dfFishIllnesses['Percentage of Illnesses from Fish'] = (dfFishIllnesses['Fish Illnesses'] 
                                                                      / dfFishIllnesses['Total Illnesses'])
#converting to csv
dfFishIllnesses.to_csv('ca mn Fish.csv')