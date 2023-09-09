ALTER TABLE names
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

INSERT INTO names (name) VALUE ("Tim Wilger");

select * from names;