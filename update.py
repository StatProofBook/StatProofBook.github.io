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
 Last edit: 2022-07-06 17:32:00
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
pr_titles = []

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
        proofs[proof_id] = {'proof_id': proof_id, 'shortcut': shortcut, 'title': title, \
                            'username': username, 'date': date, 'source': source}
        pr_titles.append(title_sort)

# List files in definition directory
#-----------------------------------------------------------------------------#
files       = os.listdir('D/')
definitions = dict()
def_titles  = []

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
        definitions[def_id] = {'def_id': def_id, 'shortcut': shortcut, 'title': title, \
                               'username': username, 'date': date, 'source': source}
        def_titles.append(title_sort)

# Count number of files
#-----------------------------------------------------------------------------#
num_pr  = len(proofs)
num_def = len(definitions)
pr_ids  = list(proofs.keys())
def_ids = list(definitions.keys())

# Output number of files
#-----------------------------------------------------------------------------#
print('\n-> StatProofBook Index Generator:')
print('   - ' + str(num_pr) + ' files found in proof directory!')
print('   - ' + str(num_def) + ' files found in definition directory!')


# Table of Contents: read index file
#-----------------------------------------------------------------------------#
print('\n1. Table of Contents:')
f1 = open('I/ToC.md', 'r')
tocs = f1.readlines()
f1.close()

# Table of Contents: check for proof Shortcuts
#-----------------------------------------------------------------------------#
incl = np.zeros(num_pr, dtype=bool)
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
incl = np.zeros(num_def, dtype=bool)
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
f2a = open('I/PbN.md', 'w')
f2a.write('---\nlayout: page\ntitle: "Proof by Number"\n---\n\n\n')
f2a.write('| ID | Shortcut | Theorem | Author | Date |\n')
f2a.write('|:-- |:-------- |:------- |:------ |:---- |\n')

# Proof by Number: sort by Proof ID
#-----------------------------------------------------------------------------#
pr_nos   = [int(pr_id[1:]) for pr_id in pr_ids]
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(pr_nos)])]
for i in sort_ind:
    f2a.write('| ' + proofs[pr_ids[i]]['proof_id'] + ' | ' + proofs[pr_ids[i]]['shortcut'] + ' | [' + \
                       proofs[pr_ids[i]]['title'] + '](/P/' + proofs[pr_ids[i]]['shortcut'] + ') | ' + \
                       proofs[pr_ids[i]]['username'] + ' | ' + proofs[pr_ids[i]]['date'].strftime('%Y-%m-%d') + ' |\n')
f2a.close()
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
    f2b.write('| ' + definitions[def_ids[i]]['def_id'] + ' | ' + definitions[def_ids[i]]['shortcut'] + ' | [' + \
                       definitions[def_ids[i]]['title'] + '](/D/' + definitions[def_ids[i]]['shortcut'] + ') | ' + \
                       definitions[def_ids[i]]['username'] + ' | ' + definitions[def_ids[i]]['date'].strftime('%Y-%m-%d') + ' |\n')
f2b.close()
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
for i in range(num_pr):
    shortcut   = proofs[pr_ids[sort_ind[i]]]['shortcut']
    title      = proofs[pr_ids[sort_ind[i]]]['title']
    title_sort = pr_titles[sort_ind[i]]
    if title_sort[0] != prev_lett:
        f3a.write('\n### ' + title_sort[0].upper() + '\n\n')
        prev_lett = title_sort[0]
    f3a.write('- [' + title + '](/P/' + shortcut + ')\n')
f3a.close()
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
for i in range(num_def):
    shortcut   = definitions[def_ids[sort_ind[i]]]['shortcut']
    title      = definitions[def_ids[sort_ind[i]]]['title']
    title_sort = def_titles[sort_ind[i]]
    if title_sort[0] != prev_lett:
        f3b.write('\n### ' + title_sort[0].upper() + '\n\n')
        prev_lett = title_sort[0]
    f3b.write('- [' + title + '](/D/' + shortcut + ')\n')
f3b.close()
print('   - successfully written to disk!')


# Proof by Author: prepare index file
#-----------------------------------------------------------------------------#
print('\n4a.Proof by Author:')
f4a = open('I/PbA.md', 'w')
f4a.write('---\nlayout: page\ntitle: "Proof by Author"\n---\n\n')

# Proof by Authors: sort by Username
#-----------------------------------------------------------------------------#
pr_words     = ['proof', 'proofs']
pr_hdr       = '\n### {} ({} {})\n\n'
pr_users     = [proofs[pr_id]['username'].lower() for pr_id in pr_ids]
unique_users = list(set(pr_users))
unique_users.sort()
for user in unique_users:
    user_proofs = [proof for proof in proofs.values() if proof['username'].lower() == user]
    user_name   = user_proofs[0]['username']
    f4a.write(pr_hdr.format(user_name, len(user_proofs), pr_words[len(user_proofs)>1]))
    user_titles = [proof['title'].lower() for proof in user_proofs]
    sort_ind    = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(user_titles)])]
    for i in range(len(user_titles)):
        shortcut = user_proofs[sort_ind[i]]['shortcut']
        title    = user_proofs[sort_ind[i]]['title']
        f4a.write('- [' + title + '](/P/' + shortcut + ')\n')
f4a.close()
print('   - successfully written to disk!')


# Definition by Author: prepare index file
#-----------------------------------------------------------------------------#
print('\n4b.Definition by Author:')
f4b = open('I/DbA.md', 'w')
f4b.write('---\nlayout: page\ntitle: "Definition by Author"\n---\n\n')

# Definition by Authors: sort by Username
#-----------------------------------------------------------------------------#
def_words    = ['definition', 'definitions']
def_hdr      = '\n### {} ({} {})\n\n'
def_users    = [definitions[def_id]['username'].lower() for def_id in def_ids]
unique_users = list(set(def_users))
unique_users.sort()
for user in unique_users:
    user_definitions = [definition for definition in definitions.values() if definition['username'].lower() == user]
    user_name        = user_definitions[0]['username']
    f4b.write(def_hdr.format(user_name, len(user_definitions), def_words[len(user_definitions)>1]))
    user_titles      = [definition['title'].lower() for definition in user_definitions]
    sort_ind         = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(user_titles)])]
    for i in range(len(user_titles)):
        shortcut = user_definitions[sort_ind[i]]['shortcut']
        title    = user_definitions[sort_ind[i]]['title']
        f4b.write('- [' + title + '](/D/' + shortcut + ')\n')
f4b.close()
print('   - successfully written to disk!')


# Proofs without Source: prepare index file
#-----------------------------------------------------------------------------#
print('\n5a.Proofs without Source:')
f5a = open('I/PwS.md', 'w')
f5a.write('---\nlayout: page\ntitle: "Proofs without Source"\n---\n\n\n')

# Proofs without Source: sort by Title
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(pr_titles)])]
for i in range(num_pr):
    shortcut = proofs[pr_ids[sort_ind[i]]]['shortcut']
    title    = proofs[pr_ids[sort_ind[i]]]['title']
    source   = proofs[pr_ids[sort_ind[i]]]['source']
    if not source:
        f5a.write('- [' + title + '](/P/' + shortcut + ')\n')
f5a.close()
print('   - successfully written to disk!')


# Definitions without Source: prepare index file
#-----------------------------------------------------------------------------#
print('\n5b.Definitions without Source:')
f5b = open('I/DwS.md', 'w')
f5b.write('---\nlayout: page\ntitle: "Definitions without Source"\n---\n\n\n')

# Definitions without Source: sort by Title
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(def_titles)])]
for i in range(num_def):
    shortcut = definitions[def_ids[sort_ind[i]]]['shortcut']
    title    = definitions[def_ids[sort_ind[i]]]['title']
    source   = definitions[def_ids[sort_ind[i]]]['source']
    if not source:
        f5b.write('- [' + title + '](/D/' + shortcut + ')\n')
f5b.close()
print('   - successfully written to disk!')