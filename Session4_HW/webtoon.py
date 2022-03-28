def extract_info(toon_list):
    result = []

    for toon in toon_list:
        title = toon.find("dl").find("a").string
        name = toon.find("dd", {"class": "desc"}).find("a").string
        star = toon.find("div", {"class": "rating_type"}).find("strong").string
        toon_info = {
            'title': title,
            'name': name,
            'star': star
        }
        result.append(toon_info)
    return result
