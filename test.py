#!/usr/bin/python

__author__ = 'vickydasta'
__app__ = 'grammar ripper'

'''
---------------
Grammar Ripper
---------------
a confuser machine to shuffle your sentence and will make your grammar looking bad
'''
#starting engine
# grammaripper/kernel/* --> grammar ripper module
# grammaripper/kernel/tobe.py --> list of tobe in English obviously
# grammaripper/kernel/procword.py --> word processor

from kernel.core import *

while True:
    try:
        sentence = raw_input('new sentence .> ')
        print '-> ',sentence2word(sentence)
        print '-> ',ripthegrammar(ripp(sentence))
    except KeyboardInterrupt:
        print '\ninterrupted by user'
        exit()
    except Exception as e:
        logging.error(e)
