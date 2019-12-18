create databse applied_encryption;

use applied_encryption;

create table users(userid varchar(32), salt varchar(64), password varchar(128), primary key(userid));