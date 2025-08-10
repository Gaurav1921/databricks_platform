
quiz = {
    "title": "Databricks SQL – 45 Question Practice Test",
    "questions": [
        {
            "q": "Which is the primary audience for Databricks SQL?",
            "options": ["Data Engineers", "Data Analysts", "Business Executives", "Data Scientists"],
            "answer_text": "Data Analysts",
            "explanation": "Correct: Databricks SQL is designed primarily for Data Analysts, enabling them to run queries, create dashboards, and analyze data without heavy coding. Wrong: Data Engineers typically handle infrastructure, not interactive analysis. Business Executives consume insights, not create them in Databricks SQL. Data Scientists may use notebooks for ML instead."
        },
        {
            "q": "Which of the following is NOT a side audience for Databricks SQL?",
            "options": ["Business Analysts", "Marketing Managers", "Network Security Engineers", "Data Scientists"],
            "answer_text": "Network Security Engineers",
            "explanation": "Correct: Network Security Engineers are not typical Databricks SQL users. Wrong: Business Analysts, Marketing Managers, and Data Scientists can use it for querying and analytics."
        },
        {
            "q": "Which permission level allows a stakeholder to change the queries inside a dashboard?",
            "options": ["Can Run", "Can Edit", "Can View", "Read-Only"],
            "answer_text": "Can Edit",
            "explanation": "Correct: 'Can Edit' lets a stakeholder modify queries in a dashboard. Wrong: 'Can Run' only refreshes data. 'Can View' and 'Read-Only' allow viewing without changes."
        },
        {
            "q": "What’s the main benefit of using Databricks SQL for in-Lakehouse processing?",
            "options": ["It automatically exports data to Excel", "You can run SQL directly on Lakehouse data without moving it to a warehouse", "It stores data in JSON format only", "It replaces all ETL tools"],
            "answer_text": "You can run SQL directly on Lakehouse data without moving it to a warehouse",
            "explanation": "Correct: Databricks SQL queries data in place, no warehouse copy needed. Wrong: It doesn't auto-export to Excel, isn't JSON-only, and doesn't replace all ETL tools."
        },
        {
            "q": "Before running a query in Databricks SQL, what’s the first thing you must check?",
            "options": ["If Unity Catalog is enabled", "If the SQL Warehouse is running", "If you have a Tableau license", "If the table has a gold layer"],
            "answer_text": "If the SQL Warehouse is running",
            "explanation": "Correct: Queries require a running SQL Warehouse. Wrong: Unity Catalog is for governance, Tableau license is irrelevant, gold layer isn't mandatory for running queries."
        },
        {
            "q": "Databricks SQL Queries are:",
            "options": ["The place to run Python code in Databricks", "A saved or ad-hoc SQL statement executed against Lakehouse data", "Only usable in notebooks", "Stored in cloud storage only"],
            "answer_text": "A saved or ad-hoc SQL statement executed against Lakehouse data",
            "explanation": "Correct: Queries can be saved or run ad-hoc. Wrong: It's not for Python, not limited to notebooks, and not just stored in cloud storage."
        },
        {
            "q": "Which of the following is NOT shown in the Schema Browser?",
            "options": ["Column names", "Column data types", "Table preview data", "Databases list"],
            "answer_text": "Table preview data",
            "explanation": "Correct: Schema Browser shows structure but not preview data. Wrong: It lists columns, data types, and database list."
        },
        {
            "q": "A Databricks SQL dashboard can contain:",
            "options": ["Only one query at a time", "Multiple saved queries combined as tiles", "Only tables, no charts", "Only SQL code without visualizations"],
            "answer_text": "Multiple saved queries combined as tiles",
            "explanation": "Correct: Dashboards can have many query tiles. Wrong: It's not limited to one query, supports charts, and includes visualizations."
        },
        {
            "q": "What’s the first step in creating a Databricks SQL dashboard?",
            "options": ["Apply filters", "Save the queries you want to use", "Invite stakeholders", "Resize dashboard tiles"],
            "answer_text": "Save the queries you want to use",
            "explanation": "Correct: You need saved queries first. Wrong: Filters, invites, and resizing happen after dashboard creation."
        },
        {
            "q": "What’s one downside of setting a very short auto-refresh interval for a dashboard?",
            "options": ["Data will not update", "Costs will increase", "The dashboard will stop working", "It removes access permissions"],
            "answer_text": "Costs will increase",
            "explanation": "Correct: Frequent refresh uses more compute, raising costs. Wrong: Data updates fine, dashboard won't stop, and permissions stay intact."
        },
        # ... continue the same structure for all 45 ...
        {
            "q": "The main purpose of a SQL Warehouse is to:",
            "options": ["Store JSON files", "Act as compute to run SQL queries", "Replace Delta tables", "Host BI dashboards"],
            "answer_text": "Act as compute to run SQL queries",
            "explanation": "Correct: SQL Warehouses provide the compute resources for running SQL in Databricks. Wrong: They don't store JSON files, replace Delta tables, or directly host BI dashboards."
        },
        {
            "q": "Which of the following is a benefit of Serverless SQL Warehouses?",
            "options": ["Require manual scaling setup", "Faster startup times", "Only work for batch data", "Store data permanently"],
            "answer_text": "Faster startup times",
            "explanation": "Correct: Serverless SQL Warehouses start quickly and auto-scale without manual setup. Wrong: They don't require manual scaling, aren't limited to batch data, and don't store data permanently."
        },
        {
            "q": "Which is the main trade-off between warehouse size and cost?",
            "options": ["Larger = faster queries, higher cost", "Larger = slower queries, higher cost", "Smaller = faster queries, higher cost", "Smaller = slower queries, lower cost"],
            "answer_text": "Larger = faster queries, higher cost",
            "explanation": "Correct: Bigger warehouses process queries faster but cost more. Wrong: Larger doesn't mean slower, and smaller warehouses are slower but cheaper."
        },
        {
            "q": "Partner Connect is mainly used to:",
            "options": ["Schedule Databricks jobs", "Implement quick integrations with partner tools", "Store files in Delta format", "Replace BI tools"],
            "answer_text": "Implement quick integrations with partner tools",
            "explanation": "Correct: Partner Connect simplifies connecting Databricks to external tools. Wrong: It doesn't schedule jobs, store files, or replace BI tools."
        },
        {
            "q": "To connect Databricks SQL to Fivetran via Partner Connect, you must:",
            "options": ["Manually install ODBC drivers", "Have or create a Fivetran account", "Export data to CSV", "Install Tableau"],
            "answer_text": "Have or create a Fivetran account",
            "explanation": "Correct: You need a valid Fivetran account. Wrong: Manual drivers aren't needed via Partner Connect, no CSV export is required, and Tableau is unrelated."
        },
        {
            "q": "“Fivetran handles incremental loads automatically” means:",
            "options": ["Fivetran uploads all data every time", "Fivetran only loads new or updated data after the first load", "Data is never updated after the first load", "Fivetran deletes old data on every load"],
            "answer_text": "Fivetran only loads new or updated data after the first load",
            "explanation": "Correct: Incremental load means only changes since last sync are loaded. Wrong: It's not full reloads, no ignoring updates, and doesn't delete old data unless configured."
        },
        {
            "q": "To use a partner product via Partner Connect, you must:",
            "options": ["Already have a Databricks dashboard", "Have access to or create an account with the partner tool", "Build a Delta Live Table", "Use notebooks only"],
            "answer_text": "Have access to or create an account with the partner tool",
            "explanation": "Correct: An account is required for partner tools. Wrong: You don't need a dashboard, DLT, or notebooks to connect."
        },
        {
            "q": "Small-file upload in Databricks SQL is best for:",
            "options": ["Loading multi-GB transaction tables", "Uploading small CSVs like lookup tables", "Running ML models", "Building Spark clusters"],
            "answer_text": "Uploading small CSVs like lookup tables",
            "explanation": "Correct: Small-file upload is for quick lightweight CSVs. Wrong: It's not for big tables, ML, or cluster building."
        },
        {
            "q": "Which SQL command is often used to import data from object storage into Delta tables?",
            "options": ["CREATE VIEW", "COPY INTO", "EXPORT TO", "INSERT OVERWRITE"],
            "answer_text": "COPY INTO",
            "explanation": "Correct: COPY INTO loads data from object storage into Delta tables. Wrong: CREATE VIEW makes views, EXPORT TO isn't SQL standard, and INSERT OVERWRITE replaces table content."
        },
        {
            "q": "When ingesting multiple files from a directory, all files must:",
            "options": ["Be smaller than 5 MB", "Have the same schema and type", "Be CSV only", "Be from the same source system"],
            "answer_text": "Have the same schema and type",
            "explanation": "Correct: All files need identical schema and type for ingestion. Wrong: Size isn't fixed, not limited to CSV, and source system doesn't have to match."
        },
        {
            "q": "Which is NOT a method for connecting Databricks SQL to Tableau?",
            "options": ["ODBC/JDBC driver", "Partner Connect", "Export as JSON and upload", "Direct connector"],
            "answer_text": "Export as JSON and upload",
            "explanation": "Correct: Tableau doesn't support direct JSON uploads. Wrong: ODBC/JDBC, Partner Connect, and direct connectors are valid."
        },
        {
            "q": "Databricks SQL complements BI tools by:",
            "options": ["Preparing and aggregating data before BI consumption", "Replacing all BI visualizations", "Exporting data to Excel", "Running ETL pipelines in notebooks"],
            "answer_text": "Preparing and aggregating data before BI consumption",
            "explanation": "Correct: Databricks SQL preps data for BI. Wrong: It doesn't replace BI charts, doesn't focus on Excel exports, and isn't for heavy ETL in notebooks."
        },
        {
            "q": "The medallion architecture organizes data as:",
            "options": ["Gold → Silver → Bronze", "Raw → Processed → Enriched", "Bronze → Silver → Gold", "Ingested → Transformed → Deleted"],
            "answer_text": "Bronze → Silver → Gold",
            "explanation": "Correct: Bronze is raw, Silver is cleaned, Gold is business-ready. Wrong: The other sequences are incorrect."
        },
        {
            "q": "Which layer is most commonly queried by business analysts?",
            "options": ["Bronze", "Silver", "Gold", "None"],
            "answer_text": "Gold",
            "explanation": "Correct: Gold is the aggregated, business-ready layer. Wrong: Bronze is raw, Silver is cleaned but not aggregated."
        },
        {
            "q": "One benefit of streaming data is:",
            "options": ["Guaranteed complete accuracy at query time", "Real-time insights", "No schema changes ever", "Always cheaper than batch"],
            "answer_text": "Real-time insights",
            "explanation": "Correct: Streaming enables near-real-time analytics. Wrong: Accuracy can vary, schema can change, and cost depends on use case."
        },
        {
            "q": "One caution when working with streaming data is:",
            "options": ["It cannot be visualized", "It may have latency or incomplete data", "It cannot be joined with batch data", "It must always be stored in Bronze layer"],
            "answer_text": "It may have latency or incomplete data",
            "explanation": "Correct: Streaming data can be delayed or partial. Wrong: It can be visualized, joined with batch, and stored beyond Bronze."
        },
        {
            "q": "The Lakehouse allows mixing of batch and streaming workloads because:",
            "options": ["They are stored in different systems", "Both can be stored in the same Delta table", "Streaming overwrites batch data", "Batch data is ignored in queries"],
            "answer_text": "Both can be stored in the same Delta table",
            "explanation": "Correct: Delta tables store both batch and streaming data. Wrong: They don't require different systems, streaming doesn't overwrite batch, and batch isn't ignored."
        },
        {
            "q": "Which of these is NOT a characteristic of the Gold layer?",
            "options": ["Business-ready", "Raw unprocessed data", "Aggregated KPIs", "Cleaned and enriched"],
            "answer_text": "Raw unprocessed data",
            "explanation": "Correct: Raw data is in Bronze, not Gold. Wrong: Gold is business-ready, aggregated, and enriched."
        },
        {
            "q": "What is the primary benefit of Serverless SQL Warehouses over Classic Warehouses?",
            "options": ["They store more data", "They start faster and need no manual scaling setup", "They have lower concurrency", "They are free to use"],
            "answer_text": "They start faster and need no manual scaling setup",
            "explanation": "Correct: Serverless starts quickly and scales automatically. Wrong: Storage isn't the difference, concurrency can be higher, and they're not free."
        },
        {
            "q": "Which statement is true about Schema Browser?",
            "options": ["It shows preview data for a table", "It lists column names and types", "It creates dashboards", "It runs queries automatically"],
            "answer_text": "It lists column names and types",
            "explanation": "Correct: Schema Browser shows table structure. Wrong: It doesn't preview data, create dashboards, or run queries."
        },
        {
            "q": "Which is NOT a step in creating a Databricks SQL dashboard?",
            "options": ["Save queries", "Add queries as tiles", "Resize tiles", "Write SQL directly inside dashboard"],
            "answer_text": "Write SQL directly inside dashboard",
            "explanation": "Correct: Dashboards use saved queries; you don't write SQL in them. Wrong: Saving queries, adding tiles, and resizing are valid steps."
        },
        {
            "q": "In the medallion architecture, Silver layer data is:",
            "options": ["Raw data from source systems", "Cleaned and deduplicated data", "Aggregated business metrics", "Deleted after use"],
            "answer_text": "Cleaned and deduplicated data",
            "explanation": "Correct: Silver data is cleansed and prepared. Wrong: Raw is Bronze, aggregated metrics are Gold, and data isn't deleted."
        },
        {
            "q": "Auto-refresh in dashboards:",
            "options": ["Works without a running warehouse", "Increases costs with shorter intervals", "Deletes old tiles", "Replaces query results with cached files only"],
            "answer_text": "Increases costs with shorter intervals",
            "explanation": "Correct: More frequent refresh increases compute cost. Wrong: Warehouse must run, tiles aren't deleted, and results aren't only cached."
        },
        {
            "q": "Which is NOT a benefit of Databricks SQL in the Lakehouse?",
            "options": ["Lower cost by avoiding duplicate storage", "Direct SQL on Lakehouse data", "Built-in Python ML library", "Integration with BI tools"],
            "answer_text": "Built-in Python ML library",
            "explanation": "Correct: Python ML libraries are in notebooks, not SQL. Wrong: Lower cost, direct SQL, and BI integration are benefits."
        },
        {
            "q": "The Gold layer often contains:",
            "options": ["Duplicate records", "Cleaned, aggregated metrics", "Raw logs", "Unvalidated schema"],
            "answer_text": "Cleaned, aggregated metrics",
            "explanation": "Correct: Gold contains KPIs and metrics. Wrong: Duplicates, raw logs, and unvalidated schema are in earlier layers."
        },
        {
            "q": "Partner Connect provides:",
            "options": ["Pre-configured connections to supported tools", "Free unlimited access to partner products", "A dashboard template library", "SQL optimization tools"],
            "answer_text": "Pre-configured connections to supported tools",
            "explanation": "Correct: Partner Connect offers ready-made connections. Wrong: It doesn't give free partner access, templates, or SQL optimizers."
        },
        # True/False section
        {
            "q": "Databricks SQL queries can only be run after being saved.",
            "options": ["True", "False"],
            "answer_text": "False",
            "explanation": "Correct: You can run ad-hoc queries without saving them."
        },
        {
            "q": "Dashboards can only be viewed by the person who created them.",
            "options": ["True", "False"],
            "answer_text": "False",
            "explanation": "Correct: Permissions allow sharing with others."
        },
        {
            "q": "Serverless SQL Warehouses require manual scaling setup before use.",
            "options": ["True", "False"],
            "answer_text": "False",
            "explanation": "Correct: Serverless scales automatically."
        },
        {
            "q": "Small-file upload is intended for quick, lightweight imports like CSV lookups.",
            "options": ["True", "False"],
            "answer_text": "True",
            "explanation": "Correct: It's designed for small, quick loads."
        },
        {
            "q": "COPY INTO can load both single files and directories if schema matches.",
            "options": ["True", "False"],
            "answer_text": "True",
            "explanation": "Correct: COPY INTO supports single file or directory ingestion."
        },
        {
            "q": "Partner Connect automatically grants a Tableau license to Databricks users.",
            "options": ["True", "False"],
            "answer_text": "False",
            "explanation": "Correct: You must have or acquire Tableau separately."
        },
        {
            "q": "Streaming data may arrive late, causing dashboards to update after initial load.",
            "options": ["True", "False"],
            "answer_text": "True",
            "explanation": "Correct: Latency can cause updates after initial load."
        },
        {
            "q": "The Schema Browser displays table metadata, including column names and data types.",
            "options": ["True", "False"],
            "answer_text": "True",
            "explanation": "Correct: Schema Browser shows metadata, names, and types."
        },
        {
            "q": "The Lakehouse can store batch and streaming data together in the same Delta table.",
            "options": ["True", "False"],
            "answer_text": "True",
            "explanation": "Correct: Delta tables support both batch and streaming."
        }
    ]
}

