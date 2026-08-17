# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Claire Marie S. Olano
**Section:** 9-Siicon
**Last Name:** Olaño
**Date:** Date Completed

## Step 1: Identify the Big Problem
### Main Problem
The canteen is often crowded due to the slow and inefficient ways of handling. Some students take too long to decide what to order, no system to automatically calculate and give the change, and there is no system to track which food items are running out.

## Step 2: Identify three to four Sub-Problems
1. Some students take too long to decide what to order and hold up the line.
2. The cashier has to manually calculate totals and give change which can have human error and takes up some time.
3. There is no system to track each food quantity.

## Step 3: Apply Computational Thinking Skills
Sub-Problem | CT Skill | Example Solution
|---|---|---|
| Long ordering time | Abstraction | Make which items are available and remove unnecessary details that may confuse or distract the students from choosing what to order
| Change calculation | Algorithm Design | Make a program or an algorithm that adds all of the chosen items' price and minus that from the given payment to get the change.
| Food inventory tracker | Pattern Recognition | Track each item's inventory and get alerted when any of them reaches zero. 

## Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
### Selected Sub-Problem
2. The cashier has to manually calculate totals and give change which can have human error and takes up some time.

### Pseudocode
START
Ask user for items selected prices

Get the corresponding value

Compute the total results

Display results

Ask user for payment 

Compute the differences between results and payment

IF payment less than results THEN

   Ask user for the remaining money

ELSE

   Give the change

END

