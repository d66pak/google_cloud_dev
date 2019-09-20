import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/user/Documents/dev/google_cloud_dev/bigquery-poc-a1111.json'
CLIENT = bigquery.Client(project='bigquery-poc')


L_TBL = [
            'tablename1',
            'tablename2'
        ]


def runQuery(query_str):
    query_job = CLIENT.query(query_str)
    return query_job

def main():
    for tbl in L_TBL:
        query_str = "UPDATE staging.{t} SET end_ts = '9999-12-31 00:00:00' WHERE TRUE".format(t=tbl)
        #query_str = "SELECT count(*) FROM staging.{t}".format(t=tbl)
        print query_str
        res = runQuery(query_str)
        for r in res:
            print tbl + ' ' + str(r)


if __name__ == '__main__':
        main()

