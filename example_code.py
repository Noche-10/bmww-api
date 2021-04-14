from bmwwAPI import bmww

# Create api object
api = bmww()

# try creating a work instance of api with id 487
# If an exception/error is found, do nothing
# If an exception/error is not found, print 'Searching:' and the work url

try:
    work = api.work(487)
    # '487' being the work id
except:
    pass
else:
    print('Searching: ' + str(work.url))

# Index variable

index = 0

# Gets information from work and puts it in a list

work_info = [

    work.title,
    work.author,
    work.summary,
    work.reviews,
    work.chapters,
    work.completed,
    work.words,
    work.read,
    work.published,
    work.updated

]


# List for labels

label = [

    "Title:",
    "Author:",
    "Summary:",
    "Reviews:",
    "Chapters:",
    "Completed:",
    "Words:",
    "Read:",
    "Published:",
    "Updated:"
]

# For every item in the list work_info, print the first item from the label list then item then new line,
# If Index is not equals to the length of work_info, add 1 to index, repeat process until index is equals to
# Lenght info

for item in work_info:
    print(label[index], item, end="\n")
    if index != len(work_info):
        index += 1

# This code will print something like this:

'''
Searching: https://batmanwonderwoman.com/fanfiction/viewstory.php?sid=487&warning=0
Title: Alone
Author: LOTSloverCSS
Summary: Batman battles his thoughts and feelings for Wonder Woman.� Which side of him will win out?� Written from Bruce�s POV.
Reviews: 4
Chapters:  1
Completed:  Yes
Words:  3934
Read:  2286
Published: 01.24.2014
Updated:  01.24.2014
'''

# --------------------------------------------------------------------------------------------------------------------------------------------


# For user information just do

user = api.users(13813)
# '13813' being the work id

# Then you can get the information out of the user ('The information that the user has in their profile')

# Refer to the readme for more information in what information you can get and with what commands
