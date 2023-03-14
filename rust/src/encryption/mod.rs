pub mod affine;
pub mod atbash;
pub mod caesar;

pub trait EncryptionMethod {
    fn encrypt(&self, message: &str) -> String;

    fn decrypt(&self, cipher: &str) -> String;
}

pub fn grab_alphabet() -> String {
    let alphabet = String::from("abcdefghijklmnopqrstuvwxyz");
    return alphabet;
}