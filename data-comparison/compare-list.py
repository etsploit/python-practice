#created this to be used for comparing two list of IP addresses for example comparing a baseline inventory to a nessus vuln scan
#hence the variable are about IPs

import difflib

#edit the path

ips1 = "/Users/your_user/sub_folder/input/file1.txt"
ips2 = "/Users/your_user/sub_folder/input/file2.txt"

ips1_lines = open(ips1, 'r').readlines()
ips2_lines = open(ips2, 'r').readlines()

difference = difflib.HtmlDiff().make_file(ips1_lines,ips2_lines,'IP Set 
1','IP Set 2')
difference_report = open('difference_report.html', 'w')
difference_report.write(difference)
difference_report.close()
