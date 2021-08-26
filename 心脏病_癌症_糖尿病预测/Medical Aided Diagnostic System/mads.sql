/*
Navicat MySQL Data Transfer

Source Server         : hotel
Source Server Version : 50016
Source Host           : localhost:3306
Source Database       : mads

Target Server Type    : MYSQL
Target Server Version : 50016
File Encoding         : 65001

Date: 2021-08-26 20:33:55
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY  (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('admin', 'admin');
