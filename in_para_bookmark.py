
content_regex =\
    {
        "type": "anchor",
        "name": '[^"]*',
        "content": '[^"]*'
    }

good_example_object =\
    {
        "type": "anchor",
        "name": "karmayOga",
        "content": ""
    }


def self_test():
    import matcher
    matcher.match(content_regex, good_example_object)


if __name__ == '__main__':
    self_test()
