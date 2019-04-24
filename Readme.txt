python -m da sourcefile.da

to count the number of messages received from the log files
grep -c Reply <logfile_for_target_run> + grep -c Request <logfile_for_target_run>
