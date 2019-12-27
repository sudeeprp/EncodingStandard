
content_regex =\
    {
        "id": '[^"]*'
    }

good_example_object =\
    {
      "id": "DEF123",
      "any other stuff": "can be here"
    }


def self_test():
    import matcher
    matcher.match(content_regex, good_example_object)


if __name__ == '__main__':
    self_test()
