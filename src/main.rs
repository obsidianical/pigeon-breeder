use std::io::{Write, stdout};

struct Pigeon {
    pub uid: String,
    name: String,
    age: i32,

    is_female: bool,
    can_reproduce: bool,
    is_alive: bool,

    did_act: bool
}

impl Pigeon {
    pub fn new(uid: String, name: String, age: i32, is_female: bool, can_reproduce: bool, is_alive: bool, did_act: bool) -> Self {
        Self {
            uid,
            name,
            age, 
            is_female,
            can_reproduce,
            is_alive,
            did_act
        }
    }
}

fn main() {
    println!("Hello, world!");

    stdout().flush(); 

    let mut input = String::new(); // Creates new variable with type String
    std::io::stdin().read_line(&mut input); // Takes user input

    let pigeon_test = Pigeon::new("P1".to_string(), input.to_string(), 1, false, true, true, false);

    println!("{}", pigeon_test.name); // Prints user input
}
