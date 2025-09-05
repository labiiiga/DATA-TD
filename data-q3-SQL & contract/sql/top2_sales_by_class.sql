SELECT product_class_name, rank, product_name, sales_value
FROM (
  SELECT 
    pc.product_class_name,
    p.product_name,
    SUM(st.quantity * p.retail_price) AS sales_value,
    ROW_NUMBER() OVER (
      PARTITION BY pc.product_class_name
      ORDER BY SUM(st.quantity * p.retail_price) DESC,
               SUM(st.quantity) ASC
    ) AS rank
  FROM sales_transaction st
  JOIN product p ON st.product_id = p.product_id
  JOIN product_class pc ON p.product_class_id = pc.product_class_id
  GROUP BY pc.product_class_name, p.product_id, p.product_name
) ranked
WHERE rank <= 2
ORDER BY product_class_name, sales_value DESC;
