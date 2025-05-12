from bs4 import BeautifulSoup

# html_content = """
# <html>
# <body>
#     <h1>This is a heading</h1>
#     <p>This is a paragraph.</p>
#     <p class="special">This is another paragraph.</p>
# </body>
# </html>
# """

html_content = """
        <html>
        <body>
            <div id="main-content">
                <h1>This is a heading</h1>
                <p class="important">This is an important paragraph.</p>
                <a href="https://www.example.com">Visit Example</a>
            </div>
        </body>
        </html>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# p_content = soup.find('p')
# # print(p_content)

# p_all_content = soup.find_all('p')
# # print(p_all_content)

# p_with_spec_class = soup.find('p', class_='special')
# print(p_with_spec_class)

main_content = soup.select_one('#main-content')
important_paragraph = main_content.select_one('.important')

paragraph_text = important_paragraph.get_text()

print(paragraph_text)

link = main_content.select_one('a')
link_url = link['href']

print(link_url)

