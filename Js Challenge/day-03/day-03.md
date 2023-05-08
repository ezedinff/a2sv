Overview
This question is intended as an introduction to closures and objects. It is recommended that you first read the editorial for counter is it contains basic information about closures not discussed here.

JavaScript Objects
At their core, objects are just mappings from strings to other values. The values can be anything: strings, functions, other objects, etc. The string that maps to the value is called the key.

const object = {
  "num": 1,
  "str": "Hello World",
  "obj": {
    "x": 5
  }
};
There are three ways to access values on an object:

Dot Notation.
const val = object.obj.x;
console.log(val); // 5
Bracket Notation. This is used when the key isn't valid variable name. For example ".123".
const val = object["obj"]["x"];
console.log(val); // 5
Destructuring Syntax. This is most useful when accessing multiple values at once. You can read more about the syntax here.
const { num, str} = object;
console.log(num, str); // 1 "Hello World"
You can read more about objects here.

Classes and Prototypes
You can also define classes in JavaScript. The classes's constructor returns an object which is an instance of that class.

class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log("My name is", this.name);
  }
}

const alice = new Person("Alice", 25);
alice.greet(); // Logs: "My name is Alice"
JavaScript implements classes with special objects call prototypes. All the methods (in this case greet) are functions stored on the object's prototype.

To make this concrete, the behavior of the above code could be replicated with the following code:

const alice = {
  name: "Alice",
  age: 25,
  __proto__: {
    greet: function() {
      console.log("My name is", this.name);
    }
  }
};
alice.greet(); // Logs: "My name is Alice"
Looking at this code, you might wonder "How can you access the greet method even though it's not a key on the alice object"?

The reason is that accessing keys on an object is actually slightly more complicated than just looking at the object's keys. There is actually an algorithm that traverse the prototype chain. First, JavaScript looks at the keys on the object. If the requested key wasn't found, it then looks on the keys of the prototype object. If it still wasn't found, it looks at the prototype's prototype, and so on. This is how inheritance is implemented in JavaScript!

You might also wonder why JavaScript has this strange prototype concept at all. Why not just store the functions on the object itself? The answer is efficiency. Every time a new Person is created, age and name fields are added to the object. However only a single reference to the prototype object is added. So no matter how many instances of Person are created or how many methods are on the class, only a single prototype object is generated.

You can read more about classes here.

Proxies
An infrequently used but powerful feature of javascript is the proxy. They allow you to override the default behavior of objects.

For example, to implement the alice object with proxies:

const alice = new Proxy({name: "Alice", age: 25}, {
  get: (target, key) => {
    if (key === 'greet') {
      return () => console.log("My name is", target.name);
    } else {
      return target[key];
    }
  },
});
alice.greet(); // Logs: "My name is Alice"
Examples
Here are some examples of potentially practical use-cases for proxies.

Perform validation to guarantee bad data is never entered into a form.
Code Example

Create a log any time a key is accessed. This could be useful as a developer tool.
Code Example

Throw an error if a an attempt was made to write to a readonly value.
Code Example

Create a modified version of an immutable object by writing to it's proxy. This is implemented with the popular library immer.
You can read more about proxies here.

Approach 1: Closure
We can declare a variable currentCount and set it equal to init. Then return an object with the three functions where we increment, decrement, and reset the currentCount.

Implementation
var createCounter = function(init) {
  let currentCount = init;
  return {
    increment: function() {
       currentCount += 1;
       return currentCount;
    },
    decrement: function() {
       currentCount -= 1;
       return currentCount;
    },
    reset: function() {
       currentCount = init;
       return currentCount;
    },
  }
};

Approach 2: Closure with Shortened Syntax
We can take the concept from Approach 1 and shorten the syntax in several ways.

We can replace += 1 and -= 1 with Prefix Increment/Decrement syntax. What this syntax allows you to do is increment or decrement a number and then return it.
Combine currentCount = init and return currentCount into a single line of code. In JavaScript, assigning a value to a variable also returns that value.
Switch from function syntax to arrow syntax when defining the functions.
Implementation
var createCounter = function(init) {
  let currentCount = init;
  return {
    increment: () => ++currentCount,
    decrement: () => --currentCount,
    reset: () => (currentCount = init),
  }
};


Approach 3: Closure with Separately Created Functions
You can declare functions with the appropriate names and then return them. What this approach highlights is syntactic sugar for creating objects. When the name of the value is the same name as the key, you can omit the value. For example, you could shorten let obj = { value: value }; to let obj = { value };

Implementation
var createCounter = function(init) {
  let currentCount = init;

  function increment() {
    return ++currentCount;
  }

  function decrement() {
      return --currentCount;
  }

  function reset() {
      return (currentCount = init);
  }

  return { increment, decrement, reset };
};

Approach 4: Class
We can define a Counter class with the appropriate methods and then return a new instance of this class.

Implementation
class Counter {
  constructor(init) {
    this.init = init;
    this.currentCount = init;
  }

  increment() {
    this.currentCount += 1;
    return this.currentCount;
  }

  decrement() {
    this.currentCount -= 1;
    return this.currentCount;
  }

  reset() {
    this.currentCount = this.init;
    return this.currentCount;
  }
}


var createCounter = function(init) {
  return new Counter(init);
};

Approach 5: Closure with Proxy
Rather than returning a normal object, we can return a Proxy which emulates the behavior of an object with methods. We can do this by listening to all property access (get) events and if the requested key matches the name of a method, perform the appropriate logic.

Note that this solution is primarily for demonstration purposes. Proxies are a very powerful tool and their use should be reserved for situations that absolutely require them.

Implementation

var createCounter = function(init) {
  let currentCount = init;
  return new Proxy({}, {
    get: (target, key) => {
      switch(key) {
        case "increment":
          return () => ++currentCount;
        case "decrement":
          return () => --currentCount;
        case "reset":
          return () => (currentCount = init);
        default:
          throw Error("Unexpected Method")
      }
    },
  });
};