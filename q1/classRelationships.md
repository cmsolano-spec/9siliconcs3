# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/classObjectUML.md)
[Part II - Class Attributes and Methods](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/classAttributesMethods.md)

## Existing Class
Class: Plants 
Description: It is a class where different characteristics like its growth or when it needs water is stored.

## New Related Class
Class: Garden
Description: It is a class where plants are stored and taken care of. It has characteristics like to remove, clean, or add plants. 

## Association
Relationship: Has Relationship
Explanation: This is because a garden has plants in it. A garden isn't a plant and also doesn't inherits the plants attributes and methods. 

## Multiplicity
Multiplicity: One-to-Many
Explanation: A garden is a place where many plants can be stored and taken cared of. A space only containing a single plant isn't a garden. 

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
