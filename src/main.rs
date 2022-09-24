use std::io::{Write, stdout, stdin};

fn main() {
    println!("Hello, world!");

    stdout().flush(); 

    let mut input = String::new(); // Creates new variable with type String
    std::io::stdin().read_line(&mut input); // Takes user input

    println!("{}", input); // Prints user input
    
}
