# Aegis
一个微型测试框架

### 安装
```text
cd aegis
python setup.py install
```

### 使用

* 第一步:创建一个工程，我们这里假如叫做MyTest
* 第二步:创建一个package来存放测试代码，我们这里假如叫做product
* 第三步:在product里创建一个package叫做testcase
* 第四步:在product里创建一个目录叫做testdata
* 第五步:完成三、四两步即可在testcase里编写测试用例


### 注意事项
* testcase和testdata是必须创建的，且其目录结构必须保持一致，一般目录结构如下:
```text
MyTest
└── product                     //一个python包,用来组织测试代码
    ├── __init__.py
    ├── conf                    //一个python包
    │   └── settings.py         //用来设置一些配置信息
    ├── testcase                //一个python包,用来组织测试用例
    │   ├── __init__.py
    │   └── demo
    │       ├── __init__.py
    │       └── test_demo.py
    └── testdata                //一个文件夹,用来存放测试数据, 该目录的结构要和testcase包保持一致
        └── demo
            └── test_demo.json  //测试的数据, 默认使用json格式
```

