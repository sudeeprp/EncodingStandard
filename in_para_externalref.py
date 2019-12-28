import re

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


def expand_extref_in_text_content(content):
    text = content['content']
    whole_ref_regex = r'(\[[\w\s,-]+](?:(?:,\s[0-9\-]*)?:?)?)'
    components = re.split(whole_ref_regex, text)
    # get rid of empties and Nones
    components = [c for c in components if c is not None and c != '']
    extracts = []
    for text_component in components:
        if text_component.startswith('['):
            extracts.append({"type": "extref",
                             "destination": text_component,
                             "content": text_component})
        else:
            extracts.append({"type": 'text',
                             "content": text_component})
    return extracts


sample_extrefs = [
    '[vishNu purAna], 6-7-28:',
    '[purusha sUkta]:',
    '[purusha sUkta]',
    '[purusha sUkta],',
    '[kaTha upanishat, 2-23]',
    '[mahAnArayaNa], 45:'
]

not_extrefs = [
    '[akShara vidya], the'
]


def test_reference_is_extracted():
    import matcher
    extract_ok = True
    for ref in sample_extrefs:
        text_with_inline_ref = 'Some text ' + ref + ' some other text'
        expanded_content = expand_extref_in_text_content\
            ({"type": "text", "content": text_with_inline_ref})
        assert len(expanded_content) == 3
        assert matcher.match(content_regex, expanded_content[1])
        if expanded_content[1]["content"].strip() != ref:
            print(f'Reference {ref} not extracted')
            extract_ok = False
    if extract_ok:
        print("Extref extraction self-test passed")


def self_test():
    import matcher
    matcher.match(content_regex, good_example_object)
    test_reference_is_extracted()


if __name__ == '__main__':
    self_test()
