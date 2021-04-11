# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def generateInsert(table,*records):
    result= 'INSERT INTO %s VALUES  %s ' % (table,records)
    print(result)
    return table,records
a=generateInsert('Students',1,'Jane', 'A+')
b=generateInsert('Phones', 42, '312-555-1212') 
#print(a)
#print(b)

#############################
'''
table='Students'
pkid=int(1)
name= 'Jane'
grade= 'A+'
data= ' %d %s %s'%( pkid, name, grade)
d=data.split()
rec=','.join(d)
print('INSERT INTO Students VALUES('+ rec+')')
'''