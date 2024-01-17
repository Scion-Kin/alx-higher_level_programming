-- creates a user with all priviledges
CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO user_0d_1;
