DROP TABLE IF EXISTS mergedGenes;

CREATE TABLE mergedGenes (
  tracking_id TEXT PRIMARY KEY,
  locus TEXT,
  h1tl_fpkm INT,
  h3tl_fpkm INT,
  h1tr_fpkm INT,
  c1tr_fpkm INT,
  c2br_fpkm INT,
  c3tr_fpkm INT
)