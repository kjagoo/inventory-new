

create database if not exists `invent_management`;

use `invent_management`;

/*
Table struture for tbl_assets
*/

drop table if exists `tbl_assets`;
CREATE TABLE `tbl_assets` (
  `assest_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `serial` varchar(100) NOT NULL,
  `andela_serial` varchar(100) NOT NULL,
  `date_bought` date NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`assest_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*
Table struture for tbl_assets_transactions
*/

drop table if exists `tbl_assets_transactions`;
CREATE TABLE `tbl_assets_transactions` (
  `transaction_id` int(11) NOT NULL,
  `asset_id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `date_borrowed` date NOT NULL,
  `date_returned` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `comment` int(11) NOT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*
Table struture for tbl_staff
*/

drop table if exists `tbl_staff`;
CREATE TABLE `tbl_staff` (
  `staff_id` int(11) NOT NULL,
  `f_name` varchar(100) NOT NULL,
  `s_name` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `right_id` int(11) NOT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*
Table struture for tbl_user_rights
*/

drop table if exists `tbl_user_rights`;
CREATE TABLE `tbl_user_rights` (
  `right_id` int(11) NOT NULL,
  `right_name` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

