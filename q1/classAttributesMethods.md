# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/classObjectUML.md)
## Design Revision
- Added visibilities to the properties
- Fixed Methods
- Added needswater method

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| + name | string | public | It really doesn't matter much and can be changed anytime that it doesnt need that much protection |
| + color |	string	| public | It is to easily identify and customize your plant |
| - height	| integer	| private | The plant's height needs to be protected and only necessarily changed when needed to avoid confusion| 
| - waterstatus	| boolean	| private | This needs to be protected to have an accurate monitoring |

## Updated UML Class Diagram
[Class Diagram](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/images/classDiagram.png)
## Python Implementation
[View Python Source](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/classImplementation.py)
## Test Run
[Test Run](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/images/classTestRun.png)
## Object Diagram
[Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
I chose the attributes height and water status to be private since I don't want the data to be easily changed and have multiple errors. These two are the most important parts so I want their data to be protected to ensure a precise documentation or recording of information.

### Which method changes the state of your object?
The method grow(amount: float) changes the height of the plant, providing the necessary the data needed to monitor the plant's state of growth.

### How did your two objects demonstrate that instances are independent?
I only used the .grow() method on Basil only modified that specific object 1(Basil). It had no effect on Cactus(object2), which did not increase by 2 inches and stayed at 3 inches.

### What is the difference between your class diagram and your object diagram?
My class diagram only focuses on the general terms and doesn't have any specific values. Meanwhile, my object diagram actually has specific values to each object that reuses the class's property format. 
