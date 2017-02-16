import json


with open('symptoms.json', 'r') as fp:
    data = json.load(fp)


causes = {}
for k, v in data.iteritems():
    for cause in v['causes']:
        if cause in causes:
            causes[cause] += 1
        else:
            causes[cause] = 1

print causes
with open('causes.json', 'w') as fp:
    json.dump(causes, fp, sort_keys=True, indent=4)
