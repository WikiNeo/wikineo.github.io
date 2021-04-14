import os
import glob

# save all files ending with .md and .html to filenames list
post_dir = '_posts/*/*'
file_types = ['.md', '.html']
tag_dir = 'tag/'
filenames = []
for file_type in file_types:
    filenames.extend(glob.glob(post_dir + file_type))

# Store values in between --- & --- starting with tags: to total_tags
total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'tags:':
                total_tags.extend(current_tags[1:])
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

# remove old tag files in tag_dir
old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

# create tag_dir if not exist
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

# generate tag files with content
for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()

# do some summary log
print("Tags generated, count", total_tags.__len__())