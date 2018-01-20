#!/usr/bin/env python3

# Program for encoding decision tree from XKCD Map Age Guide (1688).
# Author: Paul Schulz <paul@mawsonlakes.org>

nodes = {
    'instorconst': {'question': 'Istambul or Constantinople?',
                    'answers': {'Yes': 'soviet',
                                'No': 'canalatok',
                                'Neither': 'ottoman'}
    },
    'soviet': {'question': 'Does the Sov Union Exist?',
               'answers': {'Yes': 'westafrica',
                           'No': 'zaire'}
    },
#    'canalatok': {}
#    'ottoman': {}
#    'westafrica': {}
#    'zaire': {}
}

def print_node(nodedata):
    print(nodedata['question'])
    print (", ".join(nodedata['answers'].keys()))

def ask_node(nodedata):
    answer=input('?> ')
    while(not answer in nodedata['answers'].keys()):
        answer=input('(try again)?> ')
    return answer

def next_node(nodes,node,answer):
    nodedata=nodes[node]
    return nodedata['answers'][answer]

node = 'instorconst'

loop = True
while loop:
    print_node(nodes[node])
    answer=ask_node(nodes[node])
    node=next_node(nodes,node,answer)
