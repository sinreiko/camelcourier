-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Mar 25, 2022 at 01:18 PM
-- Server version: 5.7.34
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `camelcourier`
--
CREATE DATABASE IF NOT EXISTS `camelDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `camelDB`;

-- --------------------------------------------------------

--
-- Table structure for table `activity`
--
DROP TABLE IF EXISTS `activity`;
CREATE TABLE `activity` (
  `activityID` int(11) NOT NULL,
  `trackingID` bigint(64) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deliveryStatus` varchar(30) NOT NULL,
  `deliveryDesc` varchar(100) NOT NULL,
  PRIMARY KEY(`activityID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `activity`
--

INSERT INTO `activity` (`activityID`, `trackingID`, `timestamp`, `deliveryStatus`, `deliveryDesc`) VALUES
(1, 587405231468, '2022-03-19 20:45:24', 'Order Created!', 'The order has been created.'),
(2, 587405231470, '2022-03-19 20:48:49', 'Order Created!', 'The order has been created.'),
(3, 587405231470, '2022-03-20 12:09:57', 'Pickup', 'Order has been picked up by pickup driver');

-- --------------------------------------------------------

--
-- Table structure for table `order`
--
DROP TABLE IF EXISTS `order`;
CREATE TABLE IF NOT EXISTS `order` (
  `trackingID` bigint(64) NOT NULL AUTO_INCREMENT,
  `driverID` varchar(13),
  `shipperID` int NOT NULL,
  `receiverName` varchar(30) NOT NULL,
  `receiverAddress` varchar(100) NOT NULL,
  `receiverPhone` varchar(30) NOT NULL,
  `receiverEmail` varchar(50) NOT NULL,
  `pickupAddress` varchar(100) NULL,
  PRIMARY KEY(`trackingID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `order` AUTO_INCREMENT=587405231466;

--
-- Dumping data for table `order`
  -- trackingID(INT) (autoincrement)
  -- driverID (VARCHAR)
  -- shipperID (VARCHAR)
  -- receiverName (VARCHAR)
  -- receiverAddress (VARCHAR)
  -- receiverPhone (VARCHAR)
  -- receiverEmail (VARCHAR)
  -- pickupAddress (VARCHAR)

--

INSERT INTO `order` (`trackingID`, `driverID`, `shipperID`,`receiverName`,`receiverAddress`,`receiverPhone`,`receiverEmail`,`pickupAddress`) VALUES

(NULL, "D002", 1, "Lee Shao Ming", "216 Depot Rd Singapore 109702", "+65 93983698", "124@smu.sg","Block 350C HDB Canberra"),
(NULL, "D001", 2, "Vasilis Ng", "Blk 987 Family Mart", "+65 21598384", "123@smu.sg","20 Canson Road"),
(NULL, "D003", 3, "Nicholas Wong", "Blk 456 Apple Avenue", "+65 80538094", "125@smu.sg","20 Danson Road"),
(NULL, "D004", 4, "Nicholas Wong", "Blk 135 Dog Boulevard", "+65 4145427", "126@smu.sg","20 Danson Road"),
(NULL, "D005", 5, "Reiko Lee", "Blk 246 Eggs Benedict Way", "+65 55230068", "127@smu.sg","20 Danson Road"),
(NULL, "D006", 6, "Lin Po Chien", "Blk 456 Apple Avenue", "+65 56629749", "128@smu.sg","20 Danson Road"),
(NULL, "D007", 7, "Lee Jun Hui", "Blk 123 Banana Road", "+65 48697119", "129@smu.sg","20 Danson Road"),
(NULL, "D008", 8, "Vasilis Ng", "Blk 123 Banana Road", "+65 78491046", "130@smu.sg","20 Danson Road"),
(NULL, "D009", 9, "Lee Shao Ming", "Blk 123 Banana Road", "+65 45712493", "131@smu.sg","20 Canson Road"),
(NULL, "D010", 10, "Lee Jun Hui", "Blk 135 Dog Boulevard", "+65 58160590", "132@smu.sg","20 Anson Road"),
(NULL, "D001", 1, "Reiko Lee", "Blk 123 Banana Road", "+65 9627904", "133@smu.sg","20 Benson Road"),
(NULL, "D002", 2, "Lee Jun Hui", "Blk 987 Family Mart", "+65 47573668", "134@smu.sg","20 Canson Road"),
(NULL, "D003", 3, "Lin Po Chien", "Blk 135 Dog Boulevard", "+65 46171449", "135@smu.sg","20 Anson Road"),
(NULL, "D004", 4, "Reiko Lee", "Blk 246 Eggs Benedict Way", "+65 63171071", "136@smu.sg","20 Danson Road"),
(NULL, "D005", 5, "Reiko Lee", "Blk 135 Dog Boulevard", "+65 65243654", "137@smu.sg","20 Canson Road"),
(NULL, "D006", 6, "Lin Po Chien", "Blk 135 Dog Boulevard", "+65 20975705", "138@smu.sg","20 Benson Road"),
(NULL, "D007", 7, "Lee Jun Hui", "Blk 987 Family Mart", "+65 11493273", "139@smu.sg","20 Danson Road"),
(NULL, "D008", 8, "Vasilis Ng", "Blk 246 Eggs Benedict Way", "+65 50046981", "140@smu.sg","20 Benson Road"),
(NULL, "D009", 9, "Vasilis Ng", "Blk 987 Family Mart", "+65 19919575", "141@smu.sg","20 Canson Road"),
(NULL, "D010", 10, "Lin Po Chien", "Blk 246 Eggs Benedict Way", "+65 31995017", "142@smu.sg","20 Canson Road"),
(NULL, "D001", 1, "Lin Po Chien", "Blk 246 Eggs Benedict Way", "+65 89828676", "143@smu.sg","20 Benson Road"),
(NULL, "D002", 2, "Vasilis Ng", "Blk 123 Banana Road", "+65 93513176", "144@smu.sg","20 Benson Road"),
(NULL, "D003", 3, "Lee Shao Ming", "Blk 789 Cherry Drive", "+65 70549174", "145@smu.sg","20 Danson Road"),
(NULL, "D004", 4, "Reiko Lee", "Blk 789 Cherry Drive", "+65 30854679", "146@smu.sg","20 Benson Road"),
(NULL, "D005", 5, "Vasilis Ng", "Blk 135 Dog Boulevard", "+65 74032665", "147@smu.sg","20 Anson Road"),
(NULL, "D006", 6, "Vasilis Ng", "Blk 123 Banana Road", "+65 68994343", "148@smu.sg","20 Benson Road"),
(NULL, "D007", 7, "Lee Shao Ming", "Blk 987 Family Mart", "+65 23180983", "149@smu.sg","20 Anson Road"),
(NULL, "D008", 8, "Vasilis Ng", "Blk 135 Dog Boulevard", "+65 46584543", "150@smu.sg","20 Benson Road"),
(NULL, "D009", 9, "Lee Jun Hui", "Blk 135 Dog Boulevard", "+65 1989759", "151@smu.sg","20 Canson Road"),
(NULL, "D010", 10, "Vasilis Ng", "Blk 135 Dog Boulevard", "+65 17645283", "152@smu.sg","20 Benson Road"),
(NULL, "D001", 1, "Nicholas Wong", "Blk 987 Family Mart", "+65 2956181", "153@smu.sg","20 Canson Road"),
(NULL, "D002", 2, "Lin Po Chien", "Blk 246 Eggs Benedict Way", "+65 9079599", "154@smu.sg","20 Canson Road"),
(NULL, "D003", 3, "Vasilis Ng", "Blk 135 Dog Boulevard", "+65 49611946", "155@smu.sg","20 Danson Road"),
(NULL, "D004", 4, "Reiko Lee", "Blk 123 Banana Road", "+65 46795683", "156@smu.sg","20 Danson Road"),
(NULL, "D005", 5, "Lee Jun Hui", "Blk 123 Banana Road", "+65 6711747", "157@smu.sg","20 Canson Road"),
(NULL, "D006", 6, "Reiko Lee", "Blk 246 Eggs Benedict Way", "+65 70653428", "158@smu.sg","20 Danson Road"),
(NULL, "D007", 7, "Lin Po Chien", "Blk 135 Dog Boulevard", "+65 90041553", "159@smu.sg","20 Benson Road"),
(NULL, "D008", 8, "Vasilis Ng", "Blk 987 Family Mart", "+65 82489426", "160@smu.sg","20 Canson Road"),
(NULL, "D009", 9, "Lin Po Chien", "Blk 123 Banana Road", "+65 30854889", "161@smu.sg","20 Danson Road"),
(NULL, "D010", 10, "Reiko Lee", "Blk 135 Dog Boulevard", "+65 44887083", "162@smu.sg","20 Anson Road"),
(NULL, "D011", 1, "Lee Shao Ming", "Blk 246 Eggs Benedict Way", "+65 32160294", "163@smu.sg","20 Anson Road"),
(NULL, "D012", 2, "Vasilis Ng", "Blk 987 Family Mart", "+65 74381730", "164@smu.sg","20 Danson Road"),
(NULL, "D013", 3, "Lee Jun Hui", "Blk 987 Family Mart", "+65 69226820", "165@smu.sg","20 Danson Road"),
(NULL, "D014", 4, "Reiko Lee", "Blk 456 Apple Avenue", "+65 28198387", "166@smu.sg","20 Canson Road"),
(NULL, "D015", 5, "Vasilis Ng", "Blk 246 Eggs Benedict Way", "+65 71735636", "167@smu.sg","20 Canson Road"),
(NULL, "D006", 11, "Vasilis Ng", "Blk 987 Family Mart", "+65 95455018", "168@smu.sg","20 Anson Road"),
(NULL, "D007", 12, "Lee Jun Hui", "Blk 135 Dog Boulevard", "+65 42322635", "169@smu.sg","20 Anson Road"),
(NULL, "D008", 13, "Vasilis Ng", "Blk 135 Dog Boulevard", "+65 77854324", "170@smu.sg","20 Anson Road"),
(NULL, "D009", 14, "Lee Shao Ming", "Blk 789 Cherry Drive", "+65 4918214", "171@smu.sg","20 Benson Road"),
(NULL, "D010", 15, "Reiko Lee", "Blk 135 Dog Boulevard", "+65 67875626", "172@smu.sg","20 Danson Road");

-- --------------------------------------------------------

--
-- Table structure for table `shipper`
--
DROP TABLE IF EXISTS `shipper`;
CREATE TABLE `shipper` (
  `shipperID` int(12) NOT NULL,
  `shipperName` varchar(32) NOT NULL,
  `shipperAddress` varchar(64) NOT NULL,
  `shipperPhone` int(8) NOT NULL,
  `shipperEmail` varchar(64) NOT NULL,
  `createdDate` datetime NOT NULL,
  `modifiedDate` datetime NOT NULL,
  PRIMARY KEY(`shipperID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `shipper`
--

INSERT INTO `shipper` (`shipperID`, `shipperName`, `shipperAddress`, `shipperPhone`, `shipperEmail`, `createdDate`, `modifiedDate`) VALUES
(1, 'Jun Hui', 'Woodlands', 83113585, 'junhuilee98@yahoo.com.sg', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(2, 'Lee Jun Hui', 'Hougang', 83113586, 'junhuilee99@yahoo.com.sg', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(3, 'Kevin Lee', 'Tampines', 83113587, 'junhuilee00@yahoo.com.sg', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(4, 'Lin Po Chien', 'Bedok', 83837807, 'linxpochien@gmail.com', '0000-00-00 00:00:00', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `droppoint`
--
DROP TABLE IF EXISTS `droppoint`;
CREATE TABLE `droppoint` (
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `region` varchar(64) NOT NULL,
  `placeID` varchar(100) NOT NULL,
  PRIMARY KEY(`latitude`,`longitude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `droppoint`
--

INSERT INTO `droppoint` (`latitude`, `longitude`, `region`, `placeID`) VALUES
(1.285710443426781, 103.84394318783733, 'South', 'ChIJM7Kvx3QZ2jERqxq34uk5HAY'),
(1.2873912711321067, 103.83038699037779, 'South', 'ChIJz-Tz8HgZ2jER_TPrfDQFrhg'),
(1.2652501481293283, 103.82045618343764, 'South', 'ChIJr9GWQuIb2jER3YsiRj8AqFw'),
(1.446181576052929, 103.81975637505069, 'North', 'EhdTZW1iYXdhbmcgRHIsIFNpbmdhcG9yZSIuKiwKFAoSCYfBbtljE9oxEUnZp-9q-D44EhQKEgl1k4uKIxHaMRHE9atSz2l4iA'),
(1.4363720994679852, 103.78683027012158, 'North', 'ChIJVfCo8QgT2jERgKTarqz3AAU');

-- --------------------------------------------------------

--
-- Table structure for table `rate`
--
DROP TABLE IF EXISTS `rate`;
CREATE TABLE `rate` (
  `size` varchar(64) NOT NULL,
  `priceperkm` float NOT NULL,
  PRIMARY KEY(`size`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `rate`
--

INSERT INTO `rate` (`size`, `priceperkm`) VALUES
('S', 1.0),
('M', 2.0),
('L', 3.0);

-- --------------------------------------------------------
--
-- AUTO_INCREMENT for table `activity` and table `order`
--
ALTER TABLE `activity`
  MODIFY `activityID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;



COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
