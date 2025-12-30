# 👋 欢迎使用 ANSportion Mac 版！

## 🎯 从这里开始

你好！如果你是第一次在 Mac 上使用 ANSportion，请按照以下步骤操作：

## ⚡ 快速开始（2步）

### 步骤 1：安装
```bash
bash install_mac.sh
```
等待安装完成（约 1-2 分钟）

### 步骤 2：运行
```bash
bash run_ansportion.sh
```

就这么简单！🎉

## 🚚 迁移到新 Mac？

如果你想把这个项目迁移到另一台 Mac：

- **新Mac快速启动.md** ⭐⭐⭐⭐⭐
  - 5 分钟快速迁移指南
  - 简单 3 步完成
  
- **迁移到新Mac指南.md** ⭐⭐⭐⭐
  - 详细的迁移步骤
  - 两种方案对比
  - 常见问题解答

## 📖 文档导航

根据你的需求选择合适的文档：

### 🚀 我想快速开始
- **快速开始_Mac.md** ⭐⭐⭐⭐⭐
  - 3步快速指南
  - 最简单的使用方法
  - 推荐新手阅读

### 📚 我想了解详细信息
- **开始使用_Mac.md** ⭐⭐⭐⭐⭐
  - 完整的中文使用指南
  - 包含所有功能说明
  - 常见问题解答

### 🔧 我遇到了问题
- **问题已解决_Mac.md** ⭐⭐⭐⭐⭐
  - 常见问题和解决方案
  - 依赖安装问题
  - 语法警告修复

### 🌍 English Users
- **README_MAC.md** ⭐⭐⭐⭐
  - Quick start guide in English
  - Installation and usage

### 💻 技术人员
- **MAC_COMPATIBILITY_GUIDE.md**
  - 详细的兼容性分析
  - 技术细节和原理
  
- **适配完成报告.md**
  - 完整的适配工作报告
  - 功能兼容性矩阵

## 🎮 使用方法

### 普通模式
```bash
bash run_ansportion.sh
```

### 管理员模式（WiFi、DOS 攻击等）
```bash
bash run_ansportion.sh sudo
```

### 手动方式
```bash
# 激活虚拟环境
source venv/bin/activate

# 运行程序
python3 ANSportion.py

# 退出虚拟环境
deactivate
```

## ✅ 已解决的问题

如果你之前遇到过这些问题，现在都已经解决了：

- ✅ `ModuleNotFoundError: No module named 'colorama'`
- ✅ `SyntaxWarning: invalid escape sequence`
- ✅ `externally-managed-environment` 错误

详情请查看：**问题已解决_Mac.md**

## 🎯 功能概览

ANSportion 提供以下功能模块：

| 模块 | 功能 | Mac 支持 | 需要 sudo |
|------|------|---------|----------|
| check | IP 检查、网络信息 | ✅ | ❌ |
| attack | DOS、短信轰炸、CC | ✅ | 部分需要 |
| wifi | WiFi 管理 | ⚠️ 受限 | ✅ |
| port | 端口扫描 | ✅ | ❌ |
| crawler | 网页爬虫 | ✅ | ❌ |
| server | HTTP 服务器 | ✅ | ❌ |
| listen | 端口监听 | ✅ | ❌ |

## ⚠️ 重要提示

### 1. 虚拟环境
- 依赖已安装在 `venv/` 目录
- 使用 `run_ansportion.sh` 会自动处理
- 不要删除 `venv/` 目录

### 2. 管理员权限
某些功能需要 sudo：
- WiFi 相关功能
- DOS 攻击（原始套接字）

### 3. 法律警告
⚠️ **重要**：
- 仅用于授权测试
- 未经授权的渗透测试是违法的
- 使用者需自行承担法律责任

## 🆘 需要帮助？

### 常见问题
1. **提示找不到模块？**
   - 确保使用 `bash run_ansportion.sh` 运行

2. **权限不足？**
   - 使用 `bash run_ansportion.sh sudo`

3. **虚拟环境损坏？**
   ```bash
   rm -rf venv
   bash install_mac.sh
   ```

### 获取支持
- **QQ 群**：991478664
- **GitHub**：https://github.com/XXX-Stalker/ANSportion
- **GitCode**：https://gitcode.com/XXX_Stalker/ANSportion

## 📁 文件说明

### 核心文件
- `ANSportion.py` - 主程序
- `venv/` - 虚拟环境（自动创建）

### 脚本文件
- `install_mac.sh` - 安装脚本
- `run_ansportion.sh` - 启动脚本
- `test_mac_compatibility.py` - 兼容性测试

### 文档文件
- `README_FIRST.md` - 本文件
- `快速开始_Mac.md` - 快速指南
- `开始使用_Mac.md` - 完整指南
- `问题已解决_Mac.md` - 问题解决
- 更多文档请查看 `MAC_FILES_INDEX.md`

## 🎉 开始使用

现在你已经了解了基本信息，可以开始使用了！

```bash
# 1. 安装（如果还没安装）
bash install_mac.sh

# 2. 运行
bash run_ansportion.sh

# 3. 在程序中输入
help      # 查看帮助
check     # 测试功能
```

祝你使用愉快！🎊

---

**版本**: ANSportion 1.1.9 Pro (Mac 适配版)  
**最后更新**: 2025-12-30  
**适配者**: Kiro AI Assistant

💡 **提示**：建议先阅读 `快速开始_Mac.md` 快速上手！
