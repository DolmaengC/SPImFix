import subprocess

command = """/Library/Java/JavaVirtualMachines/jdk1.7.0_80.jdk/Contents/Home/bin/java \
-Dfile.encoding=UTF-8 \
-Dstdout.encoding=UTF-8 \
-Dstderr.encoding=UTF-8 \
-classpath /home/jun4161/data2/APR/SimFix/bin:/home/jun4161/data2/APR/SimFix/lib/org.eclipse.core.contenttype_3.5.0.v20150421-2214.jar:/home/jun4161/data2/APR/SimFix/lib/org.eclipse.core.jobs_3.7.0.v20150330-2103.jar:/home/jun4161/data2/APR/SimFix/lib/org.eclipse.core.resources_3.10.1.v20150725-1910.jar:/home/jun4161/data2/APR/SimFix/lib/org.eclipse.core.runtime_3.11.1.v20150903-1804.jar:/home/jun4161/data2/APR/SimFix/lib/org.eclipse.equinox.common_3.7.0.v20150402-1709.jar:/home/jun4161/data2/APR/SimFix/lib/org.eclipse.equinox.preferences_3.5.300.v20150408-1437.jar:/home/jun4161/data2/APR/SimFix/lib/org.eclipse.jdt.core_3.11.2.v20160128-0629.jar:/home/jun4161/data2/APR/SimFix/lib/org.eclipse.osgi_3.10.102.v20160118-1700.jar:/home/jun4161/data2/APR/SimFix/lib/log4j-1.2.17.jar:/home/jun4161/data2/APR/SimFix/lib/com.gzoltar-0.1.1-jar-with-dependencies.jar:/home/jun4161/data2/APR/SimFix/lib/dom4j-2.0.0-RC1.jar:/home/jun4161/data2/APR/SimFix/lib/commons-io-2.5.jar:/home/jun4161/data2/APR/SimFix/lib/json-simple-1.1.1.jar \
cofix.main.Main \
--proj_home=/home/jun4161/data2/APR/SimFix/d4j_checkout \
--proj_name=closure \
--bug_id=14"""

subprocess.run(command, shell=True)

