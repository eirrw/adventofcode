pub fn main(input: String) {
    let rps_matches_i = input.split("\n");

    for rps_match_i in rps_matches_i {
        let sp = rps_match_i.split(" ").collect::<Vec<&str>>();
        let opp = sp[0];
        let plr = sp[1];

        rps_result(plr, opp)
    } 

    println!("{}", input)
}

fn rps_result(plr: &str, opp: &str) {

}
