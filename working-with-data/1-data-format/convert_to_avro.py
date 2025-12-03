#!/usr/bin/env python3
import json
import avro.schema
import avro.io
import io

# Load the JSON data
with open('64KB-min.json', 'r') as f:
    data = json.load(f)

# Load the Avro schema
with open('person.avsc', 'r') as f:
    schema = avro.schema.parse(f.read())

# Create Avro writer
bytes_writer = io.BytesIO()
encoder = avro.io.BinaryEncoder(bytes_writer)
datum_writer = avro.io.DatumWriter(schema)

# Write each record
for record in data:
    datum_writer.write(record, encoder)

# Save to file
with open('persons.avro', 'wb') as f:
    f.write(bytes_writer.getvalue())

print(f"Converted {len(data)} records to Avro format")
print("Files created:")
print("- person.avsc (schema)")
print("- persons.avro (data)")
