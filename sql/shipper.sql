-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shipper`
--
CREATE DATABASE IF NOT EXISTS `shipper` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `shipper`;

-- --------------------------------------------------------

--
-- Table structure for table `shippers`
--

DROP TABLE IF EXISTS `shipper`;
CREATE TABLE IF NOT EXISTS `shipper` (
  `shipperID` int(12) NOT NULL,
  `shipperName` varchar(32) NOT NULL,
  `shipperAddress` varchar(64) NOT NULL,
  `shipperPhone` int(8) NOT NULL,
  `shipperEmail` varchar(64) NOT NULL,
  `createdDate` datetime NOT NULL,
  `modifiedDate` datetime NOT NULL,
  PRIMARY KEY (`shipperID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `shipper`
--

INSERT INTO `shipper` (`shipperID`, `shipperName`, `shipperAddress`, `shipperPhone`, `shipperEmail`, `createdDate`, `modifiedDate`) VALUES
(000000000001, 'Jun Hui', 'Woodlands', 83113585, 'junhuilee98@yahoo.com.sg', 22-03-22, 22-04-22),
(000000000002, 'Lee Jun Hui', 'Hougang', 83113586, 'junhuilee99@yahoo.com.sg', 22-03-22, 22-04-22),
(000000000003, 'Kevin Lee', 'Tampines', 83113587, 'junhuilee00@yahoo.com.sg', 22-03-22, 22-04-22);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
