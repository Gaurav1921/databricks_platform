quiz = {
    "title": "Databricks Certification – Quiz 4",
    "questions": [
        # Q1
        {
            "q": "Which Delta Lake feature ensures that readers never see partial data from a failed write?",
            "options": [
                "Schema enforcement",
                "Time travel",
                "ACID transactions",
                "Delta caching"
            ],
            "answer_text": "ACID transactions",
            "explanation": "ACID transactions in Delta Lake ensure atomicity so that partial or failed writes are never visible to readers. Schema enforcement validates structure, time travel retrieves historical data, and delta caching improves performance."
        },
        # Q2
        {
            "q": "What happens when Delta Lake enforces schema on write?",
            "options": [
                "It rejects data that doesn’t match the table schema",
                "It modifies the table schema to fit incoming data",
                "It stores invalid rows in a quarantine table",
                "It automatically converts all data to strings"
            ],
            "answer_text": "It rejects data that doesn’t match the table schema",
            "explanation": "Schema enforcement validates incoming data and rejects rows that don’t match the defined schema. It won’t auto-adjust the schema unless schema evolution is enabled."
        },
        # Q3
        {
            "q": "Which component stores the transaction history in a Delta table?",
            "options": [
                "_delta_log directory",
                "_history_metadata directory",
                "Table manifest file",
                "Unity Catalog metadata"
            ],
            "answer_text": "_delta_log directory",
            "explanation": "The _delta_log directory stores JSON and checkpoint files that record every table change. There’s no '_history_metadata' directory; manifests are for external systems; Unity Catalog metadata is separate."
        },
        # Q4
        {
            "q": "Which Delta Lake command can restore a table to a previous state using version number?",
            "options": [
                "RESTORE TABLE my_table TO VERSION AS OF 5",
                "RESET TABLE my_table TO VERSION 5",
                "ROLLBACK my_table TO VERSION 5",
                "UNDO TABLE my_table VERSION 5"
            ],
            "answer_text": "RESTORE TABLE my_table TO VERSION AS OF 5",
            "explanation": "Delta Lake supports RESTORE TABLE ... TO VERSION AS OF for reverting to previous versions. Other syntaxes are invalid."
        },
        # Q5
        {
            "q": "What is one reason Delta Lake enables efficient “time travel” queries?",
            "options": [
                "Each write operation stores the entire dataset twice",
                "Historical snapshots are reconstructed from transaction logs and previous data files",
                "A separate copy of data is made daily",
                "All past data is cached in memory"
            ],
            "answer_text": "Historical snapshots are reconstructed from transaction logs and previous data files",
            "explanation": "Delta reconstructs old versions using logs and unchanged files, without full dataset duplication or constant caching."
        },
        # Q6
        {
            "q": "When creating a managed table in Unity Catalog without specifying LOCATION, where is the data stored?",
            "options": [
                "In the catalog’s default managed storage path",
                "In DBFS /user/hive/warehouse",
                "In the /mnt/external mount",
                "In a temporary scratch directory"
            ],
            "answer_text": "In the catalog’s default managed storage path",
            "explanation": "Unity Catalog uses a default managed storage location for managed tables unless LOCATION is specified."
        },
        # Q7
        {
            "q": "What happens if you run DROP TABLE my_table PURGE; on a managed table?",
            "options": [
                "Only metadata is removed",
                "Data and metadata are both deleted immediately",
                "Data is archived for 30 days",
                "Table schema is preserved but data is removed"
            ],
            "answer_text": "Data and metadata are both deleted immediately",
            "explanation": "PURGE removes all table data and metadata instantly, skipping trash or recovery."
        },
        # Q8
        {
            "q": "Why might an engineer choose an unmanaged table over a managed table?",
            "options": [
                "To allow direct sharing of files outside Databricks with other systems",
                "To get faster query performance",
                "To enable automatic compaction",
                "To avoid Unity Catalog"
            ],
            "answer_text": "To allow direct sharing of files outside Databricks with other systems",
            "explanation": "Unmanaged tables store data in externally accessible locations, ideal for sharing across tools."
        },
        # Q9
        {
            "q": "Which of the following correctly describes how the LOCATION keyword works when creating a table?",
            "options": [
                "It sets where the table’s data files are stored",
                "It determines where SQL results are cached",
                "It decides which cluster executes the queries",
                "It selects the Delta table’s catalog"
            ],
            "answer_text": "It sets where the table’s data files are stored",
            "explanation": "LOCATION tells Databricks where the table data is physically stored."
        },
        # Q10
        {
            "q": "You run: CREATE TABLE orders (id INT, amount DOUBLE) USING DELTA LOCATION 'abfss://data@storageacc.dfs.core.windows.net/orders'; What type of table is created?",
            "options": [
                "Managed table",
                "Unmanaged table",
                "Temporary table",
                "Cached table"
            ],
            "answer_text": "Unmanaged table",
            "explanation": "Specifying LOCATION explicitly creates an unmanaged table."
        },
        # Q11
        {
            "q": "Which SQL sequence correctly switches to an existing database before creating a table?",
            "options": [
                "USE sales; CREATE TABLE orders ...",
                "SET DATABASE sales; CREATE TABLE orders ...",
                "ACTIVATE DATABASE sales; CREATE TABLE orders ...",
                "LOAD DATABASE sales; CREATE TABLE orders ..."
            ],
            "answer_text": "USE sales; CREATE TABLE orders ...",
            "explanation": "USE changes the current database; the others are invalid in Databricks SQL."
        },
        # Q12
        {
            "q": "Which statement about dropping a database in Unity Catalog is true?",
            "options": [
                "Managed tables in the database are deleted with it",
                "All external tables in the database are deleted",
                "The command always fails unless the database is empty",
                "Dropping a database archives all its tables for time travel"
            ],
            "answer_text": "Managed tables in the database are deleted with it",
            "explanation": "Dropping a database with CASCADE deletes its managed tables; unmanaged tables’ data remains."
        },
        # Q13
        {
            "q": "Which SQL statement will remove a table but keep its underlying data for future use?",
            "options": [
                "DROP TABLE my_table",
                "DROP TABLE my_table RETAIN DATA",
                "DROP TABLE my_table; data remains automatically for unmanaged tables",
                "DELETE TABLE my_table"
            ],
            "answer_text": "DROP TABLE my_table; data remains automatically for unmanaged tables",
            "explanation": "Unmanaged tables retain their external data after being dropped."
        },
        # Q14
        {
            "q": "What happens when you use CREATE OR REPLACE TABLE in Databricks?",
            "options": [
                "It overwrites the existing table and data",
                "It renames the old table",
                "It merges schemas automatically",
                "It appends to the existing table"
            ],
            "answer_text": "It overwrites the existing table and data",
            "explanation": "CREATE OR REPLACE drops and recreates the table, deleting existing data."
        },
        # Q15
        {
            "q": "Which command will permanently remove an unmanaged table’s metadata from the metastore?",
            "options": [
                "DROP TABLE",
                "DROP EXTERNAL TABLE",
                "REMOVE TABLE",
                "PURGE TABLE"
            ],
            "answer_text": "DROP TABLE",
            "explanation": "DROP TABLE removes metadata; unmanaged table data remains."
        },
        # Q16
        {
            "q": "Which type of view is stored in the metastore and persists across sessions?",
            "options": [
                "Temporary view",
                "Permanent view",
                "Global temp view",
                "Catalog view"
            ],
            "answer_text": "Permanent view",
            "explanation": "Permanent views are stored in the metastore and persist until dropped."
        },
        # Q17
        {
            "q": "Why use a global temp view?",
            "options": [
                "To share a query definition across multiple sessions without saving as a permanent view",
                "To store results in Delta format",
                "To cache a dataset in memory",
                "To bypass Unity Catalog"
            ],
            "answer_text": "To share a query definition across multiple sessions without saving as a permanent view",
            "explanation": "Global temp views persist across sessions while the warehouse is running."
        },
        # Q18
        {
            "q": "Which database contains all global temp views?",
            "options": [
                "temp_views",
                "global_temp",
                "shared_views",
                "default"
            ],
            "answer_text": "global_temp",
            "explanation": "Global temp views live in the global_temp database."
        },
        # Q19
        {
            "q": "What happens to a global temp view when the SQL warehouse stops?",
            "options": [
                "It persists until explicitly dropped",
                "It is dropped automatically",
                "It becomes a permanent view",
                "It is stored in DBFS until deleted"
            ],
            "answer_text": "It is dropped automatically",
            "explanation": "Global temp views are removed when the warehouse stops."
        },
        # Q20
        {
            "q": "Which SQL creates a permanent view from an existing table?",
            "options": [
                "CREATE VIEW v_orders AS SELECT * FROM orders;",
                "CREATE TEMP VIEW v_orders AS SELECT * FROM orders;",
                "CREATE GLOBAL TEMP VIEW v_orders AS SELECT * FROM orders;",
                "CREATE MATERIALIZED VIEW v_orders AS SELECT * FROM orders;"
            ],
            "answer_text": "CREATE VIEW v_orders AS SELECT * FROM orders;",
            "explanation": "CREATE VIEW without TEMP or GLOBAL TEMP creates a permanent view."
        },

        # I can continue Q21–Q45 now in exactly the same style if you confirm you want me to keep going in this message.
                # Q21
        {
            "q": "Which tab in Data Explorer allows you to see which groups have SELECT access to a table?",
            "options": [
                "Permissions",
                "Metadata",
                "Preview",
                "Schema"
            ],
            "answer_text": "Permissions",
            "explanation": "The Permissions tab in Data Explorer shows granted privileges, including which groups can SELECT from the table."
        },
        # Q22
        {
            "q": "Which of the following can you NOT do directly in Data Explorer?",
            "options": [
                "Rename a table",
                "Grant privileges",
                "View schema",
                "Preview data"
            ],
            "answer_text": "Rename a table",
            "explanation": "You cannot rename tables directly from Data Explorer — this must be done with SQL."
        },
        # Q23
        {
            "q": "If you are the owner of a table in Unity Catalog, which can you do?",
            "options": [
                "Transfer ownership to another user",
                "Disable warehouse access for a database",
                "Change the Delta log retention period",
                "Change Unity Catalog region"
            ],
            "answer_text": "Transfer ownership to another user",
            "explanation": "Table owners can transfer ownership to another user or group."
        },
        # Q24
        {
            "q": "Which permission is needed to see the list of all tables in a schema?",
            "options": [
                "USAGE on the schema",
                "SELECT on all tables",
                "READ_SCHEMA",
                "DESCRIBE_CATALOG"
            ],
            "answer_text": "USAGE on the schema",
            "explanation": "USAGE on the schema is required to list objects within it."
        },
        # Q25
        {
            "q": "What is one way to secure a table containing confidential marketing data?",
            "options": [
                "Apply row-level filters via Unity Catalog",
                "Rename the table to hide it",
                "Move the table to unmanaged storage",
                "Store it only in DBFS mounts"
            ],
            "answer_text": "Apply row-level filters via Unity Catalog",
            "explanation": "Unity Catalog supports row- and column-level security to protect sensitive data."
        },
        # Q26
        {
            "q": "Which of these is considered PII in a retail dataset?",
            "options": [
                "Transaction timestamp",
                "Customer phone number",
                "SKU ID",
                "Store region code"
            ],
            "answer_text": "Customer phone number",
            "explanation": "Personally Identifiable Information includes details like phone numbers that can directly identify a person."
        },
        # Q27
        {
            "q": "What is a good practice for handling PII in Databricks?",
            "options": [
                "Use Unity Catalog’s column masking for sensitive fields",
                "Store PII only in unmanaged tables",
                "Use the Bronze layer exclusively",
                "Avoid Delta format for PII data"
            ],
            "answer_text": "Use Unity Catalog’s column masking for sensitive fields",
            "explanation": "Column masking in Unity Catalog can restrict PII visibility based on permissions."
        },
        # Q28
        {
            "q": "Which security control can Unity Catalog apply at the column level?",
            "options": [
                "Data type casting",
                "Access permissions",
                "Schema evolution",
                "Delta caching"
            ],
            "answer_text": "Access permissions",
            "explanation": "Unity Catalog can grant/revoke access at column level."
        },
        # Q29
        {
            "q": "Which law often governs handling of PII in the EU?",
            "options": [
                "GDPR",
                "HIPAA",
                "CCPA",
                "PCI-DSS"
            ],
            "answer_text": "GDPR",
            "explanation": "The General Data Protection Regulation (GDPR) governs PII handling in the EU."
        },
        # Q30
        {
            "q": "Which is NOT an example of PII?",
            "options": [
                "Driver’s license number",
                "IP address tied to a user",
                "Product price",
                "Passport number"
            ],
            "answer_text": "Product price",
            "explanation": "Product price is not tied to a specific individual, so it's not PII."
        },
        # Q31
        {
            "q": "A teammate drops a table but the files still exist in S3. What type of table was it?",
            "options": [
                "Managed",
                "Unmanaged",
                "Global temp view",
                "Permanent view"
            ],
            "answer_text": "Unmanaged",
            "explanation": "Dropping an unmanaged table only removes metadata; files remain in the external location."
        },
        # Q32
        {
            "q": "You attempt to preview a table in Data Explorer but get an error about no running warehouse. What must you do?",
            "options": [
                "Start any SQL warehouse you have access to",
                "Restart your cluster",
                "Enable Unity Catalog",
                "Increase the Delta log retention"
            ],
            "answer_text": "Start any SQL warehouse you have access to",
            "explanation": "Previewing tables requires a running SQL warehouse."
        },
        # Q33
        {
            "q": "You need to rename a table without changing where its files are stored. Which is correct?",
            "options": [
                "ALTER TABLE old RENAME TO new",
                "MOVE TABLE old TO new",
                "ALTER TABLE LOCATION 'new_path'",
                "RENAME PATH old new"
            ],
            "answer_text": "ALTER TABLE old RENAME TO new",
            "explanation": "ALTER TABLE ... RENAME changes the table name without moving data."
        },
        # Q34
        {
            "q": "Which operation always requires a running SQL warehouse?",
            "options": [
                "Query execution",
                "Viewing table schema in Data Explorer",
                "Viewing permissions in Data Explorer",
                "Listing databases"
            ],
            "answer_text": "Query execution",
            "explanation": "Executing SQL queries always needs a running warehouse."
        },
        # Q35
        {
            "q": "You query a global temp view but get “table not found.” Most likely reason?",
            "options": [
                "Wrong warehouse size",
                "The session that created it ended and warehouse restarted",
                "The table is unmanaged",
                "The view was hidden in Unity Catalog"
            ],
            "answer_text": "The session that created it ended and warehouse restarted",
            "explanation": "Global temp views are session-scoped to the warehouse lifetime."
        },
        # Q36
        {
            "q": "How does Delta Lake handle concurrent writes?",
            "options": [
                "Last writer wins",
                "Through optimistic concurrency control",
                "By locking the table",
                "It rejects concurrent writes"
            ],
            "answer_text": "Through optimistic concurrency control",
            "explanation": "Delta uses OCC to ensure consistency while allowing concurrent writes."
        },
        # Q37
        {
            "q": "Which operation can change the schema of an existing Delta table?",
            "options": [
                "ALTER TABLE ADD COLUMNS",
                "UPDATE TABLE SCHEMA FORCE",
                "MODIFY TABLE COLUMNS",
                "CHANGE SCHEMA"
            ],
            "answer_text": "ALTER TABLE ADD COLUMNS",
            "explanation": "ALTER TABLE ADD COLUMNS is a valid way to evolve a schema."
        },
        # Q38
        {
            "q": "What happens if new data with additional columns is written to a Delta table without schema evolution enabled?",
            "options": [
                "The write fails",
                "The table adds the columns automatically",
                "The data is ignored silently",
                "The columns are stored as JSON"
            ],
            "answer_text": "The write fails",
            "explanation": "Without schema evolution, Delta rejects writes with extra columns."
        },
        # Q39
        {
            "q": "Which optimization command can improve small file performance in Delta tables?",
            "options": [
                "OPTIMIZE my_table",
                "VACUUM my_table",
                "COMPACT my_table",
                "MERGE my_table"
            ],
            "answer_text": "OPTIMIZE my_table",
            "explanation": "OPTIMIZE compacts many small files into fewer large ones for better performance."
        },
        # Q40
        {
            "q": "What does VACUUM do in Delta Lake?",
            "options": [
                "Remove old, unreferenced files from storage",
                "Reclaim memory from warehouses",
                "Delete current Delta log files",
                "Merge small files into larger ones"
            ],
            "answer_text": "Remove old, unreferenced files from storage",
            "explanation": "VACUUM cleans up data files no longer needed for any table version."
        },
        # Q41
        {
            "q": "Which statement about permanent views is correct?",
            "options": [
                "They store query definitions and persist until explicitly dropped",
                "They store actual data in Delta format",
                "They expire at warehouse restart",
                "They cannot reference unmanaged tables"
            ],
            "answer_text": "They store query definitions and persist until explicitly dropped",
            "explanation": "Permanent views are metadata objects storing SQL definitions."
        },
        # Q42
        {
            "q": "Which privilege allows a user to create a new table in a schema?",
            "options": [
                "CREATE on the schema",
                "SELECT on the schema",
                "USAGE on the schema",
                "INSERT on the schema"
            ],
            "answer_text": "CREATE on the schema",
            "explanation": "CREATE privilege is required to create objects in a schema."
        },
        # Q43
        {
            "q": "How can you quickly confirm whether a table is Delta format?",
            "options": [
                "DESCRIBE DETAIL table_name",
                "SHOW FORMAT table_name",
                "VIEW HISTORY table_name",
                "SELECT delta_format FROM metadata"
            ],
            "answer_text": "DESCRIBE DETAIL table_name",
            "explanation": "DESCRIBE DETAIL shows the format among other table properties."
        },
        # Q44
        {
            "q": "What does SHOW TABLES IN my_db return?",
            "options": [
                "All tables and views in that database",
                "Only managed tables in that database",
                "All Delta tables in Unity Catalog",
                "All temporary views created in the session"
            ],
            "answer_text": "All tables and views in that database",
            "explanation": "SHOW TABLES lists all tables and views within the database."
        },
        # Q45
        {
            "q": "Which is a valid reason to use DESCRIBE DETAIL?",
            "options": [
                "To get table format, location, and created-by information",
                "To preview first 10 rows of the table",
                "To see the last 10 SQL queries run",
                "To change table permissions"
            ],
            "answer_text": "To get table format, location, and created-by information",
            "explanation": "DESCRIBE DETAIL provides metadata about the table including format, path, and owner."
        }
    ]
}
