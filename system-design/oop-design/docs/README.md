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
        // Robert
        System.out.println("John is male? " + isMale.interpret("John"));

        // Julie
        System.out.println("Janne is married woman? " + isMarriedWoman.interpret("Janne");
    }
}
```
