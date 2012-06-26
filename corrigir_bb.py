#!/usr/bin/python

import csv, sys, time, argparse

parser = argparse.ArgumentParser(description='Corrige dados vindos do Banco do Brasil.')
parser.add_argument('arg', type=str, help="Arquivo a ser corrigido")
filename = parser.parse_args().arg

if (filename == None):
   filename = raw_input("qual o nome do arquivo? ") + '.csv'

reader = csv.reader(open(filename, 'rb')) 
writer = csv.writer(open(filename.replace('.csv', '_corrigido.csv'), 'wb'), quoting=csv.QUOTE_ALL)
firstLine = 1
try:
    for row in reader:
        [data, depOrig, hist, dataBalan, docN, valor, e] = row
        if firstLine:
            firstLine = 0
        else:
            tDate = time.strptime(data, "%m/%d/%Y")
	    data = time.strftime("%d/%m/%Y", tDate)
            valor = valor.replace('.', ',')
        row = [data, depOrig, hist, dataBalan, docN, valor]
        writer.writerow(row)
except csv.Error, e:
    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
