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
 Last edit: 2022-07-21 07:47:00
"""


# Import modules
#-----------------------------------------------------------------------------#
import os
import re
import numpy as np
from datetime import datetime

# List files in proof directory
#-----------------------------------------------------------------------------#
files  = os.listdir('P/')
proofs = []

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
                title_sort = title_edit.lower()
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
        proofs.append({'proof_id': proof_id, 'shortcut': shortcut, 'title': title, \
                       'username': username, 'date': date, 'source': source, \
                       'title_sort': title_sort})

# List files in definition directory
#-----------------------------------------------------------------------------#
files = os.listdir('D/')
defs  = []

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
                title_sort = title_edit.lower()
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
        defs.append({'def_id': def_id, 'shortcut': shortcut, 'title': title, \
                     'username': username, 'date': date, 'source': source, \
                     'title_sort': title_sort})

# Count number of files
#-----------------------------------------------------------------------------#
del title_edit, title_sort
num_pr     = len(proofs)
num_def    = len(defs)
pr_ids     = [proof['proof_id'] for proof in proofs]
def_ids    = [definition['def_id'] for definition in defs]
pr_titles  = [proof['title_sort'] for proof in proofs]
def_titles = [definition['title_sort'] for definition in defs]

# Output number of files
#-----------------------------------------------------------------------------#
print('\n-> StatProofBook Index Generator:')
print('   - ' + str(num_pr) + ' files found in proof directory!')
print('   - ' + str(num_def) + ' files found in definition directory!')


# Table of Contents: read index file
#-----------------------------------------------------------------------------#
print('\n1. Table of Contents:')
f1   = open('I/ToC.md', 'r')
ToCs = f1.readlines()
f1.close()

# Table of Contents: check for proof Shortcuts
#-----------------------------------------------------------------------------#
incl = np.zeros(num_pr, dtype=bool)
for (i, proof) in enumerate(proofs):
    for line in ToCs:
        if line.find('(/P/' + proof['shortcut'] + ')') > -1:
            incl[i] = True
    if ~incl[i]:
        print('   - WARNING: proof "' + proof['shortcut'] + '" is not in table of contents!')
if all(incl):
    print('   - ' + str(sum(incl)) + ' proofs found in table of contents!')

# Table of Contents: check for definition Shortcuts
#-----------------------------------------------------------------------------#
incl = np.zeros(num_def, dtype=bool)
for (i, definition) in enumerate(defs):
    for line in ToCs:
        if line.find('(/D/' + definition['shortcut'] + ')') > -1:
            incl[i] = True
    if ~incl[i]:
        print('   - WARNING: definition "' + definition['shortcut'] + '" is not in table of contents!')
if all(incl):
    print('   - ' + str(sum(incl)) + ' definitions found in table of contents!')


# Proof by Number: prepare index file
#-----------------------------------------------------------------------------#
print('\n2a.Proof by Number:')
f2a = open('I/PbN.md', 'w')
f2a.write('---\nlayout: page\ntitle: "Proof by Number"\n---\n\n\n')
f2a.write('| ID | Shortcut | Theorem | Author | Date |\n')
f2a.write('|:-- |:-------- |:------- |:------ |:---- |\n')

# Proof by Number: sort by Proof ID
#-----------------------------------------------------------------------------#
pr_nos   = [int(pr_id[1:]) for pr_id in pr_ids]
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(pr_nos)])]
for i in sort_ind:
    f2a.write('| ' + proofs[i]['proof_id'] + ' | ' + proofs[i]['shortcut'] + ' | [' + \
                     proofs[i]['title'] + '](/P/' + proofs[i]['shortcut'] + ') | ' + \
                     proofs[i]['username'] + ' | ' + proofs[i]['date'].strftime('%Y-%m-%d') + ' |\n')
f2a.close()
del pr_nos, sort_ind
print('   - successfully written to disk!')


# Definition by Number: prepare index file
#-----------------------------------------------------------------------------#
print('\n2b.Definition by Number:')
f2b = open('I/DbN.md', 'w')
f2b.write('---\nlayout: page\ntitle: "Definition by Number"\n---\n\n\n')
f2b.write('| ID | Shortcut | Theorem | Author | Date |\n')
f2b.write('|:-- |:-------- |:------- |:------ |:---- |\n')

# Definition by Number: sort by Definition ID
#-----------------------------------------------------------------------------#
def_nos  = [int(def_id[1:]) for def_id in def_ids]
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(def_nos)])]
for i in sort_ind:
    f2b.write('| ' + defs[i]['def_id'] + ' | ' + defs[i]['shortcut'] + ' | [' + \
                     defs[i]['title'] + '](/D/' + defs[i]['shortcut'] + ') | ' + \
                     defs[i]['username'] + ' | ' + defs[i]['date'].strftime('%Y-%m-%d') + ' |\n')
f2b.close()
del def_nos, sort_ind
print('   - successfully written to disk!')


# Proof by Topic: prepare index file
#-----------------------------------------------------------------------------#
print('\n3a.Proof by Topic:')
f3a = open('I/PbT.md', 'w')
f3a.write('---\nlayout: page\ntitle: "Proof by Topic"\n---\n\n')

# Proof by Topic: sort by Title
#-----------------------------------------------------------------------------#
prev_lett = '0'
sort_ind  = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(pr_titles)])]
for i in sort_ind:
    title_sort = pr_titles[i]
    if title_sort[0] != prev_lett:
        f3a.write('\n### ' + title_sort[0].upper() + '\n\n')
        prev_lett = title_sort[0]
    f3a.write('- [' + proofs[i]['title'] + '](/P/' + proofs[i]['shortcut'] + ')\n')
f3a.close()
del prev_lett, sort_ind, title_sort
print('   - successfully written to disk!')


# Definition by Topic: prepare index file
#-----------------------------------------------------------------------------#
print('\n3b.Definition by Topic:')
f3b = open('I/DbT.md', 'w')
f3b.write('---\nlayout: page\ntitle: "Definition by Topic"\n---\n\n')

# Definition by Topic: sort by Title
#-----------------------------------------------------------------------------#
prev_lett = '0'
sort_ind  = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(def_titles)])]
for i in sort_ind:
    title_sort = def_titles[i]
    if title_sort[0] != prev_lett:
        f3b.write('\n### ' + title_sort[0].upper() + '\n\n')
        prev_lett = title_sort[0]
    f3b.write('- [' + defs[i]['title'] + '](/D/' + defs[i]['shortcut'] + ')\n')
f3b.close()
del prev_lett, sort_ind, title_sort
print('   - successfully written to disk!')


# Proof by Author: prepare index file
#-----------------------------------------------------------------------------#
print('\n4a.Proof by Author:')
f4a = open('I/PbA.md', 'w')
f4a.write('---\nlayout: page\ntitle: "Proof by Author"\n---\n\n')

# Proof by Authors: sort by Username
#-----------------------------------------------------------------------------#
pr_words     = ['proof', 'proofs']
pr_users     = [proof['username'].lower() for proof in proofs]
sect_hdr     = '\n### {} ({} {})\n\n'
unique_users = list(set(pr_users))
unique_users.sort()
for user in unique_users:
    user_proofs = [proof for proof in proofs if proof['username'].lower() == user]
    user_titles = [proof['title_sort'] for proof in user_proofs]
    user_name   = user_proofs[0]['username']
    f4a.write(sect_hdr.format(user_name, len(user_proofs), pr_words[len(user_proofs)>1]))
    sort_ind    = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(user_titles)])]
    for i in sort_ind:
        f4a.write('- [' + user_proofs[i]['title'] + '](/P/' + user_proofs[i]['shortcut'] + ')\n')
f4a.close()
del pr_words, pr_users, sect_hdr, sort_ind
print('   - successfully written to disk!')


# Definition by Author: prepare index file
#-----------------------------------------------------------------------------#
print('\n4b.Definition by Author:')
f4b = open('I/DbA.md', 'w')
f4b.write('---\nlayout: page\ntitle: "Definition by Author"\n---\n\n')

# Definition by Authors: sort by Username
#-----------------------------------------------------------------------------#
def_words    = ['definition', 'definitions']
def_users    = [definition['username'].lower() for definition in defs]
sect_hdr     = '\n### {} ({} {})\n\n'
unique_users = list(set(def_users))
unique_users.sort()
for user in unique_users:
    user_defs   = [definition for definition in defs if definition['username'].lower() == user]
    user_titles = [definition['title_sort'] for definition in user_defs]
    user_name   = user_defs[0]['username']
    f4b.write(sect_hdr.format(user_name, len(user_defs), def_words[len(user_defs)>1]))
    sort_ind    = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(user_titles)])]
    for i in sort_ind:
        f4b.write('- [' + user_defs[i]['title'] + '](/D/' + user_defs[i]['shortcut'] + ')\n')
f4b.close()
del def_words, def_users, sect_hdr, sort_ind
print('   - successfully written to disk!')


# Proofs without Source: prepare index file
#-----------------------------------------------------------------------------#
print('\n5a.Proofs without Source:')
f5a = open('I/PwS.md', 'w')
f5a.write('---\nlayout: page\ntitle: "Proofs without Source"\n---\n\n\n')

# Proofs without Source: sort by Title
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(pr_titles)])]
for i in sort_ind:
    source = proofs[i]['source']
    if not source:
        f5a.write('- [' + proofs[i]['title'] + '](/P/' + proofs[i]['shortcut'] + ')\n')
f5a.close()
del sort_ind, source
print('   - successfully written to disk!')


# Definitions without Source: prepare index file
#-----------------------------------------------------------------------------#
print('\n5b.Definitions without Source:')
f5b = open('I/DwS.md', 'w')
f5b.write('---\nlayout: page\ntitle: "Definitions without Source"\n---\n\n\n')

# Definitions without Source: sort by Title
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(def_titles)])]
for i in sort_ind:
    source = defs[i]['source']
    if not source:
        f5b.write('- [' + defs[i]['title'] + '](/D/' + defs[i]['shortcut'] + ')\n')
f5b.close()
del sort_ind, source
print('   - successfully written to disk!')