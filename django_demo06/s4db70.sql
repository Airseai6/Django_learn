-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: s4db70
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app01_usergroup`
--

DROP TABLE IF EXISTS `app01_usergroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app01_usergroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_usergroup`
--

LOCK TABLES `app01_usergroup` WRITE;
/*!40000 ALTER TABLE `app01_usergroup` DISABLE KEYS */;
INSERT INTO `app01_usergroup` VALUES (1,'销售部'),(2,'公关部');
/*!40000 ALTER TABLE `app01_usergroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_userinfo`
--

DROP TABLE IF EXISTS `app01_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app01_userinfo` (
  `nid` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  `age` int(11) NOT NULL,
  `ug_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `app01_userinfo_ug_id_e02988bd_fk_app01_usergroup_id` (`ug_id`),
  CONSTRAINT `app01_userinfo_ug_id_e02988bd_fk_app01_usergroup_id` FOREIGN KEY (`ug_id`) REFERENCES `app01_usergroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=304 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_userinfo`
--

LOCK TABLES `app01_userinfo` WRITE;
/*!40000 ALTER TABLE `app01_userinfo` DISABLE KEYS */;
INSERT INTO `app01_userinfo` VALUES (1,'root','123',1,NULL),(2,'root','pwd',18,1),(3,'root','pwd',18,1),(4,'root0','pwd',18,1),(5,'root1','pwd',18,1),(6,'root2','pwd',18,1),(7,'root3','pwd',18,1),(8,'root4','pwd',18,1),(9,'root5','pwd',18,1),(10,'root6','pwd',18,1),(11,'root7','pwd',18,1),(12,'root8','pwd',18,1),(13,'root9','pwd',18,1),(14,'root10','pwd',18,1),(15,'root11','pwd',18,1),(16,'root12','pwd',18,1),(17,'root13','pwd',18,1),(18,'root14','pwd',18,1),(19,'root15','pwd',18,1),(20,'root16','pwd',18,1),(21,'root17','pwd',18,1),(22,'root18','pwd',18,1),(23,'root19','pwd',18,1),(24,'root20','pwd',18,1),(25,'root21','pwd',18,1),(26,'root22','pwd',18,1),(27,'root23','pwd',18,1),(28,'root24','pwd',18,1),(29,'root25','pwd',18,1),(30,'root26','pwd',18,1),(31,'root27','pwd',18,1),(32,'root28','pwd',18,1),(33,'root29','pwd',18,1),(34,'root30','pwd',18,1),(35,'root31','pwd',18,1),(36,'root32','pwd',18,1),(37,'root33','pwd',18,1),(38,'root34','pwd',18,1),(39,'root35','pwd',18,1),(40,'root36','pwd',18,1),(41,'root37','pwd',18,1),(42,'root38','pwd',18,1),(43,'root39','pwd',18,1),(44,'root40','pwd',18,1),(45,'root41','pwd',18,1),(46,'root42','pwd',18,1),(47,'root43','pwd',18,1),(48,'root44','pwd',18,1),(49,'root45','pwd',18,1),(50,'root46','pwd',18,1),(51,'root47','pwd',18,1),(52,'root48','pwd',18,1),(53,'root49','pwd',18,1),(54,'root50','pwd',18,1),(55,'root51','pwd',18,1),(56,'root52','pwd',18,1),(57,'root53','pwd',18,1),(58,'root54','pwd',18,1),(59,'root55','pwd',18,1),(60,'root56','pwd',18,1),(61,'root57','pwd',18,1),(62,'root58','pwd',18,1),(63,'root59','pwd',18,1),(64,'root60','pwd',18,1),(65,'root61','pwd',18,1),(66,'root62','pwd',18,1),(67,'root63','pwd',18,1),(68,'root64','pwd',18,1),(69,'root65','pwd',18,1),(70,'root66','pwd',18,1),(71,'root67','pwd',18,1),(72,'root68','pwd',18,1),(73,'root69','pwd',18,1),(74,'root70','pwd',18,1),(75,'root71','pwd',18,1),(76,'root72','pwd',18,1),(77,'root73','pwd',18,1),(78,'root74','pwd',18,1),(79,'root75','pwd',18,1),(80,'root76','pwd',18,1),(81,'root77','pwd',18,1),(82,'root78','pwd',18,1),(83,'root79','pwd',18,1),(84,'root80','pwd',18,1),(85,'root81','pwd',18,1),(86,'root82','pwd',18,1),(87,'root83','pwd',18,1),(88,'root84','pwd',18,1),(89,'root85','pwd',18,1),(90,'root86','pwd',18,1),(91,'root87','pwd',18,1),(92,'root88','pwd',18,1),(93,'root89','pwd',18,1),(94,'root90','pwd',18,1),(95,'root91','pwd',18,1),(96,'root92','pwd',18,1),(97,'root93','pwd',18,1),(98,'root94','pwd',18,1),(99,'root95','pwd',18,1),(100,'root96','pwd',18,1),(101,'root97','pwd',18,1),(102,'root98','pwd',18,1),(103,'root99','pwd',18,1),(104,'root100','pwd',18,1),(105,'root101','pwd',18,1),(106,'root102','pwd',18,1),(107,'root103','pwd',18,1),(108,'root104','pwd',18,1),(109,'root105','pwd',18,1),(110,'root106','pwd',18,1),(111,'root107','pwd',18,1),(112,'root108','pwd',18,1),(113,'root109','pwd',18,1),(114,'root110','pwd',18,1),(115,'root111','pwd',18,1),(116,'root112','pwd',18,1),(117,'root113','pwd',18,1),(118,'root114','pwd',18,1),(119,'root115','pwd',18,1),(120,'root116','pwd',18,1),(121,'root117','pwd',18,1),(122,'root118','pwd',18,1),(123,'root119','pwd',18,1),(124,'root120','pwd',18,1),(125,'root121','pwd',18,1),(126,'root122','pwd',18,1),(127,'root123','pwd',18,1),(128,'root124','pwd',18,1),(129,'root125','pwd',18,1),(130,'root126','pwd',18,1),(131,'root127','pwd',18,1),(132,'root128','pwd',18,1),(133,'root129','pwd',18,1),(134,'root130','pwd',18,1),(135,'root131','pwd',18,1),(136,'root132','pwd',18,1),(137,'root133','pwd',18,1),(138,'root134','pwd',18,1),(139,'root135','pwd',18,1),(140,'root136','pwd',18,1),(141,'root137','pwd',18,1),(142,'root138','pwd',18,1),(143,'root139','pwd',18,1),(144,'root140','pwd',18,1),(145,'root141','pwd',18,1),(146,'root142','pwd',18,1),(147,'root143','pwd',18,1),(148,'root144','pwd',18,1),(149,'root145','pwd',18,1),(150,'root146','pwd',18,1),(151,'root147','pwd',18,1),(152,'root148','pwd',18,1),(153,'root149','pwd',18,1),(154,'root150','pwd',18,1),(155,'root151','pwd',18,1),(156,'root152','pwd',18,1),(157,'root153','pwd',18,1),(158,'root154','pwd',18,1),(159,'root155','pwd',18,1),(160,'root156','pwd',18,1),(161,'root157','pwd',18,1),(162,'root158','pwd',18,1),(163,'root159','pwd',18,1),(164,'root160','pwd',18,1),(165,'root161','pwd',18,1),(166,'root162','pwd',18,1),(167,'root163','pwd',18,1),(168,'root164','pwd',18,1),(169,'root165','pwd',18,1),(170,'root166','pwd',18,1),(171,'root167','pwd',18,1),(172,'root168','pwd',18,1),(173,'root169','pwd',18,1),(174,'root170','pwd',18,1),(175,'root171','pwd',18,1),(176,'root172','pwd',18,1),(177,'root173','pwd',18,1),(178,'root174','pwd',18,1),(179,'root175','pwd',18,1),(180,'root176','pwd',18,1),(181,'root177','pwd',18,1),(182,'root178','pwd',18,1),(183,'root179','pwd',18,1),(184,'root180','pwd',18,1),(185,'root181','pwd',18,1),(186,'root182','pwd',18,1),(187,'root183','pwd',18,1),(188,'root184','pwd',18,1),(189,'root185','pwd',18,1),(190,'root186','pwd',18,1),(191,'root187','pwd',18,1),(192,'root188','pwd',18,1),(193,'root189','pwd',18,1),(194,'root190','pwd',18,1),(195,'root191','pwd',18,1),(196,'root192','pwd',18,1),(197,'root193','pwd',18,1),(198,'root194','pwd',18,1),(199,'root195','pwd',18,1),(200,'root196','pwd',18,1),(201,'root197','pwd',18,1),(202,'root198','pwd',18,1),(203,'root199','pwd',18,1),(204,'root200','pwd',18,1),(205,'root201','pwd',18,1),(206,'root202','pwd',18,1),(207,'root203','pwd',18,1),(208,'root204','pwd',18,1),(209,'root205','pwd',18,1),(210,'root206','pwd',18,1),(211,'root207','pwd',18,1),(212,'root208','pwd',18,1),(213,'root209','pwd',18,1),(214,'root210','pwd',18,1),(215,'root211','pwd',18,1),(216,'root212','pwd',18,1),(217,'root213','pwd',18,1),(218,'root214','pwd',18,1),(219,'root215','pwd',18,1),(220,'root216','pwd',18,1),(221,'root217','pwd',18,1),(222,'root218','pwd',18,1),(223,'root219','pwd',18,1),(224,'root220','pwd',18,1),(225,'root221','pwd',18,1),(226,'root222','pwd',18,1),(227,'root223','pwd',18,1),(228,'root224','pwd',18,1),(229,'root225','pwd',18,1),(230,'root226','pwd',18,1),(231,'root227','pwd',18,1),(232,'root228','pwd',18,1),(233,'root229','pwd',18,1),(234,'root230','pwd',18,1),(235,'root231','pwd',18,1),(236,'root232','pwd',18,1),(237,'root233','pwd',18,1),(238,'root234','pwd',18,1),(239,'root235','pwd',18,1),(240,'root236','pwd',18,1),(241,'root237','pwd',18,1),(242,'root238','pwd',18,1),(243,'root239','pwd',18,1),(244,'root240','pwd',18,1),(245,'root241','pwd',18,1),(246,'root242','pwd',18,1),(247,'root243','pwd',18,1),(248,'root244','pwd',18,1),(249,'root245','pwd',18,1),(250,'root246','pwd',18,1),(251,'root247','pwd',18,1),(252,'root248','pwd',18,1),(253,'root249','pwd',18,1),(254,'root250','pwd',18,1),(255,'root251','pwd',18,1),(256,'root252','pwd',18,1),(257,'root253','pwd',18,1),(258,'root254','pwd',18,1),(259,'root255','pwd',18,1),(260,'root256','pwd',18,1),(261,'root257','pwd',18,1),(262,'root258','pwd',18,1),(263,'root259','pwd',18,1),(264,'root260','pwd',18,1),(265,'root261','pwd',18,1),(266,'root262','pwd',18,1),(267,'root263','pwd',18,1),(268,'root264','pwd',18,1),(269,'root265','pwd',18,1),(270,'root266','pwd',18,1),(271,'root267','pwd',18,1),(272,'root268','pwd',18,1),(273,'root269','pwd',18,1),(274,'root270','pwd',18,1),(275,'root271','pwd',18,1),(276,'root272','pwd',18,1),(277,'root273','pwd',18,1),(278,'root274','pwd',18,1),(279,'root275','pwd',18,1),(280,'root276','pwd',18,1),(281,'root277','pwd',18,1),(282,'root278','pwd',18,1),(283,'root279','pwd',18,1),(284,'root280','pwd',18,1),(285,'root281','pwd',18,1),(286,'root282','pwd',18,1),(287,'root283','pwd',18,1),(288,'root284','pwd',18,1),(289,'root285','pwd',18,1),(290,'root286','pwd',18,1),(291,'root287','pwd',18,1),(292,'root288','pwd',18,1),(293,'root289','pwd',18,1),(294,'root290','pwd',18,1),(295,'root291','pwd',18,1),(296,'root292','pwd',18,1),(297,'root293','pwd',18,1),(298,'root294','pwd',18,1),(299,'root295','pwd',18,1),(300,'root296','pwd',18,1),(301,'root297','pwd',18,1),(302,'root298','pwd',18,1),(303,'root299','pwd',18,1);
/*!40000 ALTER TABLE `app01_userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user info',7,'add_userinfo'),(26,'Can change user info',7,'change_userinfo'),(27,'Can delete user info',7,'delete_userinfo'),(28,'Can view user info',7,'view_userinfo'),(29,'Can add user group',8,'add_usergroup'),(30,'Can change user group',8,'change_usergroup'),(31,'Can delete user group',8,'delete_usergroup'),(32,'Can view user group',8,'view_usergroup');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(8,'app01','usergroup'),(7,'app01','userinfo'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-01-15 01:12:47.139747'),(2,'auth','0001_initial','2020-01-15 01:12:47.354177'),(3,'admin','0001_initial','2020-01-15 01:12:48.138116'),(4,'admin','0002_logentry_remove_auto_add','2020-01-15 01:12:48.331125'),(5,'admin','0003_logentry_add_action_flag_choices','2020-01-15 01:12:48.340215'),(6,'app01','0001_initial','2020-01-15 01:12:48.374604'),(7,'contenttypes','0002_remove_content_type_name','2020-01-15 01:12:48.540957'),(8,'auth','0002_alter_permission_name_max_length','2020-01-15 01:12:48.623186'),(9,'auth','0003_alter_user_email_max_length','2020-01-15 01:12:48.718056'),(10,'auth','0004_alter_user_username_opts','2020-01-15 01:12:48.727935'),(11,'auth','0005_alter_user_last_login_null','2020-01-15 01:12:48.810986'),(12,'auth','0006_require_contenttypes_0002','2020-01-15 01:12:48.815973'),(13,'auth','0007_alter_validators_add_error_messages','2020-01-15 01:12:48.824949'),(14,'auth','0008_alter_user_username_max_length','2020-01-15 01:12:48.917043'),(15,'auth','0009_alter_user_last_name_max_length','2020-01-15 01:12:49.011175'),(16,'auth','0010_alter_group_name_max_length','2020-01-15 01:12:49.093053'),(17,'auth','0011_update_proxy_permissions','2020-01-15 01:12:49.103244'),(18,'sessions','0001_initial','2020-01-15 01:12:49.166415'),(19,'app01','0002_userinfo_age','2020-01-15 01:25:12.572561'),(20,'app01','0003_usergroup','2020-01-15 01:29:24.288942'),(21,'app01','0004_userinfo_ug','2020-01-15 01:43:53.373815');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-15 19:56:54
