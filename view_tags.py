import sys

md_file_name = sys.argv[1]

TAG_START = '<!--'
TAG_END = '-->'
TAG_CLOSE = '<!--end-->'

with open(md_file_name, 'r') as f:
    curr_tags = set()

    while True:
        line = f.readline()
        if not line:
            break
        if line.startswith(TAG_CLOSE):
            continue
        elif (line.startswith(TAG_START)):
            start_idx = len(TAG_START)
            end_idx = line.index(TAG_END)
            new_tags = line[start_idx:end_idx].strip().split(',')
            curr_tags |= {t.strip() for t in new_tags}

    print('All tags used in \"{}\":'.format(md_file_name))
    for t in curr_tags:
        print(" -", t)