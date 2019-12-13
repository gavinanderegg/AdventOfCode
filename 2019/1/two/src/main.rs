// based on this: https://riptutorial.com/rust/example/4275/read-a-file-line-by-line

use std::fs::File;
use std::io::{BufRead, BufReader};

fn find_fuel(mass: i64) -> i64 {
    return (mass / 3) - 2;
}

fn main() {
    let filename = "../input";

    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);
    
    let mut total = 0;
    
    for (_, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        
        let mass: i64 = match line.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        
        let fuel = find_fuel(mass);
        
        let mut subfuel = 0;
        let mut tempfuel = find_fuel(fuel);
        
        while tempfuel > 0 {
            subfuel += tempfuel;
            
            tempfuel = find_fuel(tempfuel);
        }
        
        total += fuel + subfuel;
    }
    
    println!("{}", total);
}