use std::vec::Vec;

fn main() {
    println!("Fibonacci of 0: {}", fib(0));
    println!("Fibonacci of 1: {}", fib(1));
    println!("Fibonacci of 2: {}", fib(2));
    println!("Fibonacci of 3: {}", fib(3));
    println!("Fibonacci of 30: {}", fib(30));
    let n = 150;
    let mut cache = vec![0u128; n + 1];
    println!("Fast Fibonacci of {n}: {}", fast_fib(n, &mut cache));
}

fn fib(n: usize) -> usize {
    if n == 0 {
        return 0;
    }
    if n == 1 {
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}

fn fast_fib(n: usize, cache: &mut Vec<u128>) -> u128 {
    if cache[n] > 0 {
        return cache[n];
    }

    let value;
    if n == 0 {
        value = 0;
    } else if n == 1 {
        value = 1;
    } else {
        value = fast_fib(n - 1, cache) + fast_fib(n - 2, cache);
    }
    cache[n] = value;
    return value;
}
