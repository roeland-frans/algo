use std::rc::Rc;

fn main() {
    let first = String::from("Ferris");
    let first_clone = first.clone();
    let full = add_suffix(first_clone);
    println!("{full}, originally {first}");
    mutable_reference();
    return_a_string();
    let mut n = 1;
    incr(&mut n);
    println!(
        "{}",
        stringify_name_with_title(&vec![String::from("James")])
    );

    let mut dst = vec![String::from("1234")];
    let src = [String::from("12"), String::from("123456")];
    add_big_strings(&mut dst, &src);
    println!("{:?}", dst);
}

fn add_suffix(mut name: String) -> String {
    name.push_str(" Jr.");
    name
}

fn mutable_reference() {
    let mut v: Vec<i32> = vec![1, 2, 3];
    let num: &mut i32 = &mut v[2];

    *num += 1;

    println!("Third element is {}", *num);
    println!("Vector is now {:?}", v);
}

fn return_a_string() -> Rc<String> {
    let s = Rc::new(String::from("Hello world"));
    Rc::clone(&s)
}

fn incr(n: &mut i32) {
    *n += 1;
}

fn stringify_name_with_title(name: &Vec<String>) -> String {
    let mut full = name.join(" ");
    full.push_str(" Esq.");
    full
}

fn add_big_strings(dst: &mut Vec<String>, src: &[String]) {
    let largest_len: usize = dst.iter().max_by_key(|s| s.len()).unwrap().len();
    for s in src {
        if s.len() > largest_len {
            dst.push(s.clone());
        }
    }
}
