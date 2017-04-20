create table article (
  id integer primary key,
  titre varchar(100),
  identifiant varchar(50),
  auteur varchar(100),
  date_publication text,
  paragraphe varchar(500)
);

insert into article values(1, 'Singe de lAfrique', 'singe', 'Jacques Berger', '2017-01-13', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci.');
insert into article values(2, 'Ours polaire', 'ours', 'Burrell Verreau', '2016-06-13', 'Pellentesque nec faucibus orci. Vestibulum ac sem eget ipsum suscipit convallis eget ac dui. Suspendisse potenti. Curabitur enim turpis, feugiat quis pellentesque ullamcorper, rhoncus sit amet massa. Nulla viverra pharetra arcu.');
insert into article values(3, 'Castor en danger', 'castor', 'Vick Gareau', '2017-02-10', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci.');
insert into article values(4, 'Pigeon voyageur', 'pigeon', 'Cosette Bedard', '2016-09-20', 'Donec sed blandit massa. In tincidunt, tortor ut faucibus porttitor, erat metus ultrices quam, in ullamcorper urna felis ut sem. In posuere eu risus vel tempus.');
insert into article values(5, 'Pygargue a tete blanche', 'aigle', 'Parfait Quirion', '2015-05-11', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci.');
insert into article values(6, 'Poisson rouge', 'poisson', 'Remy Labonte', '2014-01-01', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci.');
insert into article values(7, 'Le meilleur ami de lhomme', 'chien', 'Ray Arpin', '2017-01-05', 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Phasellus efficitur tristique enim, dictum laoreet magna molestie ut.');
insert into article values(8, 'Roi de la jungle', 'lion', 'Merlin Pirouet', '2016-12-25', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci.');
insert into article values(9, 'Allergique aux chats', 'chat', 'Logistilla Renaud', '2016-04-28', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci.');
insert into article values(10, 'Harambe', 'gorille', 'Gilbert Brunelle', '2017-02-08', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci. Ut ullamcorper vulputate mi in consectetur. ');

create table users (
  id integer primary key,
  utilisateur varchar(25),
  email varchar(100),
  salt varchar(32),
  hash varchar(128)
);

insert into users values(1, 'correcteur', 'poirier.jm.test@gmail.com', '95b883a5fe264fc19fba0fb44cf7d735', '944c15514abd941231106addd2513c8c1a42e7fcc8ad35cd6ddda2c737fea6338584dc3e6dcfb856aa939a2d53990d484d37ba2229f1b53613fcf1e483c77eda');

create table sessions (
  id integer primary key,
  id_session varchar(32),
  utilisateur varchar(25)
);

create table emails (
  id integer primary key,
  email varchar(100),
  token varchar(50),
  expiration text
);
