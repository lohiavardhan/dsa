-- Write your query below
select name from customers
where name not in (
select name from customers, orders
where customers.id = orders.customer_id)