-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 21 Haz 2022, 14:16:54
-- Sunucu sürümü: 10.4.24-MariaDB
-- PHP Sürümü: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `homework`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `carts`
--

CREATE TABLE `carts` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_id` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `carts`
--

INSERT INTO `carts` (`id`, `user_id`, `created_at`, `updated_at`) VALUES
(1, 4, '2022-06-08 15:35:40', '2022-06-08 15:35:40'),
(2, 4, '2022-06-08 15:40:28', '2022-06-08 15:40:28'),
(3, 4, '2022-06-08 15:54:21', '2022-06-08 15:54:21'),
(4, 4, '2022-06-11 08:39:58', '2022-06-11 08:39:58'),
(5, 1, '2022-06-11 08:44:04', '2022-06-11 08:44:04'),
(6, 1, '2022-06-11 08:55:46', '2022-06-11 08:55:46'),
(7, 3, '2022-06-11 12:19:26', '2022-06-11 12:19:26'),
(8, 4, '2022-06-11 12:20:08', '2022-06-11 12:20:08'),
(9, 4, '2022-06-13 14:46:38', '2022-06-13 14:46:38'),
(10, 4, '2022-06-13 14:47:26', '2022-06-13 14:47:26'),
(11, 4, '2022-06-13 14:47:43', '2022-06-13 14:47:43'),
(12, 5, '2022-06-13 14:49:35', '2022-06-13 14:49:35'),
(13, 5, '2022-06-13 14:49:49', '2022-06-13 14:49:49'),
(14, 4, '2022-06-13 15:12:40', '2022-06-13 15:12:40'),
(15, 4, '2022-06-13 16:02:28', '2022-06-13 16:02:28'),
(16, 4, '2022-06-14 16:16:37', '2022-06-14 16:16:37'),
(17, 4, '2022-06-14 16:24:14', '2022-06-14 16:24:14'),
(18, 4, '2022-06-14 17:09:43', '2022-06-14 17:09:43');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `cart_products`
--

CREATE TABLE `cart_products` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `cart_id` bigint(20) UNSIGNED NOT NULL,
  `product_id` bigint(20) UNSIGNED NOT NULL,
  `qty` int(11) NOT NULL,
  `total` decimal(5,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `cart_products`
--

INSERT INTO `cart_products` (`id`, `cart_id`, `product_id`, `qty`, `total`, `created_at`, `updated_at`) VALUES
(14, 7, 15, 1, '45.00', '2022-06-11 12:19:26', '2022-06-11 12:19:26'),
(15, 8, 15, 1, '45.00', '2022-06-11 12:20:08', '2022-06-11 12:20:08'),
(16, 9, 35, 1, '19.00', '2022-06-13 14:46:38', '2022-06-13 14:46:38'),
(17, 9, 36, 1, '19.00', '2022-06-13 14:46:40', '2022-06-13 14:46:40'),
(18, 9, 46, 1, '19.00', '2022-06-13 14:46:44', '2022-06-13 14:46:44'),
(19, 10, 44, 1, '22.00', '2022-06-13 14:47:26', '2022-06-13 14:47:26'),
(20, 10, 50, 1, '26.00', '2022-06-13 14:47:29', '2022-06-13 14:47:29'),
(21, 11, 44, 1, '22.00', '2022-06-13 14:47:43', '2022-06-13 14:47:43'),
(22, 11, 50, 1, '26.00', '2022-06-13 14:47:47', '2022-06-13 14:47:47'),
(23, 12, 35, 1, '19.00', '2022-06-13 14:49:35', '2022-06-13 14:49:35'),
(24, 12, 43, 1, '22.00', '2022-06-13 14:49:38', '2022-06-13 14:49:38'),
(25, 13, 17, 1, '45.00', '2022-06-13 14:49:49', '2022-06-13 14:49:49'),
(26, 14, 43, 2, '22.00', '2022-06-13 15:12:40', '2022-06-13 15:12:52'),
(27, 14, 35, 1, '19.00', '2022-06-13 15:12:42', '2022-06-13 15:12:42'),
(28, 15, 56, 4, '30.00', '2022-06-13 16:02:28', '2022-06-13 16:15:47'),
(29, 16, 35, 2, '19.00', '2022-06-14 16:16:37', '2022-06-14 16:16:46'),
(30, 16, 36, 1, '19.00', '2022-06-14 16:16:41', '2022-06-14 16:16:41'),
(33, 18, 57, 1, '18.00', '2022-06-14 17:09:46', '2022-06-14 17:09:46');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `categories`
--

CREATE TABLE `categories` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `shop_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `categories`
--

INSERT INTO `categories` (`id`, `shop_id`, `name`, `created_at`, `updated_at`) VALUES
(7, 3, '01/06/2022', '2022-06-11 11:43:34', '2022-06-11 11:43:34'),
(8, 3, '02/06/2022', '2022-06-11 11:43:40', '2022-06-11 11:43:40'),
(9, 3, '03/06/2022', '2022-06-11 11:43:45', '2022-06-11 11:43:45'),
(10, 3, '04/06/2022', '2022-06-11 11:43:53', '2022-06-11 11:43:53'),
(11, 3, '05/06/2022', '2022-06-11 11:44:02', '2022-06-11 11:44:02'),
(12, 3, '06/06/2022', '2022-06-11 11:44:12', '2022-06-11 11:44:12'),
(13, 3, '07/06/2022', '2022-06-11 11:44:18', '2022-06-11 11:44:18'),
(14, 3, '08/06/2022', '2022-06-11 11:44:24', '2022-06-11 11:44:24'),
(15, 3, '09/06/2022', '2022-06-11 11:44:34', '2022-06-11 11:44:34'),
(16, 3, '10/06/2022', '2022-06-11 11:44:47', '2022-06-11 11:44:47'),
(17, 3, '11/06/2022', '2022-06-11 11:44:52', '2022-06-11 11:44:52'),
(18, 3, '12/06/2022', '2022-06-11 11:44:58', '2022-06-11 11:44:58'),
(19, 3, '13/06/2022', '2022-06-11 11:45:09', '2022-06-11 11:45:09'),
(20, 3, '14/06/2022', '2022-06-11 11:45:14', '2022-06-11 11:45:14'),
(21, 3, '15/06/2022', '2022-06-11 11:45:19', '2022-06-11 11:45:19'),
(22, 3, '16/06/2022', '2022-06-11 11:45:30', '2022-06-11 11:45:30'),
(23, 3, '17/06/2022', '2022-06-11 11:45:35', '2022-06-11 11:45:35'),
(24, 3, '18/06/2022', '2022-06-11 11:45:42', '2022-06-11 11:45:51'),
(25, 3, '19/06/2022', '2022-06-11 11:46:29', '2022-06-11 11:46:29'),
(26, 3, '20/06/2022', '2022-06-11 11:46:34', '2022-06-11 11:46:34'),
(27, 3, '21/06/2022', '2022-06-11 11:46:40', '2022-06-11 11:46:40'),
(28, 3, '22/06/2022', '2022-06-11 11:46:50', '2022-06-11 11:46:50'),
(29, 3, '23/06/2022', '2022-06-11 11:46:59', '2022-06-11 11:46:59'),
(30, 3, '24/06/2022', '2022-06-11 11:47:08', '2022-06-11 11:47:08'),
(31, 3, '25/06/2022', '2022-06-11 11:47:17', '2022-06-11 11:47:17'),
(32, 3, '26/06/2022', '2022-06-11 11:47:28', '2022-06-11 11:47:28'),
(33, 3, '27/06/2022', '2022-06-11 11:47:35', '2022-06-11 11:47:35'),
(34, 3, '28/06/2022', '2022-06-11 11:47:42', '2022-06-11 11:47:42'),
(35, 3, '29/06/2022', '2022-06-11 11:47:54', '2022-06-11 11:47:54'),
(36, 3, '30/06/2022', '2022-06-11 11:48:00', '2022-06-11 11:48:00'),
(37, 1, 'Espresso Beverages', '2022-06-11 12:26:59', '2022-06-11 12:26:59'),
(38, 1, 'Specialty Tea', '2022-06-11 12:27:16', '2022-06-11 12:27:16'),
(39, 1, 'Hot Chocolate', '2022-06-11 12:27:26', '2022-06-11 12:27:26'),
(40, 1, 'Iced Espresso', '2022-06-11 12:27:36', '2022-06-11 12:27:36'),
(41, 1, 'Iced Specialty Tea', '2022-06-11 12:27:54', '2022-06-11 12:27:54'),
(42, 1, 'Refresha', '2022-06-11 12:28:02', '2022-06-11 12:28:02'),
(43, 1, 'Frappuccino', '2022-06-11 12:28:12', '2022-06-11 12:28:12'),
(45, 2, 'Kahvaltılıklar', '2022-06-11 12:55:47', '2022-06-11 12:55:47'),
(46, 2, 'Atıştırmalıklar', '2022-06-11 12:55:56', '2022-06-11 12:55:56'),
(47, 2, 'Hamburgerler', '2022-06-11 12:56:05', '2022-06-11 12:56:05'),
(48, 2, 'Pizzalar', '2022-06-11 12:56:09', '2022-06-11 12:56:09'),
(49, 2, 'Makarnalar', '2022-06-11 12:56:20', '2022-06-11 12:56:20'),
(50, 2, 'Izgara ve Tavalar', '2022-06-11 12:56:33', '2022-06-11 12:56:33'),
(51, 2, 'Salatalar', '2022-06-11 12:56:48', '2022-06-11 12:56:48'),
(52, 2, 'Tatlılar', '2022-06-11 12:56:57', '2022-06-11 12:56:57'),
(53, 2, 'İçecekler', '2022-06-11 12:57:04', '2022-06-11 12:57:04'),
(54, 2, 'Kahveler', '2022-06-11 12:57:14', '2022-06-11 12:57:14');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `failed_jobs`
--

CREATE TABLE `failed_jobs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `uuid` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `connection` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `queue` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `exception` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2014_10_12_000000_create_users_table', 1),
(2, '2014_10_12_100000_create_password_resets_table', 1),
(3, '2019_08_19_000000_create_failed_jobs_table', 1),
(4, '2019_12_14_000001_create_personal_access_tokens_table', 1),
(5, '2022_06_02_172706_create_shops_table', 1),
(6, '2022_06_02_172735_create_categories_table', 1),
(7, '2022_06_02_172746_create_products_table', 1),
(8, '2022_06_02_172755_create_carts_table', 1),
(9, '2022_06_02_172804_create_cart_products_table', 1),
(10, '2022_06_02_172815_create_orders_table', 1);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `orders`
--

CREATE TABLE `orders` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `shop_id` bigint(20) UNSIGNED NOT NULL,
  `cart_id` bigint(20) UNSIGNED NOT NULL,
  `amount` decimal(10,4) NOT NULL,
  `scholl_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `isCompleted` tinyint(1) NOT NULL DEFAULT 0 COMMENT '0 verilmemiş / 1 verilmiş',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `orders`
--

INSERT INTO `orders` (`id`, `shop_id`, `cart_id`, `amount`, `scholl_no`, `name`, `email`, `isCompleted`, `created_at`, `updated_at`) VALUES
(7, 1, 9, '57.0000', '12044171', 'Ömer Uzer', 'omeruzer@gmail.com', 1, '2022-06-13 14:46:48', '2022-06-13 16:47:38'),
(8, 1, 11, '48.0000', '12044171', 'Ömer Uzer', 'omeruzer@gmail.com', 0, '2022-06-13 14:47:51', '2022-06-13 14:47:51'),
(9, 1, 12, '41.0000', '3434535635', 'Ali Veli', 'aliveli@gmail.com', 1, '2022-06-13 14:49:41', '2022-06-13 14:50:26'),
(10, 3, 13, '45.0000', '3434535635', 'Ali Veli', 'aliveli@gmail.com', 0, '2022-06-13 14:49:54', '2022-06-13 14:49:54'),
(11, 1, 14, '63.0000', '12044171', 'Ömer Uzer', 'omeruzer@gmail.com', 1, '2022-06-13 15:13:07', '2022-06-14 17:31:15'),
(12, 1, 16, '57.0000', '12044171', 'Ömer Uzer', 'omeruzer@gmail.com', 1, '2022-06-14 16:16:51', '2022-06-14 16:21:20');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `password_resets`
--

CREATE TABLE `password_resets` (
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `personal_access_tokens`
--

CREATE TABLE `personal_access_tokens` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `tokenable_type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tokenable_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `abilities` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_used_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `products`
--

CREATE TABLE `products` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `img` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `shop_id` bigint(20) UNSIGNED NOT NULL,
  `category_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` decimal(20,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `products`
--

INSERT INTO `products` (`id`, `img`, `shop_id`, `category_id`, `name`, `price`, `created_at`, `updated_at`) VALUES
(5, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 7, '01/06/2022 Menüsü (EZOGELİN ÇORBASI ARNAVUT CİĞERİ MISIRLI PİRİNÇ PİLAVI KASE AYRAN)', '45.00', '2022-06-11 11:50:34', '2022-06-11 11:50:34'),
(6, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 8, '02/06/2022 Menüsü (YAYLA ÇORBASI RULO ET KÖFTE MERCİMEKLİ BULGUR PİLAVI TULUMBA TATLISI)', '45.00', '2022-06-11 11:51:34', '2022-06-11 11:51:34'),
(7, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 9, '03/06/2022 Menüsü (TARHANA ÇORBASI TAVUKLU NOHUT SADE PİRİNÇ PİLAVI ERİK)', '45.00', '2022-06-11 11:52:16', '2022-06-11 11:52:16'),
(8, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 10, '04/06/2022 Menüsü (DOMATES ÇORBASI ETLİ TAZE FASÜLYE SADE MAKARNA KASE YOĞURT)', '45.00', '2022-06-11 11:52:35', '2022-06-11 11:52:48'),
(9, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 11, '05/06/2022 Menüsü (KREMALI SEBZE ÇORBASI SOSLU FIRIN KÖFTE TEL ŞEHRİYELİ PİRİNÇ PİLAVI KARPUZ)', '45.00', '2022-06-11 11:53:22', '2022-06-11 11:53:22'),
(10, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 12, '06/06/2022 Menüsü (TOYGA ÇORBASI BAHÇIVAN KEBABI SADE BULGUR PİLAVI KAZANDİBİ)', '45.00', '2022-06-11 11:53:54', '2022-06-11 11:54:25'),
(11, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 13, '07/06/2022 Menüsü (MERCİMEK ÇORBASI FIRIN TAVUK BUT NOHUTLU PİRİNÇ PİLAVI ÇOBAN SALATASI)', '45.00', '2022-06-11 11:54:55', '2022-06-11 11:54:55'),
(12, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 14, '08/06/2022 Menüsü (TEL ŞEHRİYE ÇORBASI ZEYTİNYAĞLI BARBUNYA KIYMALI KOL BÖREĞİ ÜZÜM HOŞAFI)', '45.00', '2022-06-11 11:55:47', '2022-06-11 11:55:47'),
(13, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 15, '09/06/2022 Menüsü (ANDOLÜZ ÇORBASI ZEYTİNYAĞLI TÜRLÜ PEYNİRLİ MAKARNA KASE YOĞURT)', '45.00', '2022-06-11 11:56:31', '2022-06-11 11:56:31'),
(14, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 16, '10/06/2022 Menüsü (TARHANA ÇORBASI TERBİYELİ KÖFTE TEREYAĞLI ERİŞTE PİLAVI ERİK)', '45.00', '2022-06-11 11:57:29', '2022-06-11 11:57:29'),
(15, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 17, '11/06/2022 Menüsü (ARPA ŞEHRİYE ÇORBASI ETLİ KURU FASÜLYE SEBZELİ BULGUR PİLAVI KARIŞIK TURŞU)', '45.00', '2022-06-11 11:58:06', '2022-06-11 11:58:06'),
(16, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 18, '12/06/2022 Menüsü (KÖYLÜ ÇORBASI ÇEŞNİLİ PİLİÇ PANE TEL ŞEHRİYELİ PİRİNÇ PİLAVI KASE AYRAN)', '45.00', '2022-06-11 11:58:28', '2022-06-11 11:59:22'),
(17, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 19, '13/06/2022 Menüsü (EZOGELİN ÇORBASI TAS KEBABI SADE BULGUR PİLAVI YOĞURT TATLISI)', '45.00', '2022-06-11 11:58:55', '2022-06-11 11:59:38'),
(18, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 20, '14/06/2022 Menüsü (GEMİCİ ÇORBASI İZMİR KÖFTE MERCİMEKLİ BULGUR PİLAVI KİRAZ)', '45.00', '2022-06-11 12:00:53', '2022-06-11 12:00:53'),
(19, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 21, '15/06/2022 Menüsü (TERBİYELİ ŞEHRİYE ÇORBASI PİLİÇ KANAT IZGARA SADE PİRİNÇ PİLAVI ÇOBAN SALATASI)', '45.00', '2022-06-11 12:01:18', '2022-06-11 12:01:18'),
(20, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 22, '16/06/2022 Menüsü (MERCİMEK ÇORBASI MACAR GULAŞ SADE BULGUR PİLAVI KEŞKÜL)', '45.00', '2022-06-11 12:02:01', '2022-06-11 12:02:01'),
(21, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 23, '17/06/2022 Menüsü (KÖYLÜ ÇORBASI ÇEŞNİLİ PİLİÇ PANE TEL ŞEHRİYELİ PİRİNÇ PİLAVI KASE AYRAN)', '45.00', '2022-06-11 12:02:21', '2022-06-11 12:02:21'),
(22, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 24, '18/06/2022 Menüsü (TARHANA ÇORBASI TERBİYELİ KÖFTE TEREYAĞLI ERİŞTE PİLAVI ERİK)', '45.00', '2022-06-11 12:02:38', '2022-06-11 12:02:38'),
(23, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 25, '19/06/2022 Menüsü (DOMATES ÇORBASI KIYMALI BİBER DOLMASI SADE MAKARNA KASE YOĞURT)', '45.00', '2022-06-11 12:02:52', '2022-06-11 12:03:06'),
(24, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 26, '20/06/2022 Menüsü (TARHANA ÇORBASI ZEYTİNYAĞLI NOHUT YAHNİ TAVUKLU PİRİNÇ PİLAVI KASE AYRAN)', '45.00', '2022-06-11 12:04:08', '2022-06-11 12:04:08'),
(25, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 27, '21/06/2022 Menüsü (YAYLA ÇORBASI ÇİFTLİK KEBABI NAPOLİTEN SOSLU MAKARNA KARPUZ)', '45.00', '2022-06-11 12:04:28', '2022-06-11 12:04:28'),
(26, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 28, '22/06/2022 Menüsü (EZOGELİN ÇORBASI IZGARA KÖFTE ARPA ŞEHRİYELİ PİRİNÇ PİLAVI KASE AYRAN)', '45.00', '2022-06-11 12:05:04', '2022-06-11 12:05:04'),
(27, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 29, '23/06/2022 Menüsü (KREMALI MANTAR ÇORBASI TAVUK ROTİ SADE BULGUR PİLAVI ÇOBAN SALATASI)', '45.00', '2022-06-11 12:05:28', '2022-06-11 12:05:28'),
(28, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 30, '24/06/2022 Menüsü (ŞEHRİYELİ TAVUK ÇORBASI KARNIYARIK SADE PİRİNÇ PİLAVI CACIK)', '45.00', '2022-06-11 12:05:50', '2022-06-11 12:05:50'),
(29, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 31, '25/06/2022 Menüsü (EZOGELİN ÇORBASI ARNAVUT CİĞERİ MISIRLI PİRİNÇ PİLAVI KASE AYRAN)', '45.00', '2022-06-11 12:06:15', '2022-06-11 12:06:15'),
(30, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 32, '26/06/2022 Menüsü (YAYLA ÇORBASI RULO ET KÖFTE MERCİMEKLİ BULGUR PİLAVI TULUMBA TATLISI)', '45.00', '2022-06-11 12:06:34', '2022-06-11 12:06:34'),
(31, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 33, '27/06/2022 Menüsü (TARHANA ÇORBASI TAVUKLU NOHUT SADE PİRİNÇ PİLAVI ERİK)', '45.00', '2022-06-11 12:06:55', '2022-06-11 12:06:55'),
(32, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 34, '28/06/2022 Menüsü (DOMATES ÇORBASI ETLİ TAZE FASÜLYE SADE MAKARNA KASE YOĞURT)', '45.00', '2022-06-11 12:07:15', '2022-06-11 12:07:15'),
(33, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 35, '29/06/2022 Menüsü (KREMALI SEBZE ÇORBASI SOSLU FIRIN KÖFTE TEL ŞEHRİYELİ PİRİNÇ PİLAVI KARPUZ)', '45.00', '2022-06-11 12:08:12', '2022-06-11 12:08:12'),
(34, 'https://www.saglamlaryemek.com/uploads/1599504751-tabldot-yemek.jpg', 3, 36, '30/06/2022 Menüsü (TOYGA ÇORBASI BAHÇIVAN KEBABI SADE BULGUR PİLAVI KAZANDİBİ)', '45.00', '2022-06-11 12:08:36', '2022-06-11 12:08:36'),
(35, 'https://reimg-carrefour.mncdn.com/mnresize/600/600/productimage/30246809/30246809_0_MC/8813659947058_1654073788189.jpg', 1, 37, 'Caffe Latte', '19.00', '2022-06-11 12:29:48', '2022-06-11 12:29:48'),
(36, 'https://st2.myideasoft.com/idea/gb/84/myassets/products/626/karton-cappucino.png?revision=1644592113', 1, 37, 'Cappuccino', '19.00', '2022-06-11 12:30:21', '2022-06-11 12:30:21'),
(37, 'https://lzd-img-global.slatic.net/g/ff/kf/Sf8b7a9e6ebe74bf893a6627ffac0800b2.jpg_720x720q80.jpg_.webp', 1, 37, 'Caffe Mocha', '25.00', '2022-06-11 12:31:16', '2022-06-11 12:31:16'),
(38, 'https://storage.googleapis.com/images-sof-prd-9fa6b8b.sof.prd.v8.commerce.mi9cloud.com/product-images/zoom/00055000752916.jpg', 1, 37, 'White Chocolate Mocha', '25.00', '2022-06-11 12:32:19', '2022-06-11 12:32:19'),
(39, 'https://cdn.dsmcdn.com/ty10/product/media/images/20200819/0/8308652/21210037/1/1_org_zoom.jpg', 1, 37, 'Caramel Macchiato', '23.00', '2022-06-11 12:33:08', '2022-06-11 12:33:08'),
(40, 'https://www.kackalori.com.tr/Uploads/Kaloriler/1-short-kucuk-boy-starbucks-caffe-americano-kac-kalori_49_2.jpg?width=300', 1, 37, 'Caffe Americano', '18.00', '2022-06-11 12:34:32', '2022-06-11 12:34:32'),
(41, 'https://productimages.hepsiburada.net/s/4/375/9629191667762.jpg', 1, 37, 'Espresso', '13.00', '2022-06-11 12:35:15', '2022-06-11 12:35:15'),
(42, 'https://productimages.hepsiburada.net/s/51/375/11067900985394.jpg', 1, 37, 'Espresso Macchiato', '14.00', '2022-06-11 12:36:13', '2022-06-11 12:36:13'),
(43, 'https://www.kackalori.com.tr/Uploads/Kaloriler/1-adet-tall-starbucks-chai-tea-latte-yagsiz-sut-ile-kac-kalori_76_2.jpg?width=300', 1, 38, 'Chai Tea Latte', '22.00', '2022-06-11 12:37:04', '2022-06-11 12:37:04'),
(44, 'https://i2-prod.mirror.co.uk/incoming/article25351003.ece/ALTERNATES/s1200c/0_Starbucks-Fudge-Brownie-Hot-Chocolate.jpg', 1, 39, 'Hot Chocolate', '22.00', '2022-06-11 12:37:59', '2022-06-11 12:37:59'),
(45, 'https://assets.sainsburys-groceries.co.uk/gol/7260789/1/640x640.jpg', 1, 40, 'iced coffee latte', '20.00', '2022-06-11 12:38:33', '2022-06-11 12:38:33'),
(46, 'https://qph.cf2.quoracdn.net/main-qimg-aa51ad6e748efdc3eddbaf8e6dfd91bf.webp', 1, 40, 'Iced Coffee Americano', '19.00', '2022-06-11 12:39:18', '2022-06-11 12:39:18'),
(47, 'https://digitalcontent.api.tesco.com/v2/media/ghs/bd8af6a3-e2c9-403f-b9f1-0fb9054236d7/067d47a6-f392-4d38-bd1c-618f3e88d389.jpeg?h=540&w=540', 1, 40, 'Iced Caramel Macchiato', '25.00', '2022-06-11 12:39:58', '2022-06-11 12:39:58'),
(48, 'https://kalorisor.com/uploads/images/urun/starbucks-iced-caffe-mocha.jpg', 1, 40, 'Iced Caffe Mocha', '29.00', '2022-06-11 12:40:32', '2022-06-11 12:40:32'),
(49, 'https://globalassets.starbucks.com/assets/b80d893714854b5c946ee6c7f0d369d7.jpg?impolicy=1by1_wide_topcrop_630', 1, 40, 'Iced White Chocolate Mocha', '29.00', '2022-06-11 12:41:15', '2022-06-11 12:41:15'),
(50, 'https://www.digitalassets.starbucks.eu/sites/starbucks-medialibrary/files/assets/5fc6eaa716a70160802531bc55437ef2_0.jpg', 1, 42, 'Cool Lime', '26.00', '2022-06-11 12:43:13', '2022-06-11 12:43:13'),
(51, 'https://www.digitalassets.starbucks.eu/sites/starbucks-medialibrary/files/Strawberry-Acai-REVISED.jpeg', 1, 42, 'Strawberry Acai', '26.00', '2022-06-11 12:44:23', '2022-06-11 12:44:23'),
(52, 'https://www.digitalassets.starbucks.eu/sites/starbucks-medialibrary/files/Coffee-Frappuccino_0.jpeg', 1, 43, 'Coffee Frappuccino', '28.00', '2022-06-11 12:44:59', '2022-06-11 12:44:59'),
(53, 'https://www.digitalassets.starbucks.eu/sites/starbucks-medialibrary/files/Espresso-Frappuccino_0.jpeg', 1, 43, 'Espresso Frappuccino', '28.00', '2022-06-11 12:46:50', '2022-06-11 12:46:50'),
(54, 'https://www.digitalassets.starbucks.eu/sites/starbucks-medialibrary/files/Caramel-Frappuccino_0.jpeg', 1, 43, 'Caramel Frappuccino', '29.00', '2022-06-11 12:47:50', '2022-06-11 12:47:50'),
(55, 'https://www.digitalassets.starbucks.eu/sites/starbucks-medialibrary/files/Mocha-Frappuccino_0.jpeg', 1, 43, 'Mocha Frappuccino', '29.00', '2022-06-11 12:48:16', '2022-06-11 12:48:16'),
(56, 'https://www.koalarestaurant.com/wp-content/uploads/2020/10/kahvalti_tabagi-scaled.jpeg', 2, 45, 'Kahvaltı Tabağı', '30.00', '2022-06-11 13:00:44', '2022-06-11 13:00:44'),
(57, 'https://cdn.yemek.com/mnresize/940/940/uploads/2014/06/soganli-menemen-yeni.jpg', 2, 45, 'Menemen', '18.00', '2022-06-11 13:01:05', '2022-06-11 13:01:05'),
(58, 'http://www.livashop.com/Uploads/UrunResimleri/buyuk/sucuklu-kasarli-tost-9e4c.jpg', 2, 45, 'Tost Çeşitleri', '15.00', '2022-06-11 13:01:34', '2022-06-11 13:01:34'),
(59, 'https://i4.hurimg.com/i/hurriyet/75/750x422/5b8d24037152d81ed47686fb.jpg', 2, 45, 'Omlet Çeşitleri', '15.00', '2022-06-11 13:02:00', '2022-06-11 13:02:00'),
(60, 'https://www.diyetkolik.com/site_media/media/foodrecipe_images/sahanda-yumurta.210x210.png', 2, 45, 'Sahanda Yumurta Çeşitleri', '13.00', '2022-06-11 13:02:33', '2022-06-11 13:02:33'),
(61, 'https://cdn.yemek.com/mncrop/940/625/uploads/2017/12/peynirli-gozleme-buyuk.jpg', 2, 45, 'Gözleme Çeşitleri', '18.00', '2022-06-11 13:02:58', '2022-06-11 13:02:58'),
(62, 'https://i4.hurimg.com/i/hurriyet/75/750x422/5ddcf720c9de3d2cc48318a8.jpg', 2, 45, 'Sandviç Çeşitleri', '16.00', '2022-06-11 13:03:29', '2022-06-11 13:03:29'),
(63, 'https://i4.hurimg.com/i/hurriyet/75/1200x675/5c5d883ec03c0e506c6f767b.jpg', 2, 46, '8\'li Soğan Halkası', '18.00', '2022-06-11 13:04:32', '2022-06-11 13:04:32'),
(64, 'https://i.lezzet.com.tr/images-xxlarge-secondary/nugget-nasil-pisirilir-0daded81-257b-4bb5-b7ef-d0feb598e370.jpg', 2, 46, '8\'li Nuggut', '19.00', '2022-06-11 13:05:23', '2022-06-11 13:05:23'),
(65, 'http://www.portloca.com/storage/2018/08/sosis-patates.jpg', 2, 46, 'Sosis ve Patates', '29.00', '2022-06-11 13:05:45', '2022-06-11 13:05:45'),
(66, 'https://www.foodtime.com.tr/images/haberler/doner_stoptan_iki_nefis_tarif_gyro_stop_ve_deluxe_stop_h15678.jpg', 2, 47, 'Hamburger (Et)', '58.00', '2022-06-11 13:06:35', '2022-06-11 13:06:35'),
(67, 'https://www.kaloriver.com/uploads/nutrition/5517/tavuk-burger.jpg', 2, 47, 'Hamburger (Tavuk)', '46.00', '2022-06-11 13:07:03', '2022-06-11 13:07:03'),
(68, 'https://www.bonservis.com.tr/senass-karisik-pizza-25-cm-unlu-mamuller-senass-10-adet-x-1-koli-5004-25-B.jpg', 2, 48, 'Karışık Pizza', '43.00', '2022-06-11 13:07:37', '2022-06-11 13:07:37'),
(69, 'https://img.acunn.com/foto/700x600/uploads/icerikler/2020/07/29/spgetti-bolonez-tarifi8600464875f21cadf8baa4.jpg', 2, 49, 'Spagetti Bolonez', '34.00', '2022-06-11 13:09:02', '2022-06-11 13:09:02'),
(70, 'https://cdn.yemek.com/mnresize/1250/834/uploads/2021/03/korili-tavuklu-penne-makarna-tarifi.jpg', 2, 49, 'Penne Köri', '35.00', '2022-06-11 13:09:36', '2022-06-11 13:09:36'),
(71, 'https://i.lezzet.com.tr/images-xxlarge-secondary/mantinin-yanina-ne-gider-133b35e5-a9b4-4206-8140-0fdd57b907cc', 2, 49, 'Mantı', '35.00', '2022-06-11 13:09:56', '2022-06-11 13:09:56'),
(72, 'https://cdn.yemek.com/mnresize/1250/833/uploads/2020/11/inegol-kofte-one-cikan-kasim-2020.jpg', 2, 50, 'Izgara Köfte', '55.00', '2022-06-11 13:10:28', '2022-06-11 13:10:28'),
(73, 'https://i4.hurimg.com/i/hurriyet/75/750x422/5aeab7a367b0a820f041ab8c.jpg', 2, 50, 'Izgara Tavuk', '47.00', '2022-06-11 13:10:50', '2022-06-11 13:10:50'),
(74, 'https://img-s1.onedio.com/id-610905431a0b7c4f20c97c1d/rev-0/w-620/f-jpg/s-40c70234a1c33662bf042838b95776bbe56c673f.jpg', 2, 50, 'Köri Soslu Tavuk', '50.00', '2022-06-11 13:11:28', '2022-06-11 13:11:28'),
(75, 'https://img.acunn.com/uploads/icerikler/2020/11/17/kasarli-kofte-tarifi19541555845fb3f92550a57.jpg', 2, 50, 'Kaşarlı Köfte', '58.00', '2022-06-11 13:11:50', '2022-06-11 13:11:50'),
(76, 'https://ykv.s3.eu-central-1.amazonaws.com/img/w/tarif/ogt/tavuklu-sezar-salata.webp', 2, 51, 'Tavuklu Sezar Salata', '38.00', '2022-06-11 13:12:56', '2022-06-11 13:12:56'),
(77, 'https://isbh.tmgrup.com.tr/sbh/2016/03/30/650x344/1459325517043.jpg', 2, 51, 'Ton Balıklı Salata', '38.00', '2022-06-11 13:13:33', '2022-06-11 13:13:33'),
(78, 'https://i.lezzet.com.tr/images-xxlarge-recipe/beyaz_peynirli_akdeniz_salatasi-db808a1a-1457-48cb-b20f-95cda53d73b8.jpg', 2, 51, 'Akdeniz Salatası', '22.00', '2022-06-11 13:14:07', '2022-06-11 13:14:07'),
(79, 'https://i.lezzet.com.tr/images-xxlarge-recipe/magnolia-40c2dc1f-9306-4a77-8407-ee4c449dd916.jpg', 2, 52, 'Magnolia', '20.00', '2022-06-11 13:14:39', '2022-06-11 13:14:39'),
(80, 'https://i.lezzet.com.tr/images-xxlarge-recipe/san-sebastian-cheesecake-d581a84b-a9ed-4639-9536-ba1e6f0a8523.jpg', 2, 52, 'Sebastian Cheesecake', '25.00', '2022-06-11 13:15:08', '2022-06-11 13:15:08'),
(81, 'https://im.haberturk.com/2019/09/18/ver1568875032/mozaik-pasta-tarifi-nasil-yapilir_2523237_810x458.jpg', 2, 52, 'Mozaik Pasta', '22.00', '2022-06-11 13:15:36', '2022-06-14 17:28:21'),
(82, 'https://ia.tmgrup.com.tr/9f449c/812/468/0/104/1024/694?u=https://i.tmgrup.com.tr/sfr/2022/01/21/sufle-yaparken-bunlara-dikkat-1642762574308.jpg', 2, 52, 'Sufle', '20.00', '2022-06-11 13:15:57', '2022-06-11 13:15:57'),
(83, 'https://ayb.akinoncdn.com/products/2019/01/18/3544/5aa1ee14-1c83-4213-a62b-773c4785e187_size780x780_quality60_cropCenter.jpg', 2, 53, 'Coca Cola', '10.00', '2022-06-11 13:16:29', '2022-06-11 13:16:29'),
(84, 'http://www.livashop.com/Uploads/UrunResimleri/buyuk/coca-cola-zero-14e6.jpg', 2, 53, 'Coca Cola Zero', '10.00', '2022-06-11 13:16:50', '2022-06-11 13:16:50'),
(85, 'https://migros-dali-storage-prod.global.ssl.fastly.net/sanalmarket/product/08020000/08020000-b2f664-1650x1650.jpg', 2, 53, 'Fanta', '10.00', '2022-06-11 13:17:06', '2022-06-11 13:17:06'),
(86, 'https://images.ofix.com/product-image/s99509_2.jpg', 2, 53, 'Sprite', '10.00', '2022-06-11 13:17:28', '2022-06-11 13:17:28'),
(87, 'https://cdnsta.avansas.com/mnresize/300/-/urun/98629/fuse-tea-seftali-330cc-zoom-1.jpg', 2, 53, 'Fuse Tea', '10.00', '2022-06-11 13:17:50', '2022-06-11 13:17:50'),
(88, 'https://migros-dali-storage-prod.global.ssl.fastly.net/sanalmarket/product/46054715/46054715-8a2faf-1650x1650.jpg', 2, 53, 'Ayran', '6.00', '2022-06-11 13:18:08', '2022-06-11 13:18:08'),
(89, 'https://i0.wp.com/www.nazar.com.tr/wp-content/uploads/2020/12/taze-sikma-portakal-suyu.jpg?fit=600%2C600&ssl=1', 2, 53, 'Sıkma Portakal Suyu', '10.00', '2022-06-11 13:18:30', '2022-06-11 13:18:30'),
(90, 'https://esenlik.com.tr//images/prod/2928.jpg', 2, 53, 'Sade Soda', '4.00', '2022-06-11 13:18:51', '2022-06-11 13:18:51'),
(91, 'https://productimages.hepsiburada.net/s/23/500/10057716498482.jpg', 2, 53, 'Limonlu Soda', '5.00', '2022-06-11 13:19:18', '2022-06-11 13:19:18'),
(92, 'https://im.haberturk.com/2018/07/11/ver1536930406/2054140_620x410.jpg', 2, 53, 'Limonata', '8.00', '2022-06-11 13:19:46', '2022-06-11 13:19:46'),
(93, 'https://ykv.s3.eu-central-1.amazonaws.com/img/w/yazi/mgt/shutterstock_517083931.webp', 2, 54, 'Espresso', '12.00', '2022-06-11 13:20:30', '2022-06-11 13:20:30'),
(94, 'https://i.lezzet.com.tr/images-xxlarge-secondary/americano-nedir-nasil-yapilir-9002aab3-a04e-4495-9958-8d8adee0dfea.jpg', 2, 54, 'Americano', '12.00', '2022-06-11 13:21:01', '2022-06-11 13:21:01'),
(95, 'https://coffeetropic.com/wp-content/uploads/2020/06/latte.jpg', 2, 54, 'Sütlü Kahve', '12.00', '2022-06-11 13:21:29', '2022-06-11 13:21:29'),
(96, 'https://cdn.yemek.com/mncrop/940/625/uploads/2020/05/evde-latte-yapimi-2.jpg', 2, 54, 'Latte', '14.00', '2022-06-11 13:21:46', '2022-06-11 13:21:46'),
(97, 'https://d2lswn7b0fl4u2.cloudfront.net/photos/pg-cappuccino-coffee-1604848086.jpg', 2, 54, 'Cappuccino', '13.00', '2022-06-11 13:22:54', '2022-06-11 13:22:54'),
(98, 'https://i.lezzet.com.tr/images-xxlarge-recipe/fistik_ezmeli_sicak_cikolata-98f60a9e-82cc-4178-a561-1a262c949344.jpg', 2, 54, 'Sıcak Çikolata', '12.00', '2022-06-11 13:23:51', '2022-06-11 13:23:51'),
(99, 'https://www.mustespressoturkiye.com/wp-content/uploads/2020/01/12.png', 2, 54, 'Mocha', '12.00', '2022-06-11 13:24:25', '2022-06-11 13:24:25');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `shops`
--

CREATE TABLE `shops` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_id` bigint(20) UNSIGNED NOT NULL,
  `img` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `desc` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `shops`
--

INSERT INTO `shops` (`id`, `user_id`, `img`, `name`, `desc`, `created_at`, `updated_at`) VALUES
(1, 1, 'https://i.etsystatic.com/11085793/r/il/29f666/834112249/il_fullxfull.834112249_7u8q.jpg', 'Starbucks', 'Starbucks', '2022-06-08 15:31:51', '2022-06-13 16:40:44'),
(2, 2, 'https://cdn.discordapp.com/attachments/985961917925453836/985975474155040869/channels4_profile.jpg', 'İSÜ Arka Bahçe', 'İstinye\'nin Arka Bahçesi', '2022-06-08 15:31:51', '2022-06-13 15:46:38'),
(3, 3, 'https://cdn.discordapp.com/attachments/985961917925453836/985974421086937128/unknown.png', 'Yemekhane', 'Günlük 4 Çeşit Yemek', '2022-06-08 15:31:51', '2022-06-13 15:45:04');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `scholl_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `isAdmin` tinyint(1) NOT NULL DEFAULT 0 COMMENT '0 öğrenci / 1 restorant',
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`id`, `name`, `scholl_no`, `email`, `password`, `isAdmin`, `remember_token`, `created_at`, `updated_at`) VALUES
(1, 'Starbucks', NULL, 'starbucks@gmail.com', '$2y$10$yEQSmIZ4XvoUaqVpREPw2OOwKhWkbCi6o3DbmPejAwXK8jM0Oc3j.', 1, NULL, '2022-06-08 15:31:51', '2022-06-08 15:31:51'),
(2, 'Cafe2', NULL, 'isüarkabahce@gmail.com', '$2y$10$bNPmaqGWSGYqRbRP7V44XeH9YY5z2zp1SaH6sAOfONl3fk/GNAJLe', 1, NULL, '2022-06-08 15:31:51', '2022-06-08 15:31:51'),
(3, 'Cafe3', NULL, 'yemekhane@gmail.com', '$2y$10$V/FNaNMbzLcGdkGvhsTXTOkdj00B0LyQ0apP2Ru1wuN4qlri6uKni', 1, NULL, '2022-06-08 15:31:51', '2022-06-08 15:31:51'),
(4, 'Ömer Uzer', '12044171', 'omeruzer@gmail.com', '$2y$10$LSl05EpaJxEsZ4jIB0IXu.OCrbEfNLopYRDoM0mRQquHZ3uaCSAC.', 0, NULL, '2022-06-08 15:31:51', '2022-06-13 16:15:32'),
(5, 'Ali Veli', '3434535635', 'aliveli@gmail.com', '$2y$10$lHp4q8FhVZ94pUOWUV.s7uUTtpN3Wa4KyaTnJfADkhsmO257scaxi', 0, NULL, '2022-06-13 14:49:29', '2022-06-13 14:49:29');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `carts`
--
ALTER TABLE `carts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `carts_user_id_foreign` (`user_id`);

--
-- Tablo için indeksler `cart_products`
--
ALTER TABLE `cart_products`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cart_products_cart_id_foreign` (`cart_id`),
  ADD KEY `cart_products_product_id_foreign` (`product_id`);

--
-- Tablo için indeksler `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`),
  ADD KEY `categories_shop_id_foreign` (`shop_id`);

--
-- Tablo için indeksler `failed_jobs`
--
ALTER TABLE `failed_jobs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `failed_jobs_uuid_unique` (`uuid`);

--
-- Tablo için indeksler `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `orders_cart_id_unique` (`cart_id`),
  ADD KEY `orders_shop_id_foreign` (`shop_id`);

--
-- Tablo için indeksler `password_resets`
--
ALTER TABLE `password_resets`
  ADD KEY `password_resets_email_index` (`email`);

--
-- Tablo için indeksler `personal_access_tokens`
--
ALTER TABLE `personal_access_tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `personal_access_tokens_token_unique` (`token`),
  ADD KEY `personal_access_tokens_tokenable_type_tokenable_id_index` (`tokenable_type`,`tokenable_id`);

--
-- Tablo için indeksler `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD KEY `products_shop_id_foreign` (`shop_id`),
  ADD KEY `products_category_id_foreign` (`category_id`);

--
-- Tablo için indeksler `shops`
--
ALTER TABLE `shops`
  ADD PRIMARY KEY (`id`),
  ADD KEY `shops_user_id_foreign` (`user_id`);

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_email_unique` (`email`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `carts`
--
ALTER TABLE `carts`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Tablo için AUTO_INCREMENT değeri `cart_products`
--
ALTER TABLE `cart_products`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- Tablo için AUTO_INCREMENT değeri `categories`
--
ALTER TABLE `categories`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- Tablo için AUTO_INCREMENT değeri `failed_jobs`
--
ALTER TABLE `failed_jobs`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Tablo için AUTO_INCREMENT değeri `orders`
--
ALTER TABLE `orders`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Tablo için AUTO_INCREMENT değeri `personal_access_tokens`
--
ALTER TABLE `personal_access_tokens`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `products`
--
ALTER TABLE `products`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- Tablo için AUTO_INCREMENT değeri `shops`
--
ALTER TABLE `shops`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `carts`
--
ALTER TABLE `carts`
  ADD CONSTRAINT `carts_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Tablo kısıtlamaları `cart_products`
--
ALTER TABLE `cart_products`
  ADD CONSTRAINT `cart_products_cart_id_foreign` FOREIGN KEY (`cart_id`) REFERENCES `carts` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `cart_products_product_id_foreign` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE;

--
-- Tablo kısıtlamaları `categories`
--
ALTER TABLE `categories`
  ADD CONSTRAINT `categories_shop_id_foreign` FOREIGN KEY (`shop_id`) REFERENCES `shops` (`id`) ON DELETE CASCADE;

--
-- Tablo kısıtlamaları `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_cart_id_foreign` FOREIGN KEY (`cart_id`) REFERENCES `carts` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `orders_shop_id_foreign` FOREIGN KEY (`shop_id`) REFERENCES `shops` (`id`) ON DELETE CASCADE;

--
-- Tablo kısıtlamaları `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `products_shop_id_foreign` FOREIGN KEY (`shop_id`) REFERENCES `shops` (`id`) ON DELETE CASCADE;

--
-- Tablo kısıtlamaları `shops`
--
ALTER TABLE `shops`
  ADD CONSTRAINT `shops_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
