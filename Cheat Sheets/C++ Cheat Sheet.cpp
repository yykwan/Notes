C++ Cheat Sheet
1. Core Language Features
    - Basic Structure
        #include <iostream>  // Include standard I/O library
        using namespace std; // Allow use of names from std without prefix

        int main() {         // Entry point of every C++ program
            cout << "Hello, World!" << endl; // 'cout' prints to console
            return 0;        // Return 0 indicates successful execution
        }
    - Variables & Data Types
        int age = 25;               // Integer (whole numbers)
        float pi = 3.14f;           // Single-precision floating point
        double precise_pi = 3.14159; // Double-precision floating point
        char grade = 'A';           // Single character
        bool is_cpp_fun = true;     // Boolean (true/false)

        // Type modifiers
        unsigned int positive_only = 100; // Only positive integers
        short small_int = 32767;          // Smaller integer range
        long big_int = 2147483647L;       // Larger integer range
        long long huge_int = 9e18;        // Very large integer

        // C++11 type inference
        auto automatic_type = 42;         // Compiler deduces type as int
        auto precise_auto = 3.14159;      // Deduces as double
    - Operators
        // Arithmetic operators
        int sum = 5 + 3;   // Addition
        int diff = 5 - 3;  // Subtraction
        int prod = 5 * 3;  // Multiplication
        int quot = 5 / 3;  // Integer division (result: 1)
        double div = 5.0 / 3.0; // Floating-point division
        int mod = 5 % 3;   // Modulus (remainder)

        // Compound assignment
        int x = 5;
        x += 3;  // Equivalent to x = x + 3
        x *= 2;  // Equivalent to x = x * 2

        // Bitwise operations (for low-level manipulation)
        unsigned char flags = 0b00001101; // Binary literal (C++14)
        flags = flags << 2; // Left shift (result: 00110100)
        flags = flags | 0b00000010; // Bitwise OR (set bit)

2. Control Flow
    - Conditionals
        // Basic if-else
        if (temperature > 30) {
            cout << "It's hot!" << endl;
        } else if (temperature > 20) {
            cout << "It's warm" << endl;
        } else {
            cout << "It's cool" << endl;
        }

        // Switch-case (for multiple discrete values)
        switch (day_of_week) {
            case 1: cout << "Monday"; break;
            case 2: cout << "Tuesday"; break;
            // ... other cases ...
            default: cout << "Weekend"; // Default case
        }
    - Loops
        // For loop (when iterations are known)
        for (int i = 0; i < 10; i++) {
            cout << i << " "; // Prints 0 through 9
        }

        // Range-based for loop (C++11)
        vector<int> nums = {1, 2, 3};
        for (int num : nums) {  // Iterate through container
            cout << num << " ";
        }

        // While loop (condition checked before)
        int count = 0;
        while (count < 5) {
            cout << count++ << " ";
        }

        // Do-while (condition checked after)
        do {
            cout << "This runs at least once";
        } while (false);

3. Functions
    - Function Basics
        // Function declaration (prototype)
        double calculate_circle_area(double radius);

        // Function definition
        double calculate_circle_area(double radius) {
            return 3.14159 * radius * radius;
        }

        // Function call
        double area = calculate_circle_area(5.0);
    - Advanced Function Features
        // Default arguments
        void log_message(string msg, bool error = false) {
            if (error) cerr << "ERROR: " << msg;
            else cout << "LOG: " << msg;
        }

        // Function overloading
        void print(int num) { cout << "Integer: " << num; }
        void print(string str) { cout << "String: " << str; }

        // Pass by reference (modify original)
        void increment(int &num) { num++; }

        // Lambda functions (C++11)
        auto square = [](int x) { return x * x; };
        int result = square(5); // Returns 25
    
4. Object-Oriented Programming (OOP)
    - Classes & Objects
        class Rectangle {
        private:    // Accessible only within class
            double width, height;
            
        public:     // Public interface
            // Constructor
            Rectangle(double w, double h) : width(w), height(h) {}
            
            // Member function
            double area() const { return width * height; }
            
            // Setter with validation
            void setWidth(double w) { 
                if (w > 0) width = w; 
            }
            
            // Getter
            double getWidth() const { return width; }
        };

        // Usage
        Rectangle rect(10, 20);
        cout << "Area: " << rect.area();
    - Inheritance & Polymorphism
        class Shape {           // Base class
        public:
            virtual void draw() const = 0; // Pure virtual function
            virtual ~Shape() {} // Virtual destructor
        };

        class Circle : public Shape { // Derived class
            double radius;
        public:
            void draw() const override { // Override base method
                cout << "Drawing circle with radius " << radius;
            }
        };

        // Polymorphic usage
        Shape* shape = new Circle();
        shape->draw(); // Calls Circle's draw()
        delete shape;  // Calls correct destructor

5. Standard Template Library (STL)
    - Containers
        // Vector (dynamic array)
        vector<int> vec = {1, 2, 3};
        vec.push_back(4); // Add element
        vec.pop_back();   // Remove last element

        // Map (key-value pairs)
        map<string, int> ages;
        ages["Alice"] = 25; // Insert
        if (ages.count("Bob")) { // Check existence
            cout << ages["Bob"]; // Access
        }

        // Unordered_map (hash table)
        unordered_map<string, int> phonebook;
        phonebook["Emergency"] = 911;

        // Set (unique sorted elements)
        set<int> unique_nums = {3, 1, 4, 1};
        // Contains {1, 3, 4} automatically
    - Algorithms
        #include <algorithm>
        vector<int> nums = {5, 3, 1, 4, 2};

        // Sorting
        sort(nums.begin(), nums.end()); // Now {1, 2, 3, 4, 5}

        // Searching
        auto it = find(nums.begin(), nums.end(), 3);
        if (it != nums.end()) cout << "Found at position " << it - nums.begin();

        // Transform (apply function to all elements)
        vector<int> squares;
        transform(nums.begin(), nums.end(), back_inserter(squares),
                [](int x) { return x * x; });
    
6. Memory Management
    - Smart Pointers
        #include <memory>

        // Unique pointer (exclusive ownership)
        auto uptr = make_unique<int>(10);
        // uptr automatically deletes when out of scope

        // Shared pointer (reference counted)
        auto sptr = make_shared<int>(20);
        auto sptr2 = sptr; // Both point to same object
        // Deleted when last reference goes away

        // Weak pointer (non-owning reference)
        weak_ptr<int> wptr = sptr;
        if (auto temp = wptr.lock()) { // Convert to shared_ptr
            cout << *temp; // Safe to use
        }
    - Raw Pointers & Arrays
        // Dynamic allocation
        int* arr = new int[10]; // Allocate array
        delete[] arr;           // Must manually delete

        // C-style strings
        const char* str = "Hello";
        char buffer[100];       // Fixed-size character array
        strcpy(buffer, str);    // Copy string
    
7. Advanced Features
    - Templates
        // Function template
        template <typename T>
        T max(T a, T b) { return (a > b) ? a : b; }

        // Class template
        template <class T, int size>
        class Stack {
            T elements[size];
            // ... implementation ...
        };

        // Usage
        cout << max(5, 10);         // Uses int version
        Stack<double, 100> dStack;  // Double stack with size 100
    - Concurrency
        #include <thread>
        #include <mutex>

        mutex mtx; // For synchronization

        void thread_task(int id) {
            lock_guard<mutex> lock(mtx); // RAII lock
            cout << "Thread " << id << " running\n";
        }

        // Create and manage threads
        thread t1(thread_task, 1);
        thread t2(thread_task, 2);
        t1.join(); // Wait for threads to finish
        t2.join();
    - File I/O
        #include <fstream>

        // Writing to file
        ofstream outfile("data.txt");
        if (outfile.is_open()) {
            outfile << "Hello, File!" << endl;
            outfile.close();
        }

        // Reading from file
        ifstream infile("data.txt");
        string line;
        while (getline(infile, line)) {
            cout << line << endl;
        }

8. Modern C++ (C++11/14/17/20)
    - New Features
        // Structured bindings (C++17)
        auto [min, max] = minmax({5, 3, 8, 1});
        // min=1, max=8

        // Initializer lists
        vector<int> v = {1, 2, 3}; // Since C++11

        // constexpr functions (compile-time evaluation)
        constexpr int square(int x) { return x * x; }
        int array[square(5)]; // Array size 25

        // Concepts (C++20)
        template <typename T>
        concept Numeric = is_arithmetic_v<T>;

        template <Numeric T>
        T add(T a, T b) { return a + b; }
    - Move Semantics
        // Move constructor/assignment
        class Buffer {
            size_t size;
            int* data;
        public:
            // Move constructor
            Buffer(Buffer&& other) noexcept 
                : size(other.size), data(other.data) {
                other.data = nullptr; // Steal resources
            }
            
            // Move assignment
            Buffer& operator=(Buffer&& other) noexcept {
                if (this != &other) {
                    delete[] data;   // Cleanup current
                    data = other.data; // Steal
                    size = other.size;
                    other.data = nullptr;
                }
                return *this;
            }
        };
