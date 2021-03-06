import sys
import glob
import operator
import subprocess
import StringIO

cmd = 'pylint'

with open( 'pylint_output.txt', 'w' ) as output:
	files = set( sys.argv[1:] )
	for f in sorted(glob.glob('*.py'), key=operator.methodcaller('lower')):
		if files and f not in files:
			continue
		print f
		out, err = subprocess.Popen(
			[cmd, '--load-plugins', 'pylint_django', '--errors-only', f],
			stdout=subprocess.PIPE, stderr=subprocess.STDOUT
		).communicate()
		for line in out.split('\n'):
			if "Undefined variable '_' (undefined-variable)" in line:
				continue
			if "No config file found, using default configuration" in line:
				continue
			print line
			output.write( '{}\n'.format(line) )
		output.flush()
