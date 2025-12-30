# 🚀 ANSportion Mac 快速开始

## 第一步：测试兼容性

```bash
python3 test_mac_compatibility.py
```

这会检查你的系统是否准备好运行 ANSportion。

## 第二步：安装依赖

### 方法 A：自动安装（推荐）
```bash
bash install_mac.sh
```

### 方法 B：使用 pip
```bash
pip3 install -r requirements_mac.txt
```

### 方法 C：使用 Python 脚本
```bash
python3 developer/Install_library_mac.py
```

## 第三步：运行程序

### 普通模式
```bash
python3 ANSportion.py
```

### 管理员模式（WiFi 和某些攻击功能需要）
```bash
sudo python3 ANSportion.py
```

## 第四步：开始使用

启动后输入 `help` 查看所有可用命令：

```
help     - 查看帮助
check    - IP 检查工具
attack   - 攻击工具（需谨慎使用）
wifi     - WiFi 工具（需要 sudo）
port     - 端口扫描
crawler  - 网页爬虫
server   - HTTP 服务器
```

## 功能测试示例

### 1. 检查你的 IP 地址
```
check
1
```

### 2. 扫描端口
```
port
1
```

### 3. 创建简单的 HTTP 服务器
```
server
1
```

## 常见问题

### Q: 提示 "Permission denied"？
A: 某些功能需要管理员权限，使用 `sudo python3 ANSportion.py`

### Q: WiFi 功能不工作？
A: 
1. 确保使用 `sudo` 运行
2. Mac 的 WiFi API 有限制，某些功能可能不可用

### Q: 如何停止正在运行的功能？
A: 按 `Ctrl+C`

## ⚠️ 重要提示

1. **法律警告**：仅用于授权测试，未经授权的渗透测试是违法的
2. **权限要求**：某些功能需要 root 权限
3. **网络安全**：使用攻击功能前确保你有合法授权

## 需要帮助？

- 查看详细文档：`cat MAC_COMPATIBILITY_GUIDE.md`
- 查看 Mac 专用 README：`cat README_MAC.md`
- QQ 群：991478664

## 下一步

现在你可以开始探索 ANSportion 的各种功能了！记得负责任地使用这些工具。

祝你使用愉快！🎉
