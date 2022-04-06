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
(1, 1337, '2022-03-19 20:45:24', 'Order Created!', 'The order has been created.'),
(2, 42069, '2022-03-19 20:48:49', 'Order Created!', 'The order has been created.'),
(3, 1337, '2022-03-20 12:09:57', 'Pickup', 'Order has been picked up by pickup driver'),
(4, 1337, '2022-04-01 00:59:53', 'Reached facility', 'The packages is at the sorting facility.'),
(5, 587405231516, '2022-04-02 11:03:53', 'Order created', 'Order has been created by shipper'),
(7, 587405231518, '2022-04-02 11:16:23', 'Order created', 'Order has been created by shipper'),
(8, 587405231518, '2022-04-02 12:15:07', 'Waiting for pickup', 'Pick up location has been updated, awaiting for parcel pickup.'),
(9, 587405231520, '2022-04-04 17:00:40', 'Order created', 'Order has been created by shipper'),
(10, 587405231520, '2022-04-05 20:40:59', 'Waiting for pickup', 'Pick up location has been updated, awaiting for parcel pickup.'),
(11, 587405231520, '2022-04-05 21:24:41', 'Pickup', 'Order has been picked up by driver.'),
(12, 587405231520, '2022-04-05 21:32:16', 'Pickup', 'Order has been picked up by driver.'),
(13, 587405231520, '2022-04-05 21:40:21', 'Pickup', 'Order has been picked up by driver.'),
(14, 587405231518, '2022-04-05 21:54:25', 'Cancelled', 'Order has been canceled by shipper.'),
(15, 587405231518, '2022-04-05 21:58:06', 'Cancelled', 'Order has been canceled by shipper.');

-- --------------------------------------------------------

--
-- Table structure for table `droppoint`
--

DROP TABLE IF EXISTS `droppoint`;
CREATE TABLE IF NOT EXISTS `droppoint` (
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `region` varchar(64) NOT NULL,
  PRIMARY KEY (`latitude`,`longitude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `droppoint`
--

INSERT INTO `droppoint` (`latitude`, `longitude`, `region`) VALUES
(1.26525, 103.82, 'South'),
(1.28571, 103.844, 'South'),
(1.28739, 103.83, 'South'),
(1.43637, 103.787, 'North'),
(1.44618, 103.82, 'North');

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
CREATE TABLE IF NOT EXISTS `order` (
  `trackingID` bigint NOT NULL AUTO_INCREMENT,
  `driverID` varchar(13) DEFAULT NULL,
  `shipperID` varchar(13) NOT NULL,
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
(587405231466, 'D000000000001', 'S000000000001', 'Vasilis Ng', 'Blk 987 Family Mart', '+65 21598384', '123@smu.sg', '20 Canson Road'),
(587405231467, 'D000000000002', 'S000000000002', 'Lee Shao Ming', 'Blk 987 Family Mart', '+65 93983698', '124@smu.sg', '20 Canson Road'),
(587405231468, 'D000000000003', 'S000000000003', 'Nicholas Wong', 'Blk 456 Apple Avenue', '+65 80538094', '125@smu.sg', '20 Danson Road'),
(587405231469, 'D000000000004', 'S000000000004', 'Nicholas Wong', 'Blk 135 Dog Boulevard', '+65 4145427', '126@smu.sg', '20 Danson Road'),
(587405231470, 'D000000000005', 'S000000000005', 'Reiko Lee', 'Blk 246 Eggs Benedict Way', '+65 55230068', '127@smu.sg', '20 Danson Road'),
(587405231471, 'D000000000006', 'S000000000006', 'Lin Po Chien', 'Blk 456 Apple Avenue', '+65 56629749', '128@smu.sg', '20 Danson Road'),
(587405231472, 'D000000000007', 'S000000000007', 'Lee Jun Hui', 'Blk 123 Banana Road', '+65 48697119', '129@smu.sg', '20 Danson Road'),
(587405231473, 'D000000000008', 'S000000000008', 'Vasilis Ng', 'Blk 123 Banana Road', '+65 78491046', '130@smu.sg', '20 Danson Road'),
(587405231474, 'D000000000009', 'S000000000009', 'Lee Shao Ming', 'Blk 123 Banana Road', '+65 45712493', '131@smu.sg', '20 Canson Road'),
(587405231475, 'D000000000010', 'S000000000010', 'Lee Jun Hui', 'Blk 135 Dog Boulevard', '+65 58160590', '132@smu.sg', '20 Anson Road'),
(587405231476, 'D000000000001', 'S000000000011', 'Reiko Lee', 'Blk 123 Banana Road', '+65 9627904', '133@smu.sg', '20 Benson Road'),
(587405231477, 'D000000000002', 'S000000000012', 'Lee Jun Hui', 'Blk 987 Family Mart', '+65 47573668', '134@smu.sg', '20 Canson Road'),
(587405231478, 'D000000000003', 'S000000000013', 'Lin Po Chien', 'Blk 135 Dog Boulevard', '+65 46171449', '135@smu.sg', '20 Anson Road'),
(587405231479, 'D000000000004', 'S000000000014', 'Reiko Lee', 'Blk 246 Eggs Benedict Way', '+65 63171071', '136@smu.sg', '20 Danson Road'),
(587405231480, 'D000000000005', 'S000000000015', 'Reiko Lee', 'Blk 135 Dog Boulevard', '+65 65243654', '137@smu.sg', '20 Canson Road'),
(587405231481, 'D000000000006', 'S000000000016', 'Lin Po Chien', 'Blk 135 Dog Boulevard', '+65 20975705', '138@smu.sg', '20 Benson Road'),
(587405231482, 'D000000000007', 'S000000000017', 'Lee Jun Hui', 'Blk 987 Family Mart', '+65 11493273', '139@smu.sg', '20 Danson Road'),
(587405231483, 'D000000000008', 'S000000000018', 'Vasilis Ng', 'Blk 246 Eggs Benedict Way', '+65 50046981', '140@smu.sg', '20 Benson Road'),
(587405231484, 'D000000000009', 'S000000000019', 'Vasilis Ng', 'Blk 987 Family Mart', '+65 19919575', '141@smu.sg', '20 Canson Road'),
(587405231485, 'D000000000010', 'S000000000020', 'Lin Po Chien', 'Blk 246 Eggs Benedict Way', '+65 31995017', '142@smu.sg', '20 Canson Road'),
(587405231486, 'D000000000001', 'S000000000021', 'Lin Po Chien', 'Blk 246 Eggs Benedict Way', '+65 89828676', '143@smu.sg', '20 Benson Road'),
(587405231487, 'D000000000002', 'S000000000022', 'Vasilis Ng', 'Blk 123 Banana Road', '+65 93513176', '144@smu.sg', '20 Benson Road'),
(587405231488, 'D000000000003', 'S000000000023', 'Lee Shao Ming', 'Blk 789 Cherry Drive', '+65 70549174', '145@smu.sg', '20 Danson Road'),
(587405231489, 'D000000000004', 'S000000000024', 'Reiko Lee', 'Blk 789 Cherry Drive', '+65 30854679', '146@smu.sg', '20 Benson Road'),
(587405231490, 'D000000000005', 'S000000000025', 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+65 74032665', '147@smu.sg', '20 Anson Road'),
(587405231491, 'D000000000006', 'S000000000026', 'Vasilis Ng', 'Blk 123 Banana Road', '+65 68994343', '148@smu.sg', '20 Benson Road'),
(587405231492, 'D000000000007', 'S000000000027', 'Lee Shao Ming', 'Blk 987 Family Mart', '+65 23180983', '149@smu.sg', '20 Anson Road'),
(587405231493, 'D000000000008', 'S000000000028', 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+65 46584543', '150@smu.sg', '20 Benson Road'),
(587405231494, 'D000000000009', 'S000000000029', 'Lee Jun Hui', 'Blk 135 Dog Boulevard', '+65 1989759', '151@smu.sg', '20 Canson Road'),
(587405231495, 'D000000000010', 'S000000000030', 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+65 17645283', '152@smu.sg', '20 Benson Road'),
(587405231496, 'D000000000001', 'S000000000031', 'Nicholas Wong', 'Blk 987 Family Mart', '+65 2956181', '153@smu.sg', '20 Canson Road'),
(587405231497, 'D000000000002', 'S000000000032', 'Lin Po Chien', 'Blk 246 Eggs Benedict Way', '+65 9079599', '154@smu.sg', '20 Canson Road'),
(587405231498, 'D000000000003', 'S000000000033', 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+65 49611946', '155@smu.sg', '20 Danson Road'),
(587405231499, 'D000000000004', 'S000000000034', 'Reiko Lee', 'Blk 123 Banana Road', '+65 46795683', '156@smu.sg', '20 Danson Road'),
(587405231500, 'D000000000005', 'S000000000035', 'Lee Jun Hui', 'Blk 123 Banana Road', '+65 6711747', '157@smu.sg', '20 Canson Road'),
(587405231501, 'D000000000006', 'S000000000036', 'Reiko Lee', 'Blk 246 Eggs Benedict Way', '+65 70653428', '158@smu.sg', '20 Danson Road'),
(587405231502, 'D000000000007', 'S000000000037', 'Lin Po Chien', 'Blk 135 Dog Boulevard', '+65 90041553', '159@smu.sg', '20 Benson Road'),
(587405231503, 'D000000000008', 'S000000000038', 'Vasilis Ng', 'Blk 987 Family Mart', '+65 82489426', '160@smu.sg', '20 Canson Road'),
(587405231504, 'D000000000009', 'S000000000039', 'Lin Po Chien', 'Blk 123 Banana Road', '+65 30854889', '161@smu.sg', '20 Danson Road'),
(587405231505, 'D000000000010', 'S000000000040', 'Reiko Lee', 'Blk 135 Dog Boulevard', '+65 44887083', '162@smu.sg', '20 Anson Road'),
(587405231506, 'D000000000011', 'S000000000041', 'Lee Shao Ming', 'Blk 246 Eggs Benedict Way', '+65 32160294', '163@smu.sg', '20 Anson Road'),
(587405231507, 'D000000000012', 'S000000000042', 'Vasilis Ng', 'Blk 987 Family Mart', '+65 74381730', '164@smu.sg', '20 Danson Road'),
(587405231508, 'D000000000013', 'S000000000043', 'Lee Jun Hui', 'Blk 987 Family Mart', '+65 69226820', '165@smu.sg', '20 Danson Road'),
(587405231509, 'D000000000014', 'S000000000044', 'Reiko Lee', 'Blk 456 Apple Avenue', '+65 28198387', '166@smu.sg', '20 Canson Road'),
(587405231510, 'D000000000015', 'S000000000045', 'Vasilis Ng', 'Blk 246 Eggs Benedict Way', '+65 71735636', '167@smu.sg', '20 Canson Road'),
(587405231511, 'D000000000006', 'S000000000046', 'Vasilis Ng', 'Blk 987 Family Mart', '+65 95455018', '168@smu.sg', '20 Anson Road'),
(587405231512, 'D000000000007', 'S000000000047', 'Lee Jun Hui', 'Blk 135 Dog Boulevard', '+65 42322635', '169@smu.sg', '20 Anson Road'),
(587405231513, 'D000000000008', 'S000000000048', 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+65 77854324', '170@smu.sg', '20 Anson Road'),
(587405231514, 'D000000000009', 'S000000000049', 'Lee Shao Ming', 'Blk 789 Cherry Drive', '+65 4918214', '171@smu.sg', '20 Benson Road'),
(587405231515, 'D000000000010', 'S000000000050', 'Reiko Lee', 'Blk 135 Dog Boulevard', '+65 67875626', '172@smu.sg', '20 Danson Road'),
(587405231516, 'D000000000015', '4', 'Vasilis', '420 Blaze It', '82184938', 'vasilis.ng.2020@scis.smu.edu.sg', NULL),
(587405231518, 'D000000000011', '5', 'Mr D. Rock.', 'Limbang Shopping Centre', '98765432', 'dwaynetherock@abc.com', '679 Choa Chu Kang Crescent'),
(587405231519, 'D000000000012', '5', 'Tan Ah Kau', '123 Sembawang Avenue', '+6582184938', 'vasilis.ng.2020@scis.smu.edu.sg', 'Limbang Shopping Centre'),
(587405231520, 'D000000000013', '5', 'Bo Bo Man', '679 Choa Chu Kang Crescent', '+6582184938', 'vasilis.ng.2020@scis.smu.edu.sg', '429 Choa Chu Kang Ave 4');

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
