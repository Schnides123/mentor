from pymilvus import (
    connections,
    utility,
    Collection,
)

connections.connect("default", host="localhost", port="19530")

print(utility.has_collection("LangChainCollection"))
print(utility.list_collections())
collection = Collection("LangChainCollection")  # Get an existing collection.

print(collection.schema)                # Return the schema.CollectionSchema of the collection.
print(collection.description)           # Return the description of the collection.
print(collection.name)                  # Return the name of the collection.
print(collection.is_empty)              # Return the boolean value that indicates if the collection is empty.
print(collection.num_entities)          # Return the number of entities in the collection.
print(collection.primary_field)         # Return the schema.FieldSchema of the primary key field.
print(collection.partitions)            # Return the list[Partition] object.
print(collection.indexes)               # Return the list[Index] object.