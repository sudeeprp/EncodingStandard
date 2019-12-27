
"""Can make this regex better: currently it just requires a type in one of the contents
Actually we require the type in each of the contents"""
content_regex =\
    {
        "content": r'''[\[]({.*?["']type['"]:.*?}[,]?)+[\]]'''
    }

good_example_object =\
    {
        "paragraphs": [
            {
                "id": "no-content",
                "content": [
                    {
                        "type": "text",
                        "content": ""
                    }
                ]
            },
            {
                "id": "all-content",
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

        ]
    }


def paralist(encoded_docx):
    return encoded_docx['paragraphs']


def contentlist(para):
    return para['content']


def pick_para(paras, para_id):
    picked_paras = [x for x in paras if x['id'] == para_id]
    if len(picked_paras) > 1:
        print(f'--Warning: multiple paras with same id: {picked_paras}')
    return picked_paras[0]


def pick_contents(contents, content_filter):
    return [x for x in contents if content_filter(x)]


def self_test():
    import matcher
    para_with_no_content = pick_para(paralist(good_example_object), 'no-content')
    matcher.match(content_regex, para_with_no_content)

    para_with_content = pick_para(paralist(good_example_object), 'all-content')
    matcher.match(content_regex, para_with_content)

    text_content = pick_contents(contentlist(para_with_content), lambda x: x['type'] == 'text')
    if text_content[0]['type'] == 'text':
        print('Self-test passed')


if __name__ == '__main__':
    self_test()
