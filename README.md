#  Hospital Appointment and Patient Management System

**Course:** MTM4692 - Applied SQL (Spring 2026)  
**Instructor:** Fettah KIRAN  
**Project Phase:** Milestone 1 Submission  

##  Project Overview
The Hospital Appointment and Patient Management System is a robust relational database designed to solve the complexities of modern healthcare scheduling and data management. It handles patient records, doctor availability, appointment tracking, and medical histories.

##  Problem Statement
In many hospitals, appointment scheduling conflicts, fragmented patient medical histories, and inefficient doctor workload tracking lead to significant time loss and reduced quality of care. Managing dynamic patient data (like allergies or specific physical attributes) within a rigid tabular structure often proves inadequate, leading to sparse data and inflexible schemas.

##  Our Solution & Justification
This database solves these issues by utilizing a 7-table normalized relational schema (meeting the course's 6-8 table requirement). 

To handle dynamic medical data without constantly altering the schema, we implemented **JSON data types** for patient attributes. We also utilized **Views** to simplify complex multi-table queries for front-end applications (e.g., daily doctor schedules), and we laid the groundwork to use **Common Table Expressions (CTEs)** to analyze departmental workloads efficiently.

##  Key SQL Features Implemented (Course Integration)
* **Data Integrity & Constraints (Week 2):** Strict use of `PRIMARY KEY`, `FOREIGN KEY` (with `ON DELETE CASCADE`), `UNIQUE`, and `CHECK` constraints to ensure data validity (e.g., ensuring appointment statuses are valid).
* **Views (Week 5):** Abstraction of complex `JOIN` operations to provide simple, up-to-date daily schedules for doctors.
* **NoSQL Capabilities / JSON Functions (Week 6):** Storing variable patient attributes (blood type, allergies) using SQLite's JSON capabilities (`json_extract`), combining ACID guarantees with NoSQL flexibility.
* **CTEs & Advanced Queries (Week 3 & 7):** Use of `WITH` clauses for advanced aggregation to analyze department performance.

##  Database Schema Design
The database consists of the following 7 interrelated tables:
1. `departments`: Hospital departments (Cardiology, Emergency, etc.)
2. `doctors`: Physician details linked to departments.
3. `patients`: Core demographics and a `JSON` column for medical attributes.
4. **`appointments`**: The central junction table connecting patients and doctors.
5. `medical_records`: Diagnosis details linked to completed appointments.
6. `medications`: A library of available drugs.
7. `prescriptions`: A many-to-many resolution table linking records to medications.

##  Repository Contents
* **`schema.sql`**: Contains the DDL statements (Table creations and constraints).
* **`generate_data.py`**: A Python script utilizing the `Faker` library to procedurally generate thousands of realistic, relational mock data points.
* **`hastane_verileri.sql`**: The output of the Python script containing the DML (`INSERT`) statements for robust testing.
* **`Milestone_Report.pdf`**: The detailed 2-3 page technical report.

## 🚀 How to Run
1. Execute `schema.sql` in your SQLite environment to build the tables.
2. Execute `hastane_verileri.sql` to populate the database with procedurally generated mock data.
3. Test the sample queries provided in the Milestone Report.
