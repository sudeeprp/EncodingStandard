
"""Can make this regex better: currently it just requires a type in one of the contents
Actually we require the type in each of the contents"""
content_regex =\
    {
        "content": r'''[\[]({.*?["']type['"]:.*?}[,]?)+[\]]'''
    }

good_example_object =\
    {
      "id": "DFG123",
      "content": [
         {
           "type": "text",
           "content": "Work is superior."
         },
         {
           "type": "phrase",
           "destination": "karmayOga_a_defn",
           "content": "work without attachment"
         },
         {
           "type": "extref",
           "destination": "[puruSha sUkta], 1-44",
           "content": "[puruSha sUkta], 1-44"
         }
      ]
    }


def self_test():
    import matcher
    matcher.match(content_regex, good_example_object)


if __name__ == '__main__':
    self_test()
