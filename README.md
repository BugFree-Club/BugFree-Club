#FITA	

为社团打造的网站



###运行环境

```command_line
$ pip install -r requirements.txt
```



### 写在前面

- 时间有限因而bug较多，发现bug提交后团队会非常感谢您的付出

- 数据库配置(记得配置完成之后创建超级管理员)

  ```python
  #TODO：上线版本的sql密码需要改
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'FITA_WEB',
          'USER': 'root',
          'PASSWORD': 'nvzhuangdalao',
          'HOST': '127.0.0.1',
          'OPTIONS': {'init_command': 'SET sql_mode="STRICT_TRANS_TABLES" '},
          'AUTOCOMMIT': True,
      }
  }
  ```

### 测试流程

- 主页模块http://127.0.0.1:8000/
  - 对应app为manage_site
  - 展示功能为：照片墙、社团介绍、核心成员、荣誉墙等
  - 页面（未定），目录地址为manage_site/templates/manage_site/index.html
- 课程模块http://127.0.0.1:8000/courses/
  - 对应app为courses
  - 功能：展示所有已开课程
  - 页面：
    - 列表页（未定），地址courses/templates/courses/courses.html
    - 详情页（未定），地址courses/templates/courses/detail.html
- 用户模块http://127.0.0.1:8000/users/+任意id
  - 对应app为users
  - 功能：注册、登陆、发送邮件密码找回、成为课程负责人
  - 页面：所有页面都在users/templates/users目录下
- 后台模块http://127.0.0.1:8000/admin/
  - 对应app为extra_app，集成第三方xadmin





### 页面设计

- 重写各个模块下的base页面
- 将后台数据填充至继承的区块中
- 尽量考虑多屏适配



### 写在最后

项目仅仅是雏形阶段，大家一起努力
