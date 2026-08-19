# Ariel Aram's CSS Catalog

## Separate CSS Setup

```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

## Internal CSS Setup

```html
<head>
    <style>

    </style>
</head>
```

## Inline CSS Setup

```html
<tag style="">
```

### Syntax

```css
selector {
    property: value;
}
```

### Square Properties

```css
.square {
    border: 3px solid blue; /* Border width, style, and color */
    width: 100px; /* width */
    height: 100px; /* height */
    margin: 10px; /* margin */
    background-color: blueviolet; /* background-color */
    position: absolute; /* absolute positioning */
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', 'Arial', 'sans-serif'; /* font-family */
}
```

### Styling

```css
/* 
   left, right, top, bottom = absolute positioning 
   display: block = make the element into a block
*/
.square2 {
    right: 0px;
    bottom: 0px;
    background-color: crimson;
}
```

### Images

```css
.image {
    background: url("stonks.jpg") no-repeat; /* no-repeat = don't repeat the image */
    width: 200px; /* width */
    height: 200px; /* height */
    display: block; /* block = makes the image into a block */
    background-size: contain; /* contain = makes the image fit in the container */
}

.image:hover {
    background-position: 0px 50px; /* Moves the image 50px down */
}

.image:active {
    background: url("notstonks.jpg") no-repeat; /* No repeat */
    width: 200px; /* width */
    height: 200px; /* height */
    background-position: 0px -20px; /* Moves the image 20px up */
}
```

### List

```css
.alternating {
    list-style: upper-alpha;
    font-size: 30px; /* font-size */
    color: brown; /* color */
    width: fit-content; /* width */
}

/* li:nth-child(odd) = odd number */
.alternating li:nth-child(odd) {
    background-color: beige; /* beige background color */
}

/* li:nth-child(even) = even number */
.alternating li:nth-child(even) {
    background-color: coral; /* coral background color */
}

/* li:hover = When the mouse is over the element */
.alternating li:hover { 
    font-weight: bolder; /* Bolder font weight */
}
```

### Problem

```css
.problem {
    background: red;
    color: beige;
}
```

### Variables

```css
:root { /* Global variables */
    --primary-color: #4CAF50; /* primary color */
    --secondary-color: #2196F3; /* secondary color */
    --accent-color: #FF9800; /* accent color */
}

.variable-color {
    background-color: var(--primary-color);
    color: var(--secondary-color);
}
```

- :--property-name (Variable name)
- var(--property-name) (Use of variable)
