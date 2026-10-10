# [数据库设计]

[State the database design scope and governing System, Subsystem, module or component. Identify the selected database and relevant version when known; distinguish current/target design and proposed/accepted decisions. Link the governing architecture, functional designs, evidence, schema and migration scripts that exist.]

## 数据模型

[Explain the core entities, identities and relationships with an entity-relationship diagram. Identify the owner of each authoritative dataset and distinguish referenced or derived data. Explain business meaning and relevant lifecycle rules; reuse one annotated table relationship diagram when it can communicate both meaning and structure.]

## 表设计

[Introduce the table organization, then give every in-scope table a complete physical dictionary using the field contract in ../../references/database-design-writing.md. Expand shared fields locally; identify source-derived definitions or a proposed baseline. Keep a compact table inventory only as navigation, never as a substitute for individual field rows.]

### [schema.table：表名]

[State the purpose and local design status. Repeat this subsection for each table.]

| 字段名 | 数据类型 | 可空 | 默认值 | 主键序号 | 生成方式 | 字段说明 |
| --- | --- | --- | --- | --- | --- | --- |
| `[column]` | `[full native SQL type]` | [YES / NO] | [SQL expression / 无] | [position / 无] | [native generation clause / 无] | [Meaning and unit] |

[Define applicable named UNIQUE, FOREIGN KEY and CHECK constraints with exact SQL or equally explicit structured values. State ordered local/target columns, qualified targets, update/delete and deferral behavior. Define extra indexes by name, method, ordered keys, uniqueness, predicate and included columns; preserve nullable/partial uniqueness semantics. Explain design reasons locally. Add specific partitioning or archival detail only where needed. Mark unresolved physical definitions and their generation consequences.]

## 读写与事务

[Connect the main read/write operations to the tables and indexes they use. Explain index choices through actual filters, joins, ordering and update costs. State which changes commit together and how failures affect the operation. Where competing writes or duplicate requests threaten a named rule, explain the relevant constraint, conditional update, isolation or locking mechanism and caller-visible outcome. Link the owning module's business flow rather than repeating it.]

## 变更与验证

[For changes to an existing database, explain affected readers/writers, compatibility and required data transitions. Add backfill, cutover, failure disposition or recovery detail only for actual migration needs, linking executable scripts and procedures. Connect integrity rules, transaction behavior and important query expectations to planned checks or observed evidence; preserve unresolved targets and unverified results. For a new database without migration work, retain only the applicable validation explanation.]
