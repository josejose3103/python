CREATE TABLE media.article5 (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    day DATE,
    noukamei VARCHAR(50),
    byoumei  VARCHAR(100),
    kingaku DECIMAL(10,2),
    kumikan int,
    create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);