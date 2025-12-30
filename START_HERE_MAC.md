# 🎉 欢迎 Mac 用户！

## 👋 你好！

恭喜！ANSportion 现在已经完全适配 Mac 系统了！

这个项目原本是为 Windows 设计的，但好消息是：**大部分代码已经考虑了跨平台兼容性**，所以我们只需要做一些配置工作就能在 Mac 上完美运行。

## 🚀 三步开始使用

### 1️⃣ 安装依赖
```bash
bash install_mac.sh
```
这会自动创建虚拟环境并安装所有依赖。

### 2️⃣ 运行程序
```bash
# 普通模式
bash run_ansportion.sh

# 管理员模式（WiFi、DOS 攻击等功能需要）
bash run_ansportion.sh sudo
```

### 3️⃣ 开始使用
```
help      # 查看所有命令
check     # 检查 IP 地址
exit      # 退出程序
```

就这么简单！🎊

## 💡 重要更新

**已修复的问题：**
- ✅ 修复了依赖安装问题（使用虚拟环境）
- ✅ 修复了语法警告（转义序列）
- ✅ 创建了便捷的启动脚本

**新增文件：**
- `run_ansportion.sh` - 一键启动脚本
- `快速开始_Mac.md` - 3步快速开始指南

## 📚 需要帮助？

### 中文用户
👉 **开始使用_Mac.md** - 完整的中文使用指南

### English Users
👉 **README_MAC.md** - Quick start guide in English

### 遇到问题？
👉 **MAC_COMPATIBILITY_GUIDE.md** - 详细的问题解决指南

### 想了解技术细节？
👉 **MAC_SETUP_SUMMARY.md** - 适配工作技术总结

## ✅ 功能支持

| 功能 | Mac 支持 |
|------|---------|
| ✅ IP 检查 | 完全支持 |
| ✅ 端口扫描 | 完全支持 |
| ✅ 网页爬虫 | 完全支持 |
| ✅ HTTP 服务器 | 完全支持 |
| ✅ 攻击工具 | 完全支持（部分需要 sudo）|
| ⚠️ WiFi 工具 | 支持（需要 sudo，功能受限）|

## ⚠️ 重要提示

1. **法律警告**：仅用于授权测试，未经授权的渗透测试是违法的
2. **权限要求**：某些功能需要使用 `sudo python3 ANSportion.py` 运行
3. **WiFi 限制**：Mac 的 WiFi API 有限制，某些功能可能不如 Windows 完整

## 🎯 快速测试

启动程序后试试这些命令：

```
help      # 查看所有命令
check     # 检查你的 IP 地址
port      # 扫描端口
crawler   # 爬取网页
```

## 📦 我们为你准备了什么？

为了让 ANSportion 在 Mac 上完美运行，我们创建了：

- ✅ **6 个详细文档**（中英文）
- ✅ **3 个安装脚本**（自动化安装）
- ✅ **1 个测试工具**（验证兼容性）

所有文件列表请查看：**MAC_FILES_INDEX.md**

## 🆘 获取支持

- **QQ 群**：991478664
- **GitHub**：https://github.com/XXX-Stalker/ANSportion
- **GitCode**：https://gitcode.com/XXX_Stalker/ANSportion

## 🎉 开始你的旅程

现在就运行这个命令开始吧：

```bash
python3 ANSportion.py
```

祝你使用愉快！记得负责任地使用这些工具。🚀

---

**版本**: ANSportion 1.1.9 Pro  
**适配日期**: 2025-12-30  
**适配者**: Kiro AI Assistant

💡 **提示**：如果这是你第一次使用，建议先阅读 `开始使用_Mac.md`（中文）或 `README_MAC.md`（英文）
