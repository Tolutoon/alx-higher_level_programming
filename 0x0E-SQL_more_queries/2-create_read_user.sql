-- creates the database hbtn_0d_2 and the user user_0d_2
-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
<<<<<<< HEAD
-- creates a user
CREATE USER IF NOT EXITS user_0d_2@localhost IDENTIFIED BY 'user_od_2-pwd';
=======
-- creaates a user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_od_2-pwd';
>>>>>>> 31993bd350704604726264126ea0435e400957d7
-- grants SELECT privileges to a user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
