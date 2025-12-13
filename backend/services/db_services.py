from azure.cosmos import CosmosClient
from config import settings
from azure.cosmos import PartitionKey
from azure.cosmos.exceptions import CosmosResourceNotFoundError

client = CosmosClient(settings.COSMOS_URL, credential=settings.COSMOS_KEY)
database = client.create_database_if_not_exists(settings.COSMOS_DB)

user_container = database.create_container_if_not_exists(
    id=settings.COSMOS_USER_CONTAINER,
    #partition_key={"/id"}
    partition_key=PartitionKey(path="/id")
)

# log_container = database.create_container_if_not_exists(
#     id=settings.COSMOS_LOGS_CONTAINER,
#     #partition_key={"/user_id"}
#     partition_key=PartitionKey(path="/user_id")
# )


# --- User CRUD ---
def create_user(user):
    created = user_container.upsert_item(user)
    return created

def get_user(user_id):
    try:
        return user_container.read_item(item=user_id, partition_key=user_id)
    except CosmosResourceNotFoundError:
        return None

