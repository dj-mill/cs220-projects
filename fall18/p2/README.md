# Project 2

In this project, you'll learn about creating and calling functions, arguments, return values and math module. To start, download these files (Note: right click on the links below, not the links above that only show a preview):

* [main.py](https://raw.githubusercontent.com/tylerharter/cs301-projects/master/fall18/p2/main.py)
* [project.py](https://raw.githubusercontent.com/tylerharter/cs301-projects/master/fall18/p2/project.py)
* [test.py](https://raw.githubusercontent.com/tylerharter/cs301-projects/master/fall18/p2/test.py)
* [area.csv](https://raw.githubusercontent.com/tylerharter/cs301-projects/master/fall18/p2/area.csv)
* [population.csv](https://raw.githubusercontent.com/tylerharter/cs301-projects/master/fall18/p2/population.csv)

You will change main.py and hand it in. You should not change test.py and project.py, and you should not hand them in; it's only purpose is to tell you your grade in advance.

After you've downloaded all the above 5 files to the same directory, open your terminal, navigate to that directory, and run the following:

```
python test.py
```

You should see the following output:
(Note: the python version may be different depending on the version of the python interpreter you use.)

```
Your Python version: Python 3.6.5

Running your program with this command: python3 main.py

RESULTS:
  Function test 1 (getMaximumLand): function getMaximumLand not found
  Function test 2 (getMaximumLand): function getMaximumLand not found
  Function test 3 (getMinimumPopulationDensity): function getMinimumPopulationDensity not found
  Function test 4 (getMinimumPopulationDensity): function getMinimumPopulationDensity not found
  Function test 5 (getMinimumPopulationDensity): function getMinimumPopulationDensity not found
  Function test 6 (predictPopulation): function predictPopulation not found
  Function test 7 (predictPopulation): function predictPopulation not found
  Function test 8 (predictPopulation): function predictPopulation not found
  Function test 9 (predictPopulation): function predictPopulation not found
  Function test 10 (predictPopulation): function predictPopulation not found
  Function test 11 (calcGrowthRate): function calcGrowthRate not found
  Function test 12 (calcGrowthRate): function calcGrowthRate not found
  Function test 13 (calcGrowthRate): function calcGrowthRate not found
  Function test 14 (calcGrowthRate): function calcGrowthRate not found
  Main function print test 1: PASS
  Main function print test 2: expected (5686986.0) but found (0)
  Main function print test 3: expected (86935.83) but found (0)
  Main function print test 4: expected (52.002450206414075) but found (0)
  Main function print test 5: expected (796039951.1495125) but found (0)
  Main function print test 6: expected (0.005853103209551789) but found (0)
Score: 5%
```

##  Introduction
We provide you with a data file containing information about 50 states in the United States. Our task for this assignment is to look at the table and try to answer the questions that follow. We are going to write a few functions in order to make these calculations.

The table below shows a **sample** from the dataset that we have.

<center>

| State | Area (mi²) | Population (2000) | Population (2010) | population (2014) |
|------|------|------|------|------|
|Wisconsin|65496.38 |5363675|5686986|5759432|
|Minnesota|86935.83 |44919479|5303925|5457125|
|Illinois|57913.55 |12419293|12830632|12882189|

</center>
In this project, we are interested in these following 4 questions:

1. What is the value of the maximum land area among any three given states?
2. What is the least value of population density among any three given states?
3. For a given state, what’s the predicted population in the given year? (The function will take in values of initial year, final year, growth rate and state name)
4. Between any two given years, what is the population growth rate of particular state?

### Provided Functions in Module project.py
We don’t require you to know how to read from data file so we have provided the following functions. Please make sure the data file area.csv and population.csv are in the same folder along with main.py.

**getArea(stateName)**

getArea function takes the name of one state as an argument and returns the area of this state.

```
>>> import project
>>> project.getArea("Wisconsin")
>>> 65496.38
```
**getPopulation(stateName, year)**

getPopulation function takes the name of one state and a year as arguments and returns the population of this state in this year.

```
>>> import project
>>> project.getPopulation("Wisconsin", 2000)
>>> 5363675
```

## Program Requirements
You will write **at least four(4)** functions with the following names and behaviors. You will also fix some lines in main function.

**Function 1: getMaximumLand(stateName1, stateName2, stateName3)**

Find the max value for land area among the three given area values which will be passed as parameters. To do this we can use the inbuilt [max()](https://docs.python.org/2/library/functions.html#max) function.

Example:

```
>>> getMaximumLand("Wisconsin", "Iowa", "Minnesota")
>>> 86935.83
```

**Function 2: getMinimumPopulationDensity(stateName1, stateName2, stateName3, year)**

Population density is measured as population per unit area.

The formula to calculate population density is:

Population Density = Population / Land Area (mi²)

For this function, you need to retrieve population and area values for the given states and calculate the density. We then find the min value of population density among the three values passed as parameters. To do this, we can use the inbuilt [min()](https://docs.python.org/2/library/functions.html#min) function.

Example:

```
>>> getMinimumPopulationDensity("Wisconsin", "Iowa", "Minnesota", 2000)
>>> 52.002450206414075
```

**Function 3: predictPopulation(stateName, yearA, yearB, growthRate = 0.1)**

Note: This function has a default argument growthRate. By default it should be 0.1.

We use the following formula for population growth prediction in this question: <img src="Population.png" alt="drawing" width="100"/>. Here,

 1. <img src="Pa.png" alt="drawing" width="15"/> is the population for the specific state in year *a*.
 2. <img src="Pb.png" alt="drawing" width="15"/> is the predicted population for the specific state in year *b*, *b* > *a*.
 3. *r* is the growth rate.
 4. *t* is the number of years between year *a* and the year *b*.

The function should take in the values for the state name, state growth rate and year *a* and year *b*. It should return the value of the predicted population in year *b*. To implement this function, You can use exp function in Python [math library](https://docs.python.org/3/library/math.html).

Example:

```
>>> predictPopulation("Wisconsin", 2000, 2010, 0.5)
>>> 796039951.1495125
>>> predictPopulation("Wisconsin", 2000, 2010)
>>> 14579980.286260068
```

**Function 4: calcGrowthRate(stateName, yearA, yearB)**

Use the same formula as above to calculate the growth rate. To do this, you can use the log function present in Python [math library](https://docs.python.org/3/library/math.html). (Hint: math.log(e ** (rt)) == rt, you need to rearrange the above formula to isolate *r*, the growth rate.)

Example:

```
>>> calcGrowthRate("Wisconsin", 2000, 2010)
>>> 0.005853103209551789
```

**Be careful to match these names and behaviors exactly. You may implement additional helper functions if you like, but you must have the specified functions.**
