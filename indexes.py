#!/usr/bin/env python
"""
Create Indices for The Book of Statistical Proofs
"""


# Import modules
#-----------------------------------------------------------------------------#
import os
import re
from datetime import datetime

# List files in proof directory
#-----------------------------------------------------------------------------#
files  = os.listdir('Proofs/')
proofs = dict()
pr_ids = []
pr_nos = []
titles = []

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
        proofs[proof_id] = [proof_id, shortcut, title, username, date]
        pr_ids.append(proof_id)
        pr_nos.append(int(proof_id[1:]))
        titles.append(title)
        
# Proof by Number: prepare index file
#-----------------------------------------------------------------------------#
ind2 = open('Indexes/Proof_by_Number.md', 'w')
ind2.write('---\nlayout: page\ntitle: "Proof by Number"\n---\n\n\n')
ind2.write('| ID | Shortcut | Theorem | Author | Date |\n')
ind2.write('|:-- |:-------- |:------- |:------ |:---- |\n')

# Proof by Number: sort by Proof ID
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(pr_nos)])]
for i in sort_ind:
    ind2.write('| ' + proofs[pr_ids[i]][0] + ' | ' + proofs[pr_ids[i]][1] + ' | [' + \
               proofs[pr_ids[i]][2] + '](/Proofs/' + proofs[pr_ids[i]][1] + '.html) | ' + \
               proofs[pr_ids[i]][3] + ' | ' + date.strftime('%Y-%m-%d') + ' |\n')
ind2.close()

# Proof by Topic: prepare index file
#-----------------------------------------------------------------------------#
ind3 = open('Indexes/Proof_by_Topic.md', 'w')
ind3.write('---\nlayout: page\ntitle: "Proof by Topic"\n---\n\n\n')

# Proof by Topic: sort by Proof ID
#-----------------------------------------------------------------------------#
sort_ind = [i for (v, i) in sorted([(v, i) for (i, v) in enumerate(titles)])]
ind3.write('### ' + proofs[pr_ids[sort_ind[0]]][2][0] + '\n\n')
ind3.write('- [' + proofs[pr_ids[sort_ind[0]]][2] + '](/Proofs/' + proofs[pr_ids[sort_ind[0]]][1] + '.html)\n')
for j in range(1,len(titles)):
    if proofs[pr_ids[sort_ind[j]]][2][0] != proofs[pr_ids[sort_ind[j-1]]][2][0]:
        ind3.write('\n### ' + proofs[pr_ids[sort_ind[j]]][2][0] + '\n\n')
    ind3.write('- [' + proofs[pr_ids[sort_ind[j]]][2] + '](/Proofs/' + proofs[pr_ids[sort_ind[j]]][1] + '.html)\n')
ind3.close()