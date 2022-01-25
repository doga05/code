-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 25 Oca 2022, 11:57:49
-- Sunucu sürümü: 8.0.21
-- PHP Sürümü: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `personeldb`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `tblpersonel`
--

DROP TABLE IF EXISTS `tblpersonel`;
CREATE TABLE IF NOT EXISTS `tblpersonel` (
  `ADI` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `SOYADI` varchar(30) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `tblpersonel`
--

INSERT INTO `tblpersonel` (`ADI`, `SOYADI`) VALUES
('Doğa', 'Özdemir'),
('Doğa', 'Özdemir'),
('Nur Sena', ''),
('Nur Sena', 'Günay'),
('arda', 'özdemir'),
('sfgsdfsgasg', 'dsgasfad'),
('doğa', 'özdemir');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
