create table authors(
    firstname VARCHAR(50),
    fullname VARCHAR(50)
)

create table publisher(
    name VARCHAR(50),
    fullname VARCHAR(50)
)

insert into authors(firstname, fullname) values ("QUINN", "QUINN KISER");
insert into authors(firstname, fullname) values ("ERIC", "ERIC LEHMAN");
insert into authors(firstname, fullname) values ("ALBERT", "ALBERT R. MEYER");
insert into authors(firstname, fullname) values ("WILEY", "WILEY");
insert into authors(firstname, fullname) values ("STANISLAW RACZYNSKI", "STANISLAW RACZYNSKI");
insert into authors(firstname, fullname) values ("MEGAN", "MEGAN CAMPSI");
insert into authors(firstname, fullname) values ("ROBERT", "ROBERT C. MARTIN");
insert into authors(firstname, fullname) values ("LARRY", "LARRY WARWARUK");
insert into authors(firstname, fullname) values ("IE", "IE IRODOV");

insert into publisher(name, fullname) values ("APRESS", "APRESS");
insert into publisher(name, fullname) values ("WILEY", "WILEY");
insert into publisher(name, fullname) values ("PRENTICE", "PRENTICE HALL");
insert into publisher(name, fullname) values ("ARIHANT", "ARIHANT");

insert into publisher(name, fullname) values ("BONE COULEE", "COTEAU BOOKS");
insert into publisher(name, fullname) values ("Computer Networking", "");
insert into publisher(name, fullname) values ("Computer Science", "APRESS");
