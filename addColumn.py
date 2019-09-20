import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/user/Documents/dev/google_cloud_dev/bigquery-poc-a1111.json'
CLIENT = bigquery.Client(project='bigquery-poc')


L_TBL = [
            'tablename1',
            'tablename2'
        ]

def addColumn(tbl, column, dataType):
    table_ref = CLIENT.dataset('staging').table(tbl)
    table = CLIENT.get_table(table_ref)
    original_schema = table.schema
    new_schema = original_schema[:]  # creates a copy of the schema
    new_schema.append(bigquery.SchemaField(column, dataType))
    table.schema = new_schema
    table = CLIENT.update_table(table, ['schema'])  # API request
    assert len(table.schema) == len(original_schema) + 1 == len(new_schema)


def main():
    for tbl in L_TBL:
        print tbl
        addColumn(tbl, 'end_ts', 'TIMESTAMP')


if __name__ == '__main__':
        main()

