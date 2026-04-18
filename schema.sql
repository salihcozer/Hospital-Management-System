PRAGMA foreign_keys = ON;

CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tc_kimlik TEXT UNIQUE NOT NULL,
    full_name TEXT NOT NULL,
    birth_date DATE,
    medical_attributes JSON 
);

CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    appointment_datetime DATETIME NOT NULL,
    status TEXT DEFAULT 'Bekliyor' CHECK(status IN ('Bekliyor', 'Tamamlandı', 'İptal')),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE medical_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER UNIQUE NOT NULL,
    diagnosis TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);

CREATE TABLE medications (
    medication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dosage TEXT NOT NULL
);

CREATE TABLE prescriptions (
    prescription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    record_id INTEGER NOT NULL,
    medication_id INTEGER NOT NULL,
    instructions TEXT,
    FOREIGN KEY (record_id) REFERENCES medical_records(record_id),
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id)
);

CREATE VIEW v_todays_appointments AS
SELECT 
    d.last_name AS Doktor, 
    p.full_name AS Hasta, 
    a.appointment_datetime AS Saat, 
    a.status AS Durum
FROM appointments a
JOIN doctors d ON a.doctor_id = d.doctor_id
JOIN patients p ON a.patient_id = p.patient_id
WHERE DATE(a.appointment_datetime) = DATE('now');

SELECT full_name, json_extract(medical_attributes, '$.blood_type') as Kan_Grubu
FROM patients
WHERE json_extract(medical_attributes, '$.allergies') LIKE '%Penisilin%';


WITH DepartmentWorkload AS (
    SELECT d.name, COUNT(a.appointment_id) as total_appointments
    FROM appointments a
    JOIN doctors doc ON a.doctor_id = doc.doctor_id
    JOIN departments d ON doc.department_id = d.department_id
    GROUP BY d.name
)
SELECT * FROM DepartmentWorkload 
ORDER BY total_appointments DESC LIMIT 3;