
content_regex =\
    {
        "type": "text",
        "content": '[^"]*'
    }

good_example_object =\
    {
      "type": "text",
      "content": "Work is superior."
    }


def self_test():
    import matcher
    matcher.match(content_regex, good_example_object)


if __name__ == '__main__':
    self_test()
