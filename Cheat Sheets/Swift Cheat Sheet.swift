// Swift Cheat Sheet
1. Basic & Syntax
    - Hello World
        print("Hello, World!")
    - Variables & Constants
        var name = "John"  // Mutable variable
        let age = 30       // Immutable constant
    - Data Types
        let int: Int = 42
        let double: Double = 3.14
        let float: Float = 2.71
        let bool: Bool = true
        let str: String = "Swift"
        let char: Character = "S"
    - Type Conversion
        let numStr = "42"
        let num = Int(numStr)  // Optional Int?

        let pi = 3.14159
        let intPi = Int(pi)     // 3 (truncates)
    
2. Operators
    // Arithmetic
    let sum = 5 + 3       // 8
    let mod = 10 % 3       // 1

    // Comparison
    print(5 == 5)          // true
    print(5 != 3)          // true
    print(5 > 3)           // true

    // Logical
    print(true && false)   // false
    print(true || false)   // true
    print(!true)           // false

    // Nil-coalescing
    let username: String? = nil
    let displayName = username ?? "Guest"  // "Guest"

3. Control Flow
    - if else 
        if age >= 18 {
            print("Adult")
        } else {
            print("Minor")
        }
    - Ternary Operator 
        let status = age >= 18 ? "Adult" : "Minor"
    - Switch 
        switch weather {
        case "sunny":
            print("Wear sunscreen")
        case "rainy":
            print("Bring an umbrella")
        default:
            print("Enjoy your day")
        }
    - Loops 
        // For-in
        for i in 1...5 { print(i) }       // 1-5
        for i in 1..<5 { print(i) }      // 1-4

        // While
        var count = 0
        while count < 5 {
            print(count)
            count += 1
        }

        // Repeat-while (do-while)
        repeat {
            print(count)
            count -= 1
        } while count > 0

4. Collections
    - Arrays
        var fruits = ["Apple", "Banana"]
        fruits.append("Orange")      // Add
        fruits[1] = "Mango"         // Update
        let first = fruits[0]       // Access
        fruits.remove(at: 1)        // Remove

        // Iteration
        for fruit in fruits {
            print(fruit)
        }
    - Dictionaries
        var person = ["name": "John", "age": "30"]
        person["city"] = "NY"       // Add/Update
        let name = person["name"]   // Optional String?
        person.removeValue(forKey: "age")

        // Iteration
        for (key, value) in person {
            print("\(key): \(value)")
        }
    - Sets
        var colors: Set = ["Red", "Green"]
        colors.insert("Blue")       // Add
        colors.remove("Red")        // Remove
        print(colors.contains("Green")) // true       

5. Functions
    // Basic Function
    func greet(name: String) -> String {
        return "Hello, \(name)!"
    }

    // Parameter Labels
    func sendMessage(to recipient: String, from sender: String) {
        print("From \(sender) to \(recipient)")
    }

    // Default Parameters
    func multiply(_ a: Int, by b: Int = 2) -> Int {
        return a * b
    }

    // Variadic Parameters
    func sum(_ numbers: Int...) -> Int {
        return numbers.reduce(0, +)
    }

    // Closures
    let greetClosure = { (name: String) -> String in
        return "Hello, \(name)!"
    }

6. Optionals 
    var optionalName: String? = "John"

    // Force Unwrap (Dangerous)
    let name1 = optionalName!

    // Optional Binding
    if let name = optionalName {
        print(name)
    }

    // Guard Statement
    guard let name = optionalName else {
        fatalError("Name is nil")
    }

    // Optional Chaining
    let count = optionalName?.count

7. Object-Oriented Programming
    - Classes & Structures
        class Person {
            var name: String
            var age: Int
            
            init(name: String, age: Int) {
                self.name = name
                self.age = age
            }
            
            func introduce() {
                print("I'm \(name), \(age) years old")
            }
        }

        struct Point {
            var x: Int
            var y: Int
        }

        // Key Differences:
        // - Classes: Reference types, inheritance
        // - Structs: Value types, no inheritance
    - Inheritance 
        class Student: Person {
            var grade: String
            
            init(name: String, age: Int, grade: String) {
                self.grade = grade
                super.init(name: name, age: age)
            }
            
            override func introduce() {
                print("I'm \(name), a grade \(grade) student")
            }
        }
    - Protocols
        protocol Drivable {
            var speed: Double { get set }
            func startEngine()
        }

        class Car: Drivable {
            var speed = 0.0
            
            func startEngine() {
                print("Engine started")
            }
        }
    
8. Error Handling
    enum NetworkError: Error {
        case badURL
        case timeout
    }

    func fetchData() throws -> Data {
        throw NetworkError.timeout
    }

    do {
        let data = try fetchData()
    } catch NetworkError.badURL {
        print("Invalid URL")
    } catch {
        print("Other error: \(error)")
    }

9.SwiftUI
    - Basics
        - View Protocol
            import SwiftUI

            struct ContentView: View {
                var body: some View {
                    Text("Hello, SwiftUI!")
                }
            }
        Preview Provider 
            struct ContentView_Previews: PreviewProvider {
                static var previews: some View {
                    ContentView()
                }
            }
    - Layout & Stacks
        - Vertical Stack (VStack)
            VStack(alignment: .leading, spacing: 10) {
                Text("Title").font(.largeTitle)
                Text("Subtitle")
            }
        - Horizontal Stack (HStack) 
            HStack(spacing: 20) {
                Image(systemName: "star")
                Text("Favorite")
            }
        - Depth Stack (ZStack)
            ZStack {
                Circle().fill(Color.blue)
                Text("Center")
            }
        - Combined Layout 
            VStack {
                HStack {
                    Text("Left")
                    Spacer()
                    Text("Right")
                }
                Divider()
                ZStack {
                    Circle().fill(Color.red)
                    Text("Overlay")
                }
            }
    - State Management 
        - @State (Local State)
            struct CounterView: View {
                @State private var count = 0
                
                var body: some View {
                    Button("Count: \(count)") {
                        count += 1
                    }
                }
            }
        - @Binding (Shared State)
            struct ToggleView: View {
                @Binding var isOn: Bool
                
                var body: some View {
                    Toggle("Toggle", isOn: $isOn)
                }
            }

            struct ParentView: View {
                @State private var toggleState = false
                
                var body: some View {
                    ToggleView(isOn: $toggleState)
                }
            }
        - @ObservedObject (External Model)
            class UserSettings: ObservableObject {
                @Published var username = "Guest"
            }

            struct ProfileView: View {
                @ObservedObject var settings: UserSettings
                
                var body: some View {
                    Text("Welcome, \(settings.username)!")
                }
            }
        - @EnvironmentalObject (Global State)
            struct SettingsView: View {
                @EnvironmentObject var settings: UserSettings
                
                var body: some View {
                    TextField("Username", text: $settings.username)
                }
            }

            // Usage:
            // ContentView().environmentObject(UserSettings())
    - Views & Controls
        - Text 
            Text("Hello")
                .font(.title)           // Font size
                .foregroundColor(.blue) // Text color
                .bold()                // Weight
                .italic()             // Style
                .underline()          // Decoration
        - Buttons
            Button(action: {
                print("Button tapped")
            }) {
                HStack {
                    Image(systemName: "plus")
                    Text("Add Item")
                }
            }
            .buttonStyle(.borderedProminent)
        - Text Fields 
            @State private var text = ""

            TextField("Placeholder", text: $text)
                .textFieldStyle(.roundedBorder)
                .disableAutocorrection(true)
                .padding()
        - Toggle 
            @State private var isOn = false

            Toggle("Dark Mode", isOn: $isOn)
                .toggleStyle(.switch)
        - Slider
            @State private var value = 0.5

            Slider(value: $value, in: 0...1, step: 0.1)
    - Lists & Navigation
        - Static List
            List {
                Text("Item 1")
                Text("Item 2")
                Text("Item 3")
            }
            .listStyle(.insetGrouped)
        - Dynamic List 
            let items = ["Apple", "Banana", "Orange"]

            List(items, id: \.self) { item in
                Text(item)
            }
        - Navigation 
            NavigationView {
                List {
                    NavigationLink("Go to Details", destination: Text("Details View"))
                }
                .navigationTitle("Home")
            }
    - Modifiers
        - Layout Modifiers
            Text("Hello")
                .padding()            // Add space
                .frame(width: 200)    // Fixed size
                .background(Color.gray.opacity(0.2)) // Background
                .cornerRadius(10)     // Rounded corners
                .shadow(radius: 5)    // Drop shadow
        - Animation
            @State private var scale = 1.0

            Button("Animate") {
                withAnimation(.spring()) {
                    scale += 0.5
                }
            }
            .scaleEffect(scale)
    - Advanced SwiftUI 
        - Custom Views 
            struct PillButton: View {
                var label: String
                
                var body: some View {
                    Text(label)
                        .padding(.horizontal, 20)
                        .padding(.vertical, 10)
                        .background(Capsule().fill(Color.blue))
                        .foregroundColor(.white)
                }
            }

            // Usage:
            PillButton(label: "Press Me")
        - GeometryReader (Responsive Layouts)
            GeometryReader { geometry in
                HStack {
                    Text("Left")
                        .frame(width: geometry.size.width * 0.3)
                    Text("Right")
                        .frame(width: geometry.size.width * 0.7)
                }
            }    

10. Common Frameworks
    - UIKits (ios)
        import UIKit

        class ViewController: UIViewController {
            override func viewDidLoad() {
                super.viewDidLoad()
                let label = UILabel()
                label.text = "Hello, UIKit!"
                view.addSubview(label)
            }
        }
    - Combine (Reactive)
        import Combine

        let publisher = Just("Hello")
        let subscriber = publisher.sink { value in
            print(value)
        }
    - Core Data 
        let context = persistentContainer.viewContext
        let newUser = User(context: context)
        newUser.name = "John"
        try? context.save()

11. Memory Management
    // Weak Reference (prevents retain cycles)
    class Person {
        weak var friend: Person?
    }

    // Unowned Reference (when reference always exists)
    class Customer {
        unowned let creditCard: CreditCard
    }
