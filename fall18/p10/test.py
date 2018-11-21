import os, sys, subprocess, json, re, collections

Question = collections.namedtuple("Question", ["number", "weight"])

questions = [
    Question(number=1, weight=1),
]
question_nums = set([q.number for q in questions])

expected_json = None
with open('expected.json') as f:
    expected_json = json.load(f)

# find a comment something like this: #q10
def extract_question_num(cell):
    for line in cell.get('source', []):
        line = line.strip().replace(' ', '').lower()
        m = re.match(r'\#q(\d+)', line)
        if m:
            return int(m.group(1))
    return None

# rerun notebook and return parsed JSON
def rerun_notebook(orig_notebook):
    new_notebook = 'cs-301-test.ipynb'

    # re-execute it from the beginning
    cmd = 'jupyter nbconvert --execute {orig} --to notebook --output={new}'
    cmd = cmd.format(orig=orig_notebook, new=new_notebook)
    subprocess.check_output(cmd, shell=True)

    # parse notebook
    with open(new_notebook) as f:
        nb = json.load(f)
    return nb

def normalize_json(orig):
    try:
        return json.dumps(json.loads(orig.strip("'")), indent=2, sort_keys=True)
    except:
        return 'not JSON'

def check_cell_json(qnum, cell):
    actual_lines = cell.get('outputs', [])[0].get('data', {}).get('text/plain', [])
    actual = normalize_json(''.join(actual_lines))
    expected = normalize_json(expected_json[str(qnum)])
    if actual == expected:
        return 'PASS'
    return 'mismatch'

def check_cell(qnum, cell):
    if str(qnum) in expected_json:
        return check_cell_json(qnum, cell)

    return "PASS"

def grade_answers(cells):
    results = {'score':0, 'tests': []}

    for question in questions:
        cell = cells.get(question.number, None)
        status = "not found"

        if question.number in cells:
            status = check_cell(question.number, cells[question.number])

        row = {"test": question.number, "result": status, "weight": question.weight}
        results['tests'].append(row)

    return results

def main():
    # rerun everything
    orig_notebook = 'main.ipynb'
    if len(sys.argv) > 2:
        print("Usage: test.py main.ipynb")
        return
    elif len(sys.argv) == 2:
        orig_notebook = sys.argv[1]
    nb = rerun_notebook(orig_notebook)

    # extract cells that have answers
    answer_cells = {}
    for cell in nb['cells']:
        q = extract_question_num(cell)
        if q == None:
            continue
        if not q in question_nums:
            print('no question %d' % q)
            continue
        answer_cells[q] = cell

    results = grade_answers(answer_cells)
    print(results)

if __name__ == '__main__':
    main()