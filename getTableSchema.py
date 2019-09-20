import os
import json
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/user/Documents/dev/google_cloud_dev/bigquery-poc-a1111.json'
CLIENT = bigquery.Client(project='bigquery-poc')


L_TBL = [
            'tablename1',
            'tablename2'
        ]

def tableSchema(tbl):
    table_ref = CLIENT.dataset('staging').table(tbl)
    table = CLIENT.get_table(table_ref)
    l_d_schema = []
    for schemaField in table.schema:
        l_d_schema.append(schemaField.to_api_repr())
    return l_d_schema


def main():
    for tbl in L_TBL:
        print json.dumps(tableSchema(tbl), indent=2)


if __name__ == '__main__':
        main()

