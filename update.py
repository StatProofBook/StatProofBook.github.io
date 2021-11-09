#!/usr/bin/env python
"""
Index Generator for The Book of Statistical Proofs
_
This script loads all files from the proof/definition directories and
- checks if they are in "Table of Contents" (structured overview)
- writes them as a list into "Proof by Number" (chronological list)
- writes them as a list into "Proof by Topic" (an alphabetical list)
- writes them as a list into "Proof by Author" (sorted by contributor)
- writes them as a list into "Proofs without Source" (no references)
- writes them as a list into "Definition by Number" (chronological list)
- writes them as a list into "Definition by Topic" (an alphabetical list)
- writes them as a list into "Definition by Author" (sorted by contributor)
- writes them as a list into "Definitions without Source" (no references)

Author: Joram Soch, BCCN Berlin
E-Mail: joram.soch@bccn-berlin.de

First edit: 2019-09-27 12:55:00
 Last edit: 2021-11-05 07:12:00
"""


# Import modules
#-----------------------------------------------------------------------------#
import os
import re
import numpy as np
from datetime import datetime

# List files in proof directory
#-----------------------------------------------------------------------------#
files     = os.listdir('P/')
proofs    = dict()
pr_ids    = []
pr_nos    = []
pr_titles = []
pr_users  = []

# Browse through list of files
#-----------------------------------------------------------------------------#
for file in files:
    if '.md' in file:
        
        # Read proof file
        #---------------------------------------------------------------------#
        file_obj = open('P/' + file, 'r')
        file_txt = file_obj.readlines()
        file_obj.close()
        
        # Parse YAML header
        #---------------------------------------------------------------------#
        source = False
        for line in file_txt:
            if line.find('proof_id:') == 0:
                proof_id = re.sub('"', '', line[10:-1])
            if line.find('shortcut:') == 0:
                shortcut = re.sub('"', '', line[10:-1])
            if line.find('title:') == 0:
                title      = re.sub('"', '', line[7:-1])
                title_edit = re.sub('[^a-zA-Z- ]', '', title)
                title_sort = title_edit.upper()
            if line.find('author:') == 0:
                author = re.sub('"', '', line[8:-1])
            if line.find('username:') == 0:
                username = re.sub('"', '', line[10:-1])
                if not username:
                    if not author:
                        username = 'unknown'
                    else:
                        username = author
            if line.find('date:') == 0:
                date = datetime.strptime(line[6:-1], '%Y-%m-%d %H:%M:%S')
            if line.find('  - authors:') == 0:
                source = True
        
        # Write dictionary entry
        #---------------------------------------------------------------------#
        proofs[proof_id] = {'proof_id': proof_id, 'shortcut': shortcut, 'title': title, \
                            'username': username, 'date': date, 'source': source}
        pr_ids.append(proof_id)
        pr_nos.append(int(proof_id[1:]))
        pr_titles.append(title_sort)
        pr_users.append(username)

# List files in definition directory
#-----------------------------------------------------------------------------#
files       = os.listdir('D/')
definitions = dict()
def_ids     = []
def_nos     = []
def_titles  = []
def_users   = []

# Browse through list of files
#-----------------------------------------------------------------------------#
for file in files:
    if '.md' in file:
        
        # Read proof file
        #---------------------------------------------------------------------#
        file_obj = open('D/' + file, 'r')
        file_txt = file_obj.readlines()
        file_obj.close()
        
        # Parse YAML header
        #---------------------------------------------------------------------#
        source = False
        for line in file_txt:
            if line.find('def_id:') == 0:
                def_id = re.sub('"', '', line[8:-1])
            if line.find('shortcut:') == 0:
                shortcut = re.sub('"', '', line[10:-1])
            if line.find('title:') == 0:
                title      = re.sub('"', '', line[7:-1])
                title_edit = re.sub('[^a-zA-Z- ]', '', title)
                title_sort = title_edit.upper()
            if line.find('author:') == 0:
                author = re.sub('"', '', line[8:-1])
            if line.find('username:') == 0:
                username = re.sub('"', '', line[10:-1])
                if not username:
                    if not author:
                        username = 'unknown'
                    else:
                        username = author
            if line.find('date:') == 0:
                date = datetime.strptime(line[6:-1], '%Y-%m-%d %H:%M:%S')
            if line.find('  - authors:') == 0:
                source = True
        
        # Write dictionary entry
        #---------------------------------------------------------------------#
        definitions[def_id] = {'def_id': def_id, 'shortcut': shortcut, 'title': title, \
                               'username': username, 'date': date, 'source': source}
        def_ids.append(def_id)
        def_nos.append(int(def_id[1:]))
        def_titles.append(title_sort)
        def_users.append(username)

# Output number of proof files
#-----------------------------------------------------------------------------#
print('\n-> StatProofBook Index Generator:')
print('   - ' + str(len(proofs)) + ' files found in proof directory!')
print('   - ' + str(len(definitions)) + ' files found in definition directory!')


# Table of Contents: read index file
#-----------------------------------------------------------------------------#
print('\n1. Table of Contents:')
ind1 = open('I/ToC.md', 'r')
tocs = ind1.readlines()
ind1.close()

# Table of Contents: check for proof Shortcuts
#-----------------------------------------------------------------------------#
incl = np.zeros(len(proofs), dtype=bool)
for (i, proof) in enumerate(proofs):
    for line in tocs:
        if line.find('(/P/' + proofs[proof]['shortcut'] + ')') > -1:
            incl[i] = True
    if ~incl[i]:
        print('   - WARNING: proof "' + proofs[proof]['shortcut'] + '" is not in table of contents!')
if all(incl):
    print('   - ' + str(sum(incl)) + ' proofs found in table of contents!')

# Table of Contents: check for definition Shortcuts
#-----------------------------------------------------------------------------#
incl = np.zeros(len(definitions), dtype=bool)
for (i, definition) in enumerate(definitions):
    for line in tocs:
        if line.find('(/D/' + definitions[definition]['shortcut'] + ')') > -1:
            incl[i] = True
    if ~incl[i]:
        print('   - WARNING: definition "' + definitions[definition]['shortcut'] + '" is not in table of contents!')
if all(incl):
    print('   - ' + str(sum(incl)) + ' definitions found in table of contents!')


# Proof by Number: prepare index file
#-----------------------------------------------------------------------------#
print('\n2a.Proof by Number:')
ind2a = open('I/PbN.md', 'w')
ind2a.write('---\nlayout: page\ntitle: "Proof by Number"\n---\n\n\n')
ind2a.write('| ID | Shortcut | Theorem | Author | Date |\n')
ind2a.write('|:-- |:-------- |:------- |:------ |:---- |\n')

# Proof by Number: sort by Proof ID
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(pr_nos)])]
for i in sort_ind:
    ind2a.write('| ' + proofs[pr_ids[i]]['proof_id'] + ' | ' + proofs[pr_ids[i]]['shortcut'] + ' | [' + \
                       proofs[pr_ids[i]]['title'] + '](/P/' + proofs[pr_ids[i]]['shortcut'] + ') | ' + \
                       proofs[pr_ids[i]]['username'] + ' | ' + proofs[pr_ids[i]]['date'].strftime('%Y-%m-%d') + ' |\n')
ind2a.close()
print('   - successfully written to disk!')


# Definition by Number: prepare index file
#-----------------------------------------------------------------------------#
print('\n2b.Definition by Number:')
ind2b = open('I/DbN.md', 'w')
ind2b.write('---\nlayout: page\ntitle: "Definition by Number"\n---\n\n\n')
ind2b.write('| ID | Shortcut | Theorem | Author | Date |\n')
ind2b.write('|:-- |:-------- |:------- |:------ |:---- |\n')

# Definition by Number: sort by Definition ID
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(def_nos)])]
for i in sort_ind:
    ind2b.write('| ' + definitions[def_ids[i]]['def_id'] + ' | ' + definitions[def_ids[i]]['shortcut'] + ' | [' + \
                       definitions[def_ids[i]]['title'] + '](/D/' + definitions[def_ids[i]]['shortcut'] + ') | ' + \
                       definitions[def_ids[i]]['username'] + ' | ' + definitions[def_ids[i]]['date'].strftime('%Y-%m-%d') + ' |\n')
ind2b.close()
print('   - successfully written to disk!')


# Proof by Topic: prepare index file
#-----------------------------------------------------------------------------#
print('\n3a.Proof by Topic:')
ind3a = open('I/PbT.md', 'w')
ind3a.write('---\nlayout: page\ntitle: "Proof by Topic"\n---\n\n\n')

# Proof by Topic: sort by Title
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(pr_titles)])]
for i in range(0,len(pr_titles)):
    shortcut   = proofs[pr_ids[sort_ind[i]]]['shortcut']
    title      = proofs[pr_ids[sort_ind[i]]]['title']
    title_sort = pr_titles[sort_ind[i]]
    if i == 0:
        ind3a.write('### ' + title_sort[0] + '\n\n')
    else:
        if title_sort[0] != pr_titles[sort_ind[i-1]][0]:
            ind3a.write('\n### ' + title_sort[0] + '\n\n')
    ind3a.write('- [' + title + '](/P/' + shortcut + ')\n')
ind3a.close()
print('   - successfully written to disk!')


# Definition by Topic: prepare index file
#-----------------------------------------------------------------------------#
print('\n3b.Definition by Topic:')
ind3b = open('I/DbT.md', 'w')
ind3b.write('---\nlayout: page\ntitle: "Definition by Topic"\n---\n\n\n')

# Definition by Topic: sort by Title
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(def_titles)])]
for i in range(0,len(def_titles)):
    shortcut   = definitions[def_ids[sort_ind[i]]]['shortcut']
    title      = definitions[def_ids[sort_ind[i]]]['title']
    title_sort = def_titles[sort_ind[i]]
    if i == 0:
        ind3b.write('### ' + title_sort[0] + '\n\n')
    else:
        if title_sort[0] != def_titles[sort_ind[i-1]][0]:
            ind3b.write('\n### ' + title_sort[0] + '\n\n')
    ind3b.write('- [' + title + '](/D/' + shortcut + ')\n')
ind3b.close()
print('   - successfully written to disk!')


# Proof by Author: prepare index file
#-----------------------------------------------------------------------------#
print('\n4a.Proof by Author:')
ind4a = open('I/PbA.md', 'w')
ind4a.write('---\nlayout: page\ntitle: "Proof by Author"\n---\n\n')

# Proof by Authors: sort by Username
#-----------------------------------------------------------------------------#
unique_users = list(set(pr_users))
unique_users.sort()
for user in unique_users:
    user_proofs = [proof for proof in proofs.values() if proof['username'] == user]
    if len(user_proofs) == 1:
        ind4a.write('\n### ' + user + ' (1 proof)\n\n')
    else:
        ind4a.write('\n### ' + user + ' (' + str(len(user_proofs)) + ' proofs)\n\n')
    user_titles = []
    for proof in user_proofs:
        user_titles.append(proof['title'])
    sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(user_titles)])]
    for i in range(0,len(user_titles)):
        shortcut = user_proofs[sort_ind[i]]['shortcut']
        title    = user_proofs[sort_ind[i]]['title']
        ind4a.write('- [' + title + '](/P/' + shortcut + ')\n')
ind4a.close()
print('   - successfully written to disk!')


# Definition by Author: prepare index file
#-----------------------------------------------------------------------------#
print('\n4b.Definition by Author:')
ind4a = open('I/DbA.md', 'w')
ind4a.write('---\nlayout: page\ntitle: "Definition by Author"\n---\n\n')

# Definition by Authors: sort by Username
#-----------------------------------------------------------------------------#
unique_users = list(set(def_users))
unique_users.sort()
for user in unique_users:
    user_definitions = [definition for definition in definitions.values() if definition['username'] == user]
    if len(user_definitions) == 1:
        ind4a.write('\n### ' + user + ' (1 definition)\n\n')
    else:
        ind4a.write('\n### ' + user + ' (' + str(len(user_definitions)) + ' definitions)\n\n')
    user_titles = []
    for definition in user_definitions:
        user_titles.append(definition['title'])
    sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(user_titles)])]
    for i in range(0,len(user_titles)):
        shortcut = user_definitions[sort_ind[i]]['shortcut']
        title    = user_definitions[sort_ind[i]]['title']
        ind4a.write('- [' + title + '](/D/' + shortcut + ')\n')
ind4a.close()
print('   - successfully written to disk!')


# Proofs without Source: prepare index file
#-----------------------------------------------------------------------------#
print('\n5a.Proofs without Source:')
ind5a = open('I/PwS.md', 'w')
ind5a.write('---\nlayout: page\ntitle: "Proofs without Source"\n---\n\n\n')

# Proofs without Source: sort by Title
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(pr_titles)])]
for i in range(0,len(pr_titles)):
    shortcut = proofs[pr_ids[sort_ind[i]]]['shortcut']
    title    = proofs[pr_ids[sort_ind[i]]]['title']
    source   = proofs[pr_ids[sort_ind[i]]]['source']
    if not source:
        ind5a.write('- [' + title + '](/P/' + shortcut + ')\n')
ind5a.close()
print('   - successfully written to disk!')


# Definitions without Source: prepare index file
#-----------------------------------------------------------------------------#
print('\n5b.Definitions without Source:')
ind5b = open('I/DwS.md', 'w')
ind5b.write('---\nlayout: page\ntitle: "Definitions without Source"\n---\n\n\n')

# Definitions without Source: sort by Title
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(def_titles)])]
for i in range(0,len(def_titles)):
    shortcut = definitions[def_ids[sort_ind[i]]]['shortcut']
    title    = definitions[def_ids[sort_ind[i]]]['title']
    source   = definitions[def_ids[sort_ind[i]]]['source']
    if not source:
        ind5b.write('- [' + title + '](/D/' + shortcut + ')\n')
ind5b.close()
print('   - successfully written to disk!')