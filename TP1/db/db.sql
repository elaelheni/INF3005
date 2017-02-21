create table article (
  id integer primary key,
  titre varchar(100),
  identifiant varchar(50),
  auteur varchar(100),
  date_publication text,
  paragraphe varchar(500)
);

insert into article values(1, 'Singe de lAfrique', 'singe', 'Jacques Berger', '2017-01-13', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci. Ut ullamcorper vulputate mi in consectetur. Phasellus congue ligula neque, mollis dapibus metus faucibus quis. Nullam scelerisque sollicitudin efficitur. Duis maximus mi nec vestibulum semper. Proin a nisi enim. Etiam nec facilisis eros. Vivamus risus lacus, pellentesque nec tincidunt viverra, sodales eget urna. Donec elementum risus quis commodo auctor. Pellentesque placerat arcu at vestibulum commodo.');
insert into article values(2, 'Ours polaire', 'ours', 'Burrell Verreau', '2016-06-13', 'Pellentesque nec faucibus orci. Vestibulum ac sem eget ipsum suscipit convallis eget ac dui. Suspendisse potenti. Curabitur enim turpis, feugiat quis pellentesque ullamcorper, rhoncus sit amet massa. Nulla viverra pharetra arcu. In hac habitasse platea dictumst. Praesent pretium massa efficitur justo tempor cursus. Cras ornare, lorem at vehicula luctus, elit risus ornare elit, vitae placerat nisi tellus nec diam. Sed posuere bibendum metus, et scelerisque est sagittis sed.');
insert into article values(3, 'Castor en danger', 'castor', 'Vick Gareau', '2017-02-10', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci. Ut ullamcorper vulputate mi in consectetur. Phasellus congue ligula neque, mollis dapibus metus faucibus quis. Nullam scelerisque sollicitudin efficitur. Duis maximus mi nec vestibulum semper. Proin a nisi enim. Etiam nec facilisis eros. Vivamus risus lacus, pellentesque nec tincidunt viverra, sodales eget urna. Donec elementum risus quis commodo auctor. Pellentesque placerat arcu at vestibulum commodo.');
insert into article values(4, 'Pigeon voyageur', 'pigeon', 'Cosette Bedard', '2016-09-20', 'Donec sed blandit massa. In tincidunt, tortor ut faucibus porttitor, erat metus ultrices quam, in ullamcorper urna felis ut sem. In posuere eu risus vel tempus. Ut sit amet mattis sapien. Duis sollicitudin, metus nec molestie tincidunt, velit urna laoreet nibh, vitae viverra neque sapien sed nulla. Sed sodales justo ac nibh auctor, id consectetur diam ullamcorper. Pellentesque ut ante augue. Nam sed malesuada lacus. Sed blandit lacus orci, at iaculis enim tempor ut.');
insert into article values(5, 'Pygargue a tete blanche', 'aigle', 'Parfait Quirion', '2015-05-11', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci. Ut ullamcorper vulputate mi in consectetur. Phasellus congue ligula neque, mollis dapibus metus faucibus quis. Nullam scelerisque sollicitudin efficitur. Duis maximus mi nec vestibulum semper. Proin a nisi enim. Etiam nec facilisis eros. Vivamus risus lacus, pellentesque nec tincidunt viverra, sodales eget urna. Donec elementum risus quis commodo auctor. Pellentesque placerat arcu at vestibulum commodo.');
insert into article values(6, 'Poisson rouge', 'poisson', 'Remy Labonte', '2014-01-01', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci. Ut ullamcorper vulputate mi in consectetur. Phasellus congue ligula neque, mollis dapibus metus faucibus quis. Nullam scelerisque sollicitudin efficitur. Duis maximus mi nec vestibulum semper. Proin a nisi enim. Etiam nec facilisis eros. Vivamus risus lacus, pellentesque nec tincidunt viverra, sodales eget urna. Donec elementum risus quis commodo auctor. Pellentesque placerat arcu at vestibulum commodo.');
insert into article values(7, 'Le meilleur ami de lhomme', 'chien', 'Ray Arpin', '2017-01-05', 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Phasellus efficitur tristique enim, dictum laoreet magna molestie ut. Nulla ex justo, imperdiet semper blandit at, gravida vel nisl. Cras et tellus tristique, tempor purus a, cursus mauris. Nulla sed diam non nibh finibus lacinia vel a nibh. Nunc non risus consectetur, rutrum ipsum id, pretium arcu. In hac habitasse platea dictumst.');
insert into article values(8, 'Roi de la jungle', 'lion', 'Merlin Pirouet', '2016-12-25', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci. Ut ullamcorper vulputate mi in consectetur. Phasellus congue ligula neque, mollis dapibus metus faucibus quis. Nullam scelerisque sollicitudin efficitur. Duis maximus mi nec vestibulum semper. Proin a nisi enim. Etiam nec facilisis eros. Vivamus risus lacus, pellentesque nec tincidunt viverra, sodales eget urna. Donec elementum risus quis commodo auctor. Pellentesque placerat arcu at vestibulum commodo.');
insert into article values(9, 'Allergique aux chats', 'chat', 'Logistilla Renaud', '2016-04-28', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci. Ut ullamcorper vulputate mi in consectetur. Phasellus congue ligula neque, mollis dapibus metus faucibus quis. Nullam scelerisque sollicitudin efficitur. Duis maximus mi nec vestibulum semper. Proin a nisi enim. Etiam nec facilisis eros. Vivamus risus lacus, pellentesque nec tincidunt viverra, sodales eget urna. Donec elementum risus quis commodo auctor. Pellentesque placerat arcu at vestibulum commodo.');
insert into article values(10, 'Harambe', 'gorille', 'Gilbert Brunelle', '2017-02-08', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu libero eu libero luctus accumsan. Curabitur bibendum dolor vel erat tempor mollis a sit amet orci. Ut ullamcorper vulputate mi in consectetur. Phasellus congue ligula neque, mollis dapibus metus faucibus quis. Nullam scelerisque sollicitudin efficitur. Duis maximus mi nec vestibulum semper. Proin a nisi enim. Etiam nec facilisis eros. Vivamus risus lacus, pellentesque nec tincidunt viverra, sodales eget urna. Donec elementum risus quis commodo auctor. Pellentesque placerat arcu at vestibulum commodo.');
