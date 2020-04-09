package com.lb.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.extension.activerecord.Model;
import com.baomidou.mybatisplus.annotation.TableId;
import java.time.LocalDateTime;
import com.baomidou.mybatisplus.annotation.TableField;
import java.io.Serializable;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.Accessors;

/**
 * <p>
 * 账号表
 * </p>
 *
 * @author lb
 * @since 2020-04-09
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@TableName("account")
public class Account extends Model<Account> {

    private static final long serialVersionUID = 1L;

    /**
     * id
     */
    @TableId("id")
    private Long id;

    /**
     * 用户名
     */
    @TableField("username")
    private String username;

    /**
     * 密码
     */
    @TableField("password")
    private String password;

    /**
     * 邮箱
     */
    @TableField("e_mail")
    private String eMail;

    /**
     * 手机号
     */
    @TableField("mobile")
    private String mobile;

    /**
     * 姓名
     */
    @TableField("name")
    private String name;

    /**
     * 昵称/花名
     */
    @TableField("nickname")
    private String nickname;

    /**
     * 头像
     */
    @TableField("head_portrait")
    private String headPortrait;

    /**
     * 创建时间
     */
    @TableField("create_time")
    private LocalDateTime createTime;

    /**
     * 更新时间
     */
    @TableField("update_time")
    private LocalDateTime updateTime;

    /**
     * 创建者
     */
    @TableField("create_by")
    private Long createBy;

    /**
     * 更新者
     */
    @TableField("update_by")
    private Long updateBy;

    /**
     * 删除标记，0：正常  大于0，已被删除
     */
    @TableField("delete_flag")
    private Long deleteFlag;


    @Override
    protected Serializable pkVal() {
        return this.id;
    }

}
