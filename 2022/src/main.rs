use std::fs;
use std::env;

pub mod day01;
pub mod day02;

fn main() {
    let args: Vec<String> = env::args().collect();
    let opt = &args[1];
    let input:String;
    let func:fn(String);

    if opt.eq("day01") {
        input = get_input("01");
        func = day01::main;
    } else if opt.eq("day02") {
        input = get_input("02");
        func = day02::main;
    } else {
        input = String::from("");
        func = print;
    }

    func(input);
}

fn get_input(day: &str) -> String {
    return fs::read_to_string(format!("input/{day}"))
        .expect("Should have been able to read the file");
}

fn print(input: String) {
    println!("{}", input)
}
