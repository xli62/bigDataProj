#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /proj-python/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /proj-python/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /proj-python/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/access.log /proj-python/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../bigDataProj/proj-python/mapper.py -mapper ../../bigDataProj/proj-python/mapper.py \
-file ../../bigDataProj/proj-python/reducer.py -reducer ../../bigDataProj/proj-python/reducer.py \
-input /proj-python/input/* -output /proj-python/output/
/usr/local/hadoop/bin/hdfs dfs -cat /proj-python/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /proj-python/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /proj-python/output/
../../stop.sh
