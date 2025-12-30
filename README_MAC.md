# ANSportion - Mac 快速开始指南

## 🚀 快速安装

### 方法 1：使用安装脚本（推荐）
```bash
# 1. 进入项目目录
cd ANSportion-Pro

# 2. 运行安装脚本（会自动创建虚拟环境）
bash install_mac.sh
```

### 方法 2：使用 requirements 文件
```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements_mac.txt
```

## 🎯 运行程序

### 方法 A：使用启动脚本（最简单）

```bash
# 普通模式
bash run_ansportion.sh

# 管理员模式（WiFi、DOS 攻击等功能需要）
bash run_ansportion.sh sudo
```

### 方法 B：手动激活虚拟环境

```bash
# 1. 激活虚拟环境
source venv/bin/activate

# 2. 运行程序
python3 ANSportion.py

# 3. 使用完毕后退出
deactivate
```

### 方法 C：直接使用虚拟环境

```bash
# 普通模式
venv/bin/python3 ANSportion.py

# 管理员模式
sudo venv/bin/python3 ANSportion.py
```

## ✅ Mac 兼容性

### 完全支持的功能
- ✅ **check** - IP 检查、网络接口信息
- ✅ **attack** - DOS 攻击、短信轰炸、CC 攻击
- ✅ **port** - 端口扫描和检测
- ✅ **crawler** - 网页爬虫
- ✅ **server** - HTTP 服务器
- ✅ **listen** - 端口监听

### 需要管理员权限的功能
- ⚠️ **wifi** - WiFi 相关功能（需要 sudo）
- ⚠️ **attack 1** - DOS 攻击（使用原始套接字）

## 📋 系统要求

- macOS 10.15 或更高版本
- Python 3.11 或更高版本
- 管理员权限（某些功能）

## 🔧 常见问题

### Q: 如何安装 Python 3.11？
```bash
# 使用 Homebrew
brew install python@3.11
```

### Q: WiFi 功能不工作？
A: WiFi 功能需要管理员权限，使用 `sudo python3 ANSportion.py` 运行

### Q: 提示权限不足？
A: 某些功能需要 root 权限，使用 `sudo` 运行程序

### Q: comtypes 安装失败？
A: comtypes 是 Windows 专用库，Mac 不需要安装，可以忽略

## ⚠️ 法律声明

此工具仅供学习和授权测试使用。未经授权的渗透测试是违法的。使用者需自行承担法律责任。

## 📚 更多信息

- 详细兼容性指南：`MAC_COMPATIBILITY_GUIDE.md`
- 原始 README：`README.md`
- QQ 群：991478664

## 🎉 开始使用

```bash
# 1. 安装依赖
bash install_mac.sh

# 2. 运行程序
python3 ANSportion.py

# 3. 输入 help 查看帮助
help
```

祝你使用愉快！🎊
