# Advanced Class Relationships
## Previous Activities
[Class Atributes](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/classAttributesMethods.md)
[Class Relatioonships](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/classRelationships.md)
## Existing System Description:
1. What classes currently exist in your system?
Plants:
- It is a class where the user are able to grow, water and monitor whenever it needs water. Not only that but it also has a name, a color, and height that can grow. 

Garden: 
- It is a class where the user can store and remove plants in it's inventory. The Garden class has a Has-A association with the Plants class. Furthermore, the class Garden has a name, limited inventory space, and the cleanliness status.

2. What problem or limitation exists in your current design?
- The methods I have currently have in both my classes is not that useful and used to its full potential. The said methods and attributes are also repeated through out the classes and can be further improved.

## Inheritance Relationship
Parent: Plant

Child: Sunflower

Explanation: This is because Plants is a broad subject where it consists of different flowers, vegetables, fruits, trees, and shrubs. A Sunflower is a type of plants since it falls under flowers which is a type of plant.

## Inheritance UML
![Inheritance](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation/Weak HAS-A relationship

Class containing another object: GardenClass

Contained object: Plants 

Explanation: This is because Plants can live and exist even if Garden is deleted or removed.
## Advanced UML Diagram
![Advanced UML](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/images/advancedClassDiagram.png)
## Python Implementation
[Source Code](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/advancedRelationships.py)
## Test Run
![Test](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/images/advancedTestRun.png)
## Object Diagram
![Objects](https://github.com/cmsolano-spec/9siliconcs3/blob/main/q1/images/advancedObjectDiagram.png)

## Reflection
Answers:**
1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
- I chose the Inheritance relationship between Plants and Sunflower because a sunflower is a type of plant. Sunflowers has the basic characteristics of a plant, like its name, color, height, and water status. I also added an attribute where it tells you the quantity of the Sunflowers for easier management. This makes Sunflower a type and child of my parent class, Plants.

2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
- Inheritance allowed my Class Sunflower to get all of the attributes of the Plants class. I used super().__init__() so I don't have to write the same attribute again and again. This also lessen the wordiness of my code. 

3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
- My Class Garden and Class Plants relationship is Aggregation because a garden contains plants, but the plants can still exist separately with out without the garden. For example, basil and cactus objects can still exist even if the Garden is remove. This means that they have a weak HAS-A relationship.

4. What is the difference between Association from Part III and the advanced relationship you implemented?
- The Association from Part 3 OOPACT showed that Class Garden is connected to Plants because a garden can have plants. Meanwhile, in this partn I used a more specific relationship which is Aggregation. Aggregation explains that a Garden contains Plants while the Plants can still exist independently.

5. How does your design follow the DRY principle?
- My design follows the DRY principle by putting plant attributes and methods in the parent Plant class. Then I made another class, Sunflower, that can reuse the attributes name, color, height, and water status while adding its own attribute, which counts how many sunflowers there are. This reduces the wordiness of my code and makes it more efficient, especially when I have to make multiple classes.


