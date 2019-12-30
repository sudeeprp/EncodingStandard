import re
import json
import remover


def string_rep(a):
    if a is None:
        return None
    return str(a)


def match(content_regex, good_example_object):
    for key in content_regex:
        if key not in good_example_object or\
                not re.match(content_regex[key], string_rep(good_example_object[key])):
            print(f'''--Regex not matched:
                    Expected:\n{json.dumps(content_regex)}
                    Actual:\n{json.dumps(good_example_object)}''')
            return False
    print(f'Self-test passed')
    return True


def search(content_regex, good_example_object):
    example_as_jsonstr_nospace = remover.strip_whitespaces(json.dumps(good_example_object))
    expected_regex_nospace = remover.strip_whitespaces(content_regex)
    if re.search(expected_regex_nospace, example_as_jsonstr_nospace) is None:
        print(f'--Regex not matched: {content_regex}')
        print(f'searched for: {expected_regex_nospace}')
        print(f'in: {example_as_jsonstr_nospace}')
    else:
        print(f'Self-test passed')
