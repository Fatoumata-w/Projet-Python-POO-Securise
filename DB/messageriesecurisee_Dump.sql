-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: messageriesecurisee
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `conversationparticipants`
--

DROP TABLE IF EXISTS `conversationparticipants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conversationparticipants` (
  `conversationId` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  PRIMARY KEY (`conversationId`,`userId`),
  KEY `userId` (`userId`),
  CONSTRAINT `conversationparticipants_ibfk_1` FOREIGN KEY (`conversationId`) REFERENCES `conversations` (`ConversationId`),
  CONSTRAINT `conversationparticipants_ibfk_2` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conversationparticipants`
--

/*!40000 ALTER TABLE `conversationparticipants` DISABLE KEYS */;
INSERT INTO `conversationparticipants` VALUES (14,20),(14,21),(15,22),(15,23),(16,23),(16,24),(17,20),(17,24),(18,20),(18,22),(19,21),(19,22);
/*!40000 ALTER TABLE `conversationparticipants` ENABLE KEYS */;

--
-- Table structure for table `conversations`
--

DROP TABLE IF EXISTS `conversations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conversations` (
  `ConversationId` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`ConversationId`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conversations`
--

/*!40000 ALTER TABLE `conversations` DISABLE KEYS */;
INSERT INTO `conversations` VALUES (14,'2026-04-27 21:18:11'),(15,'2026-04-28 20:30:29'),(16,'2026-04-28 20:34:04'),(17,'2026-04-28 20:44:39'),(18,'2026-04-28 20:49:35'),(19,'2026-04-28 20:58:00');
/*!40000 ALTER TABLE `conversations` ENABLE KEYS */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `messageId` int(11) NOT NULL AUTO_INCREMENT,
  `conversationId` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL,
  `state` tinyint(1) NOT NULL DEFAULT 0,
  `envoyeurContent` text NOT NULL,
  PRIMARY KEY (`messageId`),
  KEY `conversationId` (`conversationId`),
  KEY `userId` (`userId`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`conversationId`) REFERENCES `conversations` (`ConversationId`),
  CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (13,14,21,'Z2HfJEAsUSozTxWVhhMffck3UEs5Y4W3vK5DFC7s0g+gHM910GsLO7xAgdjeJwHZRJ3akooDB3OXKVa4pjzNKbVQXVFdXxe4eAPP3hniiUrAjkkPpM62p0Ll3c1sp3BDWpI1HpIV4nLQwuHls3tUUFm/xI3BI+gYwge0hjcAThNBNv7v1iAYp2vAKhNzvtXi/ZnH4DaTRy5QAP0a4gYS839tNWMylwydBwv0n6GBvWtnwRY3MnpH2aOfGHH5J+afbYEN1g9hHSSAsApNPgAUKvRnFkux/pHEAT+BRW+gaBtpw9OQ9PZCrATjr5oExiNFDR1rZFI6S3y7V3D4M9ooGg==','2026-04-27 21:23:30',0,'hGHzNnLo4ShVdn7b/Y6QslY24c9zC0s06IhwSRHyfEyjd4kF5hnuGaRM30ZHVT8mU/Qgv5Ef/9gT66KIN/hBsLpMGIaYludj+AMIk/TxcgBBKlSZ6GT2GE6VIG+w0bSDgL1GcvnoIn9CaHCjALUYD4zU2hdFMJKVO+80MKz54AUsz9joWENkDjTZ70bMzp15rzIlS/eP3dVtYrfq423COQyjNCmBhXlmKt+afgf0+E9b6AtvhN1nWJUs00oyPmW4As4PpsfCP0dPvriUsk+NZ217JT+E0p1hxRDEJ3SiDPrua+hNIAvTlW8gnOqYt02nmH+Ge9FVPb9AcfmtNXLQ7w=='),(14,14,21,'KW8UbHn/WXaaunNnYirDVgJjGHwe/5F7ff0c6CmnAfL7MFPscVuz19UAfIKU+uyl6RkI65+xDp4RM1YLaW3p8FPfH46B+HLMiCwlA3uUYyd/LF5HazRt9s+RUsLebH57C6W4zEoYOfz8lKmHy9sXQuSbC8MwxgUtcB7C8R1SacF+icjPYfEi+bXzpkioFz/nfNN/mMmDioOa93C8cQY+QC+MG17QErjIIYcEdBd/vkdO7HM+7iMp8p9h94GdQM+Fc8WzYTHT96JqDSMNo9CDvaPPCO24HaCJ66kcsQhAysgcglAQxjEBzSgpPHAI+KNvnOW4Zekpt7jIeW0Cj4jOPQ==','2026-04-27 21:26:26',0,'v/SLziQy7Ri9YYXQBEkULQ1Ejt5quN6K6SOtjYj6lbZoXBLA3+Qw2NxUFHvuOMuChB1SlfuqoVGDoExewdzi5roSYUAmufmIxQ8edfko8aElfahDWy7yMEc5PHVNsUNis43euRL0Rt4Eos1Ds8ajWWZXuKLZExf+i6rHi7ZHImmvZY7hR9kz3YlhPHTetnY2GI09HrXoJ+MLWgQLQIUJwcdyssp+/0zqtgHnp6sLvqpiBfQgyNHeH5iVE+AA0vxxoPA2pGR7M4g7eh2pQtIJEdQvw90xvgYBSA++7fVCXy0wAIG1sBzpbsgMYt2XECc/7yQ5B91yzobO3aCMR6CmiQ=='),(15,14,20,'i551Ql7XsNfTcNMYJQSYLM8W456F6BVHTfrRbV1CHp4PYlTIxtxxD1bXS2olnbyi2JgW2D9oQsbOGfB6Bga/sBjhWD/k05UQ63ZLVcIBSHwPeQXm7F56ofyFGCmbtV8LRryi/7Pb0iWMvJCA/YCT6NfPiq1GD2CbIcEadzs7FFnXSRTji3yCEy4djod3D4CyBVo7GzZXR4fpE5cFe1McPngYA79k32kTbyT5u+dbeI7qI/6WNRbXGgZqNOc1bjWwfcIJeW0QMRf9wmd3ncoOidn7YPqOvX/v5a4Oo2CndxacNUHUcRyH4cldEjaE1qtVXI+jmhfy99SwTxPCj0Mj1w==','2026-04-27 21:27:11',0,'MafeTt7NDQzRTU6ycF40AKbPK3IF7AsCtsH46KyP5fgftkZCASCCp1qiTwM7VtKtyfaMGvAT/wJ/xnVEHvoJU8S3ZN5k86hsv54eL8igxi0e/vmCwckfFEn9rSYFkG37YJ5VR3+VjmwFs193PCQw9458hWTO6HUyIXqdNG/ZqDuIifBh+m48cQks5QzV9bqv/bFcEJ8qKYDlFQ6iA2Gqzz3X4C1E62+rLxS+R5jnWWVSWd21vcx7SXZYN7QRXuHk9TBtnOjn17kopoimUGxwnRLy4GHwP1mAyByK40p7xEcCD3HS7U2bmpZsRWMZ9O1IzVj3Tpxwb72UEywgXiE2iw=='),(16,14,20,'NmVXtm5ulbscA7SpaMWKV7p0OH37+/IPbnL/SW5rqWQ+oSmDrikAK1qqyc5PU/NJb7CcBl4CQyFkNoDQVpe30osSUL4tKFpXhhqmjRbdhlru1jamvYRiuiAGM8BrbWeVwIpB131Q8rDydfWaDJETzXCSU+QKNHtRHTVSDamlIG54w8YoexXEF/vBNYgRpuh/RJ+d+C5JVe3xlpjIATd2dwgNDvKwgTc37+EyfDrBRkMhX3ROuTYQMHbpLnwJFWNPF9lt3HS+GDXMlDrk9t4r9+WElrnNtW8QETmkwnYmBgguqbuQwojt77p1mIUFl1MJnoSctbhgYTet1dUTWcb9WQ==','2026-04-27 21:32:42',0,'S0zCTrhDMR9Rx89fVLtM8UB9PU+7lqY/g5Or4XX3IqDrm4yy2Mp9yv5b/3e4VCZRjzwKvJvNPGF9A+M3Wu7PE95eMhft8EaUNqxuvpfeaY1NeHuIYL2VKh4VGsk6F0A5Fb7SD/4H3gvSBxMgbzanM7EUs0IG49bcSfXdzBxNWSPWeBBi0ReT/ScehQqkIlexDAnVbpiRejbjqjSR4Qis5H5sjbJkd0++ajzoCJJ1m3dfrrgJn8zTB806kmfsS+zBySGK11a3UjNtygKu23uMSfqlD2bAq8+69i57lqrcvBYjaGbZ0TYY1MqOhuObHPjB/utiDcpZidbUnUIQUtfEtQ=='),(17,14,21,'QKdyMgblfWqf9JeXaw1R6KNSZsFxfEl3HARj1ICOVYmInJmr1HUn5GY+1ADWI3/bUAmWvGVwYH/dJj6ZpqM3WfcWZRmtVFiJxpfIu2Wfij0G9Dd8f785NXBDZWdRiUAGNH28AGTZ77dmvch0HUHRb+oh096+JCArgoBB5q0QRsCDMU/rPdvjRtWKCREmw4F3a6XPnA/VcZX41fTH8pW94b2OBrcSpTYfXkW2jSzkDW7bCOlOWQ+RUDuxvKuxzjJ0XFIJHN6m9zwHl0wmPfn4Lz1C5pjIO9d7zxNEawwfMZis5A/O8HXvLm5Za8MHS2VG86eVV8yhhAf69mHwgDifqA==','2026-04-27 21:33:34',0,'Ebm+kfpgg2eR9cTV3IlGFaDK8Wi5sQfl5Rf3QKwA8uX2e3ksFTSSzzpLGCD163YJzckapie0IDU3MkIqTZSscUuz0psXnfsBy8E9uVielbIGPhCgBUu6SAUYUyUP1tL7j5M0QTii68VysL5cfNO0YRVfR0/R24TNyaZuOWofIBSCVtuU87cww1CJCxhY3ZrNWgQ4Nc/b6qGor6SIQhVnz47a86HIoNFpuorK7NaOzgw3vG+VxdZ/g/6//JR3MiJcltNemBbE/yPWeyPEnPQXBO50FC1vJSZW9aYoVD59L4mKJ3RFCNkmVkwGtSpoIh8H7oEsvsdODRGXpdELe4mTmg=='),(18,14,20,'wgCFaRSWPWAULnAK45YhADhb+9hWJ0bBS5DbocbEdPmiKJt85sC/83Bw67HAdaR88wbmp/YREvpi+sIwfdwWv2p7QAGmvEtZyrOmfLM5XIE8ugr3swbuuYGzl6o2jaJEqSPANEhTcP3ZD59QYugIvc63rhOpq4XBAzhbbmDXC63oOgV6r18KHu/yNZc5mn65IvUwTn4dIv10llCXOq39z2fhs3sfynmZmk+LCF1ssxR1zMhfTS/x4PBwlYZN4intv8KKPHBoaAXleEP0vpWdQX4wQPU/ZhxfHHmOQWNB4vLNpoif/RZ9iXVWN5lU4MCgfVcUxmSBjFo+CYdvjZdjOA==','2026-04-27 21:33:49',0,'OM9Ou7+zwi5HhpJWUbxEBBwcrKcwznvM9/J3fTLiq12MNEfcfcwN9yDK2mH7lFkUJDlfcgsUpa7+aDyj3mM4MZ3j+1SXZgH4jZFBBeaLpPFFjjCYN2qtGqeNd4HxTjN4tztfm1JPVeeUD2oDRtDYprrcp4bNKgzB2P1VA1DcutdFF+G+FptvU+V1DNs7KdChI9Tg0lEV6JZtwIFHjXaloYLp7EkE4NvIqhHiqp6oklvetvMt5PVVUi7rPQ+DPNCIapRZCsGkOfDGJblsdJgtN4Y0XaPt+xOUbTt2ShMRGarMd3KNDdHxoqF3dluPSBxTEKmCIGxmxdXPms4sLlGytA=='),(19,14,21,'ki/rHMCmZVxZYITTbfSfAJMKrEzTON9Qd7EH1Xe6I9KFNYrXzwB28bfEAfWohVlirTioXHFWjgyL8oZVGGZOa9Pjwix5iFXbLol6/LSDMzyQx3SYgww6Oyf4T8TkPfQsEgzF3wcpiDwjcbIfqO1m5JNcWOPsFYo4SKBLOIfoQMxEkobbI9nneM8Ekm6rZwEIdCU7saqfbQ6FYABS3mv0QFbn/kSeM5ZFtRpR1c9jaUcXAQX8SHF37jYPJGE6iZyXLGzYrSp8dU/TQfs1EEhlmtsi+N0utom47XC/8I09gLZh7Ea7chsy/czsmcxAM2Nb2PleJ02IyK+/hhkw61BBRQ==','2026-04-28 14:09:57',0,'LsyLZbDGmdk8X9qTjXTIFvJZJZaQXv1YdS96s7CbFPQTeuwC0JJef0Ds/e78bHEZwT8ycbZAleWCf4S2UASfJgcj2ar50g0HGW+sdrMcFGiC+VPjqu7p6HYTu8sBv5ZfWuXO+6lBud8ywZjc7Toz3/VrF0ILvXIGtwf1yMsvIK+iGawR8mUwFMnV+coPf4Cib90yUXhFzbi+r2u7swLYqItQpRlfu2QTKdfiwzR+uARhf0628ZP/vJ4LUy7LoUtySWHyPAWVYptsvRk875FDVeO8iq8SFwlJnTDCQ/Wr6DWCimaxFz2DdMepxWxsYN7BF46aQ5ZWRUMQLVWdfdmqsA==');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(250) NOT NULL,
  `password` varchar(255) NOT NULL,
  `publicKey` text NOT NULL,
  `state` tinyint(1) NOT NULL DEFAULT 0,
  `lastSeen` datetime DEFAULT NULL,
  PRIMARY KEY (`userId`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (20,'thomas','an0MZ8g2PzD8YMwNx0jDZD3b3uzQ8CVwCLDOOuNRuUc=','-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvCWIHWrYLiiTZXjMb91V\nbBkeFga74H1N3z6wZ4svjfkT663zZ2zPcoz+TQH7CBT+Py/XUYnRDZuJCaWqkQmD\ncFX0WSiJpzCwMxtAtouZFJ93OnvL3IYMicfoV/gRVlr4tC7OROytCzXiLyaspNJ/\noLB+vAS6+seQ8ez/UJPKG5njfU2N0W96Y1WJxj7Gk+QG9Z7K4o3iybeHSqc/3iAD\n2wgodXLg8aZT0GBqXiHWJ17vp4aU/QastTmPTiIQkOOWin3zQ71p6ga2lJGBYn2l\nS0dOJxcU8dAMu35w1wAKdCLWzJU9T88Lzp/FLM4wZvQ1tHu52jv4poDrCwMD0keH\ncQIDAQAB\n-----END PUBLIC KEY-----\n',0,'2026-04-28 21:08:10'),(21,'laura','wxyCn+WP8nxxRidPn0sPsThQZts1w1b+kNtupaP/53A=','-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxpBgAykm7NcTg62cjhGp\nFoP132/0ulbjidStzikguZXKae5fPumcvL6tEzrC8Pmo4L/tHFrv8W6kJFGcEHb/\nQBXrpQzRJAJz3ZB+ocS5irKcIH0NNY6uhTElySl3VjB3X1Q08NPFdmdFnnAiE0KZ\nDLx1eBJpudLWqVjEuUOuYQ5ilGmRjRUuAoKPFvJkcEKRx7EcaUw6vgT61rg7ZIGu\nK5IQnPOPfhXHZSgLRdOY7PpP0UZRhgJGcSI0tRp7uqMqdiGs/gDXum3bwXzjCxQu\nrm2ePMW7H6BSqrOid6pAxHYLzwtUB8xNabJnkx3NM+rN+QRz6YyIJS2MxhQATeXh\ndQIDAQAB\n-----END PUBLIC KEY-----\n',0,'2026-04-28 21:08:09'),(22,'mael','GvnLG5RV+uLeqLHqmypjy8KPc3vVVGdfSRcONeToYL8=','-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvG63Ij13Dy7NTYs/iW72\nsm70aho+Ipi32X6oFmUBXc7Z0TcYu0RJj1Di/yqLDI5tjskRJNjnurnWHGbTewB4\nb3dDV5bNDbtew3Km0q3D5V/p5QR2QOOcM64tu/U0LBrle7LLjhip9IGyIiyl/WcQ\nAKNWA3cXhS7hfSZYd8nX81iI8Ucpqi+w0HIFD4V6ZcK7cCr0NkAx0RO1lC4PIhv+\n8YbH1QzxSPdDT5LtT/QhBtp2FQAn+hQ9f51GV5uDBdro4zVkI/BF1f0ltgxCtDZm\nB+EQJ1p0GkWwztIq+X87B4PtMv5VH30c7X18ipilFP7r1Kt/UzSYiPUVX1Fmksov\n6wIDAQAB\n-----END PUBLIC KEY-----\n',0,'2026-04-28 20:56:12'),(23,'dylan','yzc2WUOHatfXMLDl6y7m5BbSlfg3KTK44LlweRElyKk=','-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiresuTLBSRIepbgwTK64\nBw5vXURFGr3HQxsHgyKDsThBSJTorFJbeesT/2/Zuh/si9R/3r8aB8uzZYy2b7Qv\nVJ7YVIYumQY7BNGlFG44ZMDrk66W6M2EldSuiuCAEfuCZGePdvhVFLcwvs3rHK/h\ntgH+1mA8VYAB8ryNpwGJ5DjWclfz0GnriNFcGl+gRBXv/HaiY9yDgc8JT+vZIjQy\nRu7IYegsti5EbjoPc+eWCAL0GJWrSJYYNMsaUSk784kRU88XPXetgFq3sUcXNAc4\nqbKPXCW+Rs2UeYiGu24KvJB+GzscMlvqt98k++uYVOzLVBrKGa+U3uBu27Aa/YFY\nlwIDAQAB\n-----END PUBLIC KEY-----\n',0,NULL),(24,'fatou','WK+iFT0yDSUriItLTMYrFc5xudrVs+ZFEb3SpBjyboU=','-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA720ws/4Q6JC5nB4OF6pT\nqKfhxTvSWD01rBadjnXV0PetAYvoM+BDzC5r3dsWpBRNMhPTT62Wq4+nf/R68J81\nJ7basbog6lvialDJY20gnHcD7nmZgL02lgiPy9BBn92xbS/pk4Hvq+Z4be116WKp\nWEuuOhoRlBE92UXLatIPObyaiDdx1hICFRIiN/lnJC3MJznneoGRC8WOGNE0FfWr\n3E5n7cERzERAL/YR6qaCPS4D9qBcxEjiR6bC8BrBuXRmAcwYK3nEj0vGJFOtyPa0\nT0G7dmGpwpRJAwr1xyuBBtjZtdoJfVnPfZyE9PUHiJJGohnxzkfmoKifIhmtYB3G\nJQIDAQAB\n-----END PUBLIC KEY-----\n',0,'0000-00-00 00:00:00'),(25,'isham','wPyS67snN9S4b5K57KZDb4dacQGHoA23j7kNGo5GP1U=','-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiQCZ5XaA7annZbhIsFvp\n55LoFWzNQ7gnWLyKrfBsjlkQofmlZXyEJndtJZmseIM19Rgg18GXY87ZK1rMJGxv\nprdylAqdcqoYtgluk/fAvBA9Em+fUyWTN4Wr/INLaRgDkxPq3vPdnQJ8mKCtZAq1\nwf6xU4qvru5XrnwJfSIyYJBu2zM10qerfEp0atM5qbK97/piPnlb5wZKpZv1XDtM\nwqfDs5/ku9h/Tj/mS3ohxVFzXka7UHec9ASxpTs/rDBbVIqi9htymLRNjPYlxCm3\nhCaGIzfTQitKWapK89cGmRvDgyrVvN/zG+SQeozzvtGRNoqz7droZIyRP/bzs/Ln\njQIDAQAB\n-----END PUBLIC KEY-----\n',0,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

--
-- Dumping routines for database 'messageriesecurisee'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-28 21:09:45
