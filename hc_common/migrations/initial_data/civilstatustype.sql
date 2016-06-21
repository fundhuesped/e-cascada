insert into hc_common_civilstatustype (id, name, description, status) values (1, 'Soltero', 'Soltero', 'A');
insert into hc_common_civilstatustype (id, name, description, status) values (2, 'Casado', 'Casado', 'A');
insert into hc_common_civilstatustype (id, name, description, status) values (3, 'Divorciado', 'Divorciado', 'A');
insert into hc_common_civilstatustype (id, name, description, status) values (4, 'Viudo', 'Viudo', 'A');
SELECT setval('hc_common_civilstatustype_id_seq', 4);
