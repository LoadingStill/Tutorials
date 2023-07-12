//standard variable
  //can not change the vaule while in the immutable state, you can change the variable into a mutable state to change (but this is not the default)
fn main() {
    let bunnies = 2;
}



//32 bit variable
  //immutable
fn main() {
    let bunnies: i32 = 4;
}



//multiple variables in the same line
  //immutable
fn main() {
    let (bunnies, carrots) = (8, 50);
}



//mutable variable
fn main() {
    let mut x = 3;
}


//constant variable - more immutable then immutable varriables
  //cont is declaired - const
  //the variable is in all capitol letters
  //the type anotation is required ex: i32, f64, etc.
  // the vault must be a constiant expression that can be determined at compile time. - 9.9
fn main() {
    const WARP_FACTOR: f64 = 9.9;
}|
