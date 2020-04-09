package com.lb;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @author lb
 * @date 2020/4/7 5:50 下午
 */
@SpringBootApplication
@MapperScan("com.lb.mapper")
public class BootstrapApplication {
    public static void main(String[] args) {
        SpringApplication.run(BootstrapApplication.class,args);
    }
}
