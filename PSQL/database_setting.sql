CREATE TABLE partido(id INT,
                     nombre VARCHAR(256),
                     sigla VARCHAR(256),
                     PRIMARY KEY(id));
\COPY partido from 'Tablas_en_csv/Partidos.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE region(id INT,
                    nombre VARCHAR(256),
                    PRIMARY KEY(id));
\COPY region from 'Tablas_en_csv/Region.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE territorio(id INT,
                        nombre VARCHAR(256),
                        PRIMARY KEY(id)
);
\COPY territorio from 'Tablas_en_csv/Territorio.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE afiliacion(id INT,
                        partido_id INT,
                        categoria VARCHAR(256),
                        territorio_id INT,
                        region_id INT,
                        sexo VARCHAR(1),
                        min_edad INT,
                        max_edad INT,
                        CONSTRAINT fk1 
                            FOREIGN KEY (partido_id) 
                            REFERENCES partido(id),
                        CONSTRAINT fk2 
                            FOREIGN KEY (region_id) 
                            REFERENCES region(id),
                        CONSTRAINT fk3 
                            FOREIGN KEY (territorio_id) 
                            REFERENCES territorio(id),
                        PRIMARY KEY(id)
);
\COPY afiliacion from 'Tablas_en_csv/Afiliaciones.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE candidato(id INT,
                       nombre VARCHAR(256),
                       sexo VARCHAR(1),
                       edad INT,
                       PRIMARY KEY(id)
);
\COPY candidato from 'Tablas_en_csv/Candidatos.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE cuenta(id INT,
                    descripcion VARCHAR(256),
                    PRIMARY KEY(id)
);
\COPY cuenta from 'Tablas_en_csv/Cuentas.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE tipo_documento(id INT,
                            tipo VARCHAR(256),
                            nombre VARCHAR(256),
                            PRIMARY KEY(id)
);
\COPY tipo_documento from 'Tablas_en_csv/Tipo_documento.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE documento(id BIGINT,
                       tipo_id INT,
                       glosa VARCHAR(256),
                       CONSTRAINT fk1 
                            FOREIGN KEY (tipo_id) 
                            REFERENCES tipo_documento(id)
);
\COPY documento from 'Tablas_en_csv/Documentos.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE aportante(id INT,
                       rut BIGINT,
                       dv VARCHAR(1),
                       nombre VARCHAR(256),
                       PRIMARY KEY(id)
);
\COPY aportante from 'Tablas_en_csv/Aportante.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE candidatura(id INT,
                         cargo VARCHAR(256),
                         region_id INT,
                         territorio_id INT,
                         candidato_id INT,
                         ano INT,
                         partido_id INT,
                         CONSTRAINT fk1 
                            FOREIGN KEY (region_id) 
                            REFERENCES region(id),
                         CONSTRAINT fk2 
                            FOREIGN KEY (candidato_id) 
                            REFERENCES candidato(id),
                         CONSTRAINT fk3 
                            FOREIGN KEY (territorio_id) 
                            REFERENCES territorio(id),
                         CONSTRAINT fk4 
                            FOREIGN KEY (partido_id) 
                            REFERENCES partido(id),
                         PRIMARY KEY(id)
);
\COPY candidatura from 'Tablas_en_csv/Candidatura.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE ingresosgastos(id INT,
                            tipo VARCHAR(256),
                            candidatura_id INT,
                            aportante_id INT,
                            fecha DATE,
                            cuenta_id INT,
                            monto INT,
                            documento_id BIGINT,
                            CONSTRAINT fk1 
                              FOREIGN KEY (candidatura_id) 
                              REFERENCES candidatura(id),
                            CONSTRAINT fk2 
                              FOREIGN KEY (aportante_id) 
                              REFERENCES aportante(id),
                            CONSTRAINT fk3 
                              FOREIGN KEY (cuenta_id) 
                              REFERENCES cuenta(id),
                            PRIMARY KEY(id)
);
\COPY ingresosgastos from 'Tablas_en_csv/IngresosGastos.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE aportespublicosanuales(id INT,
                                     partido_id INT,
                                     monto INT,
                                     fecha DATE,
                                     trimestre VARCHAR(256),
                                     CONSTRAINT fk1
                                       FOREIGN KEY (partido_id) 
                                       REFERENCES partido(id)
);
\COPY aportespublicosanuales from 'Tablas_en_csv/Aportes_publicos.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE aportesprivadosapartidos(id INT,
                                      nombre_aportante VARCHAR(256),
                                      tipo_aportante VARCHAR(256),
                                      cargo VARCHAR(256),
                                      partido_id INT,
                                      tipo VARCHAR(256),
                                      fecha DATE,
                                      monto INT,
                                      CONSTRAINT fk1
                                       FOREIGN KEY (partido_id) 
                                       REFERENCES partido(id)
);
\COPY aportesprivadosapartidos from 'Tablas_en_csv/Aportes_Privados_2017_partido.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE aportesprivadosacandidatos(  id INT,
                                          nombre_aportante VARCHAR(256),
                                          tipo_aportante VARCHAR(256),
                                          candidatura_id INT,
                                          tipo VARCHAR(256),
                                          fecha DATE,
                                          monto INT,
                                          CONSTRAINT fk1
                                             FOREIGN KEY (candidatura_id) 
                                             REFERENCES candidatura(id)
);
\COPY aportesprivadosacandidatos from 'Tablas_en_csv/Aportes_Privados_2017_candidato.csv' DELIMITER ',' CSV HEADER;