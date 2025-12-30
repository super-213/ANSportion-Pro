# ANSportion Mac 兼容性指南

## 项目概述
ANSportion 是一个渗透测试工具集，原本为 Windows 设计（Python 3.11）。本指南将帮助你在 Mac 上运行此项目。

## 当前兼容性状态

### ✅ 已兼容的功能
大部分代码已经考虑了跨平台兼容性：
- 清屏命令：使用 `os.system("cls" if os.name == 'nt' else 'clear')`
- 网络功能：socket、requests 等标准库
- 端口扫描、IP 检查、爬虫等功能
- 攻击模块（DOS、CC 等）

### ⚠️ 需要注意的功能

#### 1. WiFi 相关功能 (Code/wifi_*.py)
**问题**：
- `pywifi` 库在 Mac 上支持有限
- Mac 的 WiFi 管理需要使用 `networksetup` 命令（需要管理员权限）

**解决方案**：
- WiFi 连接功能已适配 Mac（使用 `networksetup`）
- WiFi 破解功能在 Mac 上需要额外权限
- 建议使用 `airport` 工具进行 WiFi 扫描

#### 2. 系统特定命令
**check_1.py** 中的网关检测：
- ✅ 已支持 Mac（使用 `netstat -rn`）
- 代码中 `sys.platform == "darwin"` 已处理 Mac 系统

#### 3. 依赖库兼容性
大部分库在 Mac 上可用，但需要注意：
- `pywifi`：Mac 支持有限，建议使用系统命令替代
- `comtypes`：这是 Windows 专用库，Mac 上不可用（但项目中未实际使用）

## Mac 安装步骤

### 1. 安装 Python 3.11+
```bash
# 使用 Homebrew 安装
brew install python@3.11

# 或使用 pyenv
brew install pyenv
pyenv install 3.11.0
pyenv global 3.11.0
```

### 2. 安装依赖库
```bash
# 进入项目目录
cd ANSportion-Pro

# 安装核心依赖（排除 Windows 专用库）
pip3 install requests validators urllib3 tqdm psutil ipaddress colorama cryptography Pillow pyfiglet

# pywifi 在 Mac 上可选安装（功能受限）
pip3 install pywifi

# 不要安装 comtypes（Windows 专用）
```

### 3. 运行项目
```bash
python3 ANSportion.py
```

## 功能测试建议

### 完全可用的功能
```
✅ check 1-5  - IP 检查、网络接口信息
✅ attack 1-3 - DOS 攻击、短信轰炸、CC 攻击
✅ port 1-2   - 端口扫描
✅ crawler 1-2 - 网页爬虫
✅ server 1-2  - HTTP 服务器
✅ listen 1    - 端口监听
```

### 需要权限的功能
```
⚠️ wifi 1-4   - 需要管理员权限
   使用方法：sudo python3 ANSportion.py
```

## Mac 特定注意事项

### 1. 权限问题
某些功能需要 root 权限：
```bash
# 使用 sudo 运行
sudo python3 ANSportion.py
```

### 2. 防火墙设置
Mac 的防火墙可能阻止某些网络操作：
- 系统偏好设置 → 安全性与隐私 → 防火墙
- 允许 Python 的网络访问

### 3. WiFi 功能限制
Mac 的 WiFi API 受限，建议：
- 使用系统自带的 WiFi 工具
- 或使用命令行工具：`airport` 和 `networksetup`

### 4. 原始套接字权限
DOS 攻击等功能使用原始套接字，需要 root 权限：
```bash
sudo python3 ANSportion.py
```

## 已知问题和解决方案

### 问题 1：pywifi 在 Mac 上不工作
**解决方案**：
- WiFi 功能已使用 `networksetup` 命令适配
- 或手动使用系统 WiFi 设置

### 问题 2：某些攻击功能需要 root 权限
**解决方案**：
```bash
sudo python3 ANSportion.py
```

### 问题 3：comtypes 安装失败
**解决方案**：
- 这是 Windows 专用库，Mac 不需要
- 项目中未实际使用，可以忽略

## 推荐的 Mac 安装脚本

创建一个 `install_mac.sh` 脚本：
```bash
#!/bin/bash
echo "ANSportion Mac 安装脚本"
echo "========================"

# 检查 Python 版本
python3 --version

# 安装依赖
echo "正在安装依赖库..."
pip3 install requests validators urllib3 tqdm psutil ipaddress colorama cryptography Pillow pyfiglet

echo "安装完成！"
echo "运行方式："
echo "  普通模式: python3 ANSportion.py"
echo "  管理员模式: sudo python3 ANSportion.py"
```

## 测试清单

运行以下命令测试各功能：
```
1. 启动程序：python3 ANSportion.py
2. 输入 help 查看帮助
3. 测试 check 模块：check → 1
4. 测试 port 模块：port → 1
5. 测试 crawler 模块：crawler → 2
```

## 法律声明
⚠️ **重要**：此工具仅供学习和授权测试使用。未经授权的渗透测试是违法的。

## 支持
- QQ 群：991478664
- GitHub: https://github.com/XXX-Stalker/ANSportion
- GitCode: https://gitcode.com/XXX_Stalker/ANSportion
