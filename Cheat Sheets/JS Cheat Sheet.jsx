// JavaScript Cheat Sheet (including React.js and Node.js)
import React from "react";
1. JavaScript Basics
    - Variables & Data Types
        // Variables
        let name = "John"; // Block-scoped
        var age = 30;      // Function-scoped (avoid in modern JS)
        const PI = 3.14;   // Constant

        // Data Types
        let num = 10;          // Number
        let str = "Hello";     // String
        let bool = true;       // Boolean
        let arr = [1, 2, 3];  // Array
        let obj = { key: "value" }; // Object
        let nothing = null;    // Null
        let notDefined;        // Undefined
    - Operators
        // Arithmetic
        let sum = 5 + 3;   // 8
        let mod = 10 % 3;   // 1 (Modulus)

        // Comparison
        console.log(5 == "5");  // true (loose equality)
        console.log(5 === "5"); // false (strict equality)

        // Logical
        console.log(true && false); // AND → false
        console.log(true || false); // OR → true
        console.log(!true);         // NOT → false
    - Control Flow
        // If-Else
        if (age >= 18) {
        console.log("Adult");
        } else {
        console.log("Minor");
        }

        // Ternary Operator
        let status = (age >= 18) ? "Adult" : "Minor";

        // Switch
        switch (day) {
        case "Monday":
            console.log("Work day");
            break;
        default:
            console.log("Weekend");
        }

        // Loops
        for (let i = 0; i < 5; i++) { console.log(i); }
        while (condition) { /* ... */ }
        for (let item of arr) { console.log(item); } // For-of (arrays)
        for (let key in obj) { console.log(key); }   // For-in (objects)
    
2. Functions
    // Function Declaration
    function greet(name) {
    return `Hello, ${name}!`;
    }

    // Arrow Function (ES6+)
    const greet = (name) => `Hello, ${name}!`;

    // Default Parameters
    const greet = (name = "Guest") => `Hello, ${name}!`;

    // Rest Parameters
    function sum(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
    }

    // Callback Functions
    function fetchData(callback) {
    setTimeout(() => callback("Data received"), 1000);
    }
    fetchData((data) => console.log(data));

3. Arrays & Objects
    - Array Methods
        let nums = [1, 2, 3];

        nums.push(4);       // Add to end → [1, 2, 3, 4]
        nums.pop();         // Remove last → [1, 2, 3]
        nums.shift();       // Remove first → [2, 3]
        nums.unshift(0);    // Add to start → [0, 2, 3]

        nums.map(num => num * 2);  // [0, 4, 6]
        nums.filter(num => num > 2); // [4, 6]
        nums.reduce((acc, num) => acc + num, 0); // Sum: 10
    - Object Methods 
        const person = { name: "Alice", age: 25 };

        Object.keys(person);    // ["name", "age"]
        Object.values(person);  // ["Alice", 25]
        Object.entries(person); // [["name", "Alice"], ["age", 25]]

        // Destructuring
        const { name, age } = person;
        console.log(name); // "Alice"

4. Asynchronous JavaScript
    - Promises 
        const fetchData = () => {
            return new Promise((resolve, reject) => {
                setTimeout(() => resolve("Data fetched!"), 1000);
            });
            };

            fetchData()
            .then(data => console.log(data))
            .catch(err => console.error(err));
    - Async/Await
        async function getData() {
            try {
                const data = await fetchData();
                console.log(data);
            } catch (err) {
                console.error(err);
            }
            }
    - Fetch API (HTTP Requests)
        fetch("https://api.example.com/data")
            .then(res => res.json())
            .then(data => console.log(data))
            .catch(err => console.error(err));
    
5. React (Frontend Framework)
    - Components 
        // Functional Component
        function Greet({ name }) {
        return <h1>Hello, {name}!</h1>;
        }

        // Class Component
        class Counter extends React.Component {
        state = { count: 0 };
        increment = () => this.setState({ count: this.state.count + 1 });
        render() {
            return (
            <div>
                <p>Count: {this.state.count}</p>
                <button onClick={this.increment}>+</button>
            </div>
            );
        }
        }
    - Hooks (React 16.8+)
        import { useState, useEffect } from "react";

        function Counter() {
        const [count, setCount] = useState(0);

        useEffect(() => {
            console.log("Component mounted/updated");
            return () => console.log("Cleanup");
        }, [count]); // Runs when `count` changes

        return (
            <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>+</button>
            </div>
        );
        }
    - React Router (Naviagation)
        import { BrowserRouter, Route, Link } from "react-router-dom";

        function App() {
        return (
            <BrowserRouter>
            <nav>
                <Link to="/">Home</Link>
                <Link to="/about">About</Link>
            </nav>
            <Route exact path="/" component={Home} />
            <Route path="/about" component={About} />
            </BrowserRouter>
        );
        }
    
6. Node.js (Backend JavaScript)
    - Basic HTTP Server
        const http = require("http");

        const server = http.createServer((req, res) => {
        res.writeHead(200, { "Content-Type": "text/plain" });
        res.end("Hello, Node.js!");
        });

        server.listen(3000, () => console.log("Server running on port 3000"));
    - Express.js (Web Framework)
        const express = require("express");
        const app = express();

        // Middleware
        app.use(express.json());

        // Routes
        app.get("/", (req, res) => res.send("Home Page"));
        app.post("/api/data", (req, res) => res.json(req.body));

        app.listen(3000, () => console.log("Server started"));
    - File System (fs)
        const fs = require("fs");

        // Read file
        fs.readFile("file.txt", "utf8", (err, data) => {
        if (err) throw err;
        console.log(data);
        });

        // Write file
        fs.writeFile("file.txt", "Hello Node!", (err) => {
        if (err) throw err;
        console.log("File saved!");
        });
    
7. Error Handling 
    // Try-Catch
    try {
    nonExistentFunction();
    } catch (err) {
    console.error("Error:", err.message);
    }

    // Custom Errors
    class ValidationError extends Error {
    constructor(message) {
        super(message);
        this.name = "ValidationError";
    }
    }

    throw new ValidationError("Invalid input!");

8. ES6+ Features
    - Template Literals 
        const name = "Alice";
        console.log(`Hello, ${name}!`); // "Hello, Alice!"
    - Spread & Rest Operators 
        // Spread (arrays/objects)
        const arr1 = [1, 2];
        const arr2 = [...arr1, 3]; // [1, 2, 3]

        const obj1 = { a: 1 };
        const obj2 = { ...obj1, b: 2 }; // { a: 1, b: 2 }

        // Rest (function parameters)
        function sum(...nums) {
        return nums.reduce((acc, num) => acc + num, 0);
        }
    - Modules (Import/Export)
        // Export (module.js)
        export const PI = 3.14;
        export function greet(name) { return `Hello, ${name}!`; }

        // Import (app.js)
        import { PI, greet } from "./module.js";
        console.log(greet("Alice"));
