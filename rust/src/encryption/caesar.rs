use std::num::ParseIntError;

use super::{grab_alphabet, EncryptionMethod};

#[path = "../input.rs"]
mod input;

pub struct CaeserEncryption;

impl CaeserEncryption {
    fn try_get_shift_from_user(&self, user_shift_response: &str) -> Result<isize, ParseIntError> {
        user_shift_response.trim().parse::<isize>()
    }

    fn get_index_after_shift(&self, n: isize, shift: isize) -> isize {
        n as isize + shift
    }

    fn shift_char(&self, alphabet: &str, c: char, shift: isize) -> String {
        let alphabet_index = alphabet.chars().position(|r| r == c);
        match alphabet_index {
            Some(n) => {
                let index_after_shift = self.get_index_after_shift(n as isize, shift);
                let assured_index = self.assure_index_after_shift(index_after_shift, &alphabet.chars());
                return alphabet.chars().nth(assured_index as usize).unwrap().to_string()
            }
            None => c.to_string(),
        }
    }

    fn assure_index_after_shift(&self, index: isize, alphabet: &std::str::Chars<'_>) -> usize {
        let alphabet_len = alphabet.clone().collect::<Vec<char>>().len() as isize;
        if index >= alphabet_len {
            return (0 + (index - alphabet_len)) as usize;
        }

        if index < 0 {
            return (alphabet_len + index) as usize;
        }

        return index as usize;
    }

}

impl EncryptionMethod for CaeserEncryption {
    fn encrypt(&self, message: &str) -> String {
        let mut encrypted_message = String::new();
        let num_shift = input::question_with_callback("Shift By? (- Left || + Right)", assure_input);
        let alphabet = grab_alphabet();

        for c in message.to_lowercase().chars() {
            let shifted_car = self.shift_char(&alphabet, c, self.try_get_shift_from_user(&num_shift).unwrap());
            encrypted_message.push_str(&shifted_car);
        }

        encrypted_message
    }

    fn decrypt(&self, cipher: &str) -> String {
        self.encrypt(cipher)
    }
}

fn assure_input(response: &str) -> bool {
    let response_as_isize = response.trim().parse::<isize>();

    if let Ok(n) = response_as_isize {
        if n < -25 || n > 25 {
            println!("Can't shift by {}, please try a different number", n);
            return false;
        }
        return true;
    }

    println!("Failed to convert to an integer, try a different number");
    false
}