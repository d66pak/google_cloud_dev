#!/bin/bash

rm s3-to-gcs.zip
mkdir dist

cp s3-to-gcs/handler.py dist/
cp s3-to-gcs/service-account.json dist/
cp -rf s3-to-gcs/virtual_env/lib/python2.7/site-packages/* dist/

cd dist/
zip -rv9 ../s3-to-gcs.zip .
cd ..
rm -rf dist/