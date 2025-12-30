# 🚀 ANSportion Mac 版使用指南

## 📋 系统要求

- macOS 10.15 或更高版本
- Python 3.11 或更高版本（推荐 3.13）
- 网络连接

## 🔍 第一步：检查兼容性

运行测试脚本检查你的 Mac 是否准备好：

```bash
python3 test_mac_compatibility.py
```

测试脚本会检查：
- ✅ Python 版本
- ✅ 操作系统
- ✅ 依赖库
- ✅ 网络功能
- ✅ 权限状态

## 📦 第二步：安装依赖库

### 方法一：自动安装（最简单）

```bash
bash install_mac.sh
```

脚本会自动安装所有需要的库。

### 方法二：使用 pip（快速）

```bash
pip3 install -r requirements_mac.txt
```

### 方法三：使用 Python 脚本（可选择安装）

```bash
python3 developer/Install_library_mac.py
```

这个脚本允许你选择性地安装每个库。

### 方法四：手动安装

```bash
pip3 install requests validators urllib3 tqdm psutil ipaddress colorama cryptography Pillow pyfiglet
```

## 🎮 第三步：运行程序

### 普通模式（大部分功能）

```bash
python3 ANSportion.py
```

### 管理员模式（完整功能）

某些功能需要管理员权限：
- WiFi 相关功能
- 原始套接字（某些攻击功能）

```bash
sudo python3 ANSportion.py
```

## 📖 第四步：使用功能

启动后，你会看到欢迎界面。输入 `help` 查看所有命令：

```
ANSportion-PRO $ help
```

### 主要功能模块

#### 1. check - 检查工具
```
check    # 进入 check 模块
1        # 查看自己的各个 IP 地址
2        # 检查 IP 是否有效
3        # 查看网站真实 IP
4        # 查看 Mac 地址
5        # 查看网络接口信息
```

#### 2. attack - 攻击工具（⚠️ 需谨慎使用）
```
attack   # 进入 attack 模块
1        # DOS 攻击（需要 sudo）
2        # 短信轰炸
3        # CC 攻击
```

#### 3. wifi - WiFi 工具（需要 sudo）
```
wifi     # 进入 wifi 模块
1        # 连接 WiFi
2        # WiFi 破解
3        # 扫描周围 WiFi
4        # 无限连接 WiFi
```

#### 4. port - 端口工具
```
port     # 进入 port 模块
1        # 扫描 IP 的开放端口
2        # 检查指定端口是否开放
```

#### 5. crawler - 爬虫工具
```
crawler  # 进入 crawler 模块
1        # 爬取网站源代码
2        # 爬取网站状态
```

#### 6. server - 服务器工具
```
server   # 进入 server 模块
1        # 创建一个网站服务器
2        # 创建一个文件下载服务器
```

#### 7. listen - 监听工具
```
listen   # 进入 listen 模块
1        # 监听 IP 主机的端口状态
```

### 其他命令

```
help     # 查看帮助
about    # 关于我们
log      # 查看更新日志
log all  # 查看所有更新日志
cls      # 清屏
clear    # 清屏
exit     # 退出程序
```

## 💡 使用示例

### 示例 1：查看自己的 IP 地址

```bash
$ python3 ANSportion.py
ANSportion-PRO $ check
: 1
网关 IP 地址: 192.168.1.1
公网IP: xxx.xxx.xxx.xxx
局域网IP: 192.168.1.100
```

### 示例 2：扫描端口

```bash
ANSportion-PRO $ port
: 1
请输入要扫描的IP地址: 192.168.1.1
请输入起始端口: 1
请输入结束端口: 1000
请输入线程数量: 50
```

### 示例 3：创建简单的 HTTP 服务器

```bash
ANSportion-PRO $ server
: 1
请输入端口号: 8080
# 然后在浏览器访问 http://localhost:8080
```

## ⚠️ 重要注意事项

### 1. 法律警告

```
根据《中华人民共和国刑法》第285、286条规定：
- 未经授权对计算机系统实施攻击可处5年以下有期徒刑
- 造成严重后果者可处5年以上有期徒刑
```

**请确保：**
- ✅ 你有目标系统的授权
- ✅ 仅用于学习和合法测试
- ✅ 了解相关法律风险

### 2. 权限要求

某些功能需要管理员权限：

| 功能 | 需要 sudo | 说明 |
|------|----------|------|
| check | ❌ | 不需要 |
| attack (DOS) | ✅ | 使用原始套接字 |
| attack (其他) | ❌ | 不需要 |
| wifi | ✅ | Mac WiFi API 限制 |
| port | ❌ | 不需要 |
| crawler | ❌ | 不需要 |
| server | ❌ | 不需要 |
| listen | ❌ | 不需要 |

### 3. Mac 特定限制

- **WiFi 功能**：Mac 的 WiFi API 有限制，某些功能可能不如 Windows 完整
- **防火墙**：确保防火墙允许 Python 的网络访问
- **权限提示**：首次运行某些功能时可能会弹出权限请求

## 🔧 常见问题

### Q1: 提示 "Permission denied"？
**A**: 使用 `sudo python3 ANSportion.py` 运行

### Q2: WiFi 功能不工作？
**A**: 
1. 确保使用 `sudo` 运行
2. Mac 的 WiFi API 有限制，某些功能可能不可用
3. 检查系统偏好设置中的 WiFi 权限

### Q3: 如何停止正在运行的功能？
**A**: 按 `Ctrl+C` 或 `Command+C`

### Q4: 提示找不到某个库？
**A**: 重新运行安装脚本：`bash install_mac.sh`

### Q5: comtypes 安装失败？
**A**: comtypes 是 Windows 专用库，Mac 不需要安装，可以忽略

### Q6: 程序运行很慢？
**A**: 
1. 减少线程数量
2. 检查网络连接
3. 关闭其他占用网络的程序

## 📚 更多文档

- **快速开始**：`QUICKSTART_MAC.md`（英文）
- **详细指南**：`MAC_COMPATIBILITY_GUIDE.md`（英文）
- **适配总结**：`MAC_SETUP_SUMMARY.md`（英文）
- **原始文档**：`README.md`

## 🆘 获取帮助

- **QQ 群**：991478664
- **GitHub**：https://github.com/XXX-Stalker/ANSportion
- **GitCode**：https://gitcode.com/XXX_Stalker/ANSportion

## 🎯 测试清单

在开始使用前，建议测试以下功能：

- [ ] 运行兼容性测试：`python3 test_mac_compatibility.py`
- [ ] 启动程序：`python3 ANSportion.py`
- [ ] 查看帮助：输入 `help`
- [ ] 测试 check 模块：`check` → `1`
- [ ] 测试 port 模块：`port` → `2`
- [ ] 测试 crawler 模块：`crawler` → `2`

## 🎉 开始使用

现在你已经准备好了！运行以下命令开始：

```bash
python3 ANSportion.py
```

祝你使用愉快！记得负责任地使用这些工具。🎊

---

**版本**: 1.1.9 Pro  
**适用系统**: macOS  
**最后更新**: 2025-12-30
