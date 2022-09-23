import sys

md_file_name = sys.argv[1]

my_tags = sys.argv[2:]

TAG_START = '<!--'
TAG_END = '-->'
TAG_CLOSE = '<!--end-->'

with open(md_file_name, 'r') as f:
    within_tag_section = False
    curr_tags = []

    while True:
        should_render = len(my_tags) == 0 or not within_tag_section or any(t in my_tags for t in curr_tags)
        line = f.readline()
        if not line:
            break
        if line.startswith(TAG_CLOSE):
            within_tag_section = False
            curr_tags.clear()
        elif (line.startswith(TAG_START)):
            start_idx = len(TAG_START)
            end_idx = line.index(TAG_END)
            new_tags = line[start_idx:end_idx].strip().split(',')
            curr_tags = [t.strip() for t in new_tags]
            within_tag_section = True
        elif should_render:
            print(line, end='')