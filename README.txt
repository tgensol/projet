Test Codalab Competitions
Author: Isabelle Guyon
Date: October 2014


Drill #3: Submit results
========================
Go to the submission page http://codalabtest.cloudapp.net/competitions/NNN#participate-submit_results
Submit the sample_submission.zip file. Refresh until finished. Check:
Download your submission
View standard output log
View standard error log
View predict standard output log
View predict standard error log
Download evaluation output from prediction step
Download evaluation output from scoring step
Goto http://codalabtest.cloudapp.net/competitions/NNN#results
and check the leaderboard. The leaderboard displays the average rank and the results on set1 and set2. For result submission, the execution time is 0.
Note: we have only one sample submission, which includes both results and code. With the original setting sod the YAML file, in phase 1, only the results are checked because the flag “Results Scoring Only” is checked.


Drill #8: Admin tasks
=====================
Go to:
http://codalabtest.cloudapp.net/my/#manage
Under your competition, you can try the buttons:
- Delete: delete this competition.
- Edit: go to the editor. In the editor, under “Admins” more administrators can be added, having the privilege of editing the competition.
- Publish: make the competition public (note, this ca be reverted by going to the editor and unchecking “Publicly available”). A published competition cannot be deleted, it should be unpublished first.
and click on “Delete”.
- Participants: list of participants. If in the editor “registration required” is checked, the participant must be approved before they can enter the competition. The participants can also be revoked. Mail can be sent to all participants.
- Submissions: A table recapitulating all submissions.

Drill #9: Understanding the scoring program
===========================================
Example_competition_bundle contains a scoring program bundle scoring_program.zip. Unzip this bundle in a directory scoring_program/. The program score.py must be called with 2 arguments: input_dir and output_dir.
Go to scoring_program/ and at the shell prompt type:
python score.py ../../scoring_input/ ../../scoring_output/
Check ../../scoring_output/score.txt: theses are the scores shown on the leaderboard.

In this example, the scoring program computes the MSE between the solution files and the predicted files. The results are displayed as set1 and set2 in the leaderboard, corresponding to the results on the validation data for phase 1 and on the test data for phase 2. The sets are ordered in alphabetical order (set1=ada, set2=arcene). So other datasets may be provided and they will always be called set1 and set1.

In the competition bundle Example_compet_bundle.zip, the reference data (solution files) are given in 2 zip files: ref_valid.zip for phase 1 and ref_test.zip for phase 2. So, even though the scoring program remains the same, the scores computed differ: the scores are computed on validation data in phase 1 and on test data in phase 2.

Note: the leaderboard remains unchanged for both phases.

Drill #10: Understanding the sample code
=======================================
Sample code to be submitted in found in sample_submission.zip. Unzip in a directory sample_submission/. The code to generate predictions is called run.py. Usage:
python run.py <input_dir> <output_dir>
Go to the directory sample_submission/ and type at the shell prompt:
python run.py ../sample_input/ .
The program outputs the results of prediction xxx.predict.

