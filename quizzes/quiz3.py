# quiz2.py
title = "Databricks SQL – Section 2 Advanced Practice Test (Data Management)"

questions = [
    {
        "q": "Which of the following best describes Delta Lake within the Databricks Lakehouse?",
        "options": [
            "A storage format for JSON and CSV data only.",
            "A transaction layer that adds ACID properties and metadata management to data files.",
            "A streaming-only database for Delta tables.",
            "A warehouse type for low-latency queries."
        ],
        "answer_text": "A transaction layer that adds ACID properties and metadata management to data files.",
        "explanation": "Delta Lake is a storage layer that brings ACID transactions and metadata management to data lakes."
    },
    {
        "q": "What is one direct benefit of Delta Lake’s ability to maintain table history?",
        "options": [
            "Enables rollback to earlier versions of the data for recovery or auditing.",
            "Automatically compresses old data files to reduce storage.",
            "Guarantees faster queries as history grows.",
            "Deletes PII data after 30 days."
        ],
        "answer_text": "Enables rollback to earlier versions of the data for recovery or auditing.",
        "explanation": "Delta Lake allows time travel to restore or audit historical data versions."
    },
    {
        "q": "You run the command: CREATE TABLE sales_data (id INT, amount DOUBLE) USING DELTA LOCATION 's3://company/data/sales'; Which statement is true about this table?",
        "options": [
            "It is a managed table because you specified a schema.",
            "It is unmanaged because you provided a LOCATION outside the default database path.",
            "It is managed and its files will be deleted on DROP TABLE.",
            "It is unmanaged and cannot be queried until manually registered in Unity Catalog."
        ],
        "answer_text": "It is unmanaged because you provided a LOCATION outside the default database path.",
        "explanation": "Specifying an external LOCATION makes the table unmanaged."
    },
    {
        "q": "A database has a default storage path in DBFS. You create a table with the LOCATION keyword pointing to an external S3 path. Which effect does this have?",
        "options": [
            "The table’s files are stored in the external path instead of the DBFS default.",
            "The table remains managed but with extra copies in S3.",
            "LOCATION is ignored unless used with CREATE VIEW.",
            "LOCATION automatically converts the table to Gold layer."
        ],
        "answer_text": "The table’s files are stored in the external path instead of the DBFS default.",
        "explanation": "LOCATION overrides the default managed path and stores files externally."
    },
    {
        "q": "Which statement about managed vs. unmanaged tables in Databricks is correct?",
        "options": [
            "Managed tables always store data in DBFS or Unity Catalog’s default location and delete data when the table is dropped.",
            "Unmanaged tables store metadata in Delta but always delete data when dropped.",
            "Managed tables require the LOCATION keyword to store data.",
            "Unmanaged tables cannot be created in Unity Catalog."
        ],
        "answer_text": "Managed tables always store data in DBFS or Unity Catalog’s default location and delete data when the table is dropped.",
        "explanation": "Managed tables are stored in the system's default path and deleted fully when dropped."
    },
    {
        "q": "Which command will create a temporary view named temp_sales that disappears after the session ends?",
        "options": [
            "CREATE VIEW temp_sales AS SELECT * FROM sales;",
            "CREATE TEMP VIEW temp_sales AS SELECT * FROM sales;",
            "CREATE OR REPLACE VIEW temp_sales AS SELECT * FROM sales;",
            "CREATE GLOBAL TEMP VIEW temp_sales AS SELECT * FROM sales;"
        ],
        "answer_text": "CREATE TEMP VIEW temp_sales AS SELECT * FROM sales;",
        "explanation": "TEMP VIEWs are session-scoped and disappear after the session ends."
    },
    {
        "q": "Which is true about temp views compared to permanent views?",
        "options": [
            "Temp views persist across all user sessions.",
            "Temp views are session-scoped and do not persist beyond the session.",
            "Temp views are stored in the Gold layer.",
            "Temp views are automatically converted to permanent views on save."
        ],
        "answer_text": "Temp views are session-scoped and do not persist beyond the session.",
        "explanation": "Temp views exist only in the session where they are created."
    },
    {
        "q": "You create a view sales_summary and later the underlying table sales is dropped. What happens when you query the view?",
        "options": [
            "The query returns NULL values for all columns.",
            "The view automatically recreates the sales table from Delta history.",
            "The query fails because the underlying table no longer exists.",
            "The view returns stale cached results."
        ],
        "answer_text": "The query fails because the underlying table no longer exists.",
        "explanation": "Views depend on the source table; if it’s dropped, the view becomes invalid."
    },
    {
        "q": "In Data Explorer, which information is not displayed about a table?",
        "options": [
            "Column names and types.",
            "Table owner.",
            "Physical file size in bytes.",
            "Access control settings."
        ],
        "answer_text": "Physical file size in bytes.",
        "explanation": "Data Explorer does not display the exact storage size of a table."
    },
    {
        "q": "A table owner grants “SELECT” permission to another user in Data Explorer. Which responsibility does the owner still retain?",
        "options": [
            "Ensuring the user writes correct SQL queries.",
            "Maintaining data quality and schema consistency.",
            "Paying for the warehouse costs of that user’s queries.",
            "Automatically approving any dashboard using the table."
        ],
        "answer_text": "Maintaining data quality and schema consistency.",
        "explanation": "Table owners are responsible for maintaining the table's integrity."
    },
    # Q11 - Q45 would continue here in the same format...
        {
        "q": "Which statement about table ownership in Databricks is correct?",
        "options": [
            "The table owner can transfer ownership to another user.",
            "The table owner cannot view access permissions.",
            "The table owner loses privileges if the table becomes unmanaged.",
            "Table ownership is tied to SQL Warehouse configuration."
        ],
        "answer_text": "The table owner can transfer ownership to another user.",
        "explanation": "Ownership can be reassigned in Unity Catalog by an existing owner or admin."
    },
    {
        "q": "In an organization with strict PII handling rules, which is the best practice when storing sensitive customer data in Databricks?",
        "options": [
            "Store PII only in Bronze layer to avoid exposure in Gold tables.",
            "Apply row-level or column-level access controls and masking for sensitive fields.",
            "Delete PII every 24 hours to comply with GDPR.",
            "Store PII only in unmanaged tables so it can be physically deleted."
        ],
        "answer_text": "Apply row-level or column-level access controls and masking for sensitive fields.",
        "explanation": "Proper masking and fine-grained access control protects sensitive data."
    },
    {
        "q": "You need to preview the first 10 rows of a Delta table without writing SQL. Which tool in Databricks can you use?",
        "options": [
            "Data Explorer’s “Preview Table” feature.",
            "Query Editor autocomplete.",
            "Partner Connect schema sync.",
            "Managed table inspector."
        ],
        "answer_text": "Data Explorer’s “Preview Table” feature.",
        "explanation": "Data Explorer lets you preview rows of a table directly."
    },
    {
        "q": "Which command sequence correctly creates, switches to, and drops a database?",
        "options": [
            "CREATE DATABASE finance; USE finance; DROP DATABASE finance;",
            "CREATE DATABASE finance; USE DATABASE finance; DELETE DATABASE finance;",
            "CREATE SCHEMA finance; ACTIVATE finance; DROP SCHEMA finance;",
            "CREATE DATABASE finance; USE finance; REMOVE DATABASE finance;"
        ],
        "answer_text": "CREATE DATABASE finance; USE finance; DROP DATABASE finance;",
        "explanation": "This is the valid SQL syntax in Databricks."
    },
    {
        "q": "Dropping a managed Delta table in Unity Catalog will:",
        "options": [
            "Remove both the table metadata and its underlying data files.",
            "Keep the data files but remove only the metadata.",
            "Archive the table for 30 days.",
            "Remove metadata but leave the data files in DBFS."
        ],
        "answer_text": "Remove both the table metadata and its underlying data files.",
        "explanation": "Managed tables are fully deleted when dropped."
    },
    {
        "q": "Dropping an unmanaged Delta table in Unity Catalog will:",
        "options": [
            "Remove both metadata and files.",
            "Remove metadata but leave underlying files untouched.",
            "Archive the table for version history.",
            "Delete files only if LOCATION is in DBFS."
        ],
        "answer_text": "Remove metadata but leave underlying files untouched.",
        "explanation": "Unmanaged tables leave their data files intact."
    },
    {
        "q": "Which statement about Delta Lake table history is true?",
        "options": [
            "History can be viewed with the DESCRIBE HISTORY command.",
            "History is stored in Unity Catalog only.",
            "History is enabled only for managed tables.",
            "History prevents schema changes."
        ],
        "answer_text": "History can be viewed with the DESCRIBE HISTORY command.",
        "explanation": "The DESCRIBE HISTORY command shows the full table modification history."
    },
    {
        "q": "You rename a table using: ALTER TABLE sales RENAME TO revenue; Which statement is correct?",
        "options": [
            "The table’s Delta files are moved to a new path automatically.",
            "The metadata name changes but underlying files remain in the same location.",
            "Both metadata and files are deleted.",
            "Table history is cleared."
        ],
        "answer_text": "The metadata name changes but underlying files remain in the same location.",
        "explanation": "Renaming a table only changes metadata; files stay in place."
    },
    {
        "q": "Which scenario best illustrates a managed table?",
        "options": [
            "Created without LOCATION and dropped along with its data files by Databricks.",
            "Created with LOCATION and stored in S3.",
            "Stored in external cloud storage controlled by the user.",
            "Created only via Partner Connect ingestion."
        ],
        "answer_text": "Created without LOCATION and dropped along with its data files by Databricks.",
        "explanation": "Managed tables have no external LOCATION specified."
    },
    {
        "q": "Which is not a benefit of Delta Lake within the Lakehouse?",
        "options": [
            "ACID transactions.",
            "Schema enforcement and evolution.",
            "Built-in support for proprietary non-Delta formats.",
            "Time travel queries."
        ],
        "answer_text": "Built-in support for proprietary non-Delta formats.",
        "explanation": "Delta Lake works with open formats; proprietary formats are not a built-in feature."
    },
    {
        "q": "Which SQL statement will create a table whose data is stored in the default location for its database?",
        "options": [
            "CREATE TABLE orders (id INT) USING DELTA;",
            "CREATE TABLE orders (id INT) USING DELTA LOCATION 's3://bucket/orders';",
            "CREATE UNMANAGED TABLE orders (id INT) USING DELTA;",
            "CREATE DATABASE orders;"
        ],
        "answer_text": "CREATE TABLE orders (id INT) USING DELTA;",
        "explanation": "Omitting LOCATION stores the data in the default managed path."
    },
    {
        "q": "Which describes a global temp view in Databricks?",
        "options": [
            "Exists for the duration of the current session.",
            "Is shared across all sessions until the cluster/warehouse restarts.",
            "Is permanently stored in Unity Catalog.",
            "Cannot reference managed tables."
        ],
        "answer_text": "Is shared across all sessions until the cluster/warehouse restarts.",
        "explanation": "Global temp views are shared but cleared when the cluster ends."
    },
    {
        "q": "When previewing data in Data Explorer, what warehouse requirement must be met?",
        "options": [
            "Any running SQL Warehouse with read access to the table.",
            "A Serverless SQL Warehouse only.",
            "The largest warehouse size available.",
            "Unity Catalog must be disabled."
        ],
        "answer_text": "Any running SQL Warehouse with read access to the table.",
        "explanation": "Previewing data requires a running SQL Warehouse."
    },
    {
        "q": "You want to identify whether an existing table is managed or unmanaged. Where is the quickest place to check?",
        "options": [
            "DESCRIBE EXTENDED <table_name> in SQL Editor.",
            "Dashboard permissions page.",
            "Partner Connect integration list.",
            "Table owner profile in Data Explorer."
        ],
        "answer_text": "DESCRIBE EXTENDED <table_name> in SQL Editor.",
        "explanation": "DESCRIBE EXTENDED shows the storage location and table type."
    },
    {
        "q": "Which of the following is true about views in Databricks?",
        "options": [
            "A view stores query results physically in Delta.",
            "A view is a stored query definition, not the data itself.",
            "Views must always be created in the Gold layer.",
            "Dropping a view deletes the underlying data."
        ],
        "answer_text": "A view is a stored query definition, not the data itself.",
        "explanation": "Views are logical objects that store SQL, not data."
    },
    {
        "q": "Which Delta Lake feature allows querying a table’s state from last week without maintaining a separate snapshot table?",
        "options": [
            "Schema enforcement",
            "Time travel",
            "ACID transactions",
            "Delta caching"
        ],
        "answer_text": "Time travel",
        "explanation": "Time travel lets you query historical versions of data."
    },
    {
        "q": "Which is a valid reason to use an unmanaged table in Databricks?",
        "options": [
            "To ensure the table is included in DROP DATABASE cleanup.",
            "To store data in a specific cloud location outside the default DBFS/Unity Catalog path.",
            "To guarantee faster query performance.",
            "To make it compatible only with Partner Connect tools."
        ],
        "answer_text": "To store data in a specific cloud location outside the default DBFS/Unity Catalog path.",
        "explanation": "Unmanaged tables allow control over data location."
    },
    {
        "q": "If a managed table is dropped, what happens to its underlying files?",
        "options": [
            "They are archived in Delta history.",
            "They are deleted from storage along with the metadata.",
            "They remain in place but are hidden from queries.",
            "They move automatically to a Bronze folder."
        ],
        "answer_text": "They are deleted from storage along with the metadata.",
        "explanation": "Dropping a managed table removes both files and metadata."
    },
    {
        "q": "What does the USING DELTA clause in a CREATE TABLE statement specify?",
        "options": [
            "That the table will store data in JSON format.",
            "That the table will use the Delta Lake transaction log and storage format.",
            "That the table will be created as unmanaged.",
            "That the table will be created in the Gold layer."
        ],
        "answer_text": "That the table will use the Delta Lake transaction log and storage format.",
        "explanation": "USING DELTA enables Delta Lake features for the table."
    },
    {
        "q": "Which view type can be referenced by any session within the same cluster/warehouse until it restarts?",
        "options": [
            "Local temp view",
            "Global temp view",
            "Managed view",
            "Catalog-scoped view"
        ],
        "answer_text": "Global temp view",
        "explanation": "Global temp views persist across sessions until the cluster stops."
    },
    {
        "q": "What is a key difference between managed and unmanaged Delta tables when dropping the table?",
        "options": [
            "Managed tables remove both data and metadata; unmanaged remove only metadata.",
            "Managed tables remove only metadata; unmanaged remove both.",
            "Managed tables cannot be dropped in Unity Catalog.",
            "There is no difference — both behave identically."
        ],
        "answer_text": "Managed tables remove both data and metadata; unmanaged remove only metadata.",
        "explanation": "Managed tables delete files too, unmanaged tables keep files."
    },
    {
        "q": "Which SQL statement both creates and assigns the current session to a new database?",
        "options": [
            "CREATE DATABASE finance; USE finance;",
            "CREATE DATABASE finance USE IMMEDIATELY;",
            "CREATE DATABASE finance; ACTIVATE DATABASE finance;",
            "CREATE OR USE DATABASE finance;"
        ],
        "answer_text": "CREATE DATABASE finance; USE finance;",
        "explanation": "You must issue CREATE DATABASE and then USE to switch context."
    },
    {
        "q": "In Data Explorer, you see that a table is marked with an external location path. What does this indicate?",
        "options": [
            "It is a managed table in Unity Catalog.",
            "It is an unmanaged table storing files outside the default managed location.",
            "It is a temp table that persists across sessions.",
            "It is a Gold layer table."
        ],
        "answer_text": "It is an unmanaged table storing files outside the default managed location.",
        "explanation": "External paths are a hallmark of unmanaged tables."
    },
    {
        "q": "Which of the following operations requires a running SQL Warehouse in Databricks?",
        "options": [
            "Viewing table metadata in Data Explorer.",
            "Previewing sample rows of a table in Data Explorer.",
            "Viewing the table owner name.",
            "Seeing the database list."
        ],
        "answer_text": "Previewing sample rows of a table in Data Explorer.",
        "explanation": "Previewing rows needs compute from a SQL Warehouse."
    },
    {
        "q": "You want to rename a managed table without moving its data files. Which command achieves this?",
        "options": [
            "ALTER TABLE old_name RENAME TO new_name;",
            "RENAME DELTA PATH old TO new;",
            "MOVE TABLE old TO new;",
            "ALTER TABLE LOCATION 'new_path';"
        ],
        "answer_text": "ALTER TABLE old_name RENAME TO new_name;",
        "explanation": "This changes only the metadata name."
    },
    {
        "q": "Which is a benefit of schema enforcement in Delta Lake?",
        "options": [
            "Prevents data from being overwritten when schema changes.",
            "Ensures only data matching the defined column structure can be inserted.",
            "Automatically compresses files on schema change.",
            "Speeds up SELECT queries."
        ],
        "answer_text": "Ensures only data matching the defined column structure can be inserted.",
        "explanation": "Schema enforcement validates incoming data against the table schema."
    },
    {
        "q": "Which best describes a permanent view in Databricks?",
        "options": [
            "A saved query definition that persists until dropped, stored in a database.",
            "A cached dataset that updates automatically.",
            "A temp table that disappears after the session ends.",
            "A global view that can only be queried from the Gold layer."
        ],
        "answer_text": "A saved query definition that persists until dropped, stored in a database.",
        "explanation": "Permanent views remain until explicitly dropped."
    },
    {
        "q": "You have sensitive PII data in a Gold table. Which is the most secure approach to limit exposure?",
        "options": [
            "Move the table to Bronze.",
            "Use column-level masking and fine-grained access controls in Unity Catalog.",
            "Rename columns containing PII.",
            "Store PII in unmanaged tables only."
        ],
        "answer_text": "Use column-level masking and fine-grained access controls in Unity Catalog.",
        "explanation": "Masking and access control are best practices for PII."
    },
    {
        "q": "What happens when you DROP VIEW myview;?",
        "options": [
            "Only the view definition is removed; underlying tables remain intact.",
            "Both the view and its underlying tables are deleted.",
            "The view is marked as deprecated but kept in history.",
            "The view becomes a temp view."
        ],
        "answer_text": "Only the view definition is removed; underlying tables remain intact.",
        "explanation": "Dropping a view doesn’t affect its source tables."
    },
    {
        "q": "Which command can be used to check the history of changes to a Delta table?",
        "options": [
            "DESCRIBE EXTENDED",
            "DESCRIBE HISTORY",
            "SHOW METADATA",
            "SHOW HISTORY"
        ],
        "answer_text": "DESCRIBE HISTORY",
        "explanation": "DESCRIBE HISTORY lists all past commits to the table."
    },
    {
        "q": "A temp view created without GLOBAL scope:",
        "options": [
            "Is visible only in the session where it was created.",
            "Is visible across all sessions until manually dropped.",
            "Is persisted in Unity Catalog.",
            "Is stored in the Gold layer by default."
        ],
        "answer_text": "Is visible only in the session where it was created.",
        "explanation": "Local temp views are scoped to a single session."
    },
    {
        "q": "Which LOCATION path will result in a managed table in Unity Catalog?",
        "options": [
            "LOCATION set to the default catalog-managed storage location.",
            "LOCATION set to any S3 bucket path.",
            "LOCATION set to /mnt/externaldata.",
            "LOCATION set to a local temp directory."
        ],
        "answer_text": "LOCATION set to the default catalog-managed storage location.",
        "explanation": "Only the default managed storage path produces managed tables."
    },
    {
        "q": "Which is not a benefit of Delta Lake’s ACID compliance?",
        "options": [
            "Reliable transaction commits.",
            "Protection against partial writes.",
            "Automatic conversion of CSV to Delta format.",
            "Read consistency during writes."
        ],
        "answer_text": "Automatic conversion of CSV to Delta format.",
        "explanation": "ACID compliance is unrelated to format conversion."
    },
    {
        "q": "Which operation can be performed without dropping and recreating a table?",
        "options": [
            "Renaming the table.",
            "Changing the table from managed to unmanaged.",
            "Moving the table’s files to a new LOCATION.",
            "Removing table history."
        ],
        "answer_text": "Renaming the table.",
        "explanation": "ALTER TABLE RENAME does not require recreation."
    },
    {
        "q": "In Data Explorer, where can you check and modify table permissions?",
        "options": [
            "Permissions tab in the table’s details page.",
            "Query Editor under “Access Control.”",
            "SQL Warehouse configuration.",
            "Unity Catalog cluster settings."
        ],
        "answer_text": "Permissions tab in the table’s details page.",
        "explanation": "The Permissions tab controls access rights for tables."
    }
]

quiz = {
    "title": title,
    "questions": questions
}