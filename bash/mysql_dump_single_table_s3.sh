#!/bin/bash

DB_HOST=x
DB_NAME=x
DB_USERNAME=x
DB_PASSWORD=x

DB_DUMP_PATH=x

AWS_PROFILE=x
AWS_S3_BUCKET=x

for TABLE in $(echo "SELECT table_name FROM information_schema.tables WHERE table_schema = '$DB_NAME';" | mysql -h $DB_HOST -u $DB_USERNAME -p$DB_PASSWORD $DB_NAME | tail -n +2)
do
        /usr/bin/mysqldump --column-statistics=0 --set-gtid-purged=OFF -h $DB_HOST -u $DB_USERNAME -p$DB_PASSWORD $DB_NAME $TABLE | zip > $DB_DUMP_PATH/$TABLE.sql.zip
        /usr/local/bin/aws --profile $AWS_PROFILE s3 cp $DB_DUMP_PATH/$TABLE.sql.zip s3://$AWS_S3_BUCKET/db/`date +"%Y-%m-%d"`/$TABLE.sql.zip
        rm $DB_DUMP_PATH/$TABLE.sql.zip
done