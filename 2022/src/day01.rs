pub fn main(input: String) {
    let elves = input.split("\n\n");
    let mut cal_sums: Vec<i32> = Vec::new();

    for elf in elves {
        let items = elf.split("\n").collect::<Vec<&str>>();

        let mut cals = 0;
        for item in items {
            if !item.is_empty() {
                cals += item.parse::<i32>().unwrap()
            }
        }

        cal_sums.push(cals);
    }

    cal_sums.sort_unstable();
    cal_sums.reverse();

    let sum = cal_sums[0] + cal_sums[1] + cal_sums[2];
    println!("{sum}");
}
