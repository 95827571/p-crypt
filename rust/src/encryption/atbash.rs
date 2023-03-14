use super::{EncryptionMethod, grab_alphabet};

pub struct AtbashEncryption;

impl AtbashEncryption {
    fn reverse_char(&self, alphabet: &str, c: char) -> String {
        let alphabet_index = &alphabet.chars().position(|r| r == c);

        // if the character isn't in the alphabet, then add it to the string as itself
        match alphabet_index {
            Some(n) => {
                let reverse_c = alphabet.chars().nth((alphabet.len()-1) - *n);
                return reverse_c.unwrap().to_string();
            },
            None => c.to_string(),
        }
    }
}

impl EncryptionMethod for AtbashEncryption {
    fn encrypt(&self, message: &str) -> String {
        let mut encrypted_string = String::new();
        let alphabet = grab_alphabet();

        // loops through each character and reverses it
        for c in message.to_lowercase().chars() {
            let reversed_char = self.reverse_char(&alphabet, c);

            encrypted_string.push_str(&reversed_char);
        }

        encrypted_string
    }

    // literally just does the same thing LOL
    fn decrypt(&self, cipher: &str) -> String {
        self.encrypt(cipher)
    }
}