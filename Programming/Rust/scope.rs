fn main() {
    let x = 5;
    {
        let y = 99;
        println!("{}, {}" , x, y);
    }
    println!("{}, {}" , x, y);  //this line will error out because it is not in the same block as when the variable y was declaired.
}
