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

-- --------------------------------------------------------

--
-- Table structure for table `activity`
--

CREATE TABLE `activity` (
  `activityID` int(11) NOT NULL,
  `trackingID` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deliveryStatus` varchar(30) NOT NULL,
  `deliveryDesc` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `activity`
--

INSERT INTO `activity` (`activityID`, `trackingID`, `timestamp`, `deliveryStatus`, `deliveryDesc`) VALUES
(1, 1337, '2022-03-19 20:45:24', 'Order Created!', 'The order has been created.'),
(2, 42069, '2022-03-19 20:48:49', 'Order Created!', 'The order has been created.'),
(3, 1337, '2022-03-20 12:09:57', 'Pickup', 'Order has been picked up by pickup driver');

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `trackingID` int(64) NOT NULL,
  `driverID` varchar(13) DEFAULT NULL,
  `shipperID` varchar(13) NOT NULL,
  `receiverName` varchar(30) NOT NULL,
  `receiverAddress` varchar(100) NOT NULL,
  `receiverPhone` varchar(30) NOT NULL,
  `receiverEmail` varchar(50) NOT NULL,
  `pickupAddress` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`trackingID`, `driverID`, `shipperID`, `receiverName`, `receiverAddress`, `receiverPhone`, `receiverEmail`, `pickupAddress`) VALUES
(1, 'D000000000001', 'S000000000001', 'Vasilis Ng', 'Blk 987 Family Mart', '+65 21598384', '123@smu.sg', '20 Canson Road'),
(2, 'D000000000002', 'S000000000002', 'Lee Shao Ming', 'Blk 987 Family Mart', '+65 93983698', '124@smu.sg', '20 Canson Road'),
(3, 'D000000000003', 'S000000000003', 'Nicholas Wong', 'Blk 456 Apple Avenue', '+65 80538094', '125@smu.sg', '20 Danson Road'),
(4, 'D000000000004', 'S000000000004', 'Nicholas Wong', 'Blk 135 Dog Boulevard', '+65 4145427', '126@smu.sg', '20 Danson Road'),
(5, 'D000000000005', 'S000000000005', 'Reiko Lee', 'Blk 246 Eggs Benedict Way', '+65 55230068', '127@smu.sg', '20 Danson Road'),
(6, 'D000000000006', 'S000000000006', 'Lin Po Chien', 'Blk 456 Apple Avenue', '+65 56629749', '128@smu.sg', '20 Danson Road'),
(7, 'D000000000007', 'S000000000007', 'Lee Jun Hui', 'Blk 123 Banana Road', '+65 48697119', '129@smu.sg', '20 Danson Road'),
(8, 'D000000000008', 'S000000000008', 'Vasilis Ng', 'Blk 123 Banana Road', '+65 78491046', '130@smu.sg', '20 Danson Road'),
(9, 'D000000000009', 'S000000000009', 'Lee Shao Ming', 'Blk 123 Banana Road', '+65 45712493', '131@smu.sg', '20 Canson Road'),
(10, 'D000000000010', 'S000000000010', 'Lee Jun Hui', 'Blk 135 Dog Boulevard', '+65 58160590', '132@smu.sg', '20 Anson Road'),
(11, 'D000000000001', 'S000000000011', 'Reiko Lee', 'Blk 123 Banana Road', '+65 9627904', '133@smu.sg', '20 Benson Road'),
(12, 'D000000000002', 'S000000000012', 'Lee Jun Hui', 'Blk 987 Family Mart', '+65 47573668', '134@smu.sg', '20 Canson Road'),
(13, 'D000000000003', 'S000000000013', 'Lin Po Chien', 'Blk 135 Dog Boulevard', '+65 46171449', '135@smu.sg', '20 Anson Road'),
(14, 'D000000000004', 'S000000000014', 'Reiko Lee', 'Blk 246 Eggs Benedict Way', '+65 63171071', '136@smu.sg', '20 Danson Road'),
(15, 'D000000000005', 'S000000000015', 'Reiko Lee', 'Blk 135 Dog Boulevard', '+65 65243654', '137@smu.sg', '20 Canson Road'),
(16, 'D000000000006', 'S000000000016', 'Lin Po Chien', 'Blk 135 Dog Boulevard', '+65 20975705', '138@smu.sg', '20 Benson Road'),
(17, 'D000000000007', 'S000000000017', 'Lee Jun Hui', 'Blk 987 Family Mart', '+65 11493273', '139@smu.sg', '20 Danson Road'),
(18, 'D000000000008', 'S000000000018', 'Vasilis Ng', 'Blk 246 Eggs Benedict Way', '+65 50046981', '140@smu.sg', '20 Benson Road'),
(19, 'D000000000009', 'S000000000019', 'Vasilis Ng', 'Blk 987 Family Mart', '+65 19919575', '141@smu.sg', '20 Canson Road'),
(20, 'D000000000010', 'S000000000020', 'Lin Po Chien', 'Blk 246 Eggs Benedict Way', '+65 31995017', '142@smu.sg', '20 Canson Road'),
(21, 'D000000000001', 'S000000000021', 'Lin Po Chien', 'Blk 246 Eggs Benedict Way', '+65 89828676', '143@smu.sg', '20 Benson Road'),
(22, 'D000000000002', 'S000000000022', 'Vasilis Ng', 'Blk 123 Banana Road', '+65 93513176', '144@smu.sg', '20 Benson Road'),
(23, 'D000000000003', 'S000000000023', 'Lee Shao Ming', 'Blk 789 Cherry Drive', '+65 70549174', '145@smu.sg', '20 Danson Road'),
(24, 'D000000000004', 'S000000000024', 'Reiko Lee', 'Blk 789 Cherry Drive', '+65 30854679', '146@smu.sg', '20 Benson Road'),
(25, 'D000000000005', 'S000000000025', 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+65 74032665', '147@smu.sg', '20 Anson Road'),
(26, 'D000000000006', 'S000000000026', 'Vasilis Ng', 'Blk 123 Banana Road', '+65 68994343', '148@smu.sg', '20 Benson Road'),
(27, 'D000000000007', 'S000000000027', 'Lee Shao Ming', 'Blk 987 Family Mart', '+65 23180983', '149@smu.sg', '20 Anson Road'),
(28, 'D000000000008', 'S000000000028', 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+65 46584543', '150@smu.sg', '20 Benson Road'),
(29, 'D000000000009', 'S000000000029', 'Lee Jun Hui', 'Blk 135 Dog Boulevard', '+65 1989759', '151@smu.sg', '20 Canson Road'),
(30, 'D000000000010', 'S000000000030', 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+65 17645283', '152@smu.sg', '20 Benson Road'),
(31, 'D000000000001', 'S000000000031', 'Nicholas Wong', 'Blk 987 Family Mart', '+65 2956181', '153@smu.sg', '20 Canson Road'),
(32, 'D000000000002', 'S000000000032', 'Lin Po Chien', 'Blk 246 Eggs Benedict Way', '+65 9079599', '154@smu.sg', '20 Canson Road'),
(33, 'D000000000003', 'S000000000033', 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+65 49611946', '155@smu.sg', '20 Danson Road'),
(34, 'D000000000004', 'S000000000034', 'Reiko Lee', 'Blk 123 Banana Road', '+65 46795683', '156@smu.sg', '20 Danson Road'),
(35, 'D000000000005', 'S000000000035', 'Lee Jun Hui', 'Blk 123 Banana Road', '+65 6711747', '157@smu.sg', '20 Canson Road'),
(36, 'D000000000006', 'S000000000036', 'Reiko Lee', 'Blk 246 Eggs Benedict Way', '+65 70653428', '158@smu.sg', '20 Danson Road'),
(37, 'D000000000007', 'S000000000037', 'Lin Po Chien', 'Blk 135 Dog Boulevard', '+65 90041553', '159@smu.sg', '20 Benson Road'),
(38, 'D000000000008', 'S000000000038', 'Vasilis Ng', 'Blk 987 Family Mart', '+65 82489426', '160@smu.sg', '20 Canson Road'),
(39, 'D000000000009', 'S000000000039', 'Lin Po Chien', 'Blk 123 Banana Road', '+65 30854889', '161@smu.sg', '20 Danson Road'),
(40, 'D000000000010', 'S000000000040', 'Reiko Lee', 'Blk 135 Dog Boulevard', '+65 44887083', '162@smu.sg', '20 Anson Road'),
(41, 'D000000000011', 'S000000000041', 'Lee Shao Ming', 'Blk 246 Eggs Benedict Way', '+65 32160294', '163@smu.sg', '20 Anson Road'),
(42, 'D000000000012', 'S000000000042', 'Vasilis Ng', 'Blk 987 Family Mart', '+65 74381730', '164@smu.sg', '20 Danson Road'),
(43, 'D000000000013', 'S000000000043', 'Lee Jun Hui', 'Blk 987 Family Mart', '+65 69226820', '165@smu.sg', '20 Danson Road'),
(44, 'D000000000014', 'S000000000044', 'Reiko Lee', 'Blk 456 Apple Avenue', '+65 28198387', '166@smu.sg', '20 Canson Road'),
(45, 'D000000000015', 'S000000000045', 'Vasilis Ng', 'Blk 246 Eggs Benedict Way', '+65 71735636', '167@smu.sg', '20 Canson Road'),
(46, 'D000000000006', 'S000000000046', 'Vasilis Ng', 'Blk 987 Family Mart', '+65 95455018', '168@smu.sg', '20 Anson Road'),
(47, 'D000000000007', 'S000000000047', 'Lee Jun Hui', 'Blk 135 Dog Boulevard', '+65 42322635', '169@smu.sg', '20 Anson Road'),
(48, 'D000000000008', 'S000000000048', 'Vasilis Ng', 'Blk 135 Dog Boulevard', '+65 77854324', '170@smu.sg', '20 Anson Road'),
(49, 'D000000000009', 'S000000000049', 'Lee Shao Ming', 'Blk 789 Cherry Drive', '+65 4918214', '171@smu.sg', '20 Benson Road'),
(50, 'D000000000010', 'S000000000050', 'Reiko Lee', 'Blk 135 Dog Boulevard', '+65 67875626', '172@smu.sg', '20 Danson Road');

-- --------------------------------------------------------

--
-- Table structure for table `shipper`
--

CREATE TABLE `shipper` (
  `shipperID` int(12) NOT NULL,
  `shipperName` varchar(32) NOT NULL,
  `shipperAddress` varchar(64) NOT NULL,
  `shipperPhone` int(8) NOT NULL,
  `shipperEmail` varchar(64) NOT NULL,
  `createdDate` datetime NOT NULL,
  `modifiedDate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `shipper`
--

INSERT INTO `shipper` (`shipperID`, `shipperName`, `shipperAddress`, `shipperPhone`, `shipperEmail`, `createdDate`, `modifiedDate`) VALUES
(1, 'Jun Hui', 'Woodlands', 83113585, 'junhuilee98@yahoo.com.sg', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(2, 'Lee Jun Hui', 'Hougang', 83113586, 'junhuilee99@yahoo.com.sg', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(3, 'Kevin Lee', 'Tampines', 83113587, 'junhuilee00@yahoo.com.sg', '0000-00-00 00:00:00', '0000-00-00 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activity`
--
ALTER TABLE `activity`
  ADD PRIMARY KEY (`activityID`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`trackingID`);

--
-- Indexes for table `shipper`
--
ALTER TABLE `shipper`
  ADD PRIMARY KEY (`shipperID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity`
--
ALTER TABLE `activity`
  MODIFY `activityID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `trackingID` int(64) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
