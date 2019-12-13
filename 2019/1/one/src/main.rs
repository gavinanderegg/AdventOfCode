// based on this: https://riptutorial.com/rust/example/4275/read-a-file-line-by-line

use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let filename = "../input";

    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);
    
    let mut total = 0;
    
    for (_, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        
        let mass: u32 = match line.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        
        let fuel = (mass / 3) - 2;
        
        total += fuel;
    }
    
    println!("{}", total);
}