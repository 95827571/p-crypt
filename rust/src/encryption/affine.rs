use super::{EncryptionMethod, grab_alphabet};


pub struct AffineEncryption;

impl AffineEncryption {
    fn grab_alphabet_index(&self, alphabet: &str, c: char) -> String {
        let alphabet_index = &alphabet.chars().position(|r| r == c);

        match alphabet_index {
            Some(n) => n.to_string(),
            None => c.to_string(),
        }
    }

    fn grab_character(&self, alphabet: &str, c_as_string: &str) -> String {
        let c_as_usize = c_as_string.parse::<usize>();

        // if the character is not in the alphabet then do nothing
        match c_as_usize {
            Ok(n) => alphabet.chars().nth(n).unwrap().to_string(),
            Err(_) => String::from(c_as_string),
        }
    }
}

impl EncryptionMethod for AffineEncryption {
    fn encrypt(&self, message: &str) -> String {
        let mut encrypted_string = String::new();
        let alphabet = grab_alphabet();

        // loops through each char and turns it into a integer
        for c in message.to_lowercase().chars() {
            let alphabet_index = self.grab_alphabet_index(&alphabet, c);
            encrypted_string.push_str(&alphabet_index);
            encrypted_string.push_str("-");
        }

        encrypted_string
    }

    fn decrypt(&self, cipher: &str) -> String {
        let mut decrypted_cipher = String::new();
        let alphabet = grab_alphabet();

        // loops through each number and converts it to a character in the alphabet
        for c in cipher.split("-") {
            let character = self.grab_character(&alphabet, c);
            decrypted_cipher.push_str(&character);
        }

        decrypted_cipher
    }
}