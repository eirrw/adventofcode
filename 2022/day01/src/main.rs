use std::fs;

fn main() {
    let contents = fs::read_to_string("input")
        .expect("Should have been able to read the file");

    let elves = contents.split("\n\n");
    let mut high = 0;

    for elf in elves {
        let items = elf.split("\n").collect::<Vec<&str>>();
        println!("{:?}", items);

        let mut cals = 0;
        for item in items {
            if !item.is_empty() {
                cals += item.parse::<i32>().unwrap()
            }
        }

        if cals > high {
            high = cals
        }
    }


    println!("{high}");
}
