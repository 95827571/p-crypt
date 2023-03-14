#[allow(dead_code)]
pub fn read_line_from_user(prompt: &str) -> String {
    let mut line = String::new();
    println!("{}", prompt);
    std::io::stdin().read_line(&mut line).unwrap();
    return line;
}

#[allow(dead_code)]
// Asks the user a question until they pick a valid answer
pub fn question_with_known_answers<'a>(question: &str, prompt: &str, answers: &'a Vec<Box<str>>) -> &'a str {
    println!("{}", question); 
    std::mem::drop(question);
    let mut answers_string: String = "".to_owned();

    // Formats answer string
    for (i, answer) in answers.iter().enumerate() {
        let answer_line: String = format!("{}) {}\n", i+1, answer).to_owned();
        let a_slice: &str = &answer_line[..];
        answers_string.push_str(a_slice);
    }
    println!("{}", answers_string);
    std::mem::drop(answers_string);

    // Loops through until we have a proper answer
    loop {
        let user_response = read_line_from_user(prompt);
        let res_as_usize = user_response.trim().parse::<usize>();

        // Makes sure it is actually a usize, if not then we go to next iter and ask again.
        if let Err(_) = res_as_usize {
            println!("Input a valid digit");
            continue;
        }

        // Makes sure its within the range
        let res_ref = res_as_usize.as_ref().unwrap_or(&0);
        if res_ref <= &0 || res_ref > &answers.len() {
            println!("Value is not in range");
            continue;
        }
        
        return &answers[*res_ref-1];
    }
}

#[allow(dead_code)]
// Asks the user a question until a condition is met in the callback
pub fn question_with_callback(question: &str, callback: fn(arg: &str) -> bool) -> String {
    loop {
        let user_response = read_line_from_user(question);

        if !callback(&user_response) {
            continue;
        }

        return user_response;
    }
}