insert into hc_common_documenttype (id, name, description, status) values (1, 'DNI', 'DNI', 'A');
insert into hc_common_documenttype (id, name, description, status) values (2, 'CI', 'CI', 'A');
insert into hc_common_documenttype (id, name, description, status) values (3, 'LE', 'LE', 'A');
insert into hc_common_documenttype (id, name, description, status) values (4, 'LC', 'LC', 'A');
insert into hc_common_documenttype (id, name, description, status) values (5, 'Pas', 'Pas', 'A');
insert into hc_common_documenttype (id, name, description, status) values (6, 'Otro', 'Otro', 'A');
SELECT setval('hc_common_documenttype_id_seq', 6);
