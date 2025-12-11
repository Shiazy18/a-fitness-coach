from azure.cosmos import CosmosClient
from config import settings

client = CosmosClient(settings.COSMOS_URL, credential=settings.COSMOS_KEY)
database = client.create_database_if_not_exists(settings.COSMOS_DB)

user_container = database.create_container_if_not_exists(
    id=settings.COSMOS_USER_CONTAINER,
    partition_key={"/id"}
)

log_container = database.create_container_if_not_exists(
    id=settings.COSMOS_LOGS_CONTAINER,
    partition_key={"/user_id"}
)


# --- User CRUD ---
def create_user(user):
    user_container.upsert_item(user)
    return user

def get_user(user_id):
    return user_container.read_item(item=user_id, partition_key=user_id)


# --- Logs ---
def add_log(log):
    log_container.upsert_item(log)
    return log

def get_logs(user_id):
    query = f"SELECT * FROM c WHERE c.user_id='{user_id}'"
    return list(log_container.query_items(query=query, enable_cross_partition_query=True))
