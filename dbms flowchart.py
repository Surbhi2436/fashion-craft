from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment="Main Components of a DBMS", format='png')

# Define nodes
components = [
    ("1", "Storage Manager\n(Manages data storage, indexing, buffering, space allocation)"),
    ("2", "Query Processor\n(Parser, Optimizer, Execution Engine)"),
    ("3", "Transaction Manager\n(Ensures ACID, handles locking, logging, rollback)"),
    ("4", "DDL Compiler\n(Processes CREATE, ALTER, DROP; updates catalog)"),
    ("5", "DML Compiler\n(Processes SELECT, INSERT, UPDATE, DELETE)"),
    ("6", "System Catalog / Data Dictionary\n(Metadata repository)"),
    ("7", "Concurrency Control Manager\n(Manages simultaneous access without conflicts)"),
    ("8", "Backup & Recovery Manager\n(Recovers database after failures)")
]

for id, label in components:
    dot.node(id, label, shape='box')

# Define relationships based on typical DBMS architecture flow
dot.edges([
    ("4", "6"),  # DDL Compiler updates System Catalog
    ("5", "2"),  # DML Compiler sends to Query Processor
    ("2", "1"),  # Query Processor interacts with Storage Manager
    ("3", "1"),  # Transaction Manager interacts with Storage Manager
    ("3", "7"),  # Transaction Manager works with Concurrency Control
    ("3", "8"),  # Transaction Manager works with Backup & Recovery
    ("7", "1"),  # Concurrency Control influences storage operations
    ("8", "1"),  # Backup & Recovery influences storage operations
    ("6", "2"),  # System Catalog used by Query Processor
    ("6", "4"),  # System Catalog referenced by DDL Compiler
    ("6", "5")   # System Catalog referenced by DML Compiler
])

# Save and render the diagram
output_path = '/mnt/data/dbms_components'
dot.render(output_path, cleanup=True)

output_path + '.png'
