//console.log("Hello World")
//var hello = "Hello from Node js Variable!"
//console.log(hello)

var path = require("path");

console.log (`Printing variable hello: ${hello}`);

console.log("directory name: " + _dirname);

console.log("directory and file name: " + _filename);

console.log("Using PATH module:");
console.log(`Hell from file ${path.basename(_filename)}`);

console.log(`Process args: ${process.argv}`)
