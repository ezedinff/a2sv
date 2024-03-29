# Object Oriented Design

Object Oriented Design is a way of designing software applications by using objects. Objects are the basic building blocks of Object Oriented Programming. Objects are created using classes. A class is a blueprint for creating objects. Objects have properties and methods. Properties are the characteristics of an object. Methods are the actions that an object can perform.

I choose Java as the programming language for this course. Java is an object oriented programming language. Java is a general purpose programming language. It is used to develop desktop and mobile applications, web applications, enterprise applications and so on. Java is a popular programming language. It is used by many companies and organizations. It is a high level programming language. It is easy to learn and use. Java is a statically typed programming language. It is a compiled programming language. It is a multi paradigm programming language. It supports object oriented programming, functional programming and imperative programming.

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
- [Object Oriented Design Case Studies](#object-oriented-analysis-and-design-case-studies)
    - [Designing Chess](./case-studies/chess)

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

#### Builder
Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

use cases:
- When the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled.
- When the construction process must allow different representations for the object that's constructed.

Example:
```java
public class Meal {
    private List<Item> items = new ArrayList<>();

    public void addItem(Item item) {
        items.add(item);
    }

    public float getCost() {
        float cost = 0.0f;
        for (Item item : items) {
            cost += item.price();
        }
        return cost;
    }

    public void showItems() {
        for (Item item : items) {
            System.out.print("Item : " + item.name());
            System.out.print(", Packing : " + item.packing().pack());
            System.out.println(", Price : " + item.price());
        }
    }
}

public interface Item {
    String name();
    Packing packing();
    float price();
}

public interface Packing {
    String pack();
}

public class Wrapper implements Packing {
    @Override
    public String pack() {
        return "Wrapper";
    }
}

public class Bottle implements Packing {
    @Override
    public String pack() {
        return "Bottle";
    }
}

public abstract class Burger implements Item {
    @Override
    public Packing packing() {
        return new Wrapper();
    }

    @Override
    public abstract float price();
}

public abstract class ColdDrink implements Item {
    @Override
    public Packing packing() {
        return new Bottle();
    }

    @Override
    public abstract float price();
}

public class VegBurger extends Burger {
    @Override
    public String name() {
        return "Veg Burger";
    }

    @Override
    public float price() {
        return 25.0f;
    }
}

public class ChickenBurger extends Burger {
    @Override
    public String name() {
        return "Chicken Burger";
    }

    @Override
    public float price() {
        return 50.5f;
    }
}

public class Coke extends ColdDrink {
    @Override
    public String name() {
        return "Coke";
    }

    @Override
    public float price() {
        return 30.0f;
    }
}

public class Pepsi extends ColdDrink {
    @Override
    public String name() {
        return "Pepsi";
    }

    @Override
    public float price() {
        return 35.0f;
    }
}

public class MealBuilder {
    public Meal prepareVegMeal() {
        Meal meal = new Meal();
        meal.addItem(new VegBurger());
        meal.addItem(new Coke());
        return meal;
    }

    public Meal prepareNonVegMeal() {
        Meal meal = new Meal();
        meal.addItem(new ChickenBurger());
        meal.addItem(new Pepsi());
        return meal;
    }
}

public class BuilderPatternDemo {
    public static void main(String[] args) {
        MealBuilder mealBuilder = new MealBuilder();

        Meal vegMeal = mealBuilder.prepareVegMeal();
        System.out.println("Veg Meal");
        vegMeal.showItems();
        System.out.println("Total Cost: " + vegMeal.getCost());

        Meal nonVegMeal = mealBuilder.prepareNonVegMeal();
        System.out.println("\n\nNon-Veg Meal");
        nonVegMeal.showItems();
        System.out.println("Total Cost: " + nonVegMeal.getCost());
    }
}
```

#### Prototype
Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

use cases:
- When your code shouldn't depend on the concrete classes of objects that you need to copy.
- When you want to reduce the number of subclasses that only differ in the way they initialize their respective objects. Instead of creating a bunch of subclasses with the same code, you can put the varying initialization code into a single class and use it as a prototype.

Example:
```java
public interface PrototypeCapable extends Cloneable {
    PrototypeCapable clone() throws CloneNotSupportedException;
}

public class Movie implements PrototypeCapable {
    private String name;
    private double price;

    public Movie() {
        super();
    }

    public Movie(Movie movie) {
        super();
        this.name = movie.name;
        this.price = movie.price;
    }

    @Override
    public Movie clone() throws CloneNotSupportedException {
        return (Movie) super.clone();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}

public class PrototypePatternTest {
    public static void main(String[] args) throws CloneNotSupportedException {
        Movie movie = new Movie();
        movie.setName("Avengers");
        movie.setPrice(100.00);
        System.out.println(movie);

        Movie movie1 = movie.clone();
        movie1.setName("Avengers: Age of Ultron");
        movie1.setPrice(200.00);
        System.out.println(movie1);
    }
}
```

#### Singleton
Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

use cases:
- When there must be exactly one instance of a class, and it must be accessible to clients from a well-known access point.
- When you need stricter control over global variables.

Example:
```java
public class Singleton {
    private static Singleton instance;

    private Singleton() {
    }

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}

public class SingletonPatternTest {
    public static void main(String[] args) {
        Singleton singleton = Singleton.getInstance();
        System.out.println(singleton);
    }
}
```

### Structural Design Patterns
Structural design patterns are concerned with how classes and objects are composed to form larger structures.

#### Adapter
Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.

use cases:
- When you want to use an existing class, and its interface does not match the one you need.
- When you want to create a reusable class that cooperates with unrelated or unforeseen classes, that is, classes that don't necessarily have compatible interfaces.

Example:
```java
public interface MediaPlayer {
    void play(String audioType, String fileName);
}

public interface AdvancedMediaPlayer {
    void playVlc(String fileName);
    void playMp4(String fileName);
}

public class VlcPlayer implements AdvancedMediaPlayer {
    @Override
    public void playVlc(String fileName) {
        System.out.println("Playing vlc file. Name: " + fileName);
    }

    @Override
    public void playMp4(String fileName) {
        //do nothing
    }
}

public class Mp4Player implements AdvancedMediaPlayer {
    @Override
    public void playVlc(String fileName) {
        //do nothing
    }

    @Override
    public void playMp4(String fileName) {
        System.out.println("Playing mp4 file. Name: " + fileName);
    }
}

public class MediaAdapter implements MediaPlayer {
    AdvancedMediaPlayer advancedMusicPlayer;

    public MediaAdapter(String audioType) {
        if (audioType.equalsIgnoreCase("vlc")) {
            advancedMusicPlayer = new VlcPlayer();
        } else if (audioType.equalsIgnoreCase("mp4")) {
            advancedMusicPlayer = new Mp4Player();
        }
    }

    @Override
    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("vlc")) {
            advancedMusicPlayer.playVlc(fileName);
        } else if (audioType.equalsIgnoreCase("mp4")) {
            advancedMusicPlayer.playMp4(fileName);
        }
    }
}

public class AudioPlayer implements MediaPlayer {
    MediaAdapter mediaAdapter;

    @Override
    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("mp3")) {
            System.out.println("Playing mp3 file. Name: " + fileName);
        } else if (audioType.equalsIgnoreCase("vlc") || audioType.equalsIgnoreCase("mp4")) {
            mediaAdapter = new MediaAdapter(audioType);
            mediaAdapter.play(audioType, fileName);
        } else {
            System.out.println("Invalid media. " + audioType + " format not supported");
        }
    }
}

public class AdapterPatternTest {
    public static void main(String[] args) {
        AudioPlayer audioPlayer = new AudioPlayer();

        audioPlayer.play("mp3", "beyond the horizon.mp3");
        audioPlayer.play("mp4", "alone.mp4");
        audioPlayer.play("vlc", "far far away.vlc");
        audioPlayer.play("avi", "mind me.avi");
    }
}
```

#### Bridge
Bridge is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

use cases:
- When you want to avoid a permanent binding between an abstraction and its implementation. This might be the case, for example, when the implementation must be selected or switched at run-time.
- When both the abstractions and their implementations should be extensible by subclassing. In this case, the Bridge pattern lets you combine the different abstractions and implementations and extend them independently.

Example:
```java
public interface Color {
    void applyColor();
}

public class Red implements Color {
    @Override
    public void applyColor() {
        System.out.println("red.");
    }
}

public class Green implements Color {
    @Override
    public void applyColor() {
        System.out.println("green.");
    }
}

public class Blue implements Color {
    @Override
    public void applyColor() {
        System.out.println("blue.");
    }
}

public abstract class Shape {
    protected Color color;

    protected Shape(Color color) {
        this.color = color;
    }

    abstract public void applyColor();
}

public class Circle extends Shape {
    public Circle(Color color) {
        super(color);
    }

    @Override
    public void applyColor() {
        System.out.print("Circle filled with color ");
        color.applyColor();
    }
}

public class Square extends Shape {
    public Square(Color color) {
        super(color);
    }

    @Override
    public void applyColor() {
        System.out.print("Square filled with color ");
        color.applyColor();
    }
}

public class BridgePatternTest {
    public static void main(String[] args) {
        Shape greenCircle = new Circle(new Green());
        Shape redCircle = new Circle(new Red());
        Shape blueSquare = new Square(new Blue());

        greenCircle.applyColor();
        redCircle.applyColor();
        blueSquare.applyColor();
    }
}
```

#### Composite
Composite is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.

use cases:
- When you have to implement a tree-like object structure.
- When you want the client code to treat both single (scalar) and composite objects uniformly.

Example:
```java
public interface Employee {
    void showEmployeeDetails();
}

public class Developer implements Employee {
    private String name;
    private long empId;
    private String position;

    public Developer(long empId, String name, String position) {
        this.empId = empId;
        this.name = name;
        this.position = position;
    }

    @Override
    public void showEmployeeDetails() {
        System.out.println(empId + " " + name + " " + position);
    }
}

public class Manager implements Employee {
    private String name;
    private long empId;
    private String position;

    public Manager(long empId, String name, String position) {
        this.empId = empId;
        this.name = name;
        this.position = position;
    }

    @Override
    public void showEmployeeDetails() {
        System.out.println(empId + " " + name + " " + position);
    }
}

public class CompanyDirectory implements Employee {
    private List<Employee> employeeList = new ArrayList<>();

    @Override
    public void showEmployeeDetails() {
        for (Employee emp : employeeList) {
            emp.showEmployeeDetails();
        }
    }

    public void addEmployee(Employee emp) {
        employeeList.add(emp);
    }

    public void removeEmployee(Employee emp) {
        employeeList.remove(emp);
    }
}

public class CompositePatternTest {
    public static void main(String[] args) {
        Employee dev1 = new Developer(100, "Messeret Kassaye", "Pro Developer");
        Employee dev2 = new Developer(101, "Ezedin Fedlu", "Developer");
        Employee manager1 = new Manager(200, "Luleseged Ayele", "SEO Manager");
        Employee manager2 = new Manager(201, "Abenezer Chala", "Project Manager");

        CompanyDirectory engDirectory = new CompanyDirectory();
        engDirectory.addEmployee(dev1);
        engDirectory.addEmployee(dev2);
        engDirectory.addEmployee(manager1);

        CompanyDirectory accDirectory = new CompanyDirectory();
        accDirectory.addEmployee(manager2);

        CompanyDirectory directory = new CompanyDirectory();
        directory.addEmployee(engDirectory);
        directory.addEmployee(accDirectory);
        directory.showEmployeeDetails();
    }
}
```

#### Decorator
Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

use cases:
- When you want to add responsibilities to individual objects, without affecting other objects from the same class.
- When you want to add responsibilities to a whole class of objects, without creating new subclasses.

Example:
```java
public interface Sandwich {
    String make();
}

public class SimpleSandwich implements Sandwich {
    @Override
    public String make() {
        return "Bread";
    }
}

public class SandwichDecorator implements Sandwich {
    protected Sandwich customSandwich;

    public SandwichDecorator(Sandwich customSandwich) {
        this.customSandwich = customSandwich;
    }

    @Override
    public String make() {
        return customSandwich.make();
    }
}

public class DressingDecorator extends SandwichDecorator {
    public DressingDecorator(Sandwich customSandwich) {
        super(customSandwich);
    }

    @Override
    public String make() {
        return super.make() + " + Mayo";
    }
}

public class MeatDecorator extends SandwichDecorator {
    public MeatDecorator(Sandwich customSandwich) {
        super(customSandwich);
    }

    @Override
    public String make() {
        return super.make() + " + Turkey";
    }
}

public class CheeseDecorator extends SandwichDecorator {
    public CheeseDecorator(Sandwich customSandwich) {
        super(customSandwich);
    }

    @Override
    public String make() {
        return super.make() + " + Swiss";
    }
}

public class DecoratorPatternTest {
    public static void main(String[] args) {
        Sandwich sandwich = new DressingDecorator(new MeatDecorator(new CheeseDecorator(new SimpleSandwich())));
        System.out.println(sandwich.make());
    }
}
```

#### Facade
Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

use cases:
- When you want to provide a simple interface to a complex subsystem.
- When there are many dependencies between clients and the implementation classes of an abstraction.

Example:
```java
public class ShapeMaker {
    private Shape circle;
    private Shape rectangle;
    private Shape square;

    public ShapeMaker() {
        circle = new Circle();
        rectangle = new Rectangle();
        square = new Square();
    }

    public void drawCircle() {
        circle.draw();
    }

    public void drawRectangle() {
        rectangle.draw();
    }

    public void drawSquare() {
        square.draw();
    }
}

public class FacadePatternTest {
    public static void main(String[] args) {
        ShapeMaker shapeMaker = new ShapeMaker();

        shapeMaker.drawCircle();
        shapeMaker.drawRectangle();
        shapeMaker.drawSquare();
    }
}
```

#### Flyweight
Flyweight is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.

use cases:
- When your program needs to support a large number of objects that have part of their internal state in common where the other part of state can vary.
- When you need to reduce the total number of objects in your program.

Example:
```java
public interface Shape {
    void draw();
}

public class Circle implements Shape {
    private String color;
    private int x;
    private int y;
    private int radius;

    public Circle(String color) {
        this.color = color;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public void setRadius(int radius) {
        this.radius = radius;
    }

    @Override
    public void draw() {
        System.out.println("Circle: Draw() [Color : " + color + ", x : " + x + ", y :" + y + ", radius :" + radius);
    }
}

public class ShapeFactory {
    private static final Map<String, Shape> circleMap = new HashMap<>();

    public static Shape getCircle(String color) {
        Circle circle = (Circle) circleMap.get(color);

        if (circle == null) {
            circle = new Circle(color);
            circleMap.put(color, circle);
            System.out.println("Creating circle of color : " + color);
        }
        return circle;
    }
}

public class FlyweightPatternTest {
    private static final String colors[] = {"Red", "Green", "Blue", "White", "Black"};
    public static void main(String[] args) {

        for(int i=0; i < 20; ++i) {
            Circle circle = (Circle)ShapeFactory.getCircle(getRandomColor());
            circle.setX(getRandomX());
            circle.setY(getRandomY());
            circle.setRadius(100);
            circle.draw();
        }
    }

    private static String getRandomColor() {
        return colors[(int)(Math.random()*colors.length)];
    }

    private static int getRandomX() {
        return (int)(Math.random()*100 );
    }

    private static int getRandomY() {
        return (int)(Math.random()*100);
    }
}
```

#### Proxy
Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

use cases:
- When you need a more versatile or sophisticated reference to an object than a simple pointer.
- When you want to be able to create and destroy objects dynamically.
- When you want to control access to the original object.

Example:
```java
public interface Image {
    void display();
}

public class RealImage implements Image {
    private String fileName;

    public RealImage(String fileName) {
        this.fileName = fileName;
        loadFromDisk(fileName);
    }

    @Override
    public void display() {
        System.out.println("Displaying " + fileName);
    }

    private void loadFromDisk(String fileName) {
        System.out.println("Loading " + fileName);
    }
}

public class ProxyImage implements Image {
    private RealImage realImage;
    private String fileName;

    public ProxyImage(String fileName) {
        this.fileName = fileName;
    }

    @Override
    public void display() {
        if (realImage == null) {
            realImage = new RealImage(fileName);
        }
        realImage.display();
    }
}

public class ProxyPatternTest {
    public static void main(String[] args) {
        Image image = new ProxyImage("test_10mb.jpg");

        //image will be loaded from disk
        image.display();
        System.out.println("");

        //image will not be loaded from disk
        image.display();
    }
}
```

### Behavioral Patterns
Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects.

#### Chain of Responsibility
Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

use cases:
- When more than one object may handle a request, and the handler isn’t known a priori. The handler should be ascertained automatically.
- When you want to issue a request to one of several objects without specifying the receiver explicitly.
- When the set of objects that can handle a request should be specified dynamically.

Example:
```java
public abstract class AbstractLogger {
    public static int INFO = 1;
    public static int ERROR = 2;
    public static int DEBUG = 3;

    protected int level;

    //next element in chain or responsibility
    protected AbstractLogger nextLogger;

    public void setNextLogger(AbstractLogger nextLogger) {
        this.nextLogger = nextLogger;
    }

    public void logMessage(int level, String message) {
        if (this.level <= level) {
            write(message);
        }
        if (nextLogger != null) {
            nextLogger.logMessage(level, message);
        }
    }

    abstract protected void write(String message);
}

public class ConsoleLogger extends AbstractLogger {
    public ConsoleLogger(int level) {
        this.level = level;
    }

    @Override
    protected void write(String message) {
        System.out.println("Standard Console::Logger: " + message);
    }
}

public class ErrorLogger extends AbstractLogger {
    public ErrorLogger(int level) {
        this.level = level;
    }

    @Override
    protected void write(String message) {
        System.out.println("Error Console::Logger: " + message);
    }
}

public class FileLogger extends AbstractLogger {
    public FileLogger(int level) {
        this.level = level;
    }

    @Override
    protected void write(String message) {
        System.out.println("File::Logger: " + message);
    }
}
public class ChainPatternTest {
    private static AbstractLogger getChainOfLoggers() {
        AbstractLogger errorLogger = new ErrorLogger(AbstractLogger.ERROR);
        AbstractLogger fileLogger = new FileLogger(AbstractLogger.DEBUG);
        AbstractLogger consoleLogger = new ConsoleLogger(AbstractLogger.INFO);

        errorLogger.setNextLogger(fileLogger);
        fileLogger.setNextLogger(consoleLogger);

        return errorLogger;
    }

    public static void main(String[] args) {
        AbstractLogger loggerChain = getChainOfLoggers();

        loggerChain.logMessage(AbstractLogger.INFO, "This is an information.");

        loggerChain.logMessage(AbstractLogger.DEBUG, "This is an debug level information.");

        loggerChain.logMessage(AbstractLogger.ERROR, "This is an error information.");
    }
}
```


#### Command
Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request’s execution, and support undoable operations.

use cases:
- When you want to parametrize objects by an action to perform.
- When you want to queue operations, schedule their execution, or execute them remotely.
- When you want to support undo.

Example:
```java
public interface Order {
    void execute();
}

public class Stock {
    private String name = "ABC";
    private int quantity = 10;

    public void buy() {
        System.out.println("Stock [ Name: " + name + ", Quantity: " + quantity + " ] bought");
    }

    public void sell() {
        System.out.println("Stock [ Name: " + name + ", Quantity: " + quantity + " ] sold");
    }
}

public class BuyStock implements Order {
    private Stock abcStock;

    public BuyStock(Stock abcStock) {
        this.abcStock = abcStock;
    }

    @Override
    public void execute() {
        abcStock.buy();
    }
}

public class SellStock implements Order {
    private Stock abcStock;

    public SellStock(Stock abcStock) {
        this.abcStock = abcStock;
    }

    @Override
    public void execute() {
        abcStock.sell();
    }
}

public class Broker {
    private List<Order> orderList = new ArrayList<Order>();

    public void takeOrder(Order order) {
        orderList.add(order);
    }

    public void placeOrders() {
        for (Order order : orderList) {
            order.execute();
        }
        orderList.clear();
    }
}

public class CommandPatternTest {
    public static void main(String[] args) {
        Stock abcStock = new Stock();

        BuyStock buyStockOrder = new BuyStock(abcStock);
        SellStock sellStockOrder = new SellStock(abcStock);

        Broker broker = new Broker();
        broker.takeOrder(buyStockOrder);
        broker.takeOrder(sellStockOrder);

        broker.placeOrders();
    }
}
```

#### Interpreter
Interpreter is a behavioral design pattern that lets you define a grammar for a language, and then create an interpreter that uses this grammar to interpret sentences in the language.

use cases:
- When there is a language that needs to be interpreted frequently.
- When there is a simple grammar for statements in the language that can be easily represented in the code.

Example:
```java
public interface Expression {
    boolean interpret(String context);
}

public class TerminalExpression implements Expression {
    private String data;

    public TerminalExpression(String data) {
        this.data = data;
    }

    @Override
    public boolean interpret(String context) {
        if (context.contains(data)) {
            return true;
        }
        return false;
    }
}

public class OrExpression implements Expression {
    private Expression expr1 = null;
    private Expression expr2 = null;

    public OrExpression(Expression expr1, Expression expr2) {
        this.expr1 = expr1;
        this.expr2 = expr2;
    }

    @Override
    public boolean interpret(String context) {
        return expr1.interpret(context) || expr2.interpret(context);
    }
}

public class AndExpression implements Expression {
    private Expression expr1 = null;
    private Expression expr2 = null;

    public AndExpression(Expression expr1, Expression expr2) {
        this.expr1 = expr1;
        this.expr2 = expr2;
    }

    @Override
    public boolean interpret(String context) {
        return expr1.interpret(context) && expr2.interpret(context);
    }
}

public class InterpreterPatternTest {
    //Rule: Robert
    public static Expression getMaleExpression() {
        Expression robert = new TerminalExpression("Robert");
        Expression john = new TerminalExpression("John");
        return new OrExpression(robert, john);
    }

    //Rule: Julie
    public static Expression getMarriedWomanExpression() {
        Expression julie = new TerminalExpression("Julie");
        Expression married = new TerminalExpression("Married");
        return new AndExpression(julie, married);
    }

    public static void main(String[] args) {
        Expression isMale = getMaleExpression();
        Expression isMarriedWoman = getMarriedWomanExpression();
    }
}
```


#### Iterator
Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

use cases:
- When your collection has a complex data structure under the hood, but you want to hide its complexity from the clients.
- When you want to provide multiple traversal algorithms for a collection.

Example:
```java
public interface Iterator {
    boolean hasNext();
    Object next();
}

public interface Container {
    Iterator getIterator();
}

public class NameRepository implements Container {
    public String names[] = {"Robert" , "John" ,"Julie" , "Lora"};

    @Override
    public Iterator getIterator() {
        return new NameIterator();
    }

    private class NameIterator implements Iterator {
        int index;

        @Override
        public boolean hasNext() {
            if(index < names.length){
                return true;
            }
            return false;
        }

        @Override
        public Object next() {
            if(this.hasNext()){
                return names[index++];
            }
            return null;
        }
    }
}

public class IteratorPatternTest {
    public static void main(String[] args) {
        NameRepository namesRepository = new NameRepository();

        for(Iterator iter = namesRepository.getIterator(); iter.hasNext();){
            String name = (String)iter.next();
            System.out.println("Name : " + name);
        }
    }
}
```

#### Mediator
Mediator is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

use cases:
- When you want to reduce coupling between components of a program.
- When you want to control how and when objects interact.

Example:
```java
public interface ChatMediator {
    void sendMessage(String msg, User user);
    void addUser(User user);
}

public abstract class User {
    protected ChatMediator mediator;
    protected String name;

    public User(ChatMediator med, String name){
        this.mediator=med;
        this.name=name;
    }

    public abstract void send(String msg);
    public abstract void receive(String msg);
}

public class UserImpl extends User {

    public UserImpl(ChatMediator med, String name) {
        super(med, name);
    }

    @Override
    public void send(String msg) {
        System.out.println(this.name+": Sending Message="+msg);
        mediator.sendMessage(msg, this);
    }

    @Override
    public void receive(String msg) {
        System.out.println(this.name+": Received Message:"+msg);
    }
}

public class ChatMediatorImpl implements ChatMediator {
    private List<User> users;

    public ChatMediatorImpl(){
        this.users=new ArrayList<>();
    }

    @Override
    public void sendMessage(String msg, User user) {
        for(User u : this.users){
            //message should not be received by the user sending it
            if(u != user){
                u.receive(msg);
            }
        }
    }

    @Override
    public void addUser(User user) {
        this.users.add(user);
    }
}

public class MediatorPatternTest {
    public static void main(String[] args) {
        ChatMediator mediator = new ChatMediatorImpl();
        User user1 = new UserImpl(mediator, "Ezedin");
        User user2 = new UserImpl(mediator, "John");
        User user3 = new UserImpl(mediator, "George");
        User user4 = new UserImpl(mediator, "Messeret");
        mediator.addUser(user1);
        mediator.addUser(user2);
        mediator.addUser(user3);
        mediator.addUser(user4);

        user1.send("Hi All");
    }
}
```

#### Memento
Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.

use cases:
- When you want to provide the ability to restore the state of an object without revealing its details.
- When you want to save a snapshot of an object’s state to be able to restore it later.

Example:
```java
public class Memento {
    private String state;

    public Memento(String state){
        this.state=state;
    }

    public String getState() {
        return state;
    }
}

public class Originator {
    private String state;

    public void setState(String state){
        this.state=state;
    }

    public String getState(){
        return state;
    }

    public Memento saveStateToMemento(){
        return new Memento(state);
    }

    public void getStateFromMemento(Memento Memento){
        state = Memento.getState();
    }
}

public class CareTaker {
    private List<Memento> mementoList = new ArrayList<Memento>();

    public void add(Memento state){
        mementoList.add(state);
    }

    public Memento get(int index){
        return mementoList.get(index);
    }
}

public class MementoPatternTest {
    public static void main(String[] args) {
        Originator originator = new Originator();
        CareTaker careTaker = new CareTaker();
        originator.setState("State #1");
        originator.setState("State #2");
        careTaker.add(originator.saveStateToMemento());
        originator.setState("State #3");
        careTaker.add(originator.saveStateToMemento());
        originator.setState("State #4");
        System.out.println("Current State: " + originator.getState());
        originator.getStateFromMemento(careTaker.get(0));
        System.out.println("First saved State: " + originator.getState());
        originator.getStateFromMemento(careTaker.get(1));
        System.out.println("Second saved State: " + originator.getState());
    }
}
```

#### Observer
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

use cases:
- When you want to have a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

Example:
```java
public interface Subject {
    void register(Observer obj);
    void unregister(Observer obj);
    void notifyObservers();
    Object getUpdate(Observer obj);
}

public interface Observer {
    void update();
    void setSubject(Subject sub);
}

public class MyTopic implements Subject {

    private List<Observer> observers;
    private String message;
    private boolean changed;
    private final Object MUTEX= new Object();

    public MyTopic(){
        this.observers=new ArrayList<>();
    }

    @Override
    public void register(Observer obj) {
        if(obj == null) throw new NullPointerException("Null Observer");
        synchronized (MUTEX) {
            if(!observers.contains(obj)) observers.add(obj);
        }
    }

    @Override
    public void unregister(Observer obj) {
        synchronized (MUTEX) {
            observers.remove(obj);
        }
    }

    @Override
    public void notifyObservers() {
        List<Observer> observersLocal = null;
        //synchronization is used to make sure any observer registered after message is received is not notified
        synchronized (MUTEX) {
            if (!changed)
                return;
            observersLocal = new ArrayList<>(this.observers);
            this.changed=false;
        }
        for (Observer obj : observersLocal) {
            obj.update();
        }

    }

    @Override
    public Object getUpdate(Observer obj) {
        return this.message;
    }

    //method to post message to the topic
    public void postMessage(String msg){
        System.out.println("Message Posted to Topic:"+msg);
        this.message=msg;
        this.changed=true;
        notifyObservers();
    }

}

public class MyTopicSubscriber implements Observer {

    private String name;
    private Subject topic;

    public MyTopicSubscriber(String nm){
        this.name=nm;
    }

    @Override
    public void update() {
        String msg = (String) topic.getUpdate(this);
        if(msg == null){
            System.out.println(name+":: No new message");
        }else
            System.out.println(name+":: Consuming message::"+msg);
    }

    @Override
    public void setSubject(Subject sub) {
        this.topic=sub;
    }

}

public class ObserverPatternTest {
    public static void main(String[] args) {
        //create subject
        MyTopic topic = new MyTopic();

        //create observers
        Observer obj1 = new MyTopicSubscriber("Obj1");
        Observer obj2 = new MyTopicSubscriber("Obj2");
        Observer obj3 = new MyTopicSubscriber("Obj3");

        //register observers to the subject
        topic.register(obj1);
        topic.register(obj2);
        topic.register(obj3);

        //attach observer to subject
        obj1.setSubject(topic);
        obj2.setSubject(topic);
        obj3.setSubject(topic);

        //check if any update is available
        obj1.update();

        //now send message to subject
        topic.postMessage("New Message");
    }
}
```

#### State
State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

use cases:
- When an object’s behavior depends on its state, and it must change its behavior at runtime depending on that state.
- When operations have large, multipart conditional statements that depend on the object’s state. This state is usually represented by one or more enumerated constants. Often, several operations will contain this same conditional structure. The State pattern puts each branch of the conditional in a separate class. This lets you treat the object’s state as an object in its own right that can vary independently from other objects.

Example:
```java
public interface State {
    void doAction(Context context);
}

public class StartState implements State {

    @Override
    public void doAction(Context context) {
        System.out.println("Player is in start state");
        context.setState(this);
    }

    public String toString(){
        return "Start State";
    }
}

public class StopState implements State {

    @Override
    public void doAction(Context context) {
        System.out.println("Player is in stop state");
        context.setState(this);
    }

    public String toString(){
        return "Stop State";
    }
}

public class Context {
    private State state;

    public Context(){
        state = null;
    }

    public void setState(State state){
        this.state = state;
    }

    public State getState(){
        return state;
    }
}

public class StatePatternTest {
    public static void main(String[] args) {
        Context context = new Context();

        StartState startState = new StartState();
        startState.doAction(context);

        System.out.println(context.getState().toString());

        StopState stopState = new StopState();
        stopState.doAction(context);

        System.out.println(context.getState().toString());
    }
}
```


#### Strategy
Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

use cases:
- When you want to use different variants of an algorithm within an object and be able to switch from one algorithm to another during runtime.
- When you have a lot of similar classes that only differ in the way they execute some behavior.
- When you want to isolate the implementation details of an algorithm from the code that uses it.

Example:
```java
public interface Strategy {
    int doOperation(int num1, int num2);
}

public class OperationAdd implements Strategy{
    @Override
    public int doOperation(int num1, int num2) {
        return num1 + num2;
    }
}

public class OperationSubstract implements Strategy{
    @Override
    public int doOperation(int num1, int num2) {
        return num1 - num2;
    }
}

public class OperationMultiply implements Strategy{
    @Override
    public int doOperation(int num1, int num2) {
        return num1 * num2;
    }
}

public class Context {
    private Strategy strategy;

    public Context(Strategy strategy){
        this.strategy = strategy;
    }

    public int executeStrategy(int num1, int num2){
        return strategy.doOperation(num1, num2);
    }
}

public class StrategyPatternTest {
    public static void main(String[] args) {
        Context context = new Context(new OperationAdd());
        System.out.println("10 + 5 = " + context.executeStrategy(10, 5));

        context = new Context(new OperationSubstract());
        System.out.println("10 - 5 = " + context.executeStrategy(10, 5));

        context = new Context(new OperationMultiply());
        System.out.println("10 * 5 = " + context.executeStrategy(10, 5));
    }
}
```

#### Template
Template is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

use cases:
- When you want to let clients extend only particular steps of an algorithm, but not the whole algorithm or its structure.
- When you have several classes that contain almost the same code with only minor differences.

Example:
```java
public abstract class Game {
    abstract void initialize();
    abstract void startPlay();
    abstract void endPlay();

    //template method
    public final void play(){

        //initialize the game
        initialize();

        //start game
        startPlay();

        //end game
        endPlay();
    }
}

public class Cricket extends Game {

    @Override
    void endPlay() {
        System.out.println("Cricket Game Finished!");
    }

    @Override
    void initialize() {
        System.out.println("Cricket Game Initialized! Start playing.");
    }

    @Override
    void startPlay() {
        System.out.println("Cricket Game Started. Enjoy the game!");
    }
}

public class Football extends Game {

    @Override
    void endPlay() {
        System.out.println("Football Game Finished!");
    }

    @Override
    void initialize() {
        System.out.println("Football Game Initialized! Start playing.");
    }

    @Override
    void startPlay() {
        System.out.println("Football Game Started. Enjoy the game!");
    }
}

public class TemplatePatternTest {
    public static void main(String[] args) {

        Game game = new Cricket();
        game.play();
        System.out.println();
        game = new Football();
        game.play();
    }
}
```

#### Visitor
Visitor is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.

use cases:
- When you have a relatively complex set of structured data classes that you want to be able to traverse in various ways without changing their classes.
- When you want to be able to define new operations over existing object structures without changing those structures.
- When you want to be able to define related operations as classes instead of having to implement all variations of the operations within one class.

Example:
```java
public interface ComputerPart {
    public void accept(ComputerPartVisitor computerPartVisitor);
}

public class Computer implements ComputerPart {

    ComputerPart[] parts;

    public Computer(){
        parts = new ComputerPart[] {new Mouse(), new Keyboard(), new Monitor()};
    }

    @Override
    public void accept(ComputerPartVisitor computerPartVisitor) {
        for (int i = 0; i < parts.length; i++) {
            parts[i].accept(computerPartVisitor);
        }
        computerPartVisitor.visit(this);
    }
}

public class Keyboard implements ComputerPart {

    @Override
    public void accept(ComputerPartVisitor computerPartVisitor) {
        computerPartVisitor.visit(this);
    }
}

public class Monitor implements ComputerPart {

    @Override
    public void accept(ComputerPartVisitor computerPartVisitor) {
        computerPartVisitor.visit(this);
    }
}

public class Mouse implements ComputerPart {

    @Override
    public void accept(ComputerPartVisitor computerPartVisitor) {
        computerPartVisitor.visit(this);
    }
}

public interface ComputerPartVisitor {
    public void visit(Computer computer);
    public void visit(Mouse mouse);
    public void visit(Keyboard keyboard);
    public void visit(Monitor monitor);
}

public class ComputerPartDisplayVisitor implements ComputerPartVisitor {

    @Override
    public void visit(Computer computer) {
        System.out.println("Displaying Computer.");
    }

    @Override
    public void visit(Mouse mouse) {
        System.out.println("Displaying Mouse.");
    }

    @Override
    public void visit(Keyboard keyboard) {
        System.out.println("Displaying Keyboard.");
    }

    @Override
    public void visit(Monitor monitor) {
        System.out.println("Displaying Monitor.");
    }
}

public class VisitorPatternTest {
    public static void main(String[] args) {

        ComputerPart computer = new Computer();
        computer.accept(new ComputerPartDisplayVisitor());
    }
}
```

## Design Principles

### SOLID

#### Single Responsibility Principle
A class should have only one reason to change.

#### Open-Closed Principle
Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

#### Liskov Substitution Principle
Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.

#### Interface Segregation Principle
Many client-specific interfaces are better than one general-purpose interface.

#### Dependency Inversion Principle
Depend upon abstractions. Do not depend upon concrete classes.

### DRY
Don't Repeat Yourself - Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

### KISS
Keep It Simple, Stupid (or Keep It Short and Simple)

### YAGNI
You Ain't Gonna Need It (Don't implement something until you need it)

### Law of Demeter
A method should only call methods of:
- itself
- objects passed in as parameters
- any object the method creates or instantiates
- any components of the object

### Composition over Inheritance
Prefer composition over inheritance. Composition is the act of creating a new class by combining other classes. Inheritance is the act of creating a new class from an existing class. Inheritance is a form of specialization. Composition is a form of aggregation. Composition is a "has-a" relationship. Inheritance is an "is-a" relationship. Composition is more flexible than inheritance.