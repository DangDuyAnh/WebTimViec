-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.6.7-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for jobsite-db
CREATE DATABASE IF NOT EXISTS `jobsite-db` /*!40100 DEFAULT CHARACTER SET utf16 COLLATE utf16_unicode_ci */;
USE `jobsite-db`;

-- Dumping structure for table jobsite-db.account_emailaddress
CREATE TABLE IF NOT EXISTS `account_emailaddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) COLLATE utf16_unicode_ci NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `account_emailaddress_user_id_2c513194_fk_auth_user_id` (`user_id`),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.account_emailaddress: ~0 rows (approximately)
/*!40000 ALTER TABLE `account_emailaddress` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailaddress` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.account_emailconfirmation
CREATE TABLE IF NOT EXISTS `account_emailconfirmation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) COLLATE utf16_unicode_ci NOT NULL,
  `email_address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`),
  KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`),
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.account_emailconfirmation: ~0 rows (approximately)
/*!40000 ALTER TABLE `account_emailconfirmation` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailconfirmation` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.auth_group: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.auth_group_permissions: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf16_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.auth_permission: ~44 rows (approximately)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add email address', 7, 'add_emailaddress'),
	(26, 'Can change email address', 7, 'change_emailaddress'),
	(27, 'Can delete email address', 7, 'delete_emailaddress'),
	(28, 'Can view email address', 7, 'view_emailaddress'),
	(29, 'Can add email confirmation', 8, 'add_emailconfirmation'),
	(30, 'Can change email confirmation', 8, 'change_emailconfirmation'),
	(31, 'Can delete email confirmation', 8, 'delete_emailconfirmation'),
	(32, 'Can view email confirmation', 8, 'view_emailconfirmation'),
	(33, 'Can add social account', 9, 'add_socialaccount'),
	(34, 'Can change social account', 9, 'change_socialaccount'),
	(35, 'Can delete social account', 9, 'delete_socialaccount'),
	(36, 'Can view social account', 9, 'view_socialaccount'),
	(37, 'Can add social application', 10, 'add_socialapp'),
	(38, 'Can change social application', 10, 'change_socialapp'),
	(39, 'Can delete social application', 10, 'delete_socialapp'),
	(40, 'Can view social application', 10, 'view_socialapp'),
	(41, 'Can add social application token', 11, 'add_socialtoken'),
	(42, 'Can change social application token', 11, 'change_socialtoken'),
	(43, 'Can delete social application token', 11, 'delete_socialtoken'),
	(44, 'Can view social application token', 11, 'view_socialtoken');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf16_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf16_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf16_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf16_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf16_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.auth_user: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$320000$SFmZUpsi4sJXRIDMXa0HpM$mjYBEBfzaYtx2z2I02sxOnkjnaZ6sMjLCwsVBkRVAV4=', NULL, 1, 'admin', '', '', '', 1, 1, '2022-06-12 14:09:27.956928');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.auth_user_groups: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.auth_user_user_permissions: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.chat_room
CREATE TABLE IF NOT EXISTS `chat_room` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.chat_room: ~2 rows (approximately)
/*!40000 ALTER TABLE `chat_room` DISABLE KEYS */;
INSERT INTO `chat_room` (`ID`, `name`) VALUES
	(1, 'user_1_to_user_2'),
	(2, 'user_1_to_user_3');
/*!40000 ALTER TABLE `chat_room` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.chat_room_conversation
CREATE TABLE IF NOT EXISTS `chat_room_conversation` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `sender_user_id` bigint(20) unsigned NOT NULL DEFAULT 0,
  `room_id` bigint(20) unsigned NOT NULL DEFAULT 0,
  `text` varchar(2048) COLLATE utf16_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_chat_room_conversation_chat_room_user` (`sender_user_id`,`room_id`),
  CONSTRAINT `FK_chat_room_conversation_chat_room_user` FOREIGN KEY (`sender_user_id`, `room_id`) REFERENCES `chat_room_user` (`user_id`, `room_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.chat_room_conversation: ~6 rows (approximately)
/*!40000 ALTER TABLE `chat_room_conversation` DISABLE KEYS */;
INSERT INTO `chat_room_conversation` (`ID`, `sender_user_id`, `room_id`, `text`) VALUES
	(1, 4, 1, 'Hello, World!'),
	(2, 4, 1, 'Xin chào!'),
	(3, 6, 1, 'Chào lại!'),
	(8, 6, 1, 'Hahaha =)))'),
	(9, 4, 1, 'Hello, World from Postman!'),
	(10, 4, 1, 'Hello, World from Postman 2!');
/*!40000 ALTER TABLE `chat_room_conversation` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.chat_room_user
CREATE TABLE IF NOT EXISTS `chat_room_user` (
  `user_id` bigint(20) unsigned NOT NULL,
  `room_id` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`user_id`,`room_id`),
  KEY `FK__chat_room__chat_room` (`room_id`),
  CONSTRAINT `FK__chat_room__chat_room` FOREIGN KEY (`room_id`) REFERENCES `chat_room` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK__chat_room__user` FOREIGN KEY (`user_id`) REFERENCES `user` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.chat_room_user: ~2 rows (approximately)
/*!40000 ALTER TABLE `chat_room_user` DISABLE KEYS */;
INSERT INTO `chat_room_user` (`user_id`, `room_id`) VALUES
	(4, 1),
	(6, 1);
/*!40000 ALTER TABLE `chat_room_user` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.company
CREATE TABLE IF NOT EXISTS `company` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `address` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `province_id` bigint(20) unsigned NOT NULL,
  `desc` varchar(256) COLLATE utf16_unicode_ci NOT NULL,
  `status` tinyint(4) NOT NULL DEFAULT 0 COMMENT '0 - wait, 1 - accept, 2 - reject',
  PRIMARY KEY (`ID`),
  KEY `FK_company_province` (`province_id`) USING BTREE,
  CONSTRAINT `FK_company_province` FOREIGN KEY (`province_id`) REFERENCES `province` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.company: ~4 rows (approximately)
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` (`ID`, `name`, `address`, `province_id`, `desc`, `status`) VALUES
	(1, 'Công ty 1', 'số 1 ngõ Độc Lập, đường Tự Do, quận Hạnh Phúc', 1, 'công ty test 1', 1),
	(2, 'Công ty 2', 'Thiên Đàng', 2, 'công ty test 2', 1),
	(3, 'Công ty 3', 'Địa Ngục', 1, 'công ty test 3', 1);
/*!40000 ALTER TABLE `company` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf16_unicode_ci DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf16_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext COLLATE utf16_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.django_admin_log: ~0 rows (approximately)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.django_content_type: ~11 rows (approximately)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(7, 'account', 'emailaddress'),
	(8, 'account', 'emailconfirmation'),
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(6, 'sessions', 'session'),
	(9, 'socialaccount', 'socialaccount'),
	(10, 'socialaccount', 'socialapp'),
	(11, 'socialaccount', 'socialtoken');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf16_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf16_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.django_migrations: ~20 rows (approximately)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2022-06-12 13:59:43.595798'),
	(2, 'auth', '0001_initial', '2022-06-12 13:59:51.917520'),
	(3, 'account', '0001_initial', '2022-06-12 13:59:53.782131'),
	(4, 'account', '0002_email_max_length', '2022-06-12 13:59:54.157836'),
	(5, 'admin', '0001_initial', '2022-06-12 13:59:55.790588'),
	(6, 'admin', '0002_logentry_remove_auto_add', '2022-06-12 13:59:55.822140'),
	(7, 'admin', '0003_logentry_add_action_flag_choices', '2022-06-12 13:59:55.868342'),
	(8, 'contenttypes', '0002_remove_content_type_name', '2022-06-12 13:59:56.841412'),
	(9, 'auth', '0002_alter_permission_name_max_length', '2022-06-12 13:59:57.580695'),
	(10, 'auth', '0003_alter_user_email_max_length', '2022-06-12 13:59:57.940068'),
	(11, 'auth', '0004_alter_user_username_opts', '2022-06-12 13:59:57.971320'),
	(12, 'auth', '0005_alter_user_last_login_null', '2022-06-12 13:59:58.551126'),
	(13, 'auth', '0006_require_contenttypes_0002', '2022-06-12 13:59:58.597300'),
	(14, 'auth', '0007_alter_validators_add_error_messages', '2022-06-12 13:59:58.629267'),
	(15, 'auth', '0008_alter_user_username_max_length', '2022-06-12 13:59:58.975593'),
	(16, 'auth', '0009_alter_user_last_name_max_length', '2022-06-12 13:59:59.334967'),
	(17, 'auth', '0010_alter_group_name_max_length', '2022-06-12 13:59:59.682042'),
	(18, 'auth', '0011_update_proxy_permissions', '2022-06-12 13:59:59.728202'),
	(19, 'auth', '0012_alter_user_first_name_max_length', '2022-06-12 14:00:00.072663'),
	(20, 'sessions', '0001_initial', '2022-06-12 14:00:00.856523'),
	(21, 'socialaccount', '0001_initial', '2022-06-12 14:00:04.567290'),
	(22, 'socialaccount', '0002_token_max_lengths', '2022-06-12 14:00:05.650469'),
	(23, 'socialaccount', '0003_extra_data_default_dict', '2022-06-12 14:00:05.682429');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf16_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf16_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.django_session: ~0 rows (approximately)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.employee
CREATE TABLE IF NOT EXISTS `employee` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `gender` varchar(16) COLLATE utf16_unicode_ci DEFAULT NULL,
  `image_link` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `literacy` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `specialist_knowledge` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `experience` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `main_cv_id` bigint(20) DEFAULT NULL,
  `main_letter_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  KEY `FK_employee_user` (`user_id`),
  CONSTRAINT `FK_employee_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.employee: ~2 rows (approximately)
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` (`ID`, `user_id`, `date_of_birth`, `gender`, `image_link`, `literacy`, `specialist_knowledge`, `experience`, `main_cv_id`, `main_letter_id`) VALUES
	(1, 4, '2022-06-28 10:17:09', 'male', 'image/test1.png', '12/12', 'nothing', '0 years', 0, 0),
	(2, 6, '2022-06-28 10:18:50', 'female', 'image/test2.png', '1/12', 'smile', '100 years', 0, 0);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.employee_applied_job
CREATE TABLE IF NOT EXISTS `employee_applied_job` (
  `employee_id` bigint(20) unsigned NOT NULL,
  `job_id` bigint(20) unsigned NOT NULL,
  `status` tinyint(3) unsigned NOT NULL DEFAULT 0 COMMENT '0 - waiting, 1 - accepted, 2 - rejeccted',
  PRIMARY KEY (`employee_id`,`job_id`),
  KEY `FK__employee_job__job_id` (`job_id`),
  CONSTRAINT `FK__employee_job__employee_id` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK__employee_job__job_id` FOREIGN KEY (`job_id`) REFERENCES `job` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.employee_applied_job: ~2 rows (approximately)
/*!40000 ALTER TABLE `employee_applied_job` DISABLE KEYS */;
INSERT INTO `employee_applied_job` (`employee_id`, `job_id`, `status`) VALUES
	(1, 2, 1),
	(2, 2, 0);
/*!40000 ALTER TABLE `employee_applied_job` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.employee_cv
CREATE TABLE IF NOT EXISTS `employee_cv` (
  `employee_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `cv_id` int(11) NOT NULL,
  PRIMARY KEY (`employee_id`,`cv_id`),
  CONSTRAINT `FK__employee_cv__employee` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.employee_cv: ~0 rows (approximately)
/*!40000 ALTER TABLE `employee_cv` DISABLE KEYS */;
INSERT INTO `employee_cv` (`employee_id`, `cv_id`) VALUES
	(1, 1);
/*!40000 ALTER TABLE `employee_cv` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.employee_letter
CREATE TABLE IF NOT EXISTS `employee_letter` (
  `employee_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `letter_id` bigint(20) unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`employee_id`,`letter_id`) USING BTREE,
  CONSTRAINT `FK__employee_letter_cv__employee` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.employee_letter: ~0 rows (approximately)
/*!40000 ALTER TABLE `employee_letter` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_letter` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.employee_saved_job
CREATE TABLE IF NOT EXISTS `employee_saved_job` (
  `employee_id` bigint(20) unsigned NOT NULL,
  `job_id` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`employee_id`,`job_id`),
  KEY `FK__employee_saved_job__job_id` (`job_id`),
  CONSTRAINT `FK__employee_saved_job__employee_id` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK__employee_saved_job__job_id` FOREIGN KEY (`job_id`) REFERENCES `job` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.employee_saved_job: ~0 rows (approximately)
/*!40000 ALTER TABLE `employee_saved_job` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_saved_job` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.employer
CREATE TABLE IF NOT EXISTS `employer` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `company_id` bigint(20) unsigned NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` varchar(16) COLLATE utf16_unicode_ci DEFAULT NULL,
  `image_link` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `status` tinyint(3) unsigned NOT NULL DEFAULT 0 COMMENT '0 - wait, 1 - accepted, 2 - rejected',
  PRIMARY KEY (`ID`),
  KEY `FK__employer__user` (`user_id`),
  KEY `FK_employer_company` (`company_id`),
  CONSTRAINT `FK__employer__user` FOREIGN KEY (`user_id`) REFERENCES `user` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_employer_company` FOREIGN KEY (`company_id`) REFERENCES `company` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.employer: ~1 rows (approximately)
/*!40000 ALTER TABLE `employer` DISABLE KEYS */;
INSERT INTO `employer` (`ID`, `user_id`, `company_id`, `date_of_birth`, `gender`, `image_link`, `status`) VALUES
	(1, 4, 1, '2000-11-10', 'male', 'images/test1.png', 1),
	(2, 6, 3, '2002-06-28', 'female', 'images/test1.png', 1);
/*!40000 ALTER TABLE `employer` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.job
CREATE TABLE IF NOT EXISTS `job` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) unsigned NOT NULL DEFAULT 0,
  `title` varchar(128) COLLATE utf16_unicode_ci DEFAULT NULL,
  `public_date` date DEFAULT NULL,
  `expired_date` date DEFAULT NULL,
  `field` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `salary_min` bigint(20) unsigned DEFAULT NULL,
  `salary_max` bigint(20) unsigned DEFAULT NULL,
  `position` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `type` varchar(32) COLLATE utf16_unicode_ci DEFAULT NULL,
  `required_experience` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `avaiable_slot` int(10) unsigned DEFAULT NULL,
  `accepted_applicant` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK__job__company` (`company_id`),
  CONSTRAINT `FK__job__company` FOREIGN KEY (`company_id`) REFERENCES `company` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.job: ~1 rows (approximately)
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
INSERT INTO `job` (`ID`, `company_id`, `title`, `public_date`, `expired_date`, `field`, `salary_min`, `salary_max`, `position`, `type`, `required_experience`, `avaiable_slot`, `accepted_applicant`) VALUES
	(2, 1, 'ăn, ngủ', '2022-06-28', '2095-06-28', 'IT', 1000, 1000000, 'CEO', 'remote, ofline', '30 years', 1, 0),
	(3, 2, 'vẽ', '2022-06-28', '2029-06-28', 'ART', 10000, 100000, 'Artist', 'remote', '15 years', 100, 30),
	(4, 1, 'cười', '2022-06-29', '2025-06-29', 'IT', 1000, 100000, 'Director', 'remote', '1000 working years + 12 learing years', 1000, 0);
/*!40000 ALTER TABLE `job` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.province
CREATE TABLE IF NOT EXISTS `province` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf16_unicode_ci NOT NULL,
  `area_code` int(10) unsigned NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.province: ~0 rows (approximately)
/*!40000 ALTER TABLE `province` DISABLE KEYS */;
INSERT INTO `province` (`ID`, `name`, `area_code`) VALUES
	(1, 'Hà Nội', 24),
	(2, 'Hồ Chí Minh', 28);
/*!40000 ALTER TABLE `province` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.socialaccount_socialaccount
CREATE TABLE IF NOT EXISTS `socialaccount_socialaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) COLLATE utf16_unicode_ci NOT NULL,
  `uid` varchar(191) COLLATE utf16_unicode_ci NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext COLLATE utf16_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  KEY `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.socialaccount_socialaccount: ~0 rows (approximately)
/*!40000 ALTER TABLE `socialaccount_socialaccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialaccount` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.socialaccount_socialapp
CREATE TABLE IF NOT EXISTS `socialaccount_socialapp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) COLLATE utf16_unicode_ci NOT NULL,
  `name` varchar(40) COLLATE utf16_unicode_ci NOT NULL,
  `client_id` varchar(191) COLLATE utf16_unicode_ci NOT NULL,
  `secret` varchar(191) COLLATE utf16_unicode_ci NOT NULL,
  `key` varchar(191) COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.socialaccount_socialapp: ~0 rows (approximately)
/*!40000 ALTER TABLE `socialaccount_socialapp` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialapp` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.socialaccount_socialtoken
CREATE TABLE IF NOT EXISTS `socialaccount_socialtoken` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` longtext COLLATE utf16_unicode_ci NOT NULL,
  `token_secret` longtext COLLATE utf16_unicode_ci NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `app_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`),
  CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.socialaccount_socialtoken: ~0 rows (approximately)
/*!40000 ALTER TABLE `socialaccount_socialtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialtoken` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.user
CREATE TABLE IF NOT EXISTS `user` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `password` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `first_name` varchar(128) COLLATE utf16_unicode_ci DEFAULT NULL,
  `last_name` varchar(128) COLLATE utf16_unicode_ci DEFAULT NULL,
  `social_account` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `social_account_id` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `social_auth_iss` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  `joined_date` datetime DEFAULT NULL,
  `token` longtext COLLATE utf16_unicode_ci DEFAULT NULL,
  `token_expires` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.user: ~1 rows (approximately)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`ID`, `username`, `password`, `first_name`, `last_name`, `social_account`, `social_account_id`, `social_auth_iss`, `joined_date`, `token`, `token_expires`) VALUES
	(4, 'Nguyễn Hữu Kiệt', '28d3cf225a817ef98f79e87f85eca91080e6f77b41c21b342511bbee930f6600d65b598e61bdea4a40e5679f9f01713705b9998fb9fc813b29eabfcfea3a922406b708ddf3ed64ab74e84c0db156883b9870a5ab2d44470062182afad9f140ce3aa16762f4c3627ea6e2f174e8e0da82d9c9845642541f6f062d620ad85c78b2', 'Kiệt', 'Nguyễn Hữu', 'kietnguyen10112000@gmail.com', '114594750559756865595', 'https://accounts.google.com', '2022-06-13 21:13:15', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJleHAiOjE2NTY2NjU0NjEsImlhdCI6MTY1NjU3OTA2MX0.sOXdDU9SELPHP4umIoONkvUoCf7qdrS0KM3s4SDD7qE', '2022-07-01 08:51:01'),
	(6, 'tha_thu', 'c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646', NULL, NULL, 'haahha@gmail.com', NULL, NULL, '2022-06-20 22:36:26', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJleHAiOjE2NTY1MTI1NzIsImlhdCI6MTY1NjQyNjE3Mn0.CnECmy_WXY051FEnIk94CbrDtTIyZHvW_McKHQBBQyA', '2022-06-29 14:22:52'),
	(7, 'tha_thu2', 'c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646', NULL, NULL, 'haahha@gmail.com', NULL, NULL, '2022-06-27 21:23:33', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo3LCJleHAiOjE2NTY0MjYyMTMsImlhdCI6MTY1NjMzOTgxM30.geoSPnfSqrqJpxAJfFRi2ierOnjmbbUFlZ9SC0dCKZI', '2022-06-28 14:23:33');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.user_role
CREATE TABLE IF NOT EXISTS `user_role` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf16_unicode_ci DEFAULT NULL,
  `desc` varchar(256) COLLATE utf16_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.user_role: ~3 rows (approximately)
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` (`ID`, `name`, `desc`) VALUES
	(1, 'admin', 'full quyền'),
	(2, 'employer', 'employer desc'),
	(3, 'employee', 'employee desc');
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;

-- Dumping structure for table jobsite-db.user_role_relationship
CREATE TABLE IF NOT EXISTS `user_role_relationship` (
  `user_id` bigint(20) unsigned NOT NULL,
  `user_role` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`user_id`,`user_role`),
  KEY `FK__user_role_relationship__user_role` (`user_role`),
  CONSTRAINT `FK__user_role_relationship__user` FOREIGN KEY (`user_id`) REFERENCES `user` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK__user_role_relationship__user_role` FOREIGN KEY (`user_role`) REFERENCES `user_role` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- Dumping data for table jobsite-db.user_role_relationship: ~2 rows (approximately)
/*!40000 ALTER TABLE `user_role_relationship` DISABLE KEYS */;
INSERT INTO `user_role_relationship` (`user_id`, `user_role`) VALUES
	(4, 1),
	(4, 2);
/*!40000 ALTER TABLE `user_role_relationship` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
