//This crawler starts at a specified URL (start_url), and keeps track of visited URLs in a HashSet.
//It uses the reqwest crate to make HTTP requests and fetch the HTML content of each page.
//It then uses the select crate to parse the HTML and extract links from anchor (<a>) tags.
//Links are added to urls_to_visit if they haven't been visited before and start with "http".
//The process continues until there are no more URLs to visit in urls_to_visit.
