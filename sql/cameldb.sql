-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 06, 2022 at 11:54 AM
-- Server version: 8.0.21
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cameldb`
--
DROP DATABASE IF EXISTS `cameldb`;
CREATE DATABASE IF NOT EXISTS `cameldb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `cameldb`;

-- --------------------------------------------------------

--
-- Table structure for table `activity`
--

DROP TABLE IF EXISTS `activity`;
CREATE TABLE IF NOT EXISTS `activity` (
  `activityID` int NOT NULL AUTO_INCREMENT,
  `trackingID` bigint NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deliveryStatus` varchar(30) NOT NULL,
  `deliveryDesc` varchar(100) NOT NULL,
  PRIMARY KEY (`activityID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `activity`
--

INSERT INTO `activity` (`activityID`, `trackingID`, `timestamp`, `deliveryStatus`, `deliveryDesc`) VALUES
(1, 587405231514, '2022-03-19 20:45:24', 'Order Created!', 'The order has been created.'),
(2, 587405231515, '2022-03-19 20:48:49', 'Order Created!', 'The order has been created.'),
(3, 587405231515, '2022-03-20 12:09:57', 'Pickup', 'Order has been picked up by pickup driver'),
(4, 587405231515, '2022-04-01 00:59:53', 'Reached facility', 'The packages is at the sorting facility.'),
(5, 587405231516, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(7, 587405231518, '2022-04-02 11:16:23', 'Order created', 'Order has been created by shipper'),
(8, 587405231518, '2022-04-02 12:15:07', 'Waiting for pickup', 'Pick up location has been updated, awaiting for parcel pickup.'),
(9, 587405231520, '2022-04-04 17:00:40', 'Order created', 'Order has been created by shipper'),
(10, 587405231520, '2022-04-05 20:40:59', 'Waiting for pickup', 'Pick up location has been updated, awaiting for parcel pickup.'),
(11, 587405231520, '2022-04-05 21:24:41', 'Pickup', 'Order has been picked up by driver.'),
(12, 587405231520, '2022-04-05 21:32:16', 'Pickup', 'Order has been picked up by driver.'),
(13, 587405231520, '2022-04-05 21:40:21', 'Pickup', 'Order has been picked up by driver.'),
(14, 587405231518, '2022-04-05 21:54:25', 'Cancelled', 'Order has been canceled by shipper.'),
(15, 587405231518, '2022-04-05 21:58:06', 'Cancelled', 'Order has been canceled by shipper.'),
(16, 587405231466, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(17, 587405231467, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(18, 587405231468, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(19, 587405231469, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(20, 587405231470, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(21, 587405231471, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(22, 587405231472, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(23, 587405231473, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(24, 587405231474, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(25, 587405231475, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(26, 587405231476, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(27, 587405231477, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(28, 587405231478, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(29, 587405231479, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(30, 587405231480, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(31, 587405231481, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(32, 587405231482, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(33, 587405231483, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(34, 587405231484, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(35, 587405231485, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(36, 587405231486, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(37, 587405231487, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(38, 587405231488, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(39, 587405231489, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(40, 587405231490, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(41, 587405231491, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(42, 587405231492, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(43, 587405231493, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(44, 587405231494, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(45, 587405231495, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(46, 587405231496, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(47, 587405231497, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(48, 587405231498, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(49, 587405231499, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(50, 587405231500, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(51, 587405231501, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(52, 587405231502, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(53, 587405231503, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(54, 587405231504, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(55, 587405231505, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(56, 587405231506, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(57, 587405231507, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(58, 587405231508, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(59, 587405231509, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(60, 587405231510, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(61, 587405231511, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(62, 587405231512, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(63, 587405231513, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(64, 587405231514, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(65, 587405231515, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(66, 587405231519, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper');

-- --------------------------------------------------------

--
-- Table structure for table `droppoint`
--

DROP TABLE IF EXISTS `droppoint`;
CREATE TABLE IF NOT EXISTS `droppoint` (
  `address` varchar(64) NOT NULL,
  `placeID` varchar(100) NOT NULL,
  PRIMARY KEY (`placeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `droppoint`
--

INSERT INTO `droppoint` (`address`, `placeID`) VALUES
('1 Maritime Square, Singapore 099253', 'ChIJr9GWQuIb2jER3YsiRj8AqFw'),
('101 Upper Cross St, Singapore 058357', 'ChIJM7Kvx3QZ2jERqxq34uk5HAY'),
('298 Jln Bukit Ho Swee, Singapore 169565', 'ChIJz-Tz8HgZ2jER_TPrfDQFrhg'),
('Woodlands, Singapore', 'ChIJVfCo8QgT2jERgKTarqz3AAU'),
('Sembawang Dr, Singapore', 'EhdTZW1iYXdhbmcgRHIsIFNpbmdhcG9yZSIuKiwKFAoSCYfBbtljE9oxEUnZp-9q-D44EhQKEgl1k4uKIxHaMRHE9atSz2l4iA');

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
CREATE TABLE IF NOT EXISTS `order` (
  `trackingID` bigint NOT NULL AUTO_INCREMENT,
  `driverID` varchar(4) DEFAULT NULL,
  `shipperID` int NOT NULL,
  `receiverName` varchar(30) NOT NULL,
  `receiverAddress` varchar(100) NOT NULL,
  `receiverPhone` varchar(30) NOT NULL,
  `receiverEmail` varchar(50) NOT NULL,
  `pickupAddress` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`trackingID`)
) ENGINE=InnoDB AUTO_INCREMENT=587405231521 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`trackingID`, `driverID`, `shipperID`, `receiverName`, `receiverAddress`, `receiverPhone`, `receiverEmail`, `pickupAddress`) VALUES
(587405231466, 'D001', 1, 'Vasilis Ng', 'Blk 987 Family Mart', '+6521598384', '123@smu.sg', '20 Canson Road'),
(587405231467, 'D002', 2, 'Lee Shao Ming', 'Blk 987 Family Mart', '+6593983698', '124@smu.sg', '20 Canson Road'),
(587405231468, 'D003', 3, 'Nicholas Wong', 'Blk 456 Apple Avenue', '+6580538094', '125@smu.sg', '20 Danson Road'),
(587405231469, 'D004', 4, 'Nicholas Wong', 'Blk 135 Dog Boulevard', '+654145427', '126@smu.sg', '20 Danson Road'),
(587405231470, 'D005', 5, 'Reiko Lee', 'Blk 246 Eggs Benedict Way', '+6555230068', '127@smu.sg', '20 Danson Road'),
(587405231471, 'D006', 1, 'Lin Po Chien', 'Blk 456 Apple Avenue', '+6556629749', '128@smu.sg', '20 Danson Road'),
(587405231472, 'D007', 2, 'Lee Jun Hui', 'Blk 123 Banana Road', '+6548697119', '129@smu.sg', '20 Danson Road'),
(587405231473, 'D008', 3, 'Vasilis Ng', 'Blk 123 Banana Road', '+6578491046', '130@smu.sg', '20 Danson Road'),
(587405231474, 'D009', 4, 'Lee Shao Ming', 'Blk 123 Banana Road', '+6545712493', '131@smu.sg', '20 Canson Road'),
(587405231475, 'D010', 5, 'Lee Jun Hui', 'Blk 135 Dog Boulevard', '+6558160590', '132@smu.sg', '20 Anson Road'),
(587405231476, 'D001', 1, 'Reiko Lee', 'Blk 123 Banana Road', '+659627904', '133@smu.sg', '20 Benson Road'),
(587405231477, 'D002', 2, 'Lee Jun Hui', 'Blk 987 Family Mart', '+6547573668', '134@smu.sg', '20 Canson Road'),
(587405231478, 'D003', 3, 'Lin Po Chien', 'Blk 135 Dog Boulevard', '+6546171449', '135@smu.sg', '20 Anson Road'),
(587405231479, 'D004', 4, 'Reiko Lee', 'Blk 246 Eggs Benedict Way', '+6563171071', '136@smu.sg', '20 Danson Road'),
(587405231480, 'D005', 5, 'Reiko Lee', 'Blk 135 Dog Boulevard', '+6565243654', '137@smu.sg', '20 Canson Road'),
(587405231481, 'D006', 1, 'Lin Po Chien', 'Blk 135 Dog Boulevard', '+6520975705', '138@smu.sg', '20 Benson Road'),
(587405231482, 'D007', 2, 'Lee Jun Hui', 'Blk 987 Family Mart', '+6511493273', '139@smu.sg', '20 Danson Road'),
(587405231483, 'D008', 3, 'Vasilis Ng', 'Blk 246 Eggs Benedict Way', '+6550046981', '140@smu.sg', '20 Benson Road'),
(587405231484, 'D009', 4, 'Vasilis Ng', 'Blk 987 Family Mart', '+6519919575', '141@smu.sg', '20 Canson Road'),
(587405231485, 'D010', 5, 'Lin Po Chien', 'Blk 246 Eggs Benedict Way', '+6531995017', '142@smu.sg', '20 Canson Road'),
(587405231486, 'D001', 1, 'Lin Po Chien', 'Blk 246 Eggs Benedict Way', '+6589828676', '143@smu.sg', '20 Benson Road'),
(587405231487, 'D002', 2, 'Vasilis Ng', 'Blk 123 Banana Road', '+6593513176', '144@smu.sg', '20 Benson Road'),
(587405231488, 'D003', 3, 'Lee Shao Ming', 'Blk 789 Cherry Drive', '+6570549174', '145@smu.sg', '20 Danson Road'),
(587405231489, 'D004', 4, 'Reiko Lee', 'Blk 789 Cherry Drive', '+6530854679', '146@smu.sg', '20 Benson Road'),
(587405231490, 'D005', 5, 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+6574032665', '147@smu.sg', '20 Anson Road'),
(587405231491, 'D006', 1, 'Vasilis Ng', 'Blk 123 Banana Road', '+6568994343', '148@smu.sg', '20 Benson Road'),
(587405231492, 'D007', 2, 'Lee Shao Ming', 'Blk 987 Family Mart', '+6523180983', '149@smu.sg', '20 Anson Road'),
(587405231493, 'D008', 3, 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+6546584543', '150@smu.sg', '20 Benson Road'),
(587405231494, 'D009', 4, 'Lee Jun Hui', 'Blk 135 Dog Boulevard', '+651989759', '151@smu.sg', '20 Canson Road'),
(587405231495, 'D010', 5, 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+6517645283', '152@smu.sg', '20 Benson Road'),
(587405231496, 'D001', 1, 'Nicholas Wong', 'Blk 987 Family Mart', '+652956181', '153@smu.sg', '20 Canson Road'),
(587405231497, 'D002', 2, 'Lin Po Chien', 'Blk 246 Eggs Benedict Way', '+659079599', '154@smu.sg', '20 Canson Road'),
(587405231498, 'D003', 3, 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+6549611946', '155@smu.sg', '20 Danson Road'),
(587405231499, 'D004', 4, 'Reiko Lee', 'Blk 123 Banana Road', '+6546795683', '156@smu.sg', '20 Danson Road'),
(587405231500, 'D005', 5, 'Lee Jun Hui', 'Blk 123 Banana Road', '+656711747', '157@smu.sg', '20 Canson Road'),
(587405231501, 'D006', 1, 'Reiko Lee', 'Blk 246 Eggs Benedict Way', '+6570653428', '158@smu.sg', '20 Danson Road'),
(587405231502, 'D007', 2, 'Lin Po Chien', 'Blk 135 Dog Boulevard', '+6590041553', '159@smu.sg', '20 Benson Road'),
(587405231503, 'D008', 3, 'Vasilis Ng', 'Blk 987 Family Mart', '+6582489426', '160@smu.sg', '20 Canson Road'),
(587405231504, 'D009', 4, 'Lin Po Chien', 'Blk 123 Banana Road', '+6530854889', '161@smu.sg', '20 Danson Road'),
(587405231505, 'D010', 5, 'Reiko Lee', 'Blk 135 Dog Boulevard', '+6544887083', '162@smu.sg', '20 Anson Road'),
(587405231506, 'D011', 1, 'Lee Shao Ming', 'Blk 246 Eggs Benedict Way', '+6532160294', '163@smu.sg', '20 Anson Road'),
(587405231507, 'D012', 2, 'Vasilis Ng', 'Blk 987 Family Mart', '+6574381730', '164@smu.sg', '20 Danson Road'),
(587405231508, 'D013', 3, 'Lee Jun Hui', 'Blk 987 Family Mart', '+6569226820', '165@smu.sg', '20 Danson Road'),
(587405231509, 'D014', 4, 'Reiko Lee', 'Blk 456 Apple Avenue', '+6528198387', '166@smu.sg', '20 Canson Road'),
(587405231510, 'D015', 5, 'Vasilis Ng', 'Blk 246 Eggs Benedict Way', '+6571735636', '167@smu.sg', '20 Canson Road'),
(587405231511, 'D006', 1, 'Vasilis Ng', 'Blk 987 Family Mart', '+6595455018', '168@smu.sg', '20 Anson Road'),
(587405231512, 'D007', 2, 'Lee Jun Hui', 'Blk 135 Dog Boulevard', '+6542322635', '169@smu.sg', '20 Anson Road'),
(587405231513, 'D008', 3, 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+6577854324', '170@smu.sg', '20 Anson Road'),
(587405231514, 'D009', 4, 'Lee Shao Ming', 'Blk 789 Cherry Drive', '+654918214', '171@smu.sg', '20 Benson Road'),
(587405231515, 'D010', 5, 'Reiko Lee', 'Blk 135 Dog Boulevard', '+6567875626', '172@smu.sg', '20 Danson Road'),
(587405231516, 'D015', 1, 'Vasilis', '420 Blaze It', '82184938', 'vasilis.ng.2020@scis.smu.edu.sg', NULL),
(587405231518, 'D011', 2, 'Mr D. Rock.', 'Limbang Shopping Centre', '98765432', 'dwaynetherock@abc.com', '679 Choa Chu Kang Crescent'),
(587405231519, 'D012', 3, 'Tan Ah Kau', '123 Sembawang Avenue', '+652184938', 'vasilis.ng.2020@scis.smu.edu.sg', 'Limbang Shopping Centre'),
(587405231520, 'D013', 4, 'Bo Bo Man', '679 Choa Chu Kang Crescent', '+652184938', 'vasilis.ng.2020@scis.smu.edu.sg', '429 Choa Chu Kang Ave 4');
-- --------------------------------------------------------

--
-- Table structure for table `rate`
--

DROP TABLE IF EXISTS `rate`;
CREATE TABLE IF NOT EXISTS `rate` (
  `size` varchar(64) NOT NULL,
  `priceperkm` float NOT NULL,
  PRIMARY KEY (`size`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `rate`
--

INSERT INTO `rate` (`size`, `priceperkm`) VALUES
('L', 3),
('M', 2),
('S', 1);

-- --------------------------------------------------------

--
-- Table structure for table `shipper`
--

DROP TABLE IF EXISTS `shipper`;
CREATE TABLE IF NOT EXISTS `shipper` (
  `shipperID` int NOT NULL,
  `shipperName` varchar(32) NOT NULL,
  `shipperAddress` varchar(64) NOT NULL,
  `shipperPhone` int NOT NULL,
  `shipperEmail` varchar(64) NOT NULL,
  `createdDate` datetime NOT NULL,
  `modifiedDate` datetime NOT NULL,
  PRIMARY KEY (`shipperID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `shipper`
--

INSERT INTO `shipper` (`shipperID`, `shipperName`, `shipperAddress`, `shipperPhone`, `shipperEmail`, `createdDate`, `modifiedDate`) VALUES
(1, 'Jun Hui', 'Woodlands', 83113585, 'junhuilee98@yahoo.com.sg', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(2, 'Lee Jun Hui', 'Hougang', 83113586, 'junhuilee99@yahoo.com.sg', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(3, 'Kevin Lee', 'Tampines', 83113587, 'junhuilee00@yahoo.com.sg', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(4, 'Lin Po Chien', 'Bedok', 83837807, 'linxpochien@gmail.com', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(5, 'Vasilis Ng', 'CCK', 82184938, 'vasilis.ng.2020@scis.smu.edu.sg', '0000-00-00 00:00:00', '0000-00-00 00:00:00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
