use std::error::Error;
mod input;
mod encryption;
use encryption::{affine, atbash, caesar};

// fn question_condition(response: &str) -> bool {
//     true
// }


fn main() -> Result<(), Box<dyn Error>> {
    let encryption_method: Box<dyn encryption::EncryptionMethod>;

    // Possible encryption methods
    let encryption_methods = vec![
        Into::into("Affine"), 
        Into::into("Atbash"),
        Into::into("Caesar"),
        Into::into("Keyword"),
    ];
    let menu_response = input::question_with_known_answers("", "", &encryption_methods);

    match menu_response {
        "Affine" => encryption_method = Box::new(affine::AffineEncryption),
        "Atbash" => encryption_method = Box::new(atbash::AtbashEncryption),
        "Caesar" => encryption_method = Box::new(caesar::CaeserEncryption),
        _ => panic!("This should be impossible."),
    }

    let result = encryption_method.as_ref().encrypt(&input::read_line_from_user("What would you like to encrypt?").trim());
    let decryption = encryption_method.as_ref().decrypt(&result);

    std::mem::drop(encryption_method);
    println!("{}", result);
    println!("{}", decryption);

    Ok(())
}