'''
Some useful utility functions.
'''
import json

def dirr(obj):
    return [attr for attr in dir(obj) if attr[:1] != '_']

def csv2json(filename):
    list_of_people = []
    with open(filename) as file:
        header = file.readline().strip().split(',')
        for line in file:
            data = line.strip().split(',')
            p1 = dict(zip(header, data))
            list_of_people.append(p1)

    # file is automatically closed here
    dot_index = filename.index('.')
    new_filename = filename[:dot_index] + '.json'
    
    with open(new_filename, 'w') as file:
        json.dump(list_of_people, file, indent=3)

def csv2json_v2(filename):
    with open(filename) as file:
        header = file.readline().strip().split(',')
        list_of_people = [
            dict(zip(header, line.strip().split(',')))
            for line in file
        ]
        
    dot_index = filename.index('.')
    new_filename = filename[:dot_index] + '.json'
    
    with open(new_filename, 'w') as new_file:
        json.dump(list_of_people, new_file, indent=3)


def json2csv(filename):
    with open(filename) as file:
        data = json.load(file)
        header = ','.join(data[0].keys()) + '\n'
        rows = [
            ','.join(d.values()) + '\n'
            for d in data
        ]
        rows.insert(0, header)
        with open('output.csv', 'w') as outfile: outfile.writelines(rows)


def main():
    # csv2json_v2('people.csv')
    # print('JSON file has been generated!')
    json2csv('people.json')
    print('CSV file has been generated!')

if __name__=='__main__': main()