# labelstoClass

This is a (not-so) quick and dirty python script to convert enumerated integer class labels to string labels, for EMG/EEG dtasets in CSV format.


Motivation: WEKA was treating the integer values as numbers, which was understandable because they are, and hence assumed it was a regression problem not a classification one.

Method: Horrible and inefficient.

Input: CSV file, where the last column is integer-enumerated class.

Parameters: Takes the path for the enum-ed CSV and the target path for the new CSV as command line arguments.

Manual labour: Needs the user to actually hardcode what string each integer corresponds to. Sorry.

Output: CSV file, where the las column is class labels as strings.


Disclaimer: I put this together very quickly and also am not used to using github

To Do: convert this to one single script with a separate file (possibly another script which calls this one) that determines the enum-class mapping to reduce the manual labour aspect. Improve speed.
