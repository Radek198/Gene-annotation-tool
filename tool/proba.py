import csv



with open('goa_human_complex.gaf') as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)
    for lis in d:
        string = ''.join(lis)
        record = []
        if string.find('!'):
            record.append(lis[2])
            record.append(lis[5])

            print(lis)

            print(record)

