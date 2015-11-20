import os
import string
import re

def get_absolute_paths(directory):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    rules_dir = os.path.join(current_dir, directory)
    for dirpath,_,filenames in os.walk(rules_dir):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


def get_rules():
    censored_phrases = {}
    for file in get_absolute_paths('rules'):
        with open(file) as f:
            for line in f.readlines():
                if not line.startswith('##') and line.count('%')==1:
                    expression, reason = line.split('%')
                    expression = expression.rstrip()
                    reason = reason.strip()
                    if reason:
                        check_type = reason.split()[0]
                        if check_type == 'syntax':
                            re_exp = expression
                            regex = re.compile(re_exp)
                        elif check_type == 'capitalize':
                            re_exp = r'\b%s\b' % expression
                            regex = re.compile(re_exp)
                        elif check_type == 'phrase':
                            expression = re.sub('/ +/', '\s+', expression)
                            expression = re.sub('/([a-zA-Z\)])$/', '\1\b', expression)
                            re_exp = r'\b%s\b' % expression
                            regex = re.compile(re_exp, re.IGNORECASE)
                        elif check_type == 'spelling':
                            re_exp = r'\b%s\b' % expression
                            regex = re.compile(re_exp, re.IGNORECASE)
                        censored_phrases[regex] = reason
    return censored_phrases


def match(censored_phrases, text):
    problems = []
    characters = 128
    for ind, line in enumerate(text.split('\n')):
        for regex, reason in censored_phrases.items():
            m = regex.search(line)
            if m:
                extra = int((characters - (m.end() - m.start())) / 2)
                context = line[m.start() - extra: m.end() + extra]
                problems.append((ind+1, m.span(), context, regex.pattern, reason))
    problems = sorted(problems, key=lambda x: x[0])
    problems = ['L%d[%d:%d]:\t%s\t(%s)' % (p[0], p[1][0], p[1][1], p[2], p[4]) for p in problems]
    return problems

def check(self, code, filename):
    """Run academic-writing-checker on code and return the output."""

    print ("Called academic-writing-checker ...")
    return []