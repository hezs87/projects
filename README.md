本仓库中所涉及到的项目均为本人负责或亲身参与的，上传到GitHub除了为了记录近年来本人所涉及到的项目之外，也是将关键源代码开源出来，欢迎大家一起沟通交流！如果有问题可以与我本人联系！
## 目录
* [基于半监督学习的SDN网络异常检测系统设计与实现](#基于半监督学习的SDN网络异常检测系统设计与实现)
  * [项目背景](#项目背景一)
  * [项目介绍](#项目介绍一)
  * [关键代码](#关键代码一)
       * [代码一](#代码一一)
       * [代码二](#代码二一)
* [基于哈希散列及RSA加密传输的联网验证软件注册保护机制](#基于哈希散列及RSA加密传输的联网验证软件注册保护机制)
  * [项目背景](#项目背景二)
  * [项目介绍](#项目介绍二)
  * [关键代码](#关键代码二)
       * [代码一](#代码一二)
       * [代码二](#代码二二)
* [联系方式](#联系方式)
 
<a name="基于半监督学习的SDN网络异常检测系统设计与实现"></a>
## 基于半监督学习的SDN网络异常检测系统设计与实现
 
*Shurnim*，本项目于2019年开发。<br/>
*shurnim-storage*，2019年完成。
 
<a name="项目背景一"></a>
### 项目背景
 
*shurnim-storage* 设计初衷是给大家提供一个可方便扩展的。分后端接口和前端UI界面两部分。<br>
 
由于目前各种云存储和网盘系统层出不穷，单一工具往往支持支持某几个特定存储之间的同步，如**又拍云**到**七牛云存储**的同步工具，此时如若想同步到其他存则可能需要新的工具，给用户带来不便。*shurnim-storage*  正是为了解决此问题而设计的。
 
<a name="项目介绍一"></a>
### 项目介绍

由于目前各种云存储和网盘系统层出不穷，单一工具往往支持支持某几个特定存储之间的同步，如**又拍云**到**七牛云存储**的同步工具，此时如若想同步到其他存则可能需要新的工具，给用户带来不便。*shurnim-storage*  正是为了解决此问题而设计的。

<a name="关键代码一"></a>
### 关键代码

 由于目前各种云存储和网盘系统层出不穷，单一工具往往支持支持某几个特定存储之间的同步，如**又拍云**到**七牛云存储**的同步工具，此时如若想同步到其他存则可能需要新的工具，给用户带来不便。*shurnim-storage*  正是为了解决此问题而设计的。
 
<a name="代码一一"></a>
#### 代码一
 
* GitHub项目主页: <https://github.com/hezs87/projects><br>
 
另外你也可以通过OSChina的Maven库获取依赖，或者自己编译jar包。
 
* Gradle 编译Jar
 ```
package com.coderli.shurnim.storage.plugin;
 
import java.io.File;
import java.util.List;
 
import com.coderli.shurnim.storage.plugin.model.Resource;
 
/**
* 各种云存储插件需要实现的通用接口
*
* @author OneCoder
* @date 2014年4月22日 下午9:43:41
* @website http://www.coderli.com
*/
public interface PluginAPI {
 
     /**
      * 初始化接口
      *
      * @author OneCoder
      * @date 2014年5月19日 下午10:47:40
      */
     void init();
     /**
      * 上传资源
      *
      * @param parentPath
      *            父目录路径
      * @param name
      *            资源名称
      * @param uploadFile
      *            待上传的本地文件
      * @return
      * @author OneCoder
      * @date 2014年5月15日 下午10:40:13
      */
     boolean uploadResource(String parentPath, String name, File uploadFile);
}
```

   
<a name="代码二一"></a>
#### 代码二一
 
在*shurnim-storage*中，插件就像一块一块的积木，不但支撑着框架的功能，也是框架可扩展性的基石。开发一个插件，仅需两步：
 
1. 实现PluginAPI接口
 
```
package com.coderli.shurnim.storage.plugin;
 
import java.io.File;
import java.util.List;
 
import com.coderli.shurnim.storage.plugin.model.Resource;
 
/**
* 各种云存储插件需要实现的通用接口
*
* @author OneCoder
* @date 2014年4月22日 下午9:43:41
* @website http://www.coderli.com
*/
public interface PluginAPI {
 
     /**
      * 初始化接口
      *
      * @author OneCoder
      * @date 2014年5月19日 下午10:47:40
      */
     void init();
     /**
      * 上传资源
      *
      * @param parentPath
      *            父目录路径
      * @param name
      *            资源名称
      * @param uploadFile
      *            待上传的本地文件
      * @return
      * @author OneCoder
      * @date 2014年5月15日 下午10:40:13
      */
     boolean uploadResource(String parentPath, String name, File uploadFile);
}
```
 
     在使用源码工程时，插件配置文件统一放置在工程的*plugins*目录下。你也可以统一放置在任何位置。此时，在构造后端接口实例时，需要告知接口该位置。
 
<a name="基于哈希散列及RSA加密传输的联网验证软件注册保护机制"></a>
## 基于哈希散列及RSA加密传输的联网验证软件注册保护机制
 
*Shurnim*，本项目于2019年开发。<br/>
*shurnim-storage*，2019年完成。
 
<a name="项目背景二"></a>
### 项目背景
 
*shurnim-storage* 设计初衷是给大家提供一个可方便扩展的。分后端接口和前端UI界面两部分。<br>
 
由于目前各种云存储和网盘系统层出不穷，单一工具往往支持支持某几个特定存储之间的同步，如**又拍云**到**七牛云存储**的同步工具，此时如若想同步到其他存则可能需要新的工具，给用户带来不便。*shurnim-storage*  正是为了解决此问题而设计的。
 
<a name="项目介绍二"></a>
### 项目介绍

由于目前各种云存储和网盘系统层出不穷，单一工具往往支持支持某几个特定存储之间的同步，如**又拍云**到**七牛云存储**的同步工具，此时如若想同步到其他存则可能需要新的工具，给用户带来不便。*shurnim-storage*  正是为了解决此问题而设计的。

<a name="关键代码二"></a>
### 关键代码

 由于目前各种云存储和网盘系统层出不穷，单一工具往往支持支持某几个特定存储之间的同步，如**又拍云**到**七牛云存储**的同步工具，此时如若想同步到其他存则可能需要新的工具，给用户带来不便。*shurnim-storage*  正是为了解决此问题而设计的。
 
<a name="代码一二"></a>
#### 代码一
 
* GitHub项目主页: <https://github.com/hezs87/projects><br>
 
另外你也可以通过OSChina的Maven库获取依赖，或者自己编译jar包。
 
* Gradle 编译Jar
 ```
package com.coderli.shurnim.storage.plugin;
 
import java.io.File;
import java.util.List;
 
import com.coderli.shurnim.storage.plugin.model.Resource;
 
/**
* 各种云存储插件需要实现的通用接口
*
* @author OneCoder
* @date 2014年4月22日 下午9:43:41
* @website http://www.coderli.com
*/
public interface PluginAPI {
 
     /**
      * 初始化接口
      *
      * @author OneCoder
      * @date 2014年5月19日 下午10:47:40
      */
     void init();
     /**
      * 上传资源
      *
      * @param parentPath
      *            父目录路径
      * @param name
      *            资源名称
      * @param uploadFile
      *            待上传的本地文件
      * @return
      * @author OneCoder
      * @date 2014年5月15日 下午10:40:13
      */
     boolean uploadResource(String parentPath, String name, File uploadFile);
}
```

   
<a name="代码二一二"</a>
#### 代码二
 
在*shurnim-storage*中，插件就像一块一块的积木，不但支撑着框架的功能，也是框架可扩展性的基石。开发一个插件，仅需两步：
 
1. 实现PluginAPI接口
 
```
package com.coderli.shurnim.storage.plugin;
 
import java.io.File;
import java.util.List;
 
import com.coderli.shurnim.storage.plugin.model.Resource;
 
/**
* 各种云存储插件需要实现的通用接口
*
* @author OneCoder
* @date 2014年4月22日 下午9:43:41
* @website http://www.coderli.com
*/
public interface PluginAPI {
 
     /**
      * 初始化接口
      *
      * @author OneCoder
      * @date 2014年5月19日 下午10:47:40
      */
     void init();
     /**
      * 上传资源
      *
      * @param parentPath
      *            父目录路径
      * @param name
      *            资源名称
      * @param uploadFile
      *            待上传的本地文件
      * @return
      * @author OneCoder
      * @date 2014年5月15日 下午10:40:13
      */
     boolean uploadResource(String parentPath, String name, File uploadFile);
}
```
 
     在使用源码工程时，插件配置文件统一放置在工程的*plugins*目录下。你也可以统一放置在任何位置。此时，在构造后端接口实例时，需要告知接口该位置。
 
<a name="联系方式"></a>
## 联系方式
 
时间仓促，功能简陋，望您包涵。任意的意见和建议，欢迎随意与我沟通！
 
* Email: <hezs87@protonmail.com>
* QQ: `909400921`
* Blog:[个人博客](https://www.situ9527.cn/)
 
