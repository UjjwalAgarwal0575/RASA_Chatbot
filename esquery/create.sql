CREATE TABLE products (  
    id INT PRIMARY KEY,
    title VARCHAR(35),
    description VARCHAR(2000),
    availability VARCHAR(35),   
    product_condition VARCHAR(35),  -- Changed from 'condition'
    price INT,
    link VARCHAR(2000),  -- Adjusted length to 2000 characters
    image_link VARCHAR(2000),
    quantity_to_sell_on_facebook INT,
    item_group_id VARCHAR(50),  -- Adjusted length to 50 characters
    origin_country VARCHAR(35),
    brand VARCHAR(35)
    -- Add other columns if needed
);
