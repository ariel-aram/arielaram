# Ariel Aram's JavaScript Catalog

## Separate JS Setup

```html
<script src="script.js"></script>
```

## Internal JS Setup

```html
<script>

</script>
```

### Selectors

```js
document.getElementById("id") // Select by id
document.getElementsByClassName("class") // Select by class name
document.getElementsByTagName("tag") // Select by tag name
document.querySelector("selector") // Select by css selector
document.querySelectorAll("selector") // Select by css selector
```

### Text

```js
console.log("Hello World"); // console.log is used to print something on the console

// Change text
document.getElementById("id").textContent = "Hello World"; // changes text content
document.getElementById("id").innerHTML = "Hello World"; // changes inner html
```

### Events

```js
/* 
    onclick
    onchange
    onmouseover
    onmouseout
    onkeydown
    onkeyup
    onkeypress
    onload
    onerror
    onsubmit
*/
document.getElementById("id").addEventListener("click", function() {
    console.log("Hello World");
});
```

### Variables

```js
let variableName = "variableValue"; // Can be changed later
const variableName = "variableValue"; // Cannot be changed later
var variableName = "variableValue"; // Can be changed later
```

### Functions

```js
/* 
    functionName = name of the function
    ()
*/
function functionName() {
    console.log("Hello World");
}
```

### Arrow Functions

```js
/* 
    functionName = name of the function
    () => = arrow function
*/
const functionName = () => {
    console.log("Hello World");
};
```

### Arrays

```js
const arrayName = ["arrayValue1", "arrayValue2", "arrayValue3"]; // An array is a list of values

arrayName.push("arrayValue4"); // Add to end
arrayName.pop(); // Remove from end
arrayName.shift(); // Remove from beginning
arrayName.unshift("arrayValue0"); // Add to beginning
arrayName.splice(index, deleteCount, item1, item2, ...); // Add/Remove items
arrayName.slice(start, end); // Create a new array
```

### Objects

```js
/* An object is a collection of key-value pairs */
const objectName = {
    key1: "value1",
    key2: "value2",
    key3: "value3"
};

objectName.key1 = "newValue1"; // Change value
delete objectName.key1; // Delete property
```
