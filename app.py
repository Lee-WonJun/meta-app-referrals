from bs4 import BeautifulSoup
import csv
import re

user_id = input('Enter your user ID: ')

with open('./apps.html', 'r', encoding='UTF-8') as f:
    html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

pattern = re.compile(r'https://www.oculus.com/experiences/quest/\d+/')
label_pattern = re.compile(r'Link to view the product page of (.+)')
referral_prefix = "https://www.oculus.com/appreferrals"


a_tags = soup.find_all('a', {'aria-label': True, 'href': True})
filtered = [a_tag for a_tag in a_tags if pattern.match(a_tag['href']) and label_pattern.match(a_tag['aria-label'])]
make_tuple = lambda a_tag: (label_pattern.match(a_tag['aria-label']).group(1), a_tag['href'], f"{referral_prefix}/{user_id}/{a_tag['href'].split('/')[-2]}")
result = [ make_tuple(a_tag)   for a_tag in filtered ]
# save to csv
with open('./apps.csv', 'w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product Name', 'Original Link', 'Referral Link'])
    writer.writerows(result)
