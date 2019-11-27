#!/usr/bin/env python
"""
Index Generator for The Book of Statistical Proofs
_
This script loads all files from the proof directory and
- checks if they are in "Table of Contents" (structured overview)
- writes them as a list into "Proof by Number" (chronological list)
- writes them as a list into "Proof by Topic" (an alphabetical list)

Author: Joram Soch, BCCN Berlin
E-Mail: joram.soch@bccn-berlin.de

First edit: 2019-09-27 12:55:00
 Last edit: 2019-09-27 16:00:00
"""


# Import modules
#-----------------------------------------------------------------------------#
import os
import re
import numpy as np
from datetime import datetime

# List files in proof directory
#-----------------------------------------------------------------------------#
files  = os.listdir('Proofs/')
proofs = dict()
pr_ids = []
pr_nos = []
titles = []
users  = []

# Browse through list of files
#-----------------------------------------------------------------------------#
for file in files:
    if '.md' in file:
        
        # Read proof file
        #---------------------------------------------------------------------#
        file_obj = open('Proofs/' + file, 'r')
        file_txt = file_obj.readlines()
        file_obj.close()
        
        # Parse YAML header
        #---------------------------------------------------------------------#
        for line in file_txt:
            if line.find('proof_id:') == 0:
                proof_id = re.sub('"', '', line[10:-1])
            if line.find('shortcut:') == 0:
                shortcut = re.sub('"', '', line[10:-1])
            if line.find('title:') == 0:
                title = re.sub('"', '', line[7:-1])
            if line.find('username:') == 0:
                username = re.sub('"', '', line[10:-1])
            if line.find('date:') == 0:
                date = datetime.strptime(line[6:-1], '%Y-%m-%d %H:%M:%S')
        
        # Write dictionary entry
        #---------------------------------------------------------------------#
        proofs[proof_id] = {'proof_id': proof_id, 'shortcut': shortcut, 'title': title, \
                            'username': username, 'date': date}
        pr_ids.append(proof_id)
        pr_nos.append(int(proof_id[1:]))
        titles.append(title)
        users.append(username)

# Output number of proof files
#-----------------------------------------------------------------------------#
print('\n-> TBSP Index Generator:')
print('   - ' + str(len(proofs)) + ' files found in proof directory!')


# Table of Contents: read index file
#-----------------------------------------------------------------------------#
print('\n1. "Table_of_Contents.md":')
ind1 = open('Indexes/Table_of_Contents.md', 'r')
tocs = ind1.readlines()
ind1.close()

# Table of Contets: check for Shortcuts
#-----------------------------------------------------------------------------#
incl = np.zeros(len(proofs), dtype=bool)
for (i, proof) in enumerate(proofs):
    for line in tocs:
        if line.find('(/Proofs/' + proofs[proof]['shortcut'] + '.html)') > -1:
            incl[i] = True
    if ~incl[i]:
        print('   - WARNING: proof "' + proofs[proof]['shortcut'] + '" is not in table of contents!')
if all(incl):
    print('   - ' + str(sum(incl)) + ' proofs found in table of contents!')


# Proof by Number: prepare index file
#-----------------------------------------------------------------------------#
print('\n2. "Proof_by_Number.md":')
ind2 = open('Indexes/Proof_by_Number.md', 'w')
ind2.write('---\nlayout: page\ntitle: "Proof by Number"\n---\n\n\n')
ind2.write('| ID | Shortcut | Theorem | Author | Date |\n')
ind2.write('|:-- |:-------- |:------- |:------ |:---- |\n')

# Proof by Number: sort by Proof ID
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(pr_nos)])]
for i in sort_ind:
    ind2.write('| ' + proofs[pr_ids[i]]['proof_id'] + ' | ' + proofs[pr_ids[i]]['shortcut'] + ' | [' + \
               proofs[pr_ids[i]]['title'] + '](/Proofs/' + proofs[pr_ids[i]]['shortcut'] + '.html) | ' + \
               proofs[pr_ids[i]]['username'] + ' | ' + proofs[pr_ids[i]]['date'].strftime('%Y-%m-%d') + ' |\n')
ind2.close()
print('   - successfully written to disk!')


# Proof by Topic: prepare index file
#-----------------------------------------------------------------------------#
print('\n3. "Proof_by_Topic.md":')
ind3 = open('Indexes/Proof_by_Topic.md', 'w')
ind3.write('---\nlayout: page\ntitle: "Proof by Topic"\n---\n\n\n')

# Proof by Topic: sort by Title
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(titles)])]
for i in range(0,len(titles)):
    shortcut = proofs[pr_ids[sort_ind[i]]]['shortcut']
    title    = proofs[pr_ids[sort_ind[i]]]['title']
    if i == 0:
        ind3.write('### ' + title[0] + '\n\n')
    else:
        if title[0] != proofs[pr_ids[sort_ind[i-1]]]['title'][0]:
            ind3.write('\n### ' + title[0] + '\n\n')
    ind3.write('- [' + title + '](/Proofs/' + shortcut + '.html)\n')
ind3.close()
print('   - successfully written to disk!')


# Proof by Author: prepare index file
#-----------------------------------------------------------------------------#
print('\n4. "Proof_by_Author.md":')
ind3 = open('Indexes/Proof_by_Author.md', 'w')
ind3.write('---\nlayout: page\ntitle: "Proof by Author"\n---\n\n\n')

# Proof by Authors: sort by Username
#-----------------------------------------------------------------------------#
unique_users = list(set(users))
for user in unique_users:
    user_proofs = [proof for proof in proofs.values() if proof['username'] == user]
    if len(user_proofs) == 1:
        ind3.write('### ' + user + ' (' + str(len(user_proofs)) + ' proof)\n\n')
    else:
        ind3.write('### ' + user + ' (' + str(len(user_proofs)) + ' proofs)\n\n')
    user_titles = []
    for proof in user_proofs:
        user_titles.append(proof['title'])
    sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(user_titles)])]
    for i in range(0,len(user_titles)):
        shortcut = user_proofs[sort_ind[i]]['shortcut']
        title    = user_proofs[sort_ind[i]]['title']
        ind3.write('- [' + title + '](/Proofs/' + shortcut + '.html)\n')
ind3.close()
print('   - successfully written to disk!')