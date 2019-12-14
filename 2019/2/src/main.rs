use std::fs;

fn main() {
    let input = fs::read_to_string("./sample").expect("Error reading file");

    let mut opcodes: Vec<i32> = input.split(",")
        .map(|s| s.parse().unwrap())
        .collect();

    opcodes[11] += 100;

    for op in opcodes {
        println!("{}", op)
    }
}
