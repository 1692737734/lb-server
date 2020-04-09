SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `id` bigint(20) NOT NULL COMMENT 'id',
  `username` varchar(50) NOT NULL COMMENT '用户名',
  `password` varchar(50) DEFAULT NULL COMMENT '密码',
  `e_mail` varchar(50) DEFAULT NULL COMMENT '邮箱',
  `mobile` varchar(12) DEFAULT NULL COMMENT '手机号',
  `name` varchar(10) DEFAULT NULL COMMENT '姓名',
  `nickname` varchar(20) DEFAULT NULL COMMENT '昵称/花名',
  `head_portrait` varchar(255) DEFAULT NULL COMMENT '头像',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `create_by` bigint(255) DEFAULT NULL COMMENT '创建者',
  `update_by` bigint(20) DEFAULT NULL COMMENT '更新者',
  `delete_flag` bigint(255) DEFAULT NULL COMMENT '删除标记，0：正常  大于0，已被删除',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username and delete_flag` (`username`,`delete_flag`) USING BTREE,
  KEY `id` (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='账号表';

SET FOREIGN_KEY_CHECKS = 1;