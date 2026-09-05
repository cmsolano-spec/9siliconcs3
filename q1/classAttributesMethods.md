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
[Class Diagram](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/images/ClassDiagram.png)
## Python Implementation
[View Python Source](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/classImplementation.py)
## Test Run
[Test Run](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/images/images/classTestRun.png)
## Object Diagram
[Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
