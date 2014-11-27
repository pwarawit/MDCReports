# -*- coding: utf-8 -*-

import sys
import time
import csv
import re

orderlinelist = []
inputdata1 = csv.DictReader(open('sale.order.line.csv'))
for row in inputdata1:
    orderlinelist.append(row)


for i in orderlinelist:
    print i['Status']


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4