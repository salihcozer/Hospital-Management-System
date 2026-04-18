from faker import Faker
import random
import json
from datetime import timedelta

fake = Faker('tr_TR')

NUM_PATIENTS = 500
NUM_DOCTORS = 30
NUM_APPOINTMENTS = 1500
NUM_MEDICATIONS = 20

with open('hastane_verileri.sql', 'w', encoding='utf-8') as f:
    f.write("-- PYTHON FAKER İLE ÜRETİLMİŞ HASTANE VERİ SETİ\n")
    f.write("PRAGMA foreign_keys = ON;\n\n")

    departments = ['Kardiyoloji', 'Dahiliye', 'Ortopedi', 'Nöroloji', 'Acil Servis', 'Pediatri', 'Göz Hastalıkları', 'KBB', 'Genel Cerrahi', 'Cildiye']
    f.write("-- 1. POLİKLİNİKLER\n")
    for dept in departments:
        f.write(f"INSERT INTO departments (name) VALUES ('{dept}');\n")
    
    f.write("\n-- 2. DOKTORLAR\n")
    for i in range(1, NUM_DOCTORS + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        dept_id = random.randint(1, len(departments))
        f.write(f"INSERT INTO doctors (first_name, last_name, department_id) VALUES ('{first_name}', '{last_name}', {dept_id});\n")

    f.write("\n-- 3. HASTALAR\n")
    blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', '0+', '0-']
    allergens = ['Yok', 'Penisilin', 'Aspirin', 'Polen', 'Yer Fıstığı', 'Toz', 'Kedi Tüyü', 'Laktoz']

    for i in range(1, NUM_PATIENTS + 1):
        tc = str(random.randint(10000000000, 99999999999)) 
        name = fake.name()
        birth_date = fake.date_of_birth(minimum_age=5, maximum_age=85).strftime('%Y-%m-%d')
        
        med_attr = {
            "blood_type": random.choice(blood_types),
            "allergies": random.sample(allergens, k=random.randint(1, 2)),
            "weight_kg": random.randint(50, 110),
            "height_cm": random.randint(150, 190)
        }
        
        json_str = json.dumps(med_attr, ensure_ascii=False)
        
        f.write(f"INSERT INTO patients (tc_kimlik, full_name, birth_date, medical_attributes) VALUES ('{tc}', '{name}', '{birth_date}', '{json_str}');\n")

    f.write("\n-- 4. RANDEVULAR VE 5. TIBBİ KAYITLAR\n")
    statuses = ['Bekliyor', 'Tamamlandı', 'İptal']
    diagnoses = ['Hipertansiyon', 'Grip', 'Migren', 'Kırık Şüphesi', 'Diyabet', 'Gastrit', 'Sağlıklı']
    
    completed_records = [] 

    for i in range(1, NUM_APPOINTMENTS + 1):
        pat_id = random.randint(1, NUM_PATIENTS)
        doc_id = random.randint(1, NUM_DOCTORS)
        
        app_date = fake.date_time_between(start_date='-30d', end_date='+10d')
        app_date_str = app_date.strftime('%Y-%m-%d %H:%M:%S')
        
        if app_date > fake.date_time_this_month():
            status = random.choice(['Bekliyor', 'İptal'])
        else:
            status = random.choice(['Tamamlandı', 'İptal', 'Tamamlandı']) 
            
        f.write(f"INSERT INTO appointments (patient_id, doctor_id, appointment_datetime, status) VALUES ({pat_id}, {doc_id}, '{app_date_str}', '{status}');\n")
        
        if status == 'Tamamlandı':
            diagnosis = random.choice(diagnoses)
            f.write(f"INSERT INTO medical_records (appointment_id, diagnosis, notes) VALUES ({i}, '{diagnosis}', 'Detaylı muayene yapıldı.');\n")
            completed_records.append(len(completed_records) + 1) 

    f.write("\n-- 6. İLAÇLAR\n")
    meds = ['Parol', 'Amoklavin', 'Arveles', 'Aspirin', 'Majezik', 'Lansor', 'Calpol', 'Ventolin', 'Augmentin', 'DeliX']
    for i in range(1, NUM_MEDICATIONS + 1):
        med_name = random.choice(meds) + " " + str(random.randint(1, 5)*100) + "mg"
        f.write(f"INSERT INTO medications (name, dosage) VALUES ('{med_name}', 'Günde {random.randint(1,3)} kez');\n")

    f.write("\n-- 7. REÇETELER\n")
    for record_id in random.sample(completed_records, k=int(len(completed_records)/2)):
        med_id = random.randint(1, NUM_MEDICATIONS)
        f.write(f"INSERT INTO prescriptions (record_id, medication_id, instructions) VALUES ({record_id}, {med_id}, 'Yemekten sonra bol su ile');\n")
