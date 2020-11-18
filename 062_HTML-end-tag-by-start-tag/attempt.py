import re


def end_tag_by_start_tag(tag):
    temp = tag.split(" ")[0]
    clear_out = re.sub(r"\W+", "", temp)

    return "</" + clear_out + ">"


print(end_tag_by_start_tag("<button type='button' disabled>"))  # </button>
print(end_tag_by_start_tag("<i>"))  # </i>
