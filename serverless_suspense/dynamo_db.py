import boto3

import ServerlessSuspense


class DynamoModel(ServerlessSuspense):
    def __init__(self, table_name, maintenance_field):
        self._dynamo_db = boto3.resource("dynamodb")
        self._dynamo_table = self._dynamo_db.Table(table_name)
        self._maintenace_field = maintenance_field

    def _fetch_suspend_status(self):
        item = self._dynamo_table.get_item(Key={self._maintenace_field})
        self._suspend_status = item['status']

    def is_suspended(self):
        self._fetch_suspend_status()
        return self._suspend_status
