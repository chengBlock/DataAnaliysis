# DataAnaliysis
## 简介

> 采用前后端分离架构，python负责数据分析和Mysql的crud，JS三组件做前端处理，前后端交互数据通过json传输。

```text
1.用折线图表示商品价格走势
2.用柱状图表示不同种商品的价格
3.用饼状图表示销量占比
4.有一个后台管理员界面,功能设计类似于每天管理员更改各个商品的信息,相应的操作通过crud保存到数据库中。保存的同时，这些数据可以实时用来更新前端用户界面
```



**涉及知识点：**

- Python、JavaScript、HTML、CSS
- Numpy、Pandas、ECharts、pymysql
- MySql、Node.js、Json
- 前后端分离思想

**扩展:**

1. 系统学习MySql数据库,入门NoSql
2. 趁着前端内容的学习基础,一定要深入学习Vue.js
3. 实践和总结前后端分离思想

# npm

**npm的命令参数 : --save -dev和--save的区别 :**

- --save 会把依赖包名称添加到 package.json 的 dependencies 键下，而 --save-dev 会添加到 devDependencies 键下。
- dependencies 是运行时的依赖，而devDependencies是开发时的依赖。也就是说，采用 --save-dev 安装的包我们发布后是用不到的，只有在开发时用到。采用 --save 安装的包在发布后还会有依赖，例如：axios。如下代码：

```json
 "dependencies": {
    "axios": "^0.18.0",
    "express": "^4.16.3"
  },
  "devDependencies": {
    "babel-eslint": "^8.2.6",
    "eslint": "^5.2.0"
  }
```

- 当我们使用npm install 时会下载 dependencies 和 devDependencies 下的模块。使用 npm install -production或者给定NODE_ENV值为production时，就只下载 dependencies 下的模块。

