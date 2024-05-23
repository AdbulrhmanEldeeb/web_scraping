from requests_html import HTMLSession
import csv
import time

# Function to fetch and parse the page content
def fetch_page(session, url, headers):
    response = session.get(url, headers=headers)
    response.raise_for_status()
    return response.html

# Function to extract data from the containers and write to CSV
def extract_data_and_write_to_csv(html, writer):
    containers = html.find('div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small')
    print(f"Found {len(containers)} containers")

    for container in containers:
        name = container.find('span.a-size-base-plus.a-color-base.a-text-normal', first=True)
        price = container.find('span.a-price-whole', first=True)
        number_of_reviews = container.find('span.a-size-base.s-underline-text', first=True)
        stars = container.find('i.a-icon.a-icon-star-small.a-star-small-4-5.aok-align-bottom', first=True)
        link=container.find('a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')
        
        # Extract text or set default value if element is missing
        name_text = name.text if name else 'N/A'
        price_text = price.text if price else 'N/A'
        number_of_reviews_text = number_of_reviews.text if number_of_reviews else 'N/A'
        stars_text = stars.text if stars else 'N/A'
        
        link='https://www.amazon.eg' + link[0].attrs['href']  if link else 'N/A'
        row = [name_text, price_text, stars_text, number_of_reviews_text,link]
        writer.writerow(row)
        print(f"Scraped data: {row}")

# Main function to scrape multiple pages
def scrape_amazon(num_pages=5):
    base_url = 'https://www.amazon.eg/s?k=nvme&page={page}&crid=1CWCD4IM9PKWJ&sprefix=nv%2Caps%2C150&ref=sr_pg_{page}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }
    
    session = HTMLSession()
    header_row = ['item', 'price', 'stars', 'num_of_reviews','link']

    with open('nvme.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header_row)
        
        for page in range(1, num_pages + 1):
            url = base_url.format(page=page)
            print(f"Scraping page {page}: {url}")
            html = fetch_page(session, url, headers)
            extract_data_and_write_to_csv(html, writer)
            time.sleep(2)  # To avoid being blocked by Amazon

# Running the scraper for the first 5 pages
scrape_amazon(5)
