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

soup = BeautifulSoup(html_content, 'html.parser')

# p_content = soup.find('p')
# # print(p_content)

# p_all_content = soup.find_all('p')
# # print(p_all_content)

# p_with_spec_class = soup.find('p', class_='special')
# print(p_with_spec_class)

