
content_regex =\
    {
      "type": "extref",
      "destination": '[^"]*',
      "content": '[^"]*'
    }

good_example_object =\
    {
      "type": "extref",
      "destination": "[puruSha sUkta], 1-44",
      "content": "[puruSha sUkta], 1-44"
    }


def self_test():
    import matcher
    matcher.match(content_regex, good_example_object)


if __name__ == '__main__':
    self_test()
