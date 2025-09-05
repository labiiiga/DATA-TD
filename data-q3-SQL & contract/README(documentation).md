# Schema Documentation
ตารางที่ใช้มี 3 ตารางหลักๆ 

- **sales_transaction**
  - transaction_id (INT) = id ของ transaction
  - product_id (INT) = id ของสินค้า
  - quantity (INT) = จำนวนที่ขายได้

- **product**
  - product_id (INT) = id ของสินค้า
  - product_name (STRING) = ชื่อสินค้า
  - retail_price (NUMERIC) = ราคาสินค้า
  - product_class_id (INT) = id ของ class ที่สินค้าอยู่

- **product_class**
  - product_class_id (INT) = id ของ class
  - product_class_name (STRING) = ชื่อ class ของสินค้า
ผลลัพธ์ ออกมาเป็น
**Output Table/View**: `top2_sales_by_class`
- product_class_name (STRING)
- rank (INT) = อันดับ 1 หรือ 2
- product_name (STRING)
- sales_value (NUMERIC)

---

# Data Lineage
- เอาข้อมูลจาก 3 ตารางข้างบนมา join กัน
- คำนวณ sales_value = quantity * retail_price
- ใช้ window function ROW_NUMBER() เพื่อหาอันดับ
- ได้ output เป็น Top 2 ของแต่ละ class
- ข้อมูลอัปเดตแบบรายวัน (T+1)

---

# Business Logic
- ยอดขาย (sales_value) = จำนวน * ราคา
- เลือกมา 2 อันดับที่ยอดขายเยอะสุดต่อ class
- ถ้ายอดขายเท่ากัน เราใช้จำนวน (quantity) น้อยกว่าเป็นตัวตัด
- rank = 1 คือสินค้าขายดีสุดใน class นั้น

---

# Data Quality / Limitations
- ข้อมูลขึ้นกับระบบขาย ตรงนี้ถ้าต้นทางตกหล่นก็ตกหล่นเลย
- ไม่ได้คิดรวมกับภาษีหรืออย่างอื่น
- SLA: delay ประมาณ 1 วัน

---

# Access & Usage
- Dataset: `data-td-471107.datasetq3`
- Table/View: `top2_sales_by_class`
- ตัวอย่าง query:
  ```sql
  SELECT *
  FROM `data-td-471107.datasetq3.top2_sales_by_class`
  WHERE product_class_name = 'Class A';
