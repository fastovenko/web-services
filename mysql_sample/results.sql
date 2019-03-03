use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
SELECT name FROM store;

-- 3. Посчитать общую сумму в деньгах всех продаж
SELECT sum(total) FROM sale;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
SELECT store_id FROM sale group by store_id;

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
SELECT store_id FROM store natural left join sale where sale.store_id is null;

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
SELECT p.name, avg(s.total/s.quantity) FROM product as p natural join sale as s group by p.product_id;

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select name from(
SELECT name, count(distinct store_id) count
FROM product natural join sale
group by name) as result
where count=1;

-- 8. Получить названия всех складов, с которых продавался только один продукт
select name from(
SELECT name, count(distinct product_id) count
FROM store natural join sale
group by name) as result
where count=1

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
SELECT * FROM sale order by total  desc limit 1;

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date from (
SELECT date, sum(total) sum FROM sale
group by date
order by sum desc limit 1 ) as result;
