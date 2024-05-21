![readme_es6_data_manip](https://github.com/chloe0524/holbertonschool-web_back_end/assets/127857895/c64a4c1f-7a01-4985-b895-1284442e387a)

### :round_pushpin: 0. Basic list of objects
**Mandatory**

Create a function named `getListStudents` that returns an array of objects.

Each object should have three attributes:
- `id` (Number)
- `firstName` (String)
- `location` (String)

The array should contain the following students in order:
1. Guillaume, id: 1, location: San Francisco
2. James, id: 2, location: Columbia
3. Serena, id: 5, location: San Francisco


### :round_pushpin: 1. More mapping
**Mandatory**

Create a function `getListStudentIds` that returns an array of ids from a list of objects.

This function takes one argument, which is an array of objects—formatted the same as the array from the previous task.

If the argument is not an array, the function should return an empty array.

You must use the `map` function on the array.


### :round_pushpin: 2. Filter
**Mandatory**

Create a function `getStudentsByLocation` that returns an array of objects who are located in a specific city.

It should accept a list of students (from `getListStudents`) and a city (string) as parameters.

You must use the `filter` function on the array.


### :round_pushpin: 3. Reduce
**Mandatory**

Create a function `getStudentIdsSum` that returns the sum of all the student ids.

It should accept a list of students (from `getListStudents`) as a parameter.

You must use the `reduce` function on the array.


### :round_pushpin: 4. Combine
**Mandatory**

Create a function `updateStudentGradeByCity` that returns an array of students for a specific city with their new grade.

It should accept a list of students (from `getListStudents`), a city (String), and `newGrades` (Array of “grade” objects) as parameters.

`newGrades` is an array of objects with this format:
```javascript
{
  studentId: 31,
  grade: 78,
}
```

If a student doesn’t have a grade in `newGrades`, the final grade should be `N/A`.

You must use `filter` and `map` combined.


### :round_pushpin: 5. Typed Arrays
**Mandatory**

Create a function named `createInt8TypedArray` that returns a new `ArrayBuffer` with an `Int8` value at a specific position.

It should accept three arguments: `length` (Number), `position` (Number), and `value` (Number).

If adding the value is not possible, the error `Position outside range` should be thrown.


### :round_pushpin: 6. Set data structure
**Mandatory**

Create a function named `setFromArray` that returns a `Set` from an array.

It accepts an argument (Array, of any kind of element).


### :round_pushpin: 7. More set data structure
**Mandatory**

Create a function named `hasValuesFromArray` that returns a boolean if all the elements in the array exist within the set.

It accepts two arguments: a set (`Set`) and an array (`Array`).


### :round_pushpin: 8. Clean set
**Mandatory**

Create a function named `cleanSet` that returns a string of all the set values that start with a specific string (`startString`).

It accepts two arguments: a set (`Set`) and a `startString` (String).

When a value starts with `startString`, you only append the rest of the string. The string contains all the values of the set separated by `-`.


### :round_pushpin: 9. Map data structure
**Mandatory**

Create a function named `groceriesList` that returns a map of groceries with the following items (name, quantity):
- Apples, 10
- Tomatoes, 10
- Pasta, 1
- Rice, 1
- Banana, 5

### :round_pushpin: 10. More map data structure
**Mandatory**

Create a function named `updateUniqueItems` that returns an updated map for all items with an initial quantity of 1.

It should accept a map as an argument. The map it accepts for argument is similar to the map you create in the previous task.

For each entry of the map where the quantity is 1, update the quantity to 100. If updating the quantity is not possible (argument is not a map), the error `Cannot process` should be thrown.

