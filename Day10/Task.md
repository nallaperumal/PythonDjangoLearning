# Assessment 2
## Object Oriented Programming

### Level 1:
- Define a class called ITemployee with name, age, position, salary as property
- create an object of type ITemployee and print the properties
- In the ITEmployee class, create a method call performWork() 
- this performWork() shall just print a string called "Develop Software And Deliver it"

### Level 2:
- Define another class called NonITemployee with name, age, position, salary as property and method called performWork()
- this performWork() shall just print a string called "Perform Security, Admin, Cleaning or supportive work"
 
### Level 3:
- Define an abstract class called employee with method called abstract method performWork()
- Both the ITemployee() and  NonITemployee() class should inherit this abstract base class and implement the method performWork()
- Create an object of type ITemployee and another object of type NonITemployee() and print the performWork()
 
#### Level 4:
- Define a class called Company with properties name, founded year and employee 
- During the creation of the company object, inject any of the Employee object into the constructor 
- Now, call the perfromWork method from the via company object

## Pandas
- Download the organizations sample data from datablist.com

### Level 1:
- using pandas, load the data and display it in the graph (using matplotlib)


### Level 2:
- Create some irregularities in the data like adding null, adding duplicate values
- Cleanse the data and save to a file
- Display only selected columns like: organization, year and number of employees

### Level 3:
- Display the aggregated results like sum, average with grouping by industry


### Level 4:
- Apply transformation by classifying the company into: big(>10,000 emp), medium(>1000 emp and <10,000 emp), small (<1000 emp)


