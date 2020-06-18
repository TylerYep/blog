""" This script creates tags for your Jekyll blog hosted by Github page. """
import glob
import os

post_dir = "_posts/"
tag_dir = "tag/"

filenames = glob.glob(post_dir + "*md")

total_tags = []
for filename in filenames:
    with open(filename, encoding="utf8") as f:
        crawl = False
        for line in f:
            if crawl:
                current_tags = line.strip().split()
                if current_tags[0] == "tags:":
                    total_tags.extend(current_tags[1:])
                    break
            if line.strip() == "---":
                if crawl:
                    break
                crawl = True
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + "*.md")
for tag in old_tags:
    os.remove(tag)

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + ".md"
    with open(tag_filename, "a") as f:
        f.write(f'---\nlayout: tagpage\ntitle: "Tag: {tag}"\ntag: {tag}\nrobots: noindex\n---\n')

print("Tags generated, count", len(total_tags))
