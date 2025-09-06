# Schema Documentation
ตารางที่ใช้มี 3 ตารางหลักๆ 

- **sales_transaction**
  transaction_id (INT)
  product_id (INT)
  quantity (INT) 

- **product**
  - product_id (INT)
  - product_name (STRING)
  - retail_price (NUMERIC)
  - product_class_id (INT)

- **product_class**
  - product_class_id (INT)
  - product_class_name (STRING)

# ผลลัพธ์ ออกมาเป็น
product_class_name 
rank 
product_name 
sales_value

# Data Lineage
เอาข้อมูลจาก 3 ตารางข้างบนมา join กัน
คำนวณ sales_value = quantity * retail_price
ใช้ window function ROW_NUMBER() เพื่อหาอันดับ
ได้ output เป็น Top 2 ของแต่ละ class
ข้อมูลอัปเดตแบบรายวัน  (T+1 วัน)

# Business Logic
ยอดขาย (sales_value) เอาจำนวน คูณ(*)กับ ราคา
เลือกมา 2 อันดับที่ยอดขายเยอะสุดต่อ class 
ถ้ายอดขายเท่ากัน เราใช้จำนวน (quantity) น้อยกว่าเป็นตัวตัด
rank = 1 คือสินค้าขายดีสุดใน class นั้น

# Data Quality / Limitations
ข้อมูลขึ้นกับระบบขาย ตรงนี้ถ้าต้นทางตกหล่นก็ตกหล่นเลย
ไม่ได้คิดรวมกับภาษีหรืออย่างอื่น

# Access & Usage
- Dataset: `data-td-471107.datasetq3`
- Table/View: `top2_sales_by_class`
