from bs4 import BeautifulSoup

html_doc = """
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
<body>
	<p class="title">
		<b>The Dormouse's story</b>
	</p>
	<p class="story">Once upon a time there were three little sisters; and their names were
	<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
	<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
	<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
	and they lived at the bottom of a well.</p>
	<p class="story">...</p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
#search for first p tag
first_p =soup.find('p')
print first_p
#search and print all a tags and number of a tags.
a_tags=soup.find_all('a')
print a_tags
#a_tags is a list
print len(a_tags)
#search by classes
p_tag=soup.find('p',class_="story")
print p_tag
#finds only one class
#to find all p tags of class story we use 
p_tags=soup.find_all('p',class_="story")
print p_tags
#gives a list containing all the number of tags
#other attributes like id 
a=soup.find_all('a',{'id':'link1'})
print a
#prints the anchor tag with id link1

# tag name and a string inside a tag
a_name=soup.find_all('a',string='Elsie')
print a_name

##travel inside an html tree structure

# search for all child 
p=soup.find('p',class_='story')

all_p_children=p.findChildren()
print all_p_children

#finding the parent
p_parent=p.findParent()
print p_parent

#search for all next sibling 
first_a=soup.find('a');
all_a_sibling=first_a.findNextSiblings()
print all_a_sibling












