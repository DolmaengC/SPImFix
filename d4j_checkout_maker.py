import os

checkout_command = "defects4j checkout -p Closure -v {}b -w /tmp/closure_{}_buggy"
mv_command = "mv /tmp/closure_{}_buggy d4j_checkout/closure/closure_{}_buggy"

l = {5,33,35,41,50,57,59,62,63,70,71,75,79,98}
for i in in range(1,134):
	command = checkout_command.format(i, i)
	os.system(command)
	command = mv_command.format(i,i)
	os.system(command)

	

