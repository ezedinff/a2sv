# Object Oriented Design
## Table of Contents
- [Object Oriented Design and UML](#object-oriented-design-and-uml)
    - [Object Oriented Basics](#object-oriented-basics)
    - [Object Oriented Analysis and Design](#object-oriented-analysis-and-design)
    - [UML](#uml)
        - [Use Case Diagram](#use-case-diagram)
        - [Class Diagram](#class-diagram)
        - [Sequence Diagram](#sequence-diagram)
        - [Activity Diagram](#activity-diagram)
- [Design Patterns](#design-patterns)
    - [Creational Patterns](#creational-patterns)
        - [Abstract Factory](#abstract-factory)
        - [Builder](#builder)
        - [Factory Method](#factory-method)
        - [Prototype](#prototype)
        - [Singleton](#singleton)
    - [Structural Patterns](#structural-patterns)
        - [Adapter](#adapter)
        - [Bridge](#bridge)
        - [Composite](#composite)
        - [Decorator](#decorator)
        - [Facade](#facade)
        - [Flyweight](#flyweight)
        - [Proxy](#proxy)
    - [Behavioral Patterns](#behavioral-patterns)
        - [Chain of Responsibility](#chain-of-responsibility)
        - [Command](#command)
        - [Interpreter](#interpreter)
        - [Iterator](#iterator)
        - [Mediator](#mediator)
        - [Memento](#memento)
        - [Observer](#observer)
        - [State](#state)
        - [Strategy](#strategy)
        - [Template Method](#template-method)
        - [Visitor](#visitor)
- [Design Principles](#design-principles)
    - [SOLID](#solid)
        - [Single Responsibility Principle](#single-responsibility-principle)
        - [Open-Closed Principle](#open-closed-principle)
        - [Liskov Substitution Principle](#liskov-substitution-principle)
        - [Interface Segregation Principle](#interface-segregation-principle)
        - [Dependency Inversion Principle](#dependency-inversion-principle)
    - [GRASP](#grasp)
    - [DRY](#dry)
    - [KISS](#kiss)
    - [YAGNI](#yagni)
    - [Law of Demeter](#law-of-demeter)

## Object Oriented Design and UML
### Object Oriented Basics
OOP is a programming paradigm that uses objects and their interactions to design and program applications. It is a way of thinking about software design where programs are viewed as a collection of interacting objects rather than a collection of functions and data.

The 4 principles of OOP are:
- **Encapsulation**: The bundling of data with the methods that operate on that data, or the restricting of direct access to some of an object's components.
- **Abstraction**: The process of hiding the implementation details from the user, only the functionality will be provided to the user.
- **Inheritance**: The process of using details from a new class without modifying existing class.
- **Polymorphism**: The process of using common operation in different ways for different data input. it is the ability of an object to take on many forms.

### Object Oriented Analysis and Design
It is a step-by-step approach to analyze and design an application using object-oriented concepts. It is a top-down approach that starts with the analysis of the system and ends with the design of the system.

the steps of OOAD are:
1. Identify the objects.
2. Identify the attributes and operations.
3. Identify the relationships.
4. Make the design.

### UML
Unified Modeling Language (UML) is a general-purpose, developmental, modeling language in the field of software engineering that is intended to provide a standard way to visualize the design of a system.

Types of UML diagrams:
- Structural diagrams
    - Class diagram
    - Object diagram
    - Component diagram
    - Deployment diagram
- Behavioral diagrams
    - Use case diagram
    - Sequence diagram
    - Communication diagram
    - State machine diagram
    - Activity diagram
    - Interaction overview diagram

#### Use Case Diagram
Use case diagrams are used to model the functionality of a system using actors and use cases. It is a behavioral diagram.

#### Class Diagram
Class diagrams are used to model the structure of a system by showing the system's classes, their attributes, operations (or methods), and the relationships among objects.

#### Sequence Diagram
Sequence diagrams are used to visualize interactions among objects in terms of an exchange of messages over time for a specific scenario.

#### Activity Diagram
Activity diagrams are used to model the workflow of a system by showing the system's activities, their dependencies, and the control flow.

## Design Patterns
Design patterns are typical solutions to common problems in software design. Each pattern is like a blueprint that you can customize to solve a particular design problem in your code.

### Creational Patterns
Creational patterns are design patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.

#### Abstract Factory
Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

use cases:
- When the system should be independent of how its products are created, composed, and represented.
- When the family of related product objects is designed to be used together, and you need to enforce this constraint.
- When you want to provide a class library of products, and you want to reveal just their interfaces, not their implementations.

Example:
```java
public interface AbstractFactory<T> {
    T create(String type);
}

public class ShapeFactory implements AbstractFactory<Shape> {
    @Override
    public Shape create(String type) {
        if (type.equals("circle")) {
            return new Circle();
        } else if (type.equals("square")) {
            return new Square();
        } else if (type.equals("rectangle")) {
            return new Rectangle();
        }
        return null;
    }
}

public class ColorFactory implements AbstractFactory<Color> {
    @Override
    public Color create(String type) {
        if (type.equals("red")) {
            return new Red();
        } else if (type.equals("green")) {
            return new Green();
        } else if (type.equals("blue")) {
            return new Blue();
        }
        return null;
    }
}

public interface Shape {
    void draw();
}

public class Circle implements Shape {
    @Override
    public void draw() {
        System.out.println("Inside Circle::draw() method.");
    }
}

public class Square implements Shape {
    @Override
    public void draw() {
        System.out.println("Inside Square::draw() method.");
    }
}

public class Rectangle implements Shape {
    @Override
    public void draw() {
        System.out.println("Inside Rectangle::draw() method.");
    }
}

public interface Color {
    void fill();
}

public class Red implements Color {
    @Override
    public void fill() {
        System.out.println("Inside Red::fill() method.");
    }
}

public class Green implements Color {
    @Override
    public void fill() {
        System.out.println("Inside Green::fill() method.");
    }
}

public class Blue implements Color {
    @Override
    public void fill() {
        System.out.println("Inside Blue::fill() method.");
    }
}

public class AbstractFactoryPatternDemo {
    public static void main(String[] args) {
        AbstractFactory<Shape> shapeFactory = new ShapeFactory();
        Shape shape1 = shapeFactory.create("circle");
        shape1.draw();
        Shape shape2 = shapeFactory.create("rectangle");
        shape2.draw();
        Shape shape3 = shapeFactory.create("square");
        shape3.draw();

        AbstractFactory<Color> colorFactory = new ColorFactory();
        Color color1 = colorFactory.create("red");
        color1.fill();
        Color color2 = colorFactory.create("green");
        color2.fill();
        Color color3 = colorFactory.create("blue");
        color3.fill();
    }
}
```