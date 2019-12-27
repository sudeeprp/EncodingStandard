
content_regex =\
    {
        "type": "phrase",
        "destination": '[^"]*',
        "content": '[^"]*'
    }

good_example_object =\
    {
        "type": "phrase",
        "destination": "karmayOga_a_defn",
        "content": "work without attachment"
    }


def self_test():
    import matcher
    matcher.match(content_regex, good_example_object)


if __name__ == '__main__':
    self_test()
