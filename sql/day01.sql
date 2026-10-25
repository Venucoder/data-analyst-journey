SELECT * FROM orders LIMIT 10;

select count(*) from orders

select order_status, count(*) as total_orders
from orders 
group by order_status
order by total_orders desc;

select date_trunc('month', order_purchase_timestamp) as month, count(*) 
from orders
group by month
order by month;

select round(sum(payment_value)::numeric, 2) as total_revenue
from order_payments

select customer_state, count(*) as customers
from customers
group by customer_state
order by customers desc
limit 5

select c.customer_state, count(*) as orders
from customers c join orders o 
on c.customer_id = o.customer_id
group by c.customer_state 
order by orders desc

-- Practice
select count(*) from orders
where order_status = 'canceled'

select payment_type, count(*) as payments
from order_payments 
group by payment_type
order by payments desc

select customer_city, count(*) as customers
from customers
group by customer_city
order by customers desc 
limit 5
