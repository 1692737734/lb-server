package com.lb.service.impl;

import com.lb.entity.Account;
import com.lb.mapper.AccountMapper;
import com.lb.service.IAccountService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 * 账号表 服务实现类
 * </p>
 *
 * @author lb
 * @since 2020-04-09
 */
@Service
public class AccountServiceImpl extends ServiceImpl<AccountMapper, Account> implements IAccountService {

}
