fn main() {
    let x = 5;
    let x = x + 1;
    {
        let x = x * 2;
        println!("The value of x is: {x}");
    }
    println!("The value of x is: {x}");

    let tup: (i32, f64, u8) = (500, 4.5, 9);
    let (one, two, three) = tup;
    println!("{:#?}", tup);
    println!("{}, {}, {}", tup.0, tup.1, tup.2);
    println!("{one}, {two}, {three}");

    let a: [i32; 3] = [1, 2, 3];
    let b = [0; 5];

    println!("{:?}", a);
    println!("{:?}", b);

    let message = "1234";
    let x = (message, 100);
    println!("{:?}", x);

    let result = another_function(adder, 64);
    println!("Result is {result}");

    let result = another_function(adder, 30);
    let y = if result == 70 {
        println!("Yay {result}");
        result
    } else {
        println!("Booo {result}");
        result
    };
    println!("y = {y}");

    let mut counter = 0;
    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter + 2;
        }
    };
    println!("result = {result}");

    counter = 0;
    'counting_up: loop {
        println!("counter = {counter}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if counter == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        counter += 1;
    }

    for item in (0..4) {
        println!("Item {item}");
    }
}

fn another_function(f: fn(i32, i32) -> i32, arg: i32) -> i32 {
    fn nested_function(f: fn(i32, i32) -> i32, arg: i32) -> i32 {
        println!("Nested function");
        return f(arg, arg);
    }
    let closure = || {
        println!("Nested closure");
        return f(arg, arg);
    };
    println!("Another function");
    //return nested_function(f, arg);
    return closure();
}

fn adder(a: i32, b: i32) -> i32 {
    println!("Adding {a} + {b}");
    a + b
}
