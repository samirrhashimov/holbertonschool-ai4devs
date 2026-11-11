def add_tag_to_item(item_name, tag, tags_list=[]):
    tags_list.append(tag)
    return {
        "item": item_name,
        "tags": tags_list
    }


item1 = add_tag_to_item("Laptop", "electronics")
item2 = add_tag_to_item("Chair", "furniture")

print(item1)
print(item2)