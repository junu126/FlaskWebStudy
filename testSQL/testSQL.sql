-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.3.15-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- flasktest 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `flasktest` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `flasktest`;

-- 테이블 flasktest.sample 구조 내보내기
CREATE TABLE IF NOT EXISTS `sample` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `regdate` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='으아아ㅏ아아아아아ㅏ앙아아ㅏㅇㅇ아ㅏㅏ아아아아아아아ㅏ아앙아아아아아앙';

-- 테이블 데이터 flasktest.sample:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `sample` DISABLE KEYS */;
INSERT INTO `sample` (`uid`, `name`, `age`, `regdate`) VALUES
	(1, '홍길동', 18, NULL);
/*!40000 ALTER TABLE `sample` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
