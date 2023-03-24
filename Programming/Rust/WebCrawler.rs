//This crawler starts at a specified URL (start_url), and keeps track of visited URLs in a HashSet.
//It uses the reqwest crate to make HTTP requests and fetch the HTML content of each page.
//It then uses the select crate to parse the HTML and extract links from anchor (<a>) tags.
//Links are added to urls_to_visit if they haven't been visited before and start with "http".
//The process continues until there are no more URLs to visit in urls_to_visit.
//This version of the crawler uses the read_urls_from_file function to read URLs from the "manual_webcrawl" file and populate the urls_to_visit vector.
//The read_urls_from_file function reads each line from the file and adds it to a vector of URLs, which is then returned.
//To use this version of the crawler, simply create a file named "manual_webcrawl" in the same directory as the Rust source code, and add one URL per line to the file.
//When you run the Rust code, the crawler will read URLs from the file and crawl each of them in turn.

use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};
use select::document::Document;
use select::predicate::{Name, Attr};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut visited_urls = HashSet::new();
    let mut urls_to_visit = read_urls_from_file("manual_webcrawl")?;

    while let Some(url) = urls_to_visit.pop() {
        if visited_urls.contains(&url) {
            continue;
        }
        visited_urls.insert(url.clone());

        let body = reqwest::get(&url).await?.text().await?;

        let document = Document::from(body.as_str());

        for link in document.find(Name("a")).filter_map(|n| n.attr("href")) {
            if !link.starts_with("http") {
                continue;
            }
            if !visited_urls.contains(link) {
                urls_to_visit.push(link.to_string());
            }
        }
    }

    Ok(())
}

fn read_urls_from_file(file_path: &str) -> Result<Vec<String>, std::io::Error> {
    let file = File::open(file_path)?;
    let reader = BufReader::new(file);
    let mut urls = Vec::new();
    for line in reader.lines() {
        let url = line?;
        urls.push(url);
    }
    Ok(urls)
}
